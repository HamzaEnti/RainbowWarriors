def xor_encrypt_decrypt(input_string, KEY):
    """Cifra o descifra una cadena usando XOR con una clave."""
    return ''.join(chr(ord(char) ^ KEY) for char in input_string)

def decrypt_storage():
    KEY = int(input("Introduce la clave de acceso (0-255): "))  # Asegúrate de que la clave esté en el rango adecuado.
    if not (0 <= KEY <= 255):
        print("La clave debe estar entre 0 y 255.")
        return

    try:
        with open("storage.txt", 'r') as archivo:
            for line in archivo:
                # Separar la línea en sus componentes
                parts = line.strip().split(", ")
                ENCRYPTED_SERVEI = parts[0].split(": ")[1]
                ENCRYPTED_USER = parts[1].split(": ")[1]
                ENCRYPTED_PASSWORD = parts[2].split(": ")[1]

                # Desencriptar cada parte
                DECRYPTED_SERVEI = xor_encrypt_decrypt(ENCRYPTED_SERVEI, KEY)
                DECRYPTED_USER = xor_encrypt_decrypt(ENCRYPTED_USER, KEY)
                DECRYPTED_PASSWORD = xor_encrypt_decrypt(ENCRYPTED_PASSWORD, KEY)

                # Mostrar la información desencriptada
                print(f"Servei: {DECRYPTED_SERVEI}, Usuari: {DECRYPTED_USER}, Contrasenya: {DECRYPTED_PASSWORD}")

    except FileNotFoundError:
        print("El archivo 'storage.txt' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Llama a la función de desencriptación
if __name__ == "__main__":
    decrypt_storage()
