def login(username, password):
    """
    Valida las credenciales del usuario desde un archivo de texto.
    """
    with open("users.txt", "r") as f:
        for line in f.readlines():
            us, pw = line.strip().split("|")
            if username == us and password == pw:
                return True
    return False
