# Gestor de Contraseñas

Un gestor de contraseñas seguro que permite almacenar, recuperar, generar, cifrar y descifrar contraseñas. Además, incluye un sistema de autenticación para garantizar que solo los usuarios autorizados puedan acceder a sus contraseñas.

## Estructura del Proyecto

```bash
password_manager/
├── pass_manager.py       # Archivo principal. Orquesta las funciones de la aplicación.
├── pass_storage.py       # Gestiona el almacenamiento seguro de las contraseñas (almacén en archivo o base de datos).
├── pass_encryption.py    # Realiza el cifrado y descifrado de contraseñas para asegurar su privacidad.
├── pass_generator.py     # Genera contraseñas seguras y aleatorias.
├── authentication.py         # Maneja la autenticación del usuario (por ejemplo, mediante una contraseña maestra).
└── gui.py         # Proporciona la interfaz de usuario (CLI o GUI) para interactuar con el gestor.
```

## Funcionalidades

- **Almacenamiento seguro de contraseñas**: Guarda las contraseñas de forma cifrada para evitar accesos no autorizados.
- **Cifrado y descifrado de contraseñas**: Usa algoritmos de cifrado modernos para asegurar que las contraseñas almacenadas estén protegidas.
- **Generación de contraseñas seguras**: Permite generar contraseñas fuertes y aleatorias que cumplen con las mejores prácticas de seguridad.
- **Interfaz de usuario interactiva**: Accede al gestor de contraseñas a través de una interfaz de línea de comandos (CLI) o interfaz gráfica (GUI).
- **Autenticación de usuario**: Requiere autenticación a través de una contraseña maestra para acceder a las contraseñas guardadas.


