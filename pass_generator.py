# Ho ha de fer el Nico
# pass_generator.py
import secrets
import string


def pass_generator():
    num = int(input("Length:"))
    alfabet = string.ascii_letters + string.digits
    password = "" .join(secrets.choice(alfabet) for char in range(num))
    return print(password)

pass_generator()
