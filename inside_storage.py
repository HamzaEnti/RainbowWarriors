from pass_encryption import aes_encrypt
from pass_generator import pass_generator2
from Crypto.Protocol.KDF import PBKDF2
from pass_decrypt import aes_decrypt
import os
import base64
import json



def get_passwords():
    GENERATEDPASSWORD = pass_generator2()
    return GENERATEDPASSWORD


def edit_password(NomServei, new_password):
    # Editar una contraseña almacenada
    password = input("Introduce la contraseña para cifrar los datos: ").strip()
    salt = os.urandom(16)  # Generar un salt únic
    key = PBKDF2(password, salt, dkLen=16, count=100000)  # Derivar la clau

    try:
        with open("storage.json", 'r') as json_file:
            storage_data = json.load(json_file)

        for entry in storage_data:
            if entry["service"] == NomServei:
                new_encrypted_password = aes_encrypt(new_password, key) # Actualitzar la contrasenya
                entry["password"] = new_encrypted_password
                entry["salt"] = base64.b64encode(salt).decode('utf-8')  # Actualitzar el salt
                break
        else:
            print("Servicio no encontrado.")

        
        with open("storage.json", 'w') as json_file: # Escriure la informació nova de nou al Json
            json.dump(storage_data, json_file, indent=4)

    except FileNotFoundError:
        print("El archivo 'storage.json' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    pass
    
def delete_password(NomServei):
    try:
        with open("storage.json", 'r') as json_file:
            storage_data = json.load(json_file)

       
        new_storage_data = [entry for entry in storage_data if entry["service"] != NomServei]  # filtrar el que s'ah d'eliminar

        if len(new_storage_data) == len(storage_data):
            print("Servicio no encontrado.")
        else:
            print(f"Servicio '{NomServei}' eliminado.")

        
        with open("storage.json", 'w') as json_file: # escriure les noves dades
            json.dump(new_storage_data, json_file, indent=4)

    except FileNotFoundError:
        print("El archivo 'storage.json' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def usuari():#Això pregunta el nom que el usuari utilitza a les diferents plataformes de les que ha de guardar les contrasenyes i usuaris.
    USUARI = str(input("Usuari: "))
    return USUARI #Aquesta variable no es pot canviar. S'ha d'encriptar.
        

def servei():#Això pregunta el servei del que el usuari vol guartdar la contrasenya.
    SERVEI = str(input("Servei: "))
    return SERVEI #Aquesta variable no espot canviar. S'ha d'encriptar.



def pass_storage(): #emmagatzemar la contrasenya
    password = input("Introduce una contraseña para cifrar los datos: ").strip()
    salt = os.urandom(16)  # Generar un salt únic
    key = PBKDF2(password, salt, dkLen=16, count=100000)  # Derivar la clave

    SERVEI = servei().strip()
    USUARI = usuari().strip()
    GNPASS = get_passwords().strip()

    ENCRYPTED_USER = aes_encrypt(USUARI, key) #encripta l'usuari
    ENCRYPTED_PASSWORD = aes_encrypt(GNPASS, key) #encripta la contrasenya
    ENCRYPTED_SERVEI = aes_encrypt(SERVEI, key) #encripta el servei

    #Per fer un json hem de preparar les dades que vole emmagatzemar.
    DADES = {
        "salt": base64.b64encode(salt).decode('utf-8'),
        "service": ENCRYPTED_SERVEI,
        "user": ENCRYPTED_USER,
        "password": ENCRYPTED_PASSWORD
    }
    # Això passa per el json si ja esta creat o crea un en cs de que no estigui creat.
    try:
        with open("storage.json", 'r') as json_file:
            storage_data = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        storage_data = []

    # incloeix la nova infromació
    storage_data.append(data)

    # escriu la nova informació al json
    with open("storage.json", 'w') as json_file:
        json.dump(storage_data, json_file, indent=4)  # perque es vegui millor, es estetic

pass_storage()

def decrypt_storage(): # Això demana la contrasenya key que cada ususari tindra i no ha d'oblidar per desencriptar i encriptar.
    password = input("Introduce tu contraseña para descifrar los datos: ").strip()
    
    try:
         with open("storage.json", 'r') as json_file:
            storage_data = json.load(json_file)

            for entry in storage_data:
                # Separar los componentes de cada línea
                salt = base64.b64decode(entry["salt"])   # Decodificar el salt
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
        print("El archivo 'storage.json' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    decrypt_storage()
