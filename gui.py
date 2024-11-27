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
            login_status.config(text="Login exitoso", fg="green")
        else:
            login_status.config(text="Usuario o contraseña incorrectos", fg="red")

    # Ventana principal
    root = tk.Tk()
    root.title("RainbowWarriors - Login")
    root.geometry("450x300")
    root.config(bg="#f5f5f5")
    root.iconbitmap("myIcon.ico")

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
