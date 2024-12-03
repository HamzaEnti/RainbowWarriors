# pass_storage.py
import passwod from pass_encryption
def store_password():
     password = input("Introduce una contraseña para cifrar los datos: ").strip()
    salt = os.urandom(16)  # Generar un salt único
    key = PBKDF2(password, salt, dkLen=16, count=100000)  # Derivar la clave

    SERVEI = servei().strip()
    USUARI = usuari().strip()
    GENERATEDPASSWORD = pass_generator2().strip()

    ENCRYPTED_USER = aes_encrypt(USUARI, key)
    ENCRYPTED_PASSWORD = aes_encrypt(GENERATEDPASSWORD, key)
    ENCRYPTED_SERVEI = aes_encrypt(SERVEI, key)

    with open("storage.txt", 'a') as archivo:
        # Guardar salt y datos cifrados en una sola línea
        archivo.write(f"{base64.b64encode(salt).decode('utf-8')},{ENCRYPTED_SERVEI},{ENCRYPTED_USER},{ENCRYPTED_PASSWORD}\n")

def get_passwords():
    # Obtener todas las contraseñas almacenadas
    pass
def edit_password(name, new_password):
    # Editar una contraseña almacenada
    pass
def delete_password(name):
    # Eliminar una contraseña almacenada
    pass
#Això pregunta el nom que el usuari utilitza a les diferents plataformes de les que ha de guardar les contrasenyes i usuaris.
def usuari():
    USUARI = str(input("Usuari: "))
    return USUARI #Aquesta variable no es pot canviar. S'ha d'encriptar.
        
#Això pregunta el servei del que el usuari vol guartdar la contrasenya.
def servei():
    SERVEI = str(input("Servei: "))
    return SERVEI #Aquesta variable no espot canviar. S'ha d'encriptar.
