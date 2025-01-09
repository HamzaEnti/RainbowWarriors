import tkinter as tk
from tkinter import ttk, messagebox
from authentication import registrar_usuario, verificar_contraseña
import inside_storage



def display_ui():
    """
    Interfaz gráfica principal para login y gestor de contraseñas.
    """

    def handle_login():
        username = username_entry.get()
        password = password_entry.get()

        if not username or not password:
            login_status.config(text="Por favor, ingresa usuario y contraseña", fg="red")
            return

        try:
            if verificar_contraseña('contraseñas.json', username, password):
                show_password_manager(username)
            else:
                login_status.config(text="Usuario o contraseña incorrectos", fg="red")
                username_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
        except Exception as e:
                messagebox.showerror("Error", f"Error durante el login: {e}")
    def new_entry_window():
        """
        Ventana para crear una nueva entrada de contraseña.
        """
        new_window = tk.Toplevel()
        new_window.title("Nueva Entrada")
        new_window.geometry("400x400")

        def generate_password():
            try:
                length = int(length_entry.get())  # Obtenemos la longitud de la entrada
                if length <= 0:
                    raise ValueError("La longitud debe ser positiva.")
                generated_password = inside_storage.get_passwords(length)  # Generamos la contraseña
                password_entry.delete(0, tk.END)
                password_entry.insert(0, generated_password)
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingresa un número válido para la longitud.")
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error: {e}")

        def save_entry():
            servicio = service_entry.get().strip()
            usuario = user_entry.get().strip()
            password = password_entry.get().strip()
            master_password = master_password_entry.get().strip()

            if not all([servicio, usuario, password, master_password]):
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return

            try:
                # Llamada a la función pass_storage con los argumentos correctos
                inside_storage.pass_storage(servicio, usuario, password, master_password)
                messagebox.showinfo("Éxito", "Contraseña guardada correctamente.")
                update_password_table()
                new_window.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error al guardar: {e}")

        # Campos para la nueva entrada
        tk.Label(new_window, text="Servicio:").pack(pady=5)
        service_entry = tk.Entry(new_window)
        service_entry.pack(pady=5)

        tk.Label(new_window, text="Usuario:").pack(pady=5)
        user_entry = tk.Entry(new_window)
        user_entry.pack(pady=5)

        tk.Label(new_window, text="Longitud de la Contraseña:").pack(pady=5)
        length_entry = tk.Entry(new_window)  # Campo para la longitud
        length_entry.pack(pady=5)

        tk.Button(new_window, text="Generar Contraseña Segura", command=generate_password).pack(pady=10)

        tk.Label(new_window, text="Contraseña:").pack(pady=5)
        password_entry = tk.Entry(new_window)
        password_entry.pack(pady=5)

        tk.Label(new_window, text="Contraseña Maestra:").pack(pady=5)
        master_password_entry = tk.Entry(new_window, show="*")
        master_password_entry.pack(pady=5)

        tk.Button(new_window, text="Guardar", command=save_entry).pack(pady=10)

    def update_password_table():
        """
        Actualiza la tabla con las contraseñas descifradas.
        """
        table.delete(*table.get_children())

        # Solicitar la contraseña maestra desde la entrada en la GUI
        master_password = master_password_entry.get().strip()

        if not master_password:
            messagebox.showerror("Error", "Por favor, introduce la contraseña maestra.")
            return

        try:
            decrypted_data = inside_storage.decrypt_storage(master_password)
            for entry in decrypted_data:
                table.insert("", "end", values=(entry["service"], entry["user"], entry["password"]))
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo actualizar la tabla: {e}")

    def show_password_manager(username):

        global master_password_entry


        for widget in root.winfo_children():
            widget.destroy()

        root.title("RainbowWarriors - Gestor de Contraseñas")
        root.geometry("900x500")


        header_frame = tk.Frame(root, bg="#f5f5f5")
        header_frame.pack(fill="x", pady=5)

        tk.Label(header_frame, text="RainbowWarriors - Password Manager", font=("Arial", 16, "bold"), bg="#f5f5f5").pack(side="left", padx=10)
        tk.Label(header_frame, text=f"Logged in as: {username}", font=("Arial", 10), bg="#f5f5f5").pack(side="right", padx=10)

        master_password_frame = tk.Frame(root, bg="#f5f5f5")
        master_password_frame.pack(pady=20)
        
        tk.Label(master_password_frame, text="Contraseña Maestra:", font=("Arial", 14), bg="#f5f5f5").pack(side="left", padx=10)
        master_password_entry = tk.Entry(master_password_frame, show="*", font=("Arial", 12), width=30)
        master_password_entry.pack(side="left", padx=10)

        tk.Button(master_password_frame, text="Actualizar", font=("Arial", 10), bg="#444444", fg="white", command=update_password_table).pack(side="left", padx=10)



        tk.Button(header_frame, text="Nueva Entrada", font=("Arial", 10), bg="#444444", fg="white", command=new_entry_window).pack(side="right", padx=10)
        tk.Button(header_frame, text="Logout", font=("Arial", 10), bg="#6f52ed", fg="white", command=display_login).pack(side="right", padx=10)

        table_frame = tk.Frame(root, bg="#f5f5f5")
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        columns = ("service", "username", "password")
        global table
        table = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)
        table.heading("service", text="Service")
        table.heading("username", text="Username")
        table.heading("password", text="Password")
        table.column("service", width=150)
        table.column("username", width=150)
        table.column("password", width=150)
        table.pack(fill="both", expand=True)


    def display_login():
        for widget in root.winfo_children():
            widget.destroy()

        root.title("Inicia la sessió - RainbowWarriors")
        root.geometry("400x500")
        root.configure(bg="#f5f5f5")
        root.iconbitmap("myIcon.ico")

        # Título principal
        tk.Label(
            root,
            text="Inicia la sessió",
            font=("Arial", 18, "bold"),
            bg="#f5f5f5",
            fg="#000000"
        ).pack(pady=10)

        tk.Label(
            root,
            text="Introduïu els detalls del vostre compte de RW",
            font=("Arial", 12),
            bg="#f5f5f5",
            fg="#666666"
        ).pack(pady=5)

        # Campo de correo/nombre de usuario
        tk.Label(root, text="Correu electrònic o nom d'usuari", font=("Arial", 10), bg="#f5f5f5").pack(pady=(20, 5))
        nonlocal username_entry
        username_entry = tk.Entry(root, font=("Arial", 12), width=30, bd=1, relief="solid")
        username_entry.pack(pady=5)

        # Campo de contraseña
        tk.Label(root, text="Contrasenya", font=("Arial", 10), bg="#f5f5f5").pack(pady=(20, 5))
        nonlocal password_entry
        password_entry = tk.Entry(root, font=("Arial", 12), width=30, bd=1, relief="solid", show="*")
        password_entry.pack(pady=5)

        # Botón de login
        tk.Button(
            root,
            text="Inicia la sessió",
            font=("Arial", 12, "bold"),
            bg="#6f52ed",
            fg="white",
            width=20,
            command=handle_login  # Vinculamos con la función de login existente
        ).pack(pady=20)

        # Enlaces inferiores
        tk.Label(root, text="Sou nou a RW?", font=("Arial", 10), bg="#f5f5f5", fg="#666666").pack(pady=(10, 0))
        tk.Button(
            root,
            text="Crea un compte",
            font=("Arial", 10),
            bg="#f5f5f5",
            fg="#6f52ed",
            bd=0,
            command=display_registration  # Cambiamos a la función de registro
        ).pack()



    def display_registration():
        def handle_registration(username_entry, password_entry, confirm_password_entry, registration_status):
            username = username_entry.get()
            password = password_entry.get()
            confirm_password = confirm_password_entry.get()

            if not username or not password or not confirm_password:
                registration_status.config(text="Tots els camps són obligatoris", fg="red")
                return

            if password != confirm_password:
                registration_status.config(text="Les contrasenyes no coincideixen", fg="red")
                return

            try:
                registrar_usuario('contraseñas.json', username, password)
                registration_status.config(text="Usuari registrat amb èxit", fg="green")
                display_login()
            except Exception as e:
                messagebox.showerror("Error", f"Error durant el registre: {e}")


        for widget in root.winfo_children():
            widget.destroy()

        root.title("Registra't - RainbowWarriors")
        root.geometry("400x500")
        root.configure(bg="#f5f5f5")

        # Título principal
        tk.Label(
            root,
            text="Registra't",
            font=("Arial", 18, "bold"),
            bg="#f5f5f5",
            fg="#000000"
        ).pack(pady=10)

        tk.Label(
            root,
            text="Crea un compte amb els teus detalls",
            font=("Arial", 12),
            bg="#f5f5f5",
            fg="#666666"
        ).pack(pady=5)

        # Campo de usuario
        tk.Label(root, text="Nom d'usuari", font=("Arial", 10), bg="#f5f5f5").pack(pady=(20, 5))
        username_entry = tk.Entry(root, font=("Arial", 12), width=30, bd=1, relief="solid")
        username_entry.pack(pady=5)

        # Campo de contraseña
        tk.Label(root, text="Contrasenya", font=("Arial", 10), bg="#f5f5f5").pack(pady=(20, 5))
        password_entry = tk.Entry(root, font=("Arial", 12), width=30, bd=1, relief="solid", show="*")
        password_entry.pack(pady=5)

        # Campo de confirmar contraseña
        tk.Label(root, text="Repetir Contrasenya", font=("Arial", 10), bg="#f5f5f5").pack(pady=(20, 5))
        confirm_password_entry = tk.Entry(root, font=("Arial", 12), width=30, bd=1, relief="solid", show="*")
        confirm_password_entry.pack(pady=5)

        # Estado del registro
        registration_status = tk.Label(root, text="", font=("Arial", 10), bg="#f5f5f5", fg="red")
        registration_status.pack(pady=10)

        # Botón de registro
        tk.Button(
            root,
            text="Registrar-se",
            font=("Arial", 12, "bold"),
            bg="#6f52ed",
            fg="white",
            width=20,
            command=lambda: handle_registration(username_entry, password_entry, confirm_password_entry, registration_status)
        ).pack(pady=20)

        # Botón para volver al login
        tk.Button(
            root,
            text="Tornar al login",
            font=("Arial", 10),
            bg="#f5f5f5",
            fg="#6f52ed",
            bd=0,
            command=display_login
        ).pack(pady=10)


    root = tk.Tk()
    username_entry = None
    password_entry = None
    login_status = None
    display_login()
    root.mainloop()

display_ui()
