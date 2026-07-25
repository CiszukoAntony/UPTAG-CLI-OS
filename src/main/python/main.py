# Importacion de librerias y modulos.

import sys
import func_juego_piedra_papel_tijera
import func_juego_adivina
import func_calculadora
import func_manual_de_uso
import func_info_and_credits
import func_divisa
import func_convertidor_unidades_longitud
from utils import clear_window, loading, ansi_text, init_username, call_username, main_error, module_error

# Documentacion del Mini Sistema Operativo UPTAG CLI OS

doc_uptag = """UPTAG CLI OS

MiniProyecto de Algoritmo y Programacion.
UPTAG PNfi S10 T1T1.

INTEGRANTES

- Francisco Garcia (33.251.860)
- Luis Sanchez (32.630.801)
- Ivan Quevedo (34.570.333)
- Santiago Rojas (33.652.368)
- Hanzer Sivira (32.913.679)

Coro, Falcon, Venezuela.
2026.

Descripción General

El proyecto consiste en el diseño e implementación de un simulador de Sistema Operativo basado en una Interfaz de Línea de Comandos (CLI). El sistema operará a través de un menú visual estructurado con bordes decorativos (ej. usando el carácter "=") e índices numéricos. Este entorno integrará un conjunto de utilidades prácticas y de entretenimiento, gestionadas a través de una arquitectura modular basada en funciones. El programa garantiza una experiencia de usuario continua gracias a un ciclo de ejecución infinito que solo se interrumpe cuando el usuario selecciona explícitamente la opción de salir, además de estar blindado contra errores de digitación mediante el manejo de excepciones.

A. Entradas (Inputs):

Navegación del Sistema: Selección de opciones a través de números enteros (del 1 al máximo de opciones disponibles en el menú principal).

Datos de Aplicaciones Utilitarias: * Calculadora Científica: Ingreso de expresiones matemáticas o números y operadores.

Conversor de Divisas: Ingreso del monto a convertir y selección de la moneda de origen y destino.

Datos de Entretenimiento (Juegos):

Adivina el Número: Ingreso de intentos numéricos enteros.

Piedra, Papel o Tijera: Selección numérica o de texto (strings) representando la jugada del usuario.

Señales de interrupción: Teclas como [ENTER] para continuar o comandos de salida.

B. Proceso (Process):

Bucle Principal (Estructura Repetitiva): Un ciclo while True (o "Mientras" en PSeInt) que mantiene el OS en ejecución constante, refrescando la pantalla y mostrando el menú principal tras cada acción terminada.

Manejo y Validación de Errores: Uso de bloques try...except para capturar errores de tipo (ej. ingresar una letra cuando se pide un número para navegar el menú) y evitar el "crasheo" del sistema.

Enrutamiento Lógico (Condicionales): Estructuras if / elif / else (o "Según / Caso") que evalúan la entrada del usuario y hacen el llamado a la función correspondiente.

Ejecución Modular (Funciones): Cada "aplicación" del sistema operativo vive en su propia función.

Lógica del Juego Adivinanza: Se genera un número aleatorio; un ciclo while evalúa la entrada del usuario usando condicionales para determinar la distancia absoluta y devolver el estado de "Frio" o "Caliente".

Lógica de PPT: Uso de la librería random para la jugada de la máquina y condicionales lógicos combinados (and/or) para determinar victoria, derrota o empate.

Limpieza de pantalla: Ejecución de comandos del sistema anfitrión (cls o clear) para simular el refresco de pantalla del OS.

C. Salidas (Outputs):

Interfaz Gráfica de Texto (TUI): Menús interactivos delineados con separadores visuales (=========================) que muestran las aplicaciones instaladas:

Calculadora Científica

Conversor de Divisas

Juego: Adivina el Número

Juego: Piedra, Papel o Tijera

Manual de Uso

Información del SO y Créditos

Salir

Resultados Computados: Valores numéricos con formato exacto o decimal (resultados matemáticos y conversiones monetarias).

Feedback de Usuario: Mensajes de estado como alertas de error ("Entrada inválida, intente de nuevo"), pistas interactivas de los juegos ("¡Estás muy caliente!") y notificaciones del sistema ("Saliendo del OS...").

Requisitos Técnicos y Metodológicos a cumplir:

Trabajo Colaborativo: Cada integrante del equipo desarrollará y será responsable de al menos un módulo o "aplicación" funcional del OS.

Modularidad: Uso obligatorio de funciones (def en Python / SubProceso en PSeInt) para encapsular la lógica de cada opción del menú.

Documentación: El código fuente contará con Docstrings al inicio de cada función explicando sus parámetros y retornos, así como comentarios de línea (#) para bloques lógicos complejos.

Diseño Previo: Se entregará el Pseudocódigo y Diagrama de Flujo del menú principal y sus ramificaciones elaborados en la herramienta PSeInt.

¿Qué problemática resuelve?

En el contexto actual de la informática, los usuarios a menudo dependen de múltiples aplicaciones pesadas y separadas (una app de calculadora, consultas de divisas en navegadores web, juegos casuales independientes) para realizar tareas cotidianas sencillas. Esto genera tres problemas principales:

Consumo de recursos: Mantener múltiples aplicaciones o pestañas del navegador abiertas consume excesiva memoria RAM y ciclos de procesamiento, lo cual es ineficiente, especialmente en equipos de bajos recursos o hardware antiguo.

Pérdida de foco y tiempo (Context Switching): Cambiar constantemente entre diferentes interfaces gráficas distrae al usuario y reduce la agilidad para resolver problemas rápidos (como un cálculo relámpago o una conversión rápida).

Fragmentación Educativa: Desde la perspectiva del estudiante de informática, comprender cómo pequeñas piezas de código se unen para formar un ecosistema de software grande suele ser abstracto y difícil de asimilar.

La Solución aportada por el proyecto:
Este Mini Sistema Operativo CLI resuelve estas problemáticas ofreciendo un entorno unificado, ultra-ligero y libre de distracciones. Al centralizar herramientas vitales (matemáticas, financieras) y opciones de esparcimiento (juegos) en una sola interfaz de texto, el programa consume una cantidad ínfima de recursos del sistema anfitrión, respondiendo de manera instantánea.

Además, blinda al usuario contra la frustración operativa mediante su sistema de validación de errores (try-except), garantizando que la herramienta no se cierre abruptamente ante una equivocación humana. Finalmente, desde el punto de vista académico, resuelve el reto de la integración: demuestra en la práctica cómo la arquitectura modular (modularidad por funciones) permite a un grupo de programadores colaborar en un mismo ecosistema, construyendo un producto escalable donde cada "aplicación" es un engranaje de un sistema mayor

Según el profesor Carlos Noguera, para obtener la calificación máxima, se debe cumplir con los siguientes criterios:

- Modularidad: Uso obligatorio de funciones (def en Python / SubProceso en PSeInt) para encapsular la lógica de cada opción del menú.
- Documentación: El código fuente contará con Docstrings al inicio de cada función explicando sus parámetros y retornos, así como comentarios de línea (#) para bloques lógicos complejos.
- Diseño Previo: Se entregará el Pseudocódigo y Diagrama de Flujo del menú principal y sus ramificaciones elaborados en la herramienta PSeInt

Copyright (c) 2026 Ciszuko

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""



# Main.

def main():
    """
    Función principal del sistema operativo.
    -
        Funcion principal main del sistema operativo UPTAG CLI OS.
            1. Calculadora Científica
            2. Conversor de Divisas
            3. Convertidor De Unidades De Longitud
            4. Juego: Adivina el Número
            5. Juego: Piedra, Papel o Tijera
            6. Manual de Uso
            7. Información del SO y Créditos
            8. Apagar Sistema Operativo
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

    clear_window() # Limpia la pantalla del editor
    print(f"{ansi_text.CYAN}Cargando entorno del sistema operativo UPTAG CLI OS...{ansi_text.RESET}")
    loading(3, 1, "Cargando entorno del sistema operativo UPTAG CLI OS...  ")
    print(f"""{ansi_text.ORANGE_BACKGROUND_BOLD}
     ___  ___  ________  _________  ________  ________                 ________  ___       ___                 ________  ________      
    |\  \|\  \|\   __  \|\___   ___|\   __  \|\   ____\               |\   ____\|\  \     |\  \               |\   __  \|\   ____\     
    \ \  \|\  \ \  \|\  \|___ \  \_\ \  \|\  \ \  \___|   ____________\ \  \___|\ \  \    \ \  \  ____________\ \  \|\  \ \  \___|_    
     \ \  \|\  \ \   ____\   \ \  \ \ \   __  \ \  \  ___|\____________\ \  \    \ \  \    \ \  \|\____________\ \  \|\  \ \_____  \   
      \ \  \|\  \ \  \___|    \ \  \ \ \  \ \  \ \  \|\  \|____________|\ \  \____\ \  \____\ \  \|____________|\ \  \|\  \|____|\  \  
       \ \_______\ \__\        \ \__\ \ \__\ \__\ \_______\              \ \_______\ \_______\ \__\              \ \_______\____\_\  \ 
        \|_______|\|__|         \|__|  \|__|\|__|\|_______|               \|_______|\|_______|\|__|               \|_______|\_________\{ansi_text.RESET} \n""")

    print(f"{ansi_text.CYAN}Bienvenido/a al sistema operativo {ansi_text.ORANGE}UPTAG CLI OS{ansi_text.RESET}...", end=" ", flush=True)
    loading(3, 0)
    print(f"{ansi_text.WHITE}Estamos preparando todo para ti...{ansi_text.RESET}")

    loading(6, 1, "Preparando el equipo :p ")
    init_username()

    print(f"{ansi_text.WHITE}¡Hola! {call_username()}, ¡Bienvenido/a! al sistema operativo {ansi_text.ORANGE}UPTAG CLI OS{ansi_text.RESET}...{ansi_text.RESET}")
    loading(2, 1, "Cargando entorno... ")

    input(f"{ansi_text.WHITE}=== PRESIONA {ansi_text.GREEN}ENTER{ansi_text.RESET} PARA {ansi_text.BLUE}INICIAR{ansi_text.RESET} EL SISTEMA OPERATIVO {ansi_text.ORANGE}UPTAG CLI OS{ansi_text.RESET}{ansi_text.WHITE} ==={ansi_text.RESET}")

    while True:

        # Limpieza de pantalla pre-menu.
        clear_window()
        print(f"{ansi_text.YELLOW}={ansi_text.RESET}" * 140)
        print(f"""{ansi_text.ORANGE_BACKGROUND_BOLD}
     ___  ___  ________  _________  ________  ________                 ________  ___       ___                 ________  ________      
    |\  \|\  \|\   __  \|\___   ___|\   __  \|\   ____\               |\   ____\|\  \     |\  \               |\   __  \|\   ____\     
    \ \  \|\  \ \  \|\  \|___ \  \_\ \  \|\  \ \  \___|   ____________\ \  \___|\ \  \    \ \  \  ____________\ \  \|\  \ \  \___|_    
     \ \  \|\  \ \   ____\   \ \  \ \ \   __  \ \  \  ___|\____________\ \  \    \ \  \    \ \  \|\____________\ \  \|\  \ \_____  \   
      \ \  \|\  \ \  \___|    \ \  \ \ \  \ \  \ \  \|\  \|____________|\ \  \____\ \  \____\ \  \|____________|\ \  \|\  \|____|\  \  
       \ \_______\ \__\        \ \__\ \ \__\ \__\ \_______\              \ \_______\ \_______\ \__\              \ \_______\____\_\  \ 
        \|_______|\|__|         \|__|  \|__|\|__|\|_______|               \|_______|\|_______|\|__|               \|_______|\_________\{ansi_text.RESET} \n""")
        
        print(f"{ansi_text.YELLOW}={ansi_text.RESET}" * 140)

        print(f"\n {ansi_text.WHITE}[{ansi_text.CYAN} ! {ansi_text.WHITE}] Buenas {call_username()}. ¿Que deseas hacer hoy...?{ansi_text.RESET} \n".center(100))
        loading(1)

        opciones = [
            "Calculadora Científica",                 #1
            "Conversor de Divisas",                   #2
            "convertidor de unidades de longitud",    #3
            "Juego: Adivina el Número",               #4
            "Juego: Piedra, Papel o Tijera",          #5
            "Manual de Uso",                          #6
            "Información del SO y Créditos",          #7
            "Apagar Sistema Operativo"                #8
        ]
        llamadas=[func_calculadora.main,
                  func_divisa.main,
                  func_convertidor_unidades_longitud.main,
                  func_juego_adivina.main,
                  func_juego_piedra_papel_tijera.main,
                  func_manual_de_uso.main,
                  func_info_and_credits.main
                  ]

        print(f"{ansi_text.WHITE}={ansi_text.RESET}" * 100)
        print(f"""{ansi_text.ORANGE}
         __   __                          _                            _                        
        |  \_/  |                        | |                          (_)                       
        |       |_____ ____  _   _     __| |_____     ___  ____   ____ _  ___  ____  _____  ___ 
        | |\_/| | ___ |  _ \| | | |   / _  | ___ |   / _ \|  _ \ / ___) |/ _ \|  _ \| ___ |/___)
        | |   | | ____| | | | |_| |  ( (_| | ____|  | |_| | |_| ( (___| | |_| | | | | ____|___ |
        |_|   |_|_____)_| |_|____/    \____|_____)   \___/|  __/ \____)_|\___/|_| |_|_____|___/{ansi_text.RESET} \n""")
        print(f"{ansi_text.WHITE}={ansi_text.RESET}" * 100)
        print(f"{ansi_text.CYAN}( INDICE. ) {ansi_text.WHITE}| {ansi_text.ORANGE}[ OPCION. ]{ansi_text.RESET}")
        print(f"{ansi_text.GRAY}-{ansi_text.RESET}" * 80)

        for indice, opcion in enumerate(opciones):
            if opcion == opciones[-1]:
                print(f"{ansi_text.CYAN}( {indice + 1}. ){ansi_text.GRAY} | {ansi_text.ORANGE}[ {opcion}. ]{ansi_text.GRAY} | {ansi_text.RED}[ Control + C para Salir ]{ansi_text.RESET}")

            else:
                print(f"{ansi_text.CYAN}( {indice + 1}. ){ansi_text.GRAY} | {ansi_text.ORANGE}[ {opcion}. ]{ansi_text.RESET}")

        print(f"{ansi_text.GRAY}-{ansi_text.RESET}" * 80)

        try:
            opcion_usuario = int(input(f"{call_username()}, seleccione una opción dentro del rango {ansi_text.ORANGE}1 a {len(opciones)}{ansi_text.WHITE} opciones... \n {ansi_text.BLUE_BACKGROUND_BOLD}>>>{ansi_text.RESET} "))-1


            if opcion_usuario < 0 or opcion_usuario > len(llamadas):
                print(f"{ansi_text.RED}Error: Opción inválida, {call_username()}, intente de nuevo. Seleccione una opción dentro del rango {ansi_text.ORANGE}1 a {len(opciones)}{ansi_text.WHITE} opciones... {ansi_text.RESET}")

            else:
                print(f"\n{call_username()}{ansi_text.WHITE}, seleccionó la opción {ansi_text.ORANGE}{opciones[opcion_usuario]}.{ansi_text.RESET}")                
                if opcion_usuario == len(llamadas):
                    break
            
                elif opcion_usuario >= 0 and opcion_usuario <= len(llamadas)-1:
                    print("error")
                    llamadas[opcion_usuario]()
            
            


        except ValueError:
            print(f"{ansi_text.RED}Error: la opcion no es valido, {ansi_text.CYAN}{call_username()}{ansi_text.RESET}, intente de nuevo. Seleccione una opción dentro del rango {ansi_text.ORANGE}1 a {len(opciones)}{ansi_text.WHITE} opciones... {ansi_text.RESET}")

        loading(1)
        input(f"\n{ansi_text.WHITE}=== {call_username()}, presiona {ansi_text.GREEN}ENTER{ansi_text.WHITE} para volver al {ansi_text.ORANGE}MENU PRINCIPAL{ansi_text.RESET} ===\n")

    print(f"\n{ansi_text.WHITE}¡Adios {call_username()}!")
    loading(1)

### Comprobación de main ###
if __name__ == "__main__":
    try:
        clear_window()
        main()

    except KeyboardInterrupt as kd:
        print(f"\n{ansi_text.RED}Error: (Control + C) detectado de forma abrupta... {kd}{ansi_text.RESET}")
        

    print(f"\n{ansi_text.RED}Saliendo del sistema operativo...{ansi_text.RESET}\n")
    loading(3, 1, "Apagando...")
    clear_window()
    print(f"{ansi_text.WHITE}Gracias por usar {ansi_text.ORANGE}UPTAG CLI OS.{ansi_text.RESET}\n")
    loading(2, 1, "Cerrando...")
    sys.exit()

else:
    clear_window()
    main_error(__name__, __file__, __package__, __doc__)
