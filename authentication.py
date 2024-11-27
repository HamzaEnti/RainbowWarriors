def login(username, password): #Aquesta password es la que hem d'utilitzar per encriptar i desencriptar la resta de dades, es la clau.
    """
    Valida las credenciales del usuario desde un archivo de texto.
    """
    with open("users.txt", "r") as f:
        for line in f.readlines():
            us, pw = line.strip().split("|")
            if username == us and password == pw:
                return True
    return False
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
