# pass_generator.py
import secrets
import string

#Aixo fa la contrasenya.
def pass_generator():
    num = int(input("Length:"))# Això marca la llargada de la contrasenya. En principu a la GUI no es pot escollir res que no sigui numero, per lo tant no s'ha de fer error management. 
    alfabet = string.ascii_letters + string.digits
    GENERATEDPASSWORD = "" .join(secrets.choice(alfabet) for char in range(num))
    return GENERATEDPASSWORD #aquesta variable no es pot canviar
    
