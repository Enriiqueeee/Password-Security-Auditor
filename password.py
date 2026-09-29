# Librerías

import getpass

from rich.console import Console
from rich.panel import Panel
from rich.table import Table


console = Console()

CARACTERES_RECOMENDADOS = 12


# Pedir la contraseña del usuario

def pedir_credenciales():
    password = getpass.getpass("Introduce la contraseña: ")
    return password


# Comprobar cuántos caracteres tiene

def comprobar_caracteres(password):
    caracteres_password = len(password)
    return caracteres_password


# Comprobar mayúsculas

def comprobar_mayusculas(password):
    for caracter in password:
        if caracter.isupper():
            return True

    return False


# Comprobar minúsculas

def comprobar_minusculas(password):
    for caracter in password:
        if caracter.islower():
            return True

    return False


# Comprobar números

def comprobar_numeros(password):
    for caracter in password:
        if caracter.isdigit():
            return True

    return False


# Comprobar caracteres especiales

def comprobar_especiales(password):
    for caracter in password:
        if not caracter.isalnum():
            return True

    return False


# Cargar wordlist

def cargar_wordlist():
    try:
        with open(
            "wordlists/10k-most-common.txt",
            "r",
            encoding="utf-8"
        ) as archivo:

            return {
                linea.strip().lower()
                for linea in archivo
                if linea.strip()
            }

    except FileNotFoundError:
        console.print(
            "[red]Error: No se pudo encontrar el archivo de wordlist.[/red]"
        )

        return set()


# Comprobar si aparece en la wordlist

def comprobar_diccionario(password, wordlist):
    return password.lower() in wordlist


# Detectar patrones comunes

def patrones_comunes(password):

    patrones = [
        "123456",
        "password",
        "qwerty",
        "abc123",
        "letmein",
        "monkey",
        "dragon",
        "111111",
        "baseball",
        "iloveyou"
    ]

    for patron in patrones:

        if patron in password.lower():
            return patron

    return None


# Analizar la seguridad de la contraseña

def comprobar_seguridad(password, wordlist):

    resultados = {

        "Longitud": comprobar_caracteres(password) >= CARACTERES_RECOMENDADOS,

        "Mayúsculas": comprobar_mayusculas(password),

        "Minúsculas": comprobar_minusculas(password),

        "Números": comprobar_numeros(password),

        "Especiales": comprobar_especiales(password),

    }

    diccionario = comprobar_diccionario(password, wordlist)

    patrones = patrones_comunes(password)

    puntuacion = sum(resultados.values())

    return resultados, puntuacion, diccionario, patrones


# Mostrar resultado

def mostrar_resultado(resultados, puntuacion, diccionario, patrones):

    table = Table(title="Password Security Assessment")

    table.add_column(
        "Criterio",
        style="cyan",
        no_wrap=True
    )

    table.add_column(
        "Cumple",
        style="magenta"
    )

    for criterio, cumple in resultados.items():

        estado = "[green]Sí[/green]" if cumple else "[red]No[/red]"

        table.add_row(criterio, estado)

    console.print(table)

    console.print(
        f"\nPuntuación total: [bold]{puntuacion}[/bold] de 5\n"
    )

    if puntuacion < 3:

        console.print(
            "[red]La contraseña es débil. Se recomienda cambiarla.[/red]"
        )

    elif puntuacion < 5:

        console.print(
            "[yellow]La contraseña es aceptable, pero podría mejorarse.[/yellow]"
        )

    else:

        console.print(
            "[green]La contraseña es fuerte.[/green]"
        )

    if diccionario:

        console.print(
            "[red]⚠ La contraseña aparece en el diccionario.[/red]"
        )

    else:

        console.print(
            "[green]✓ La contraseña no aparece en el diccionario.[/green]"
        )

    if patrones:

        console.print(
            f"[red]⚠ Patrón común detectado: {patrones}[/red]"
        )

    else:

        console.print(
            "[green]✓ No se han detectado patrones comunes.[/green]"
        )


# Programa principal

if __name__ == "__main__":

    console.print(
        Panel(
            "PASSWORD SECURITY AUDITOR",
            subtitle="Security assessment tool",
            expand=False
        )
    )

    password = pedir_credenciales()

    wordlist = cargar_wordlist()

    resultados, puntuacion, diccionario, patrones = comprobar_seguridad(
        password,
        wordlist
    )

    mostrar_resultado(
        resultados,
        puntuacion,
        diccionario,
        patrones
    )