# pass_generator.py
import secrets
import string

def preguntes():
    #Aixo fa la contrasenya.
    def pass_generator():
        num = int(input("Length:"))# Això marca la llargada de la contrasenya. En principu a la GUI no es pot escollir res que no sigui numero, per lo tant no s'ha de fer error management. 
        alfabet = string.ascii_letters + string.digits
        GENERATEDPASSWORD = "" .join(secrets.choice(alfabet) for char in range(num))
        return GENERATEDPASSWORD #Aquesta variable no es pot canviar. Aquesta variable s'ha d'encriptar.
        
    #Això pregunta el nom que el usuari utilitza a les diferents plataformes de les que ha de guardar les contrasenyes i usuaris.
    def usuari():
        USUARI = str(input("Usuari: "))
        return USUARI #Aquesta variable no es pot canviar. S'ha d'encriptar.
        
    #Això pregunta el servei del que el usuari vol guartdar la contrasenya.
    def servei():
        SERVEI = str(input("Servei: "))
        return SERVEI #Aquesta variable no espot canviar. S'ha d'encriptar.
        
  


    
