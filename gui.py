import tkinter as tk
from tkinter import ttk
from authentication import login

def display_ui():
    """
    Interfaz gráfica principal para login.
    """
    def handle_login():
        username = username_entry.get()
        password = password_entry.get()
        
        if login(username, password):
            show_password_manager(username)
        else:
            login_status.config(text="Usuario o contraseña incorrectos", fg="red")

    def show_password_manager(username):
        """
        Cambia a la ventana del gestor de contraseñas.
        """
        # Eliminar todos los widgets de la ventana actual
        for widget in root.winfo_children():
            widget.destroy()

        # Cambiar el fondo de la ventana y el título
        root.config(bg="white")
        root.title("RainbowWarriors - Gestor de Contraseñas")

        # Encabezado
        header_frame = tk.Frame(root, bg="white")
        header_frame.pack(fill="x", pady=5)

        # Título
        tk.Label(header_frame, text="RainbowWarriors - Password Manager", font=("Arial", 16, "bold"), bg="white").pack(side="left", padx=10)

        # Campo de búsqueda
        search_entry = tk.Entry(header_frame, font=("Arial", 12), width=30)
        search_entry.pack(side="left", padx=10)
        tk.Button(header_frame, text="Search", font=("Arial", 10), bg="#444444", fg="white").pack(side="left", padx=10)

        # Texto para mostrar el usuario
        tk.Label(header_frame, text=f"Logged in as: {username}", font=("Arial", 10), bg="white").pack(side="left", padx=10)

        # Botones
        tk.Button(header_frame, text="new entry", font=("Arial", 10), bg="#444444", fg="white").pack(side="right", padx=10)
        tk.Button(header_frame, text="logout", font=("Arial", 10), bg="#FF5733", fg="white", command=display_login).pack(side="right", padx=10)

        # Tabla para mostrar contraseñas
        table_frame = tk.Frame(root, bg="white")
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        columns = ("name", "username", "password")
        table = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)

        # Definir encabezados de columnas
        table.heading("name", text="Name")
        table.heading("username", text="Username")
        table.heading("password", text="Password")

        # Configurar tamaño de columnas
        table.column("name", width=150)
        table.column("username", width=150)
        table.column("password", width=150)

        # Insertar datos de ejemplo
    
        table.pack(fill="both", expand=True)

    def display_login():
        """
        Muestra la pantalla de inicio de sesión.
        """
        # Eliminar todos los widgets de la ventana actual
        for widget in root.winfo_children():
            widget.destroy()

        # Configurar de nuevo la ventana para la pantalla de inicio
        root.config(bg="#f5f5f5")
        root.title("RainbowWarriors - Login")

        # Cargar logo
        logo_label = tk.Label(root, image=logo, bg="#f5f5f5")
        logo_label.image = logo  # Mantener referencia
        logo_label.pack(pady=10)

        # Widgets de login
        tk.Label(root, text="Username:", font=("Arial", 12), bg="#f5f5f5").pack(pady=5)
        nonlocal username_entry, password_entry  # Para que se pueda usar fuera de esta función
        username_entry = tk.Entry(root, font=("Arial", 12), width=25)
        username_entry.pack(pady=5)

        tk.Label(root, text="Password:", font=("Arial", 12), bg="#f5f5f5").pack(pady=5)
        password_entry = tk.Entry(root, show="*", font=("Arial", 12), width=25)
        password_entry.pack(pady=5)

        login_button = tk.Button(root, text="Login", font=("Arial", 12), bg="#444444", fg="white", width=15, command=handle_login)
        login_button.pack(pady=20)

        nonlocal login_status  # Permitir acceso desde fuera de la función
        login_status = tk.Label(root, text="", font=("Arial", 10), bg="#f5f5f5")
        login_status.pack(pady=5)

    # Ventana principal
    root = tk.Tk()
    root.title("RainbowWarriors - Login")
    root.geometry("1200x600")  # Ventana más rectangular
    root.config(bg="#f5f5f5")

    # Cargar logo
    logo = tk.PhotoImage(file="logo.png")
    logo = logo.subsample(4, 4)  # Redimensionar el logo

    # Variables necesarias para widgets reutilizables
    username_entry = None
    password_entry = None
    login_status = None

    # Mostrar pantalla de inicio
    display_login()

    root.mainloop()

display_ui()

