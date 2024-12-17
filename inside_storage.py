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


def edit_password(service_name):
    password = input("Introduce la contraseña maestra para editar los datos: ").strip()
    try:
        with open("storage.json", 'r') as json_file:
            storage_data = json.load(json_file)

        updated = False
        for entry in storage_data:
            salt = base64.b64decode(entry["salt"])
            key = PBKDF2(password, salt, dkLen=16, count=100000)

            try:
                DECRYPTED_SERVEI = aes_decrypt(entry["service"], key)
                if DECRYPTED_SERVEI == service_name:
                    # Generar nueva contraseña
                    new_password = get_passwords()
                    ENCRYPTED_NEW_PASSWORD = aes_encrypt(new_password, key)

                    # Actualizar la entrada con la nueva contraseña
                    entry["password"] = ENCRYPTED_NEW_PASSWORD
                    updated = True

                    print(f"Nueva contraseña generada automáticamente para '{service_name}': {new_password}")
                    break
            except Exception as e:
                print(f"Error al descifrar el servicio: {e}")

        if updated:
            with open("storage.json", 'w') as json_file:
                json.dump(storage_data, json_file, indent=4)
            print(f"Contraseña para el servicio '{service_name}' editada correctamente.")
        else:
            print(f"No se encontró el servicio '{service_name}' o la contraseña maestra no coincide.")

    except FileNotFoundError:
        print("El archivo 'storage.json' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def delete_password(service_name):
    password = input("Introduce la contraseña maestra para eliminar los datos: ").strip()
    try:
        with open("storage.json", 'r') as json_file:
            storage_data = json.load(json_file)

        new_data = []
        deleted = False
        for entry in storage_data:
            salt = base64.b64decode(entry["salt"])
            key = PBKDF2(password, salt, dkLen=16, count=100000)

            try:
                DECRYPTED_SERVEI = aes_decrypt(entry["service"], key)
                if DECRYPTED_SERVEI == service_name:
                    deleted = True
                    continue
                new_data.append(entry)
            except Exception as e:
                print(f"Error al descifrar el servicio: {e}")

        if deleted:
            with open("storage.json", 'w') as json_file:
                json.dump(new_data, json_file, indent=4)
            print(f"Servicio '{service_name}' eliminado correctamente.")
        else:
            print(f"No se encontró el servicio '{service_name}' o la contraseña maestra no coincide.")

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

def pass_storage():
    password = input("Introduce una contraseña para cifrar los datos: ").strip()
    salt = os.urandom(16)
    key = PBKDF2(password, salt, dkLen=16, count=100000)

    SERVEI = servei().strip()
    USUARI = usuari().strip()
    GNPASS = get_passwords().strip()

    ENCRYPTED_USER = aes_encrypt(USUARI, key)
    ENCRYPTED_PASSWORD = aes_encrypt(GNPASS, key)
    ENCRYPTED_SERVEI = aes_encrypt(SERVEI, key)

    DADES = {
        "salt": base64.b64encode(salt).decode('utf-8'),
        "service": ENCRYPTED_SERVEI,
        "user": ENCRYPTED_USER,
        "password": ENCRYPTED_PASSWORD
    }

    try:
        with open("storage.json", 'r') as json_file:
            storage_data = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        storage_data = []

    storage_data.append(DADES)

    with open("storage.json", 'w') as json_file:
        json.dump(storage_data, json_file, indent=4)
        print("El archivo 'storage.json' ha sido actualizado correctamente.")


def decrypt_storage():
    password = input("Introduce tu contraseña maestra para descifrar los datos: ").strip()

    try:
        with open("storage.json", 'r') as json_file:
            storage_data = json.load(json_file)

        for entry in storage_data:
            try:
                salt = base64.b64decode(entry["salt"])
                key = PBKDF2(password, salt, dkLen=16, count=100000)

                DECRYPTED_SERVEI = aes_decrypt(entry["service"], key)
                DECRYPTED_USER = aes_decrypt(entry["user"], key)
                DECRYPTED_PASSWORD = aes_decrypt(entry["password"], key)

                print(f"Servei: {DECRYPTED_SERVEI}, Usuari: {DECRYPTED_USER}, Contrasenya: {DECRYPTED_PASSWORD}")
            except Exception:
                print("Contraseña maestra incorrecta para este registro.")

    except FileNotFoundError:
        print("El archivo 'storage.json' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    while True:
        print("\nOpciones:")
        print("1. Añadir contraseña")
        print("2. Editar contraseña")
        print("3. Eliminar contraseña")
        print("4. Mostrar contraseñas")
        print("5. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            pass_storage()
        elif opcion == "2":
            NomServei = input("Introduce el nombre del servicio a editar: ").strip()
            new_password = input("Introduce la nueva contraseña: ").strip()
            edit_password(NomServei, new_password)
        elif opcion == "3":
            NomServei = input("Introduce el nombre del servicio a eliminar: ").strip()
            delete_password(NomServei)
        elif opcion == "4":
            decrypt_storage()
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")
