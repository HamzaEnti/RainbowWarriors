import getpass

# authentication.py
def login():    
    user = input("Username: ")
    passw = getpass.getpass("Password: ")
    f = open("users.txt", "r")
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

def main():
    while True:
        log = login()
        if log == True:
             menu()
             break


main()