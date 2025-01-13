# pass_manager.py
from inside_storage import pass_storage, get_passwords, delete_password, edit_password, usuari, servei, decrypt_storage
from GUI_manager import display_ui



def main():
    # Aquí se puede implementar el flujo principal de la aplicación
    def update():
        #aqui va tot l'apartat de lògica del programa.
        get_passwords()
        edit_password()
        delete_password()
        usuari()
        servei()
        pass_storage()
        decrypt_storage()
        update()
        
    def draw():
        #aqui va tot l'apartat visual del programa. en principi aqui es on s'ajunta la lògica amb la GUI.
        display_ui()
        draw

main
