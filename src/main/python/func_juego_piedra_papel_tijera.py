""" Ejecuta una partdia del juego Piedra, Papel o tijera contra la computadora 
  pide datos al usuario para la eleccion
  genera una opcion aleatoria de la computadora que determina el resultado 
    gana el usuario o gana la computadora o hay un empate
    
    Args:
       None
    ---
    Return:
          Retorna si el usuario ingresa opcion que no es valida
          Retorna si el usuario quiere salir 
    ---
    Raises:
       None
    ---
    
    """

import random
import utils 

def main():
    """
    
    Ejecuta una partida del juego Piedra, Papel o Tijera contra la computadora.
    -
     
       La función solicita la elección del usuario por consola, valida la entrada,
       genera una opción aleatoria para la computadora y determina el resultado
       (gana el usuario, gana la computadora o hay un empate).
    
    ---
    
    Args: 
        None
    ---
    Return:
         Retorna si la opcion que ingresa el usuario no es valida 
         Retorna si el usuario quiere salir
    --- 
    Raises:
         None
    ---
    
    
    """
    opciones = ["piedra", "papel", "tijera"]
    
    print("=" * 90)
    print(f"{utils.ansi_text.GREEN}¡Bienvenido a Piedra, Papel o Tijera!")
    print("=" * 90)
    
    # Entrada del jugador
    usuario = input("Elige una opción (piedra, papel, tijera O Salir): ").lower()
    # verifica si el usuario quiere salir 
    if usuario == "salir":
       print ("Gracias por jugar hasta la proxima")
       return
    # Validar que la entrada sea correcta
    if usuario not in opciones:
        print(f"{utils.ansi_text.RESET} {utils.ansi_text.RED}Opción no válida. Inténtalo de nuevo escribiendo piedra, papel o tijera.{utils.ansi_text.RESET}")
        return
       
    # Elección de la computadora
    computadora = random.choice(opciones)
    print(f"{utils.ansi_text.BLUE}\nTú elegiste: {usuario.capitalize()}")
    print(f"La computadora eligió: {computadora.capitalize()}\n{utils.ansi_text.RESET}")
    
    # Determinar el ganador
    if usuario == computadora:
        print(f"{utils.ansi_text.ORANGE}🤝 ¡Es un empate!{utils.ansi_text.RESET}")
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        print(f"{utils.ansi_text.PURPLE}🎉 ¡Ganaste! ¡Felicitaciones!{utils.ansi_text.RESET}")
    else:
        print(f"{utils.ansi_text.RED}😢 Perdiste. ¡Suerte para la próxima!{utils.ansi_text.RESET}")

### Comprobación de main ###

if __name__ == "__main__":
    utils.clear_window()
    utils.module_error(__name__, __file__, __package__, __doc__)
