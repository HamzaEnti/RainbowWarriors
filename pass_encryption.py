from pass_generator import pass_generator2 
from general_storage import usuari
from general_storage import servei

def xor_encrypt_decrypt(input_string, KEY):
    return ''.join(chr(ord(char) ^ KEY) for char in input_string) #Cifra o descifra una cadena usando XOR con una clave.

def pass_storage():
    KEY = int(input("Crear clave de acceso (0-255): "))  # Asegúrate de que la clave esté en el rango adecuado.
    if not (0 <= KEY <= 255):
        print("La clave debe estar entre 0 y 255.")
        return
    SERVEI = servei().strip() 
    USUARI = usuari().strip()  
    GENERATEDPASSWORD = pass_generator2().strip()
    ENCRYPTED_USER = xor_encrypt_decrypt(USUARI, KEY)
    ENCRYPTED_PASSWORD = xor_encrypt_decrypt(GENERATEDPASSWORD, KEY)
    ENCRYPTED_SERVEI = xor_encrypt_decrypt(SERVEI, KEY)
    with open("storage.txt", 'a') as archivo:
        archivo.write(f"Servei: {ENCRYPTED_SERVEI}, Usuari: {ENCRYPTED_USER}, Contrasenya: {ENCRYPTED_PASSWORD}\n")
pass_storage()
