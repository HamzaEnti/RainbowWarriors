from pass_encryption import aes_encrypt
from pass_generator import pass_generator2
from Crypto.Protocol.KDF import PBKDF2
import os
import base64


def get_passwords():
    GENERATEDPASSWORD = pass_generator2()
   
get_passwords()


def edit_password(name, new_password):
    # Editar una contraseña almacenada
    pass
def delete_password(name):
    # Eliminar una contraseña almacenada
    pass

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
    GENERATEDPASSWORD = pass_generator2().strip()

    ENCRYPTED_USER = aes_encrypt(USUARI, key) #encripta l'usuari
    ENCRYPTED_PASSWORD = aes_encrypt(GENERATEDPASSWORD, key) #encripta la contrasenya
    ENCRYPTED_SERVEI = aes_encrypt(SERVEI, key) #encripta el servei

    with open("storage.txt", 'a') as archivo:
        # Guardar salt y datos cifrados en una sola línea
        archivo.write(f"{base64.b64encode(salt).decode('utf-8')},{ENCRYPTED_SERVEI},{ENCRYPTED_USER},{ENCRYPTED_PASSWORD}\n") # crea el arxiu storage per guardar el usuari servei i contrasenya emmagatzemats.

pass_storage()
