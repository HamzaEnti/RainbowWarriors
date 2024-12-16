import subprocess
import sys

# Comprobar e instalar pycryptodome si no esta instalado.(biblioteca de Python diseñada para realizar operaciones criptográficas)
def install_pycryptodome():
    try:
        import Crypto
    except ImportError:
        print("La biblioteca 'pycryptodome' no está instalada. Procediendo con la instalación...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pycryptodome"])
        print("Instalación completada. Reinicia el programa si encuentras algún problema.")
install_pycryptodome()

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64

def aes_encrypt(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    return base64.b64encode(cipher.iv + ct_bytes).decode('utf-8')
