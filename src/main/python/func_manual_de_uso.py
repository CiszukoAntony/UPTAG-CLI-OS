# Manual de Uso Simple
# Este programa muestra instrucciones básicas de uso

import utils 

def mostrar_menu():
    
    """muestra el menu de opciones"""
    lista_menu=["calculadora",
                "conversión de divisas",
                "Convertidor de unidades de longitud",
                "piedra,papel,tijera",
                "adivina el número",
                "información y creditos",
                "salir"]
    print("\n" + "="*40)
    print("        MANUAL DE USO      ")
    print("="*40)
    
    for indice, opcion in enumerate(lista_menu):
        
        print(f"{utils.ansi_text.CYAN}( {indice + 1}. ){utils.ansi_text.GRAY} | {utils.ansi_text.ORANGE}[ {opcion}. ]{utils.ansi_text.RESET}")
    
    print("="*40)
    
#ahora se continua con las opciones
#enpezando con las divisas.

def mostrar_conversion_de_divisa():
    
    """muestra la información sobre la conversión de divisas"""
    
    print("\n[conversion de divisas]")
    print("para el correcto uso de esta funcion, no se debe colocar numeros negativos,no se debe colocar una divisa la cual no esta en el conversor, la cantidad de la moneda solicitada debe ser logica y correcta, en caso de no cumplir con estos parametros la conversion asi tambien como el programa no iniciara.") 
    print("Presiona ENTER para continuar...")
    input()
    
    #seguimos con adivinar el número.
    
def mostrar_adivina_el_numero():
    
    """muestra la información sobre adivinar el numero"""
        
    print("\n[adivina el número]")
    print("para el correcto uso de esta funcion se necesita daber que: no de podren colocar numeros negativos asi mismo como no se deben colocar letros signos o algun simbolo mas, no se debe exceder el valor numerico preestablecido o sea se del 1 al 100, en caso tal de colocar un valor incorrecto bien sea numerico o simbolico el programa no iniciara y se debera colocar un valor correcto.")
    print("Presiona ENTER para continuar...")
    input()
    
    #el siguiente piedra papel o tijeras.
    
def mostrar_piedra_papel_tijeras():
    
    """muestra la información sobre piedra,papel tijeras"""
    
    print("\n[piedra,papel,tijera]")
    print("para el correcto uso de esta función no se debe seleccionar otra opción que no este implicita en el juego, se debe respetar las instrucciones dentro de este para que no haya errores, no se debe usar ninguna simbologia o carácter especial, en dado caso de esta situación el juego no iniciará o dara errores a la hora de continuar.")
    print("Presiona ENTER para continuar...")
    input()
    
    #ahora con información y creditos.
    
def mostrar_informacion_creditos():
    
    """muestra información sobre los creditos y algo amdde información"""
    
    print("\n[Información y creditos]")
    print("una vez dentro se mostrara la información mas relevante del proyecto asi como los créditos correspondientes a los autores, no se debera mover ni modificar nada ya que podria dañar el proyecto y afectar su rendimiento, lo autores de este proyecto son: francisco García, santaigo rojas,ivan quevedo,luis colina y hanzer sivira :.")
    print("Presiona ENTER para continuar...")
    input()
#Manual del convertidor de unidades de longitud  
def mostrar_convertidor_de_unidades_de_longitud():
    print("\n[Convertidor de unidades de longitud]")
    print("\nUn programa creado para su finalidad expresa en su titulo, convertir unidades")
    print("La forma correcta de uso es dejarse guiar por la informacion misma en la herramienta")
    print(f"""En colaboracion con:
{utils.ansi_text.ORANGE}Gustavo Noguera
Luis pinzon
Isaac Soto          
Jean Prado
Marlon Valles{utils.ansi_text.RESET}""")
    input()    
    
    
#y por ultimo la calculadora
    
def mostrar_calculadora():
    
    """muestra la información sobre la calculadora"""
    
    print("\n[calculadora]")
    print("Este programa es una herramienta simple")
    print("para el correcto uso de la calculadora se le pide al usuario que no ingrese ningún otro valor que no ingrese ninguna opcion que no posea la calculadora asi como también ningun valor que no sea numerico en tal caso de que so llegue a pasar la calculadora fallara y tendra que iniciar denuevo.")
    print("Presiona ENTER para continuar...")
    input()

# Programa principal

def main():

    lista_menu=[mostrar_calculadora,
            mostrar_conversion_de_divisa,
            mostrar_convertidor_de_unidades_de_longitud,
            mostrar_piedra_papel_tijeras,
            mostrar_adivina_el_numero,
            mostrar_informacion_creditos
            ]

    """Esta función controla el flujo principal del programa mostrando el menú
    de opciones al usuario, procesando su selección y llamando a las funciones
    correspondientes. El bucle se mantiene activo hasta que el usuario elige
    la opción de salir."""
    
    while True:
        mostrar_menu()
        try:
            opcion = int(input(f"{utils.ansi_text.ORANGE}Selecciona una opción {utils.ansi_text.BLUE}(1-{len(lista_menu)+1}){utils.ansi_text.ORANGE}: {utils.ansi_text.RESET}"))-1
        
            if opcion < 0 or opcion > len(lista_menu):
                print(f"\n{utils.ansi_text.RED}¡Opción inválida! Por favor, elige 1-{len(lista_menu)}.") 
                input(f"{utils.ansi_text.ORANGE}Presiona ENTER para continuar...{utils.ansi_text.RESET}")
        
            else:
                if opcion == len(lista_menu):
                    break
                elif opcion >= 0 and opcion<=len(lista_menu)-1:
                    utils.clear_window()
                    lista_menu[opcion]()
                    utils.clear_window()
        except ValueError:
             print(f"\n{utils.ansi_text.RED}¡Opción inválida! Por favor, elige 1-{len(lista_menu)}.") 
             input(f"{utils.ansi_text.ORANGE}Presiona ENTER para continuar...{utils.ansi_text.RESET}")
  
    print("Gracias por usar el Manual")

### Comprobación de main ###

if __name__ == "__main__":
    utils.clear_window()
    utils.module_error(__name__, __file__, __package__, __doc__)
