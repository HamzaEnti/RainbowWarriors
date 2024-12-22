from pass_encryption import aes_encrypt
from pass_generator import pass_generator2
from Crypto.Protocol.KDF import PBKDF2
from pass_decrypt import aes_decrypt
import os
import base64
import json
from pass_generator import pass_generator2


def get_passwords(length):
    return pass_generator2(length)



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
                        new_password = pass_generator2()
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

def pass_storage(service, user, password, master_password):
    """
    Guarda una nueva entrada en el archivo de almacenamiento cifrado.
    """
    import os
    import base64
    import json
    from pass_encryption import aes_encrypt
    from Crypto.Protocol.KDF import PBKDF2

    salt = os.urandom(16)  # Generar un salt único para esta entrada
    key = PBKDF2(master_password, salt, dkLen=16, count=100000)

    encrypted_service = aes_encrypt(service, key)
    encrypted_user = aes_encrypt(user, key)
    encrypted_password = aes_encrypt(password, key)

    new_entry = {
        "salt": base64.b64encode(salt).decode('utf-8'),
        "service": encrypted_service,
        "user": encrypted_user,
        "password": encrypted_password
    }

    try:
        with open("storage.json", "r") as file:
            try:
                storage_data = json.load(file)
                if not isinstance(storage_data, list):
                    raise ValueError("El archivo JSON no contiene una lista válida.")
            except json.JSONDecodeError:
                # Si el archivo está vacío o mal formateado, inicializamos una lista
                storage_data = []
    except FileNotFoundError:
        # Si el archivo no existe, inicializamos una lista vacía
        storage_data = []

    storage_data.append(new_entry)

    with open("storage.json", "w") as file:
        json.dump(storage_data, file, indent=4)

    print(f"Entrada para el servicio '{service}' guardada correctamente.")


def decrypt_storage(master_password):
    """
    Descifra y devuelve todas las entradas almacenadas en el archivo JSON.
    """
    import base64
    import json
    from Crypto.Protocol.KDF import PBKDF2
    from pass_decrypt import aes_decrypt

    try:
        with open("storage.json", "r") as json_file:
            storage_data = json.load(json_file)

        decrypted_data = []
        for entry in storage_data:
            try:
                salt = base64.b64decode(entry["salt"])
                key = PBKDF2(master_password, salt, dkLen=16, count=100000)

                decrypted_service = aes_decrypt(entry["service"], key)
                decrypted_user = aes_decrypt(entry["user"], key)
                decrypted_password = aes_decrypt(entry["password"], key)

                decrypted_data.append({
                    "service": decrypted_service,
                    "user": decrypted_user,
                    "password": decrypted_password,
                })
            except Exception as e:
                print(f"Error al descifrar una entrada: {e}")
        return decrypted_data

    except FileNotFoundError:
        print("El archivo 'storage.json' no se encontró.")
        return []
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return []

