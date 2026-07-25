"""Módulo para ejecutar una partida interactiva de Piedra, Papel o Tijera."""

import random
import utils


def main():
    """Ejecuta una partida del juego Piedra, Papel o Tijera contra la computadora.

    La función solicita la elección del usuario por consola, valida la entrada,
    genera una opción aleatoria para la computadora y determina el resultado.
    Permite jugar múltiples rondas hasta que el usuario decida salir.
    """
    opciones = ["piedra", "papel", "tijera"]

    print("=" * 90)
    print(
        f"{utils.ansi_text.GREEN}¡Bienvenido a Piedra, Papel o Tijera!{utils.ansi_text.RESET}"
    )
    print("=" * 90)

    # Bucle principal para mantener el juego activo
    while True:
        # Entrada del jugador con limpieza de espacios (.strip())
        usuario = (
            input(f"""
{utils.ansi_text.GREEN}Piedra le gana a la Trijera
Tijera le gana al Papel
Papel le gana a Piedra
                  \n{utils.ansi_text.BLUE}Elige una opción (piedra, papel, tijera) o salir:{utils.ansi_text.RESET} """)
            .strip()
            .lower()
        )

        # Verifica si el usuario quiere salir
        if usuario == "salir":
            print(
                f"{utils.ansi_text.GREEN}Gracias por jugar, ¡hasta la próxima!{utils.ansi_text.RESET}"
            )
            break

        # Validar que la entrada sea correcta
        if usuario not in opciones:
            print(
                f"{utils.ansi_text.RED}Opción no válida. Inténtalo de nuevo escribiendo piedra, papel o tijera.{utils.ansi_text.RESET}"
            )
            continue  # Vuelve al inicio del bucle si la opción no es válida

        # Elección de la computadora
        computadora = random.choice(opciones)
        print(f"{utils.ansi_text.BLUE}\nTú elegiste: {usuario.capitalize()}")
        print(
            f"La computadora eligió: {computadora.capitalize()}\n{utils.ansi_text.RESET}"
        )

        # Determinar el ganador
        if usuario == computadora:
            print(
                f"{utils.ansi_text.ORANGE}🤝 ¡Es un empate!{utils.ansi_text.RESET}"
            )
        elif (
            (usuario == "piedra" and computadora == "tijera")
            or (usuario == "papel" and computadora == "piedra")
            or (usuario == "tijera" and computadora == "papel")
        ):
            print(
                f"{utils.ansi_text.MAGENTA}🎉 ¡Ganaste! ¡Felicitaciones!{utils.ansi_text.RESET}"
            )
        else:
            print(
                f"{utils.ansi_text.RED}😢 Perdiste. ¡Suerte para la próxima!{utils.ansi_text.RESET}"
            )

        # Pregunta para volver a jugar o cerrar el juego
        print("-" * 50)
        otra_vez = (
            input("¿Quieres jugar otra ronda? (s/n): ").strip().lower()
        )
        if otra_vez not in ["s", "si", "sí"]:
            print(
                f"{utils.ansi_text.GREEN}\n¡Gracias por jugar! Cerrando el juego...{utils.ansi_text.RESET}"
            )
            break


### Comprobación de main ###


if __name__ == "__main__":
    utils.clear_window()
    utils.module_error(__name__, __file__, __package__, __doc__)
