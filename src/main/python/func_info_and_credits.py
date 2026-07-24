# Documentacion del main

"""
Modulo de informacion y creditos del sistema operativo.
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

import time
import os
import sys
import platform
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from utils import clear_window, loading, ansi_text, init_username, call_username, main_error, module_error

def main():
    """
    Informacion y creditos.
    -
            Displays information and credits about the application.

    Args:
        None.
    ---
    Returns:
        print info and credits.
    ---
    Raises:
        None.
    ---
    """

    # SOPORTE DE RESPALDO SEGURO PARA WINDOWS (Evita caídas si falta el paquete tzdata)
    try:
        tz_caracas = ZoneInfo("America/Caracas")
        info_tz_name = datetime.now(tz_caracas).tzname()
        info_tz_loc = str(tz_caracas)
        info_tz_time = datetime.now(tz_caracas).strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        info_tz_name = "VET (Huso Horario No Detectado)"
        info_tz_loc = "America/Caracas (Requiere paquete tzdata)"
        info_tz_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " (Usando Hora Local)"

    print(f"{ansi_text.ORANGE}={ansi_text.RESET}" * 95)
    print(f"{ansi_text.WHITE}CENTRO DE INFORMACION Y CREDITOS{ansi_text.RESET}".center(95))
    print(f"{ansi_text.ORANGE}={ansi_text.RESET}" * 95)
    print(f"{ansi_text.CYAN}- Application Name: {ansi_text.RESET}UPTAG CLI OS - Command Line Interface Operating System")
    print(f"{ansi_text.CYAN}- Description: {ansi_text.RESET}Sistema operativo de linea de comandos para la gestion de archivos y directorios.")
    print(f"{ansi_text.CYAN}- Hecho en: {ansi_text.RESET}Coro, Falcon, Venezuela. 2026.")
    print(f"{ansi_text.CYAN}- Version: {ansi_text.RESET}Beta v1.0.0")
    print(f"{ansi_text.CYAN}- Hora actual: {ansi_text.RESET}", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print(f"{ansi_text.CYAN}- Zona horaria: {ansi_text.RESET}", info_tz_name)
    print(f"{ansi_text.CYAN}- Ubicacion de la zona horaria: {ansi_text.RESET}", info_tz_loc)
    print(f"{ansi_text.CYAN}- Fecha y hora UTC: {ansi_text.RESET}", datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"))
    print(f"{ansi_text.CYAN}- Fecha y hora local: {ansi_text.RESET}", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print(f"{ansi_text.CYAN}- Fecha y hora del sistema: {ansi_text.RESET}", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print(f"{ansi_text.CYAN}- Fecha y hora del sistema en UTC: {ansi_text.RESET}", datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"))
    print(f"{ansi_text.CYAN}- Fecha y hora del sistema en zona horaria: {ansi_text.RESET}", info_tz_time)
    print(f"{ansi_text.CYAN}- Sistema operativo: {ansi_text.RESET}", os.name)
    print(f"{ansi_text.CYAN}- Plataforma: {ansi_text.RESET}", sys.platform)
    print(f"{ansi_text.CYAN}- Version de Python: {ansi_text.RESET}", sys.version)
    print(f"{ansi_text.CYAN}- Fecha de creacion del OS: {ansi_text.RESET}", "28 de Junio del 2026")
    print(f"{ansi_text.CYAN}- Maquina: {ansi_text.RESET}", platform.machine())
    print(f"{ansi_text.CYAN}- Procesador: {ansi_text.RESET}", platform.processor())
    print(f"{ansi_text.CYAN}- Arquitectura: {ansi_text.RESET}", platform.architecture())
    print(f"{ansi_text.CYAN}- Usuario actual: {ansi_text.RESET}", os.getlogin())
    print(f"{ansi_text.CYAN}- Directorio actual: {ansi_text.RESET}", os.getcwd())
    print(f"{ansi_text.CYAN}- Directorio home: {ansi_text.RESET}", os.path.expanduser("~"))
    print(f"{ansi_text.CYAN}- Directorio raiz: {ansi_text.RESET}", os.path.abspath(os.sep))
    print(f"{ansi_text.CYAN}- Directorio temporal: {ansi_text.RESET}", os.path.abspath(os.getenv("TMPDIR", "/tmp")))
    print(f"{ansi_text.CYAN}- Directorio de trabajo: {ansi_text.RESET}", os.path.abspath(os.getcwd()))
    print(f"{ansi_text.CYAN}- Files en el directorio actual: {ansi_text.RESET}", os.listdir(os.getcwd()))
    print(f"{ansi_text.CYAN}- Variables de entorno: {ansi_text.RESET}", "[OCULTO POR SEGURIDAD EN INTERFAZ]") # Nota: imprimir os.environ directamente satura la pantalla CLI con strings masivos impredecibles.
    print(f"{ansi_text.CYAN}- Ruta del script: {ansi_text.RESET}", os.path.abspath(__file__))
    print(f"{ansi_text.GRAY}Datos de depuración del Intérprete:{ansi_text.RESET}")
    print(f"- Entorno (__name__): {__name__} (Modo de ejecución directa)")
    print(f"- Paquete (__package__): {__package__}")
    print(f"- Ubicación de la interpretación del archivo: ", os.path.abspath(sys.argv[0]))
    print(f"- Documentación activa:\n{__doc__}")
    print(f"""{ansi_text.CYAN}      - Autores:{ansi_text.RESET}
        
        - {ansi_text.ORANGE}Francisco Garcia (33.251.860){ansi_text.RESET} | Creador del proyecto y desarrollador principal, creador del codigo del run.bat, main.py, este modulo de funcion de informacion y creditos y utils.py. Creador de la webpage index.html e style.css, archivos markdowns, implicaciones en el algoritmo, pseudocodigo y diagramas de flujo. Creador del LICENSE.md y CONTRIBUTING.md. Creador de sistema ANSI Y ASCII. Organizacion de la modulacion, CI workflow y estructura de carpetas .git y .github. Depurador y debugger beta testing. \n
        
        - {ansi_text.ORANGE}Luis Sanchez (32.630.801){ansi_text.RESET} | Creador del modulo funcion de los 2 juegos, adivinanza y piedra, papel o tijera. Documentador, depurador y debugger beta testing. \n
        
        - {ansi_text.ORANGE}Ivan Quevedo (34.570.333){ansi_text.RESET} | Creador del modulo funcion de calculadora cientifica y funcion de comprobacion de inputs globales del OS, documentador, depurador y debugger beta testing. \n
        
        - {ansi_text.ORANGE}Santiago Rojas (33.652.368){ansi_text.RESET} | Creador del modulo funcion convertor de divisas, suplentador auxiliar, documentador, depurador y debugger beta testing. \n
        
        - {ansi_text.ORANGE}Hanzer Sivira (32.913.679){ansi_text.RESET} | Creador del modulo funcion de manual de uso, documentador, depurador y debugger beta testing. \n
    """)
    print(f"""Licencia: Copyright (c) 2026 Ciszuko

{ansi_text.GRAY}- Permission is hereby granted, free of charge, to any person obtaining a copy
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
SOFTWARE.{ansi_text.RESET}
""")
    print(f"{ansi_text.ORANGE}={ansi_text.RESET}" * 95)

### Comprobación de main ###

if __name__ == "__main__":
    clear_window()
    module_error(__name__, __file__, __package__, __doc__)
