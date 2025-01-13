# RainbowWarriors 🌈

## Descripció general
Rainbow Warriors és un gestor de contrasenyes segur i fàcil d’utilitzar dissenyat per ajudar els usuaris a generar, emmagatzemar i gestionar contrasenyes fortes. Ofereix funcions de xifrat, desxifrat i una interfície gràfica d’usuari (GUI) per a una interacció intuïtiva.

## Característiques
- **Generació de contrasenyes**: Crea contrasenyes segures i aleatòries.
- **Emmagatzematge segur**: Xifra i guarda les contrasenyes utilitzant mètodes criptogràfics moderns.
- **Recuperació de contrasenyes**: Desxifra i recupera les contrasenyes guardades quan sigui necessari.
- **Interfície gràfica fàcil d’utilitzar**: Una interfície senzilla basada en Tkinter.

## Estructura dels fitxers
- `authentication.py`: Gestió de la lògica d’autenticació d’usuaris.
- `GUI_manager.py`: Gestió de la interfície gràfica d’usuari.
- `inside_storage.py`: Proporciona emmagatzematge segur i gestió de contrasenyes.
- `pass_decrypt.py`: Implementa la lògica per desxifrar contrasenyes.
- `pass_encryption.py`: Gestió del xifrat de contrasenyes.
- `pass_generator.py`: Generació de contrasenyes segures.
- `main.py`: Coordina les funcionalitats principals del gestor de contrasenyes.

## Funcionalitats principals
- **Generació de contrasenyes segures**: Genera contrasenyes complexes i úniques.
- **Encriptació i desencriptació**: Protegeix les contrasenyes amb algorismes de xifrat robustos.
- **Gestió d'usuaris**: Permet autenticar i gestionar múltiples usuaris de manera segura.
- **Interfície gràfica**: Inclou una GUI senzilla per facilitar l'accés a les funcionalitats.

## Requisits
- Python 3.8 o superior.
- Llibreries requerides (especificades a `requirements.txt`).

## Instal·lació
Segueix aquests passos per instal·lar i executar l'aplicació:

1. Clona aquest repositori:
   ```bash
   git clone https://github.com/username/RainbowWarriors.git
   ```
2. Accedeix al directori del projecte:
   ```bash
   cd RainbowWarriors
   ```
3. Instal·la les dependències:
   ```bash
   pip install -r requirements.txt
   ```
4. Executa l'aplicació:
   ```bash
   python main.py
   ```

## Preguntes freqüents
**1. L'aplicació guarda les contrasenyes al núvol?**  
No, totes les contrasenyes es guarden localment per garantir la privadesa.

**2. Què faig si oblido la meva contrasenya principal?**  
No és possible recuperar-la per seguretat. Hauràs de reiniciar el programa.

