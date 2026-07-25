import random
import utils

def validarEntradaInt(limite,mensaje, juego):
    """
    Args:
        limite:Establece el limite de numero maximo
        
        mensaje: La indicacion de que debe ingresar el usuario
        
        juego: habilita la capacidad de ingresar un numero fuera del limite establecido si esta activo
    ---
    Returns:
        La entrada del usuario
    ---
    Raises:
        except: puede detectar errores de entradas
    ---
    
    """
    while True:
        try:
            Entrada=int(input(f"{utils.ansi_text.CYAN}{mensaje}{utils.ansi_text.RESET}"))
            if juego==True and Entrada==111:
                return Entrada
            elif Entrada < 1 or Entrada > limite:
                print(f"{utils.ansi_text.RED}Error, ese Numero esta fuera del limite{utils.ansi_text.RESET}")
            
            else:
                return Entrada
            
        except ValueError:
            print(f"{utils.ansi_text.RED}❌ Entrada inválida. Por favor, introduce un número entero.{utils.ansi_text.RESET}")
            
def adivinar(limite):
    """
    Ejecuta el mode de juego de 'Adivina el número'.
    -
    
     Esta función centraliza toda la lógica del juego:
     1. Muestra las reglas del juego.
     2. Genera un número aleatorio entre 1 y el limite.
     3. Solicita y valida que la entrada del usuario sea un número entero.
     4. Compara el intento, da pistas (alto/bajo) y cuenta los intentos.
     5. Permite reiniciar el modo al terminar.
    
    
    Args:
        limite:Establece el limite de numero maximo
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
        numero_secreto = random.randint(1, limite)
        intentos = 0
        adivinado = False
        
        # Bienvenida
        print("=" * 90)
        print(f"{utils.ansi_text.GREEN} ¡QUE COMIENCE EL JUEGO!{utils.ansi_text.RESET} ")
        print("=" * 90)
        print(f"{utils.ansi_text.BLUE} He pensado un número entre {utils.ansi_text.YELLOW}1{utils.ansi_text.BLUE} y {utils.ansi_text.YELLOW}{limite}.")
        print(f"{utils.ansi_text.GREEN}Intenta adivinarlo en el menor número de intentos posible.\n")
        print(f"Intenta adivinarlo en el menor número de intentos posible (o ingresa 111 para salir).{utils.ansi_text.RESET}\n")
        # Bucle principal de la partida actual
        while not adivinado:
            intentos += 1
            print(f"{utils.ansi_text.GREEN}--- Intento número {intentos} --- {utils.ansi_text.RESET}")
            

            intento_usuario = validarEntradaInt(limite=limite,mensaje="Introduce tu número: ",juego=True)
            if intento_usuario == 111:
                print("Juego Finalizado")
                return            
            # Verificación del número
            if intento_usuario < numero_secreto:
                print(f"{utils.ansi_text.BLUE}➡ Demasiado bajo. ¡Intenta con uno más grande!\n")
                
            elif intento_usuario > numero_secreto:
                print(f"{utils.ansi_text.ORANGE}➡ Demasiado alto. ¡Intenta con uno más chico!\n")
                
            else:
                print(f"\n🎉 {utils.ansi_text.YELLOW}¡Felicidades! ¡Has adivinado el número secreto!")
                print(f"🏆 Te tomó un total de {intentos} intentos ganar la partida.\n{utils.ansi_text.RESET}")
                adivinado = True
        
        # Preguntar si desea volver a jugar
        otra_vez = input(f"{utils.ansi_text.GREEN}¿Quieres jugar otra partida? (s/n): ").strip().lower()
        if otra_vez != 's':
            print(f"\n👋 ¡Gracias por jugar!{utils.ansi_text.RESET}.")
            break
        print("\n" * 2)  # Separador para la nueva partida
        
def main():
    """
    Ejecuta el el menu de 'Adivina el número'.
    -
    
    Permite al usuario elegir los modos y la opcion de salir
    
    Args:
        None
    ---
    Returns:
        None
    ---
    Raises:
        None
    ---
    
    """
    while True:
        niveles=[25,50,100]
        print(f"""{utils.ansi_text.GREEN}Juego de adivina el numero.

{utils.ansi_text.GRAY}{"="*20+"|||"+"="*67}
{utils.ansi_text.BLUE}( 1. ) Facil        {utils.ansi_text.GRAY}|||      {utils.ansi_text.YELLOW}{niveles[0]} 
{utils.ansi_text.BLUE}( 2. ) Medio        {utils.ansi_text.GRAY}|||      {utils.ansi_text.BLUE}{niveles[1]} 
{utils.ansi_text.BLUE}( 3. ) Dificil      {utils.ansi_text.GRAY}|||     {utils.ansi_text.RED}{niveles[2]} 
{utils.ansi_text.BLUE}( 4. ) Salir        {utils.ansi_text.GRAY}|||
{"="*20+"|||"+"="*67}

""")
        opcion_us=validarEntradaInt(limite=len(niveles)+1,mensaje=(f"ingrese un numero entre 1 y {len(niveles)+1}: "),juego= False) -1
        if opcion_us == len(niveles):
            break
        else:
            utils.clear_window()
            adivinar(limite=niveles[opcion_us])
    print(f"\n👋{utils.ansi_text.GREEN} Hasta la próxima{utils.ansi_text.RESET}.")
         

### Comprobación de main ###

if __name__ == "__main__":
    utils.clear_window()
    utils.module_error(__name__, __file__, __package__, __doc__)
