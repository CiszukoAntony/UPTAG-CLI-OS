"""
Módulo para la conversión de divisas mediante un menú interactivo.
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

from func_comprobacion import validar_mayor_cero
from utils import clear_window, module_error

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
        print("1. Convertir")
        print("2. Salir")
        
        opcion = input("Elige una opción: ")
        
        # Si elige salir, terminamos la función
        if opcion == "2":
            print("Hasta luego.")
            return
        # Si elige una opción inválida, reiniciamos el bucle
        elif opcion != "1":
            print("Opción inválida. Intenta de nuevo.")
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
            base = monto * 633.02
        elif de == "eur":
            base = monto * 710.10

        # Paso 2: moneda a la que se desea convertir
        if a == "bolivares":
            resultado = base
        elif a == "usd":
            resultado = base / 633.02
        elif a == "eur":
            resultado = base / 710.10

        # Paso 3: conversión final de la moneda
        print(f"Resultado: {resultado:.2f}")

if __name__ == "__main__":
    clear_window()
    module_error(__name__, __file__, __package__, __doc__) 
