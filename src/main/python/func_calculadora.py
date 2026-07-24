from utils import module_error,clear_window
import math
import cmath
from func_comprobacion import validar_flotante,validar_divisor,validar_entero
def main():
    # Calculadora Númerica Basica

    print("Bienvenido a la calculadora básica de Python")
    # Menú de la calculadora
    while True:
        print("Ingrese el valor númerico de la operacion que quieres realizar")
        print("="*90)
        print("""
        1. Suma					8. Coseno
        2. Resta				9. Seno
        3. Multiplicacion			10. Tangente
        4. Division				11. Porcentaje
        5. Potencia				12. Logaritmo base 10
        6. Raíz Cuadrada			13. Factorial
        7. Raíz Cúbica				14. Salida del programa.
        """)
        print("="*90)
        
        op = validar_entero ("Elija: ")
        
        if op not in [1,2,3,4,5,6,7,8,9,10,11,12,13,14]:
            print("Error. Escoja una de las opciones a partir del 1 (Suma) hasta el 14 (Salida).")
            
        else:  
            # Suma
            if op == 1:
                num1= validar_flotante("Ingrese el valor del primer número a sumar: ")
                num2= validar_flotante("Ingrese el valor del segundo número a sumar: ")
                print("El resultado de su sumatoria es: ", num1+num2)
            # Resta
            elif op == 2:
                num1= validar_flotante("Ingrese el valor del minuendo de la resta: ")
                num2= validar_flotante("Ingrese el valor del sustraendo de la resta: ")
                print("El resultado de su resta es: ", num1-num2)
            # Multiplicación
            elif op == 3:
                num1= validar_flotante("Ingrese el valor del primer numero a multiplicar: ")
                num2= validar_flotante("Ingrese el valor del segundo numero a multiplicar: ")
                print("El resultado de su multiplicación es: ", num1*num2)
            # División
            elif op == 4:
                num1= validar_flotante("Ingrese el valor del dividendo: ")
                num2= validar_divisor("Ingrese el valor del divisor: ")
                print("El resultado de su división es: ", num1/num2)
                print("Y el resto de dicha división es: ", num1%num2)
            # Potencia
            elif op == 5:
                num1= validar_flotante("Ingrese el valor base para potenciar: ")
                num2= validar_flotante("Ingrese el valor de la potencia: ")
                print("El resultado de su potenciación fue de: ", num1**num2)
            # Raíz Cuadrada
            elif op == 6:
                num1= validar_flotante("Ingrese el valor del número para calcular su raíz cuadrada: ")
                print(f"La raíz cuadrada de {num1} es: ", cmath.sqrt(num1))
            # Raíz Cúbica
            elif op == 7:
                num1= validar_flotante("Ingrese el valor para calcular su raiz cubica: ")
                print(f"La raiz cubica de {num1} es: ", round(math.cbrt(num1), 9))
            # Coseno
            elif op == 8:
                num1=validar_flotante("Ingrese los grados para calcular su coseno: ")
                resultado = math.cos(math.radians(num1))
                print(f"el coseno de {num1}° es: ",resultado)
            # Seno
            elif op == 9:
                num1=validar_flotante("Ingrese los grados para calcular su seno: ")
                resultado = math.sin(math.radians(num1))
                print(f"El seno de {num1}° es: ",resultado)
            # Tangente
            elif op == 10:
                num1=validar_flotante("Ingrese los grados para calcular su tangente: ")
                resultado = math.tan(math.radians(num1))
                print(f"La tangente de {num1}° es: ",resultado)
            # Porcentaje
            elif op == 11:
                num1 = validar_flotante("Ingrese el valor total de su número: ")
                num2 = validar_flotante("Ingrese el porcentaje que quiere calcular de el anterior número (sin el símbolo %): ")
                resultado = (num1 * num2) / 100
                print(f"El {num2}% de {num1} es: ", resultado)
            # Logaritmo base 10
            elif op == 12:
                num1 = validar_flotante("Ingrese el valor para calcular su logaritmo base 10: ")
                if num1 > 0:
                    print(f"El logaritmo base 10 de {num1} es: ", math.log10(num1))
                else:
                    print("Error: El logaritmo solo se puede definir en números mayores a cero (Positivos).")
            # Factorial
            elif op == 13:
                num1 = validar_entero("Ingrese un número entero positivo para calcular su factorial: ")
                if num1 >= 0:
                    print(f"El factorial de {num1} es: ", math.factorial(num1))
                else:
                    print("Error: No se puede calcular el factorial de un número negativo.")
            # Salida
            elif op == 14:
                print("Se ha cerrado el programa. Gracias por utilizarlo.")
        # Pregunta de continuación 
        continuar = input("¿Desea continuar utilizando el programa? (s/n): ").lower().strip()
        if continuar != "s":
            print("Saliste del programa. Gracias por utilizarlo, suerte! ")
            break
### Comprobación de main ###

if __name__ == "__main__":
    clear_window()
    module_error(__name__, __file__, __package__, __doc__)
