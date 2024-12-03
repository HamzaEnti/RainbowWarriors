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
                # Separar los componentes de cada línea
                parts = line.strip().split(",")
                salt = base64.b64decode(parts[0])  # Decodificar el salt
                ENCRYPTED_SERVEI = parts[1]
                ENCRYPTED_USER = parts[2]
                ENCRYPTED_PASSWORD = parts[3]

                # Derivar la clave con el salt
                key = PBKDF2(password, salt, dkLen=16, count=100000)

                try:
                    # Intentar desencriptar
                    DECRYPTED_SERVEI = aes_decrypt(ENCRYPTED_SERVEI, key)
                    DECRYPTED_USER = aes_decrypt(ENCRYPTED_USER, key)
                    DECRYPTED_PASSWORD = aes_decrypt(ENCRYPTED_PASSWORD, key)

                    # Mostrar el registro desencriptado
                    print(f"Servei: {DECRYPTED_SERVEI}, Usuari: {DECRYPTED_USER}, Contrasenya: {DECRYPTED_PASSWORD}")
                except Exception:
                    # Si falla, la contraseña no corresponde a este registro
                    print("Contraseña incorrecta para este registro.")

    except FileNotFoundError:
        print("El archivo 'storage.txt' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    decrypt_storage()
