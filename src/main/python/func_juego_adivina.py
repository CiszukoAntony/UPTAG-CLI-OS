""" Esta función centraliza toda la lógica del juego:
    #1. Muestra la bienvenida.
    #2. Genera un número aleatorio entre 1 y 100.
    #3. Solicita y valida que la entrada del usuario sea un número entero.
    #4. Compara el intento, da pistas (alto/bajo) y cuenta los intentos.
    #5. Permite reiniciar el juego al terminar.
    ---
    Args:
        None
    ---
    Returns:
        None
    ---
    Raises:
        
        except
        Retorna un ValueError
    ---
    """


import random
import utils

def main():
    """
    Ejecuta el juego completo de 'Adivina el número'.
    -
    
     Esta función centraliza toda la lógica del juego:
     1. Muestra la bienvenida.
     2. Genera un número aleatorio entre 1 y 100.
     3. Solicita y valida que la entrada del usuario sea un número entero.
     4. Compara el intento, da pistas (alto/bajo) y cuenta los intentos.
     5. Permite reiniciar el juego al terminar.
    
    
    Args:
        None
    ---
    Returns:
        None
    ---
    Raises:
        except: Retorna un valueErrror
    ---
    
    """
    while True:
        # Configuración inicial de la partida
        numero_secreto = random.randint(1, 100)
        intentos = 0
        adivinado = False
        
        # Bienvenida
        print("=" * 90)
        print(f"{utils.ansi_text.GREEN} ¡BIENVENIDO AL JUEGO DE ADIVINA EL NÚMERO!{utils.ansi_text.RESET} ")
        print("=" * 90)
        print(f" {utils.ansi_text.BLUE} He pensado un número entre 1 y 100.{utils.ansi_text.RESET}")
        print(f" {utils.ansi_text.GREEN}Intenta adivinarlo en el menor número de intentos posible.{utils.ansi_text.RESET}\n")
        
        # Bucle principal de la partida actual
        while not adivinado:
            intentos += 1
            print(f"--- {utils.ansi_text.GREEN}Intento número {intentos} --- {utils.ansi_text.RESET}")
            
            # Bucle de solicitud y validación de datos
            while True:
                try:
                    intento_usuario = int(input("Introduce tu número: "))
                    break  # Salimos del bucle de validación si es un entero válido
                except ValueError:
                    print(f"{utils.ansi_text.RED}❌ Entrada inválida. Por favor, introduce un número entero.{utils.ansi_text.RESET}")
            
            # Verificación del número
            if intento_usuario < numero_secreto:
                print(f"{utils.ansi_text.GREEN}➡ Demasiado bajo. ¡Intenta con uno más grande!\n")
            elif intento_usuario > numero_secreto:
                print(f"➡ Demasiado alto. ¡Intenta con uno más chico!{utils.ansi_text.RESET}\n")
            else:
                print(f"\n🎉 {utils.ansi_text.YELLOW}¡Felicidades! ¡Has adivinado el número secreto!")
                print(f"🏆 Te tomó un total de {intentos} intentos ganar la partida.\n{utils.ansi_text.RESET}")
                adivinado = True
        
        # Preguntar si desea volver a jugar
        otra_vez = input(f"{utils.ansi_text.GREEN}¿Quieres jugar otra partida? (s/n): ").lower().strip()
        if otra_vez != 's':
            print(f"\n👋 ¡Gracias por jugar! Hasta la próxima{utils.ansi_text.RESET}.")
            break
        print("\n" * 2)  # Separador para la nueva partida

### Comprobación de main ###

if __name__ == "__main__":
    utils.clear_window()
    utils.module_error(__name__, __file__, __package__, __doc__)
