# pass_storage.py
def store_password(name, password):
    # Almacenar la contraseña de forma segura
    pass

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
        
