"""
Versión simple del gestor de tareas.
"""

def mostrar_menu():
    print("\n=== MENÚ DE TAREAS ===")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")


def pausa():
    input("\nPresiona ENTER para continuar...")


def main():
    tareas = []  # lista de diccionarios: {"texto": str, "completada": bool}
    nombre = input("Tu nombre (opcional): ").strip() or "Usuario"

    while True:
        print(f"\nHola, {nombre}! Tienes {len(tareas)} tareas.")
        mostrar_menu()

        opcion = input("Selecciona una opción (1-5): ").strip()
        if opcion == "1":
            texto = input("Escribe la tarea: ").strip()
            if texto:
                tareas.append({"texto": texto, "completada": False})
                print("Tarea agregada.")
            else:
                print("No se agregó: texto vacío.")
            pausa()

        elif opcion == "2":
            if not tareas:
                print("No hay tareas.")
            else:
                for i, t in enumerate(tareas, 1):
                    mark = "[x]" if t["completada"] else "[ ]"
                    print(f"{i}. {mark} {t['texto']}")
            pausa()

        elif opcion == "3":
            if not tareas:
                print("No hay tareas para completar.")
            else:
                try:
                    num = int(input("Número de tarea a completar: "))
                    if 1 <= num <= len(tareas):
                        tareas[num - 1]["completada"] = True
                        print("Tarea marcada como completada.")
                    else:
                        print("Número inválido.")
                except ValueError:
                    print("Debes ingresar un número.")
            pausa()

        elif opcion == "4":
            if not tareas:
                print("No hay tareas para eliminar.")
            else:
                try:
                    num = int(input("Número de tarea a eliminar: "))
                    if 1 <= num <= len(tareas):
                        eliminado = tareas.pop(num - 1)
                        print(f"Eliminada: {eliminado['texto']}")
                    else:
                        print("Número inválido.")
                except ValueError:
                    print("Debes ingresar un número.")
            pausa()

        elif opcion == "5":
            print("Saliendo. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Ingresa 1-5.")
            pausa()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrumpido por el usuario.")
# Fin del script
