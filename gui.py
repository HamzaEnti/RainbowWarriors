import tkinter as tk
import os

def display_ui():
    root = tk.Tk()
    root.title("Authentication")
    root.geometry("350x300")
    root.config(bg="#f5f5f5")  # Fondo más agradable

    logo = tk.PhotoImage(file="logo.png")
    logo = logo.subsample(13, 13)  # Redimensiona el logo (reduce el tamaño)

    logo_label = tk.Label(root, image=logo, bg="#f5f5f5")
    logo_label.image = logo  # Mantener referencia
    logo_label.pack(pady=10)

    tk.Label(root, text="Usuari:", font=("Arial", 12), bg="#f5f5f5").pack(pady=5)
    username_entry = tk.Entry(root, font=("Arial", 12), width=25)
    username_entry.pack(pady=5)

    tk.Label(root, text="Contrasenya:", font=("Arial", 12), bg="#f5f5f5").pack(pady=5)
    password_entry = tk.Entry(root, show="*", font=("Arial", 12), width=25)
    password_entry.pack(pady=5)

    login_button = tk.Button(root, text="Login", font=("Arial", 12), bg="#4CAF50", fg="white", width=15, height=1)
    login_button.pack(pady=20)

    root.mainloop()


display_ui()
