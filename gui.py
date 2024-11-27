import tkinter as tk
from authentication import login

def display_ui():
    """
    Interfaz gráfica principal para login.
    """
    def handle_login():
        username = username_entry.get()
        password = password_entry.get()
        
        if login(username, password):
            show_password_manager()
        else:
            login_status.config(text="Usuario o contraseña incorrectos", fg="red")

    def show_password_manager():
        """
        Cambia a la ventana del gestor de contraseñas.
        """
        # Eliminar todos los widgets de la ventana actual
        for widget in root.winfo_children():
            widget.destroy()

        # Cambiar el fondo a blanco (pantalla en blanco)
        root.config(bg="white")
        root.title("Gestor de Contraseñas")

    # Ventana principal
    root = tk.Tk()
    root.title("RainbowWarriors - Login")
    root.geometry("450x400")
    root.config(bg="#f5f5f5")
    root.iconbitmap("myIcon.ico")

    # Cargar logo
    logo = tk.PhotoImage(file="logo.png")
    logo = logo.subsample(4, 4)  # Redimensiona el logo
    logo_label = tk.Label(root, image=logo, bg="#f5f5f5")
    logo_label.image = logo  # Mantener referencia
    logo_label.pack(pady=10)

    # Widgets de login
    tk.Label(root, text="Username:", font=("Arial", 12), bg="#f5f5f5").pack(pady=5)
    username_entry = tk.Entry(root, font=("Arial", 12), width=25)
    username_entry.pack(pady=5)

    tk.Label(root, text="Password:", font=("Arial", 12), bg="#f5f5f5").pack(pady=5)
    password_entry = tk.Entry(root, show="*", font=("Arial", 12), width=25)
    password_entry.pack(pady=5)

    login_button = tk.Button(root, text="Login", font=("Arial", 12), bg="#4CAF50", fg="white", width=15, command=handle_login)
    login_button.pack(pady=20)

    login_status = tk.Label(root, text="", font=("Arial", 10), bg="#f5f5f5")
    login_status.pack(pady=5)

    root.mainloop()


display_ui()
