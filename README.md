# 🔐 Password Security Auditor

Herramienta desarrollada en Python para realizar una evaluación básica de seguridad de contraseñas desde la terminal.

El proyecto analiza diferentes características de una contraseña y comprueba si aparece en una lista de contraseñas comunes. También detecta algunos patrones predecibles que pueden indicar una contraseña débil.

> Proyecto educativo desarrollado para practicar Python aplicado a ciberseguridad.

## 🚀 Características

* 🔐 Entrada de contraseña mediante `getpass`, evitando mostrarla en pantalla.
* 📏 Comprobación de longitud mínima recomendada.
* 🔠 Detección de letras mayúsculas.
* 🔡 Detección de letras minúsculas.
* 🔢 Detección de números.
* 🔣 Detección de caracteres especiales.
* 📚 Comprobación contra una wordlist de contraseñas comunes.
* 🔎 Detección de patrones comunes como `password`, `qwerty`, `123456`, etc.
* 🧮 Sistema de puntuación de 0 a 5 basado en los criterios de composición.
* 🛡️ Manejo de errores cuando la wordlist no está disponible.
* 🎨 Interfaz de terminal utilizando Rich.

## 🛠️ Tecnologías

* Python 3
* Rich
* SecLists
* Git / GitHub

## 📂 Estructura

```text
Password Security Auditor/
├── password.py
├── requirements.txt
├── wordlists/
│   └── 10k-most-common.txt
├── .gitignore
└── README.md
```

## ⚙️ Instalación

Clona el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd "Password Security Auditor"
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

## ▶️ Uso

Ejecuta:

```bash
python3 password.py
```

El programa solicitará una contraseña de forma segura:

```text
Introduce la contraseña:
```

Después mostrará una evaluación similar a:

```text
   Password Security
      Assessment

┏━━━━━━━━━━━━┳━━━━━━━━┓
┃ Criterio   ┃ Cumple ┃
┡━━━━━━━━━━━━╇━━━━━━━━┩
│ Longitud   │ Sí     │
│ Mayúsculas │ Sí     │
│ Minúsculas │ Sí     │
│ Números    │ Sí     │
│ Especiales │ Sí     │
└────────────┴────────┘

Puntuación total: 5 de 5

✓ La contraseña no aparece en el diccionario.
✓ No se han detectado patrones comunes.
```

## 🔎 Wordlist

El proyecto utiliza una lista de contraseñas comunes para identificar credenciales potencialmente predecibles.

La wordlist utilizada pertenece al proyecto **SecLists**.

Para mantener el proyecto organizado, se encuentra en:

```text
wordlists/10k-most-common.txt
```

## 🧠 Funcionamiento

El programa separa el análisis en diferentes funciones:

```text
                    Contraseña
                         │
                         ▼
                pedir_credenciales()
                         │
                         ▼
               comprobar_seguridad()
                    /    |     \
                   /     |      \
                  ▼      ▼       ▼
            Composición  Wordlist  Patrones
                  │        │         │
                  └────────┼─────────┘
                           ▼
                    Resultado final
```

La puntuación de 0 a 5 únicamente representa los criterios básicos de composición:

1. Longitud
2. Mayúsculas
3. Minúsculas
4. Números
5. Caracteres especiales

La presencia en la wordlist y los patrones comunes se muestran como indicadores de riesgo independientes.

## ⚠️ Limitaciones

Este proyecto es una herramienta educativa y no pretende proporcionar una medición completa de la fortaleza de una contraseña.

Una contraseña puede cumplir todos los criterios de composición y seguir siendo predecible. Por este motivo, el programa también realiza comprobaciones independientes mediante una wordlist y patrones comunes.

La detección de una contraseña en la wordlist significa que aparece en la lista utilizada por el programa; no implica por sí sola que una cuenta concreta haya sido comprometida.

## 📚 Qué he aprendido

Durante el desarrollo del proyecto he practicado:

* Funciones y modularización.
* Diccionarios y conjuntos (`set`).
* Comprensiones de conjuntos.
* Lectura de archivos.
* Manejo de excepciones con `try/except`.
* Uso de `getpass`.
* Procesamiento y análisis de strings.
* Uso de librerías externas.
* Diseño de una herramienta CLI.
* Organización de un proyecto Python.
* Conceptos básicos de seguridad de contraseñas.

## 🔮 Próximas mejoras

Algunas posibles mejoras para futuras versiones:

* Detección de secuencias numéricas y alfabéticas.
* Detección de caracteres repetidos.
* Análisis más avanzado de patrones.
* Estimación de entropía.
* Generación de informes.
* Mejor gestión de rutas mediante `pathlib`.
* Tests automatizados.
* Configuración mediante argumentos de línea de comandos.

## 👨‍💻 Autor
Proyecto desarrollado como parte de mi aprendizaje práctico en Python y ciberseguridad.
