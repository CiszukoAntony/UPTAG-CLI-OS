from func_comprobacion import validar_mayor_cero
import utils

def validarEntradaInt(limite,mensaje):
    """
    Args:
        limite:Establece el limite de numero maximo
        
        mensaje: La indicacion de que debe ingresar el usuario
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
            Entrada=int(input(f"{utils.ansi_text.CYAN}{mensaje}: {utils.ansi_text.RESET}"))
            
            if Entrada < 1 or Entrada > limite:
                print(f"{utils.ansi_text.RED}Error, ese Numero esta fuera del limite{utils.ansi_text.RESET}")
            
            else:
                return Entrada
            
        except ValueError:
            print(f"{utils.ansi_text.RED}❌ Entrada inválida. Por favor, introduce un número entero.{utils.ansi_text.RESET}")
            
def validarEntradaFloat(mensaje):
    """
    Args:
        mensaje: La indicacion de que debe ingresar el usuario
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
            Entrada=float(input(f"{utils.ansi_text.BLUE}{mensaje}: {utils.ansi_text.RESET}"))
            if Entrada <= 0:
                print(f"{utils.ansi_text.RED}ERROR: Por favor ingrese un numero positivo mayor a 0")
            else:
                return Entrada
        except ValueError:
            print(f"{utils.ansi_text.RED}ERROR: Por favor ingrese un numero flotante")

def taza_personalizada():
    """
    Puedes convertir dolares con tazas personalizadas
    Args:
        Nonw
    ---
    Returns:
        None
    ---
    Raises:
        except: puede detectar errores de entradas
    ---
    
    """
    taza_personalizada=None
    while True:
        
        print("""Taza personalizada
1.Ingresar taza personalizada(el valor de la taza no se guardara cuando salgas)
2.Usar taza personalizada
3.Salir""")
        opcion=validarEntradaInt(limite=3,mensaje="Por favor ingrese una opcion")
    
        if opcion == 1:
            taza_personalizada=validarEntradaFloat(mensaje="Por favor ingrese el valor de la taza")
        
        elif opcion == 2 and taza_personalizada==None:
            taza_personalizada=validarEntradaFloat(mensaje="Por favor ingrese el valor de la taza") 
            Valor=validarEntradaFloat(mensaje="Por favor ingrese el los dolares que quiere convertir")
            print(f"\n{Valor} convertido a la taza personalizada es igual a: {Valor*taza_personalizada}")
            input("\nPresione ENTER para continuar")
               
        elif opcion == 2 and not(taza_personalizada==None):
            Valor=validarEntradaFloat(mensaje="Por favor ingrese el los dolares que quiere convertir")
            print(f"\n{Valor} convertido a la taza personalizada es igual a: {Valor*taza_personalizada}")
            input("\nPresione ENTER para continuar")
        
        elif opcion == 3:
            print("\nSaliste de la funcion taza personalizada")
            print("\nno se guardara el valor de la taza personalizada")
            input("\nPresione ENTER para continuar")
            break
            
def main():
    """
    Solicita al usuario las divisas de origen y destino, junto con el monto,
    para calcular y mostrar el resultado de la conversión.
    ---
    Args:
        None.
    ---
    Returns:
        None.
    ---
    Raises:
        Exception: Si ocurre un error inesperado.
    ---
    """
    moneda = ["bolivares", "usd", "eur"]
    
    # Bucle principal del programa
    while True:
        print("\n--- CONVERSOR DE DIVISAS ---")
        print("1. Convertir(Dolares, Euros, Bolivares)")
        print("2. Convertir(Taza personalizada, Bolivares)")
        print("3. Salir")
        
        opcion = validarEntradaInt(limite=3,mensaje="Ingrese una opcion entre 1-3")
        
        # Si elige salir, terminamos la función
        if opcion == 3:
            print("Hasta luego.")
            return
        
        # funcion de taza personalizada
        elif opcion == 2:
            taza_personalizada()
            continue

        # Validación de la moneda que se desea convertir (origen)
        while True:
            de = input("De (bolivares, usd, eur): ").lower()
            if de in moneda:
                break
            print("Error: Moneda no reconocida. Intenta de nuevo.")

        # Validación de la moneda a la que se desea convertir (destino)
        while True:
            a = input("A (bolivares, usd, eur): ").lower()
            if a in moneda:
                break
            print("Error: Moneda no reconocida. Intenta de nuevo.")

        # Validación del monto a convertir
        while True:
            monto = validar_mayor_cero("Monto a convertir: ")
            if monto is not None:
                break

        # Paso 1: moneda de origen
        if de == "bolivares":
            base = monto
        elif de == "usd":
            base = monto * 737.52
        elif de == "eur":
            base = monto * 844,22

        # Paso 2: moneda a la que se desea convertir
        if a == "bolivares":
            resultado = base
        elif a == "usd":
            resultado = base / 737.52
        elif a == "eur":
            resultado = base / 844,22

        # Paso 3: conversión final de la moneda
        print(f"Resultado: {resultado:.2f}")
        input("\nPresione ENTER para continuar")

if __name__ == "__main__":
    utils.clear_window()
    utils.module_error(__name__, __file__, __package__, __doc__) 
