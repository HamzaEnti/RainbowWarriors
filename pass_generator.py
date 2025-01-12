import secrets
import string

def pass_generator2(length):
    if length <= 0:
        raise ValueError("La longitud debe ser un número positivo.")
    alfabet = string.asciiletters + string.digits + string.punctuation

    GENERATEDPASSWORD = "".join(secrets.choice(alfabet) for  in range(length))
    return GENERATEDPASSWORD
