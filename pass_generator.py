# pass_generator.py
import secrets
import string

#Això genera la contrasenya, en cas de que l'usuari no tingui una contrasenya que guardar.
def pass_generator2():
    num = int(input("Length:"))# Això marca la llargada de la contrasenya. En principu a la GUI no es pot escollir res que no sigui numero, per lo tant no s'ha de fer error management. 
    alfabet = string.ascii_letters + string.digits
    GENERATEDPASSWORD = "" .join(secrets.choice(alfabet) for char in range(num))
    return GENERATEDPASSWORD #Aquesta variable no es pot canviar. Aquesta variable s'ha d'encriptar.
        

  


    
