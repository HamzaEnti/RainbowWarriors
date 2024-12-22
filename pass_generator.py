import secrets
import string

def pass_generator2(length):
    if length <= 0:
        raise ValueError("La longitud debe ser un número positivo.")
    alfabet = string.ascii_letters + string.digits
    GENERATEDPASSWORD = "".join(secrets.choice(alfabet) for _ in range(length))
    return GENERATEDPASSWORD
