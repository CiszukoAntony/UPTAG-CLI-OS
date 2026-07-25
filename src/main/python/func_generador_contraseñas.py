"""
Módulo: Generador de Contraseñas
Descripción: Genera contraseñas aleatorias con niveles de complejidad
Autor: Nellfrancis Garcia
Fecha: 2026
"""
import random
import string


def main():
    # Nombre opcional
    nombre = input("Tu nombre (opcional): ").strip() or "Usuario"

    # Niveles rápidos
    print("Niveles: 1)Básica 2)Media 3)Fuerte 4)Muy fuerte")
    try:
        nivel = int(input("Nivel (1-4): "))
    except ValueError:
        print("Nivel inválido")
        return

    try:
        longitud = int(input("Longitud (4-50): "))
    except ValueError:
        longitud = 8
    longitud = max(4, min(50, longitud))

    opts = [
        string.ascii_lowercase,
        string.ascii_letters,
        string.ascii_letters + string.digits,
        string.ascii_letters + string.digits + string.punctuation,
    ]

    chars = opts[min(max(nivel, 1), 4) - 1]
    pwd = ''.join(random.choice(chars) for _ in range(longitud))

    print(f"\n{nombre}: {pwd} ({longitud} chars, nivel {nivel})")

    if input("Guardar en mis_contrasenas.txt? (s/n): ").lower().startswith('s'):
        with open("mis_contrasenas.txt", "a", encoding="utf-8") as f:
            f.write(f"{pwd} | nivel:{nivel} | {longitud}\n")
        print("Guardado.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrumpido por el usuario")