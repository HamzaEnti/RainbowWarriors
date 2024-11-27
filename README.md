# RainbowWarriors 🌈

RainbowWarriors és una eina senzilla i eficient per gestionar contrasenyes segures, protegint la informació personal dels usuaris mitjançant encriptació avançada i una interfície gràfica intuïtiva.

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
   python pass_manager.py
   ```

## Ús
- Inicia l'aplicació i segueix els passos de la GUI per generar i gestionar contrasenyes.
- Per utilitzar el xifrat i desxifrat manualment:
   ```bash
   python pass_encryption.py
   python pass_decypt.py
   ```

## Estructura del projecte
```
RainbowWarriors/
│
├── authentication.py       # Gestió d'autenticació
├── general_storage.py      # Emmagatzematge d'informació
├── gui.py                  # Interfície gràfica
├── pass_generator.py       # Generació de contrasenyes
├── pass_encryption.py      # Xifrat de dades
├── pass_decypt.py          # Desxifrat de dades
├── pass_manager.py         # Gestor principal de contrasenyes
├── requirements.txt        # Llibreries requerides
└── README.md               # Documentació del projecte
```

## Preguntes freqüents
**1. L'aplicació guarda les contrasenyes al núvol?**  
No, totes les contrasenyes es guarden localment per garantir la privadesa.

**2. Què faig si oblido la meva contrasenya principal?**  
No és possible recuperar-la per seguretat. Hauràs de reiniciar el sistema.

**3. És segur compartir les contrasenyes generades?**  
Només comparteix contrasenyes en entorns segurs i amb xifrat.

