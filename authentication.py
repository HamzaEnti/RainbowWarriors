import getpass

# authentication.py
def login():    
    user = input("Username: ")
    passw = getpass.getpass("Password: ") #getpass pilla la contraseña, et dema un input i quan ho escrius no es veu exemple; Password: (123) lo que esta entre parentesis no es mostra en pantalla pero ho has escrit
    f = open("users.txt", "r") #Obre la base de dades, en un futur haurem de fer que en canvi de obrir un .txt que sobri una bdd
    # tota la funcio d'abaix el que fa es llegir el txt i comprova que estas escrivint be la password i username, quan sigui en bdd shaura de canviar
    for line in f.readlines():
        us, pw = line.strip().split("|")
        if (user in us) and (passw in pw):
            print ("Login successful!")
            return True
    print ("Wrong username/password")
    return False

def menu():
    print("Menu")
    #Aqui va el menu 

#comprova tot i fa que entris al menu
def main():
    while True:
        log = login()
        if log == True:
             menu()
             break


main()
