import tkinter as tk
from tkinter import ttk, messagebox
from authentication import registrar_usuario, verificar_contraseña
from PIL import Image, ImageTk
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
        for widget in root.winfo_children():
            widget.destroy()

        root.title("RainbowWarriors - Gestor de Contraseñas")

        header_frame = tk.Frame(root, bg="white")
        header_frame.pack(fill="x", pady=5)

        tk.Label(header_frame, text="RainbowWarriors - Password Manager", font=("Arial", 16, "bold"), bg="white").pack(side="left", padx=10)
        tk.Label(header_frame, text=f"Logged in as: {username}", font=("Arial", 10), bg="white").pack(side="right", padx=10)

        tk.Label(root, text="Contraseña Maestra:", font=("Arial", 12)).pack(pady=5)
        global master_password_entry
        master_password_entry = tk.Entry(root, show="*", font=("Arial", 12), width=25)
        master_password_entry.pack(pady=5)

        tk.Button(header_frame, text="Nueva Entrada", font=("Arial", 10), bg="#444444", fg="white", command=new_entry_window).pack(side="right", padx=10)
        tk.Button(header_frame, text="Logout", font=("Arial", 10), bg="#FF5733", fg="white", command=display_login).pack(side="right", padx=10)

        table_frame = tk.Frame(root, bg="white")
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

        tk.Button(root, text="Actualizar Tabla", command=update_password_table).pack(pady=5)


    def display_login():
        nonlocal login_status
        for widget in root.winfo_children():
            widget.destroy()

        root.title("RainbowWarriors - Login")
        root.geometry("1200x600")  # Tamaño exacto de la ventana principal
        root.config(bg="#f5f5f5")


        root.iconbitmap("myIcon.ico")
        logo_image = Image.open("logo.png")
        logo_image = logo_image.resize((150, 150))  # Ajusta el tamaño (ancho, alto) según tus necesidades
        logo_image = ImageTk.PhotoImage(logo_image)
        logo_label = tk.Label(root, image=logo_image)
        logo_label.image = logo_image
        logo_label.pack(pady=20)


        tk.Label(root, text="Username:", font=("Arial", 12), bg="#f5f5f5").pack(pady=5)
        nonlocal username_entry, password_entry
        username_entry = tk.Entry(root, font=("Arial", 12), width=25)
        username_entry.pack(pady=5)

        tk.Label(root, text="Password:", font=("Arial", 12), bg="#f5f5f5").pack(pady=5)
        password_entry = tk.Entry(root, show="*", font=("Arial", 12), width=25)
        password_entry.pack(pady=5)

        tk.Button(root, text="Login", font=("Arial", 12), bg="#444444", fg="white", width=15, command=handle_login).pack(pady=10)
        login_status = tk.Label(root, text="", font=("Arial", 10), bg="#f5f5f5")
        login_status.pack(pady=5)

        tk.Button(root, text="Crear Cuenta", font=("Arial", 12), bg="#FF5733", fg="white", command=display_registration).pack(pady=10)

    def display_registration():
        def handle_registration():
            username = username_entry.get()
            password = password_entry.get()
            confirm_password = confirm_password_entry.get()

            if not username or not password or not confirm_password:
                registration_status.config(text="Todos los campos son obligatorios", fg="red")
                return

            if password != confirm_password:
                registration_status.config(text="Las contraseñas no coinciden", fg="red")
                return

            try:
                registrar_usuario('contraseñas.json', username, password)
                registration_status.config(text="Usuario registrado con éxito", fg="green")
                display_login()
            except Exception as e:
                messagebox.showerror("Error", f"Error durante el registro: {e}")

        for widget in root.winfo_children():
            widget.destroy()

        root.title("Registro de Usuario")

        tk.Label(root, text="Nombre de Usuario:").pack(pady=5)
        username_entry = tk.Entry(root)
        username_entry.pack(pady=5)

        tk.Label(root, text="Contraseña:").pack(pady=5)
        password_entry = tk.Entry(root, show="*")
        password_entry.pack(pady=5)

        tk.Label(root, text="Confirmar Contraseña:").pack(pady=5)
        confirm_password_entry = tk.Entry(root, show="*")
        confirm_password_entry.pack(pady=5)

        registration_status = tk.Label(root, text="", fg="red")
        registration_status.pack(pady=5)

        tk.Button(root, text="Registrar", command=handle_registration).pack(pady=10)
        tk.Button(root, text="Volver", command=display_login).pack(pady=5)

    root = tk.Tk()
    username_entry = None
    password_entry = None
    login_status = None
    display_login()
    root.mainloop()

display_ui()
