import tkinter as tk
from tkinter import ttk
from authentication import registrar_usuario, verificar_contraseña

def display_ui():
    """
    Interfaz gráfica principal para login.
    """
    def handle_login():
        username = username_entry.get()
        password = password_entry.get()
        
        if not username or not password:
            login_status.config(text="Por favor ingresa usuario y contraseña", fg="red")
            return
        
        if verificar_contraseña('contraseñas.json', username, password):
            show_password_manager(username)
        else:
            login_status.config(text="Usuario o contraseña incorrectos", fg="red")

    def show_password_manager(username):
        """
        Cambia a la ventana del gestor de contraseñas.
        """
        for widget in root.winfo_children():
            widget.destroy()

        root.config(bg="white")
        root.title("RainbowWarriors - Gestor de Contraseñas")

        header_frame = tk.Frame(root, bg="white")
        header_frame.pack(fill="x", pady=5)

        tk.Label(header_frame, text="RainbowWarriors - Password Manager", font=("Arial", 16, "bold"), bg="white").pack(side="left", padx=10)
        search_entry = tk.Entry(header_frame, font=("Arial", 12), width=30)
        search_entry.pack(side="left", padx=10)
        tk.Button(header_frame, text="Search", font=("Arial", 10), bg="#444444", fg="white").pack(side="left", padx=10)
        tk.Label(header_frame, text=f"Logged in as: {username}", font=("Arial", 10), bg="white").pack(side="left", padx=10)
        tk.Button(header_frame, text="new entry", font=("Arial", 10), bg="#444444", fg="white").pack(side="right", padx=10)
        tk.Button(header_frame, text="logout", font=("Arial", 10), bg="#FF5733", fg="white", command=display_login).pack(side="right", padx=10)

        table_frame = tk.Frame(root, bg="white")
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        columns = ("name", "username", "password")
        table = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)
        table.heading("name", text="Name")
        table.heading("username", text="Username")
        table.heading("password", text="Password")
        table.column("name", width=150)
        table.column("username", width=150)
        table.column("password", width=150)
        table.pack(fill="both", expand=True)

    def display_login():
        """
        Muestra la pantalla de inicio de sesión.
        """
        nonlocal login_status  # Asegura que login_status sea accesible
        for widget in root.winfo_children():
            widget.destroy()

        root.config(bg="#f5f5f5")
        root.title("RainbowWarriors - Login")

        logo_label = tk.Label(root, image=logo, bg="#f5f5f5")
        logo_label.image = logo
        logo_label.pack(pady=10)

        tk.Label(root, text="Username:", font=("Arial", 12), bg="#f5f5f5").pack(pady=5)
        nonlocal username_entry, password_entry
        username_entry = tk.Entry(root, font=("Arial", 12), width=25)
        username_entry.pack(pady=5)

        tk.Label(root, text="Password:", font=("Arial", 12), bg="#f5f5f5").pack(pady=5)
        password_entry = tk.Entry(root, show="*", font=("Arial", 12), width=25)
        password_entry.pack(pady=5)

        login_button = tk.Button(root, text="Login", font=("Arial", 12), bg="#444444", fg="white", width=15, command=handle_login)
        login_button.pack(pady=20)

        login_status = tk.Label(root, text="", font=("Arial", 10), bg="#f5f5f5")
        login_status.pack(pady=5)

        register_button = tk.Button(root, text="Crear Cuenta", font=("Arial", 12), bg="#FF5733", fg="white", command=display_registration)
        register_button.pack(pady=10)

    def display_registration():
        """
        Muestra la pantalla de registro de usuarios.
        """
        def handle_registration():
            username = username_entry.get()
            password = password_entry.get()
            confirm_password = confirm_password_entry.get()

            if password != confirm_password:
                registration_status.config(text="Las contraseñas no coinciden", fg="red")
                return

            if not username or not password:
                registration_status.config(text="Por favor, completa todos los campos.", fg="red")
                return

            registrar_usuario('contraseñas.json', username, password)
            registration_status.config(text="Usuario registrado con éxito", fg="green")
            display_login()

        for widget in root.winfo_children():
            widget.destroy()

        root.title("RainbowWarriors - Registro")
        
        tk.Label(root, text="Registro de Usuario", font=("Arial", 16, "bold")).pack(pady=10)

        tk.Label(root, text="Nombre de usuario:", font=("Arial", 12)).pack(pady=5)
        username_entry = tk.Entry(root, font=("Arial", 12), width=25)
        username_entry.pack(pady=5)
        
        tk.Label(root, text="Contraseña:", font=("Arial", 12)).pack(pady=5)
        password_entry = tk.Entry(root, show="*", font=("Arial", 12), width=25)
        password_entry.pack(pady=5)

        tk.Label(root, text="Confirmar contraseña:", font=("Arial", 12)).pack(pady=5)
        confirm_password_entry = tk.Entry(root, show="*", font=("Arial", 12), width=25)
        confirm_password_entry.pack(pady=5)

        register_button = tk.Button(root, text="Registrar", font=("Arial", 12), bg="#444444", fg="white", width=15, command=handle_registration)
        register_button.pack(pady=20)

        registration_status = tk.Label(root, text="", font=("Arial", 10), bg="#f5f5f5")
        registration_status.pack(pady=5)
        
    root = tk.Tk()
    root.title("RainbowWarriors - Login")
    root.geometry("1200x600")
    root.config(bg="#f5f5f5")
    logo = tk.PhotoImage(file="logo.png")
    logo = logo.subsample(4, 4)
    username_entry = None
    password_entry = None
    login_status = None  # Declaración inicial
    display_login()
    root.mainloop()

display_ui()
