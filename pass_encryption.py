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

from pass_generator import pass_generator2
from general_storage import usuari, servei
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
from Crypto.Protocol.KDF import PBKDF2
import os

def aes_encrypt(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    return base64.b64encode(cipher.iv + ct_bytes).decode('utf-8')

def pass_storage():
    # Solicitar la clave al usuario
    password = input("Introduce una contraseña para cifrar los datos: ").strip()
    
    # Derivar una clave AES segura a partir de la contraseña del usuario
    salt = os.urandom(16)  # Generar un "salt" aleatorio para aumentar seguridad
    key = PBKDF2(password, salt, dkLen=16, count=100000)  # Derivar clave de 16 bytes
    
    SERVEI = servei().strip()
    USUARI = usuari().strip()
    GENERATEDPASSWORD = pass_generator2().strip()
    
    ENCRYPTED_USER = aes_encrypt(USUARI, key)
    ENCRYPTED_PASSWORD = aes_encrypt(GENERATEDPASSWORD, key)
    ENCRYPTED_SERVEI = aes_encrypt(SERVEI, key)
    
    with open("storage.txt", 'a') as archivo:
        archivo.write(f"Salt: {base64.b64encode(salt).decode('utf-8')}, Servei: {ENCRYPTED_SERVEI}, Usuari: {ENCRYPTED_USER}, Contrasenya: {ENCRYPTED_PASSWORD}\n")

pass_storage()
