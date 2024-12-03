import subprocess
import sys

# Comprobar e instalar pycryptodome
def install_pycryptodome():
    try:
        import Crypto
    except ImportError:
        print("La biblioteca 'pycryptodome' no está instalada. Procediendo con la instalación...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pycryptodome"])
        print("Instalación completada. Reinicia el programa si encuentras algún problema.")

install_pycryptodome()

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64
from Crypto.Protocol.KDF import PBKDF2

def aes_decrypt(data, key):
    raw_data = base64.b64decode(data)
    iv = raw_data[:AES.block_size]
    ct = raw_data[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')

def decrypt_storage():
    password = input("Introduce tu contraseña para descifrar los datos: ").strip()
    
    try:
        with open("storage.txt", 'r') as archivo:
            for line in archivo:
                # Separar la línea en sus componentes
                parts = line.strip().split(", ")
                salt = base64.b64decode(parts[0].split(": ")[1])  # Extraer y decodificar el "salt"
                ENCRYPTED_SERVEI = parts[1].split(": ")[1]
                ENCRYPTED_USER = parts[2].split(": ")[1]
                ENCRYPTED_PASSWORD = parts[3].split(": ")[1]
                
                # Derivar la clave con el mismo "salt"
                key = PBKDF2(password, salt, dkLen=16, count=100000)
                
                # Desencriptar cada parte
                DECRYPTED_SERVEI = aes_decrypt(ENCRYPTED_SERVEI, key)
                DECRYPTED_USER = aes_decrypt(ENCRYPTED_USER, key)
                DECRYPTED_PASSWORD = aes_decrypt(ENCRYPTED_PASSWORD, key)
                
                # Mostrar la información desencriptada
                print(f"Servei: {DECRYPTED_SERVEI}, Usuari: {DECRYPTED_USER}, Contrasenya: {DECRYPTED_PASSWORD}")

    except FileNotFoundError:
        print("El archivo 'storage.txt' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    decrypt_storage()
