import hashlib
import json

#prova

def encriptar_contraseña(contrasena):
    """
    Encripta la contraseña utilizando SHA-256.
    """
    sha256 = hashlib.sha256()
    sha256.update(contrasena.encode('utf-8'))
    return sha256.hexdigest()

def verificar_contraseña(archivo, usuario, contrasena_ingresada):
    """
    Verifica si la contraseña ingresada coincide con la almacenada en el archivo JSON.
    """
    try:
        with open(archivo, 'r') as file:
            contraseñas = json.load(file)
    except FileNotFoundError:
        print("El archivo de contraseñas no existe.")
        return False

    if usuario in contraseñas:
        hash_guardado = contraseñas[usuario]
        if encriptar_contraseña(contrasena_ingresada) == hash_guardado:
            return True
    return False

def guardar_contraseña(archivo, usuario, contrasena):
    """
    Guarda una nueva contraseña encriptada en el archivo JSON.
    """
    hash_contrasena = encriptar_contraseña(contrasena)
    
    try:
        with open(archivo, 'r') as file:
            contraseñas = json.load(file)
    except FileNotFoundError:
        contraseñas = {}

    contraseñas[usuario] = hash_contrasena
    
    with open(archivo, 'w') as file:
        json.dump(contraseñas, file, indent=4)
    
    print(f"Contraseña para '{usuario}' guardada exitosamente.")

def registrar_usuario(archivo, usuario, contrasena):
    """
    Registra un nuevo usuario guardando su contraseña encriptada.
    """
    guardar_contraseña(archivo, usuario, contrasena)
    print(f"Usuario '{usuario}' registrado exitosamente.")
    


"""
Per garantir la seguretat de les nostres bases de dades, hem de mantenir les dades dels usuaris encriptades, 
de manera que ni nosaltres puguem accedir-hi directament. Tot i això, els usuaris han de poder visualitzar les 
seves dades desencriptades un cop hagin iniciat sessió. Per aconseguir-ho, utilitzarem la contrasenya que l'usuari 
introdueix per iniciar sessió com a clau per encriptar i desencriptar les seves dades.

A més, com que estem emmagatzemant les credencials de login (usuaris i contrasenyes), 
aquestes també han d'estar encriptades per evitar que es puguin accedir en text pla. Cada vegada que un 
usuari iniciï sessió, el programa haurà d'encriptar les credencials introduïdes seguint el mateix algoritme 
i procés utilitzat per la base de dades (és a dir, d'una manera consistent, no aleatòria) i comparar-les 
amb les credencials emmagatzemades encriptades.
"""
