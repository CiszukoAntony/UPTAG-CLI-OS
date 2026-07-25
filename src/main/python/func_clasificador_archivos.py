"""
Módulo: Clasificador de Archivos por Extensión
Descripción: Organiza archivos en carpetas según su extensión (.txt, .jpg, .pdf, etc.)
Autor: Edmar Garcia
Fecha: 2026
"""

import os
import shutil

# Intentamos importar utilidades extra (colores, limpieza de pantalla, carga).
# Si no existen, definimos sustitutos sencillos para que el script funcione
# sin dependencias adicionales — útil para principiantes.
try:
    from utils import clear_window, ansi_text, call_username, loading
except Exception:
    def clear_window():
        # Limpia la consola (Windows/Unix)
        os.system("cls" if os.name == "nt" else "clear")

    class _AnsiFallback:
        RESET = ""
        CYAN = ""
        YELLOW = ""
        WHITE = ""
        GRAY = ""
        BLUE_BACKGROUND_BOLD = ""
        GREEN = ""
        RED = ""

    ansi_text = _AnsiFallback()

    def loading(seconds=0, steps=1, text=""):
        # Pequeña función de carga no bloqueante para no requerir utilidades externas
        if text:
            print(text)

def main():
    """
    Función principal del Clasificador de Archivos
    
    Args:
        None
    
    Returns:
        None
    """
    clear_window()
    
    print(f"{ansi_text.CYAN}=" * 60)
    print(f"{ansi_text.YELLOW}📂 CLASIFICADOR DE ARCHIVOS POR EXTENSIÓN{ansi_text.RESET}")
    print(f"{ansi_text.CYAN}=" * 60)
    
    print(f"\n{ansi_text.WHITE}Esta herramienta organiza tus archivos en carpetas según su tipo.{ansi_text.RESET}")
    print(f"{ansi_text.GRAY}Ejemplo: .txt → Carpeta 'Textos', .jpg → Carpeta 'Imágenes'{ansi_text.RESET}\n")
    
    # Solicitar la ruta al usuario
    print(f"{ansi_text.CYAN}📁 Ingresa la ruta de la carpeta que quieres organizar:{ansi_text.RESET}")
    print(f"{ansi_text.GRAY}Ejemplo: C:/Users/TuUsuario/Descargas{ansi_text.RESET}")
    print(f"{ansi_text.GRAY}También puedes usar: . (para la carpeta actual){ansi_text.RESET}")
    
    ruta = input(f"\n{ansi_text.BLUE_BACKGROUND_BOLD}>>>{ansi_text.RESET} ").strip()
    
    # Si el usuario presiona Enter sin escribir, usa la carpeta actual
    if ruta == "":
        ruta = "."
        print(f"{ansi_text.YELLOW}Usando carpeta actual: {os.getcwd()}{ansi_text.RESET}")
    
    # Verificar si la ruta existe
    if not os.path.exists(ruta):
        print(f"\n{ansi_text.RED}❌ Error: La ruta '{ruta}' no existe.{ansi_text.RESET}")
        input(f"\n{ansi_text.WHITE}Presiona {ansi_text.GREEN}ENTER{ansi_text.RESET} para continuar...")
        return
    
    # Verificar si es una carpeta
    if not os.path.isdir(ruta):
        print(f"\n{ansi_text.RED}❌ Error: '{ruta}' no es una carpeta.{ansi_text.RESET}")
        input(f"\n{ansi_text.WHITE}Presiona {ansi_text.GREEN}ENTER{ansi_text.RESET} para continuar...")
        return
    
    print(f"\n{ansi_text.GREEN}✅ Ruta válida. Analizando archivos...{ansi_text.RESET}")
    loading(2, 1, "Analizando...")
    
    # Diccionario para clasificar extensiones
    extensiones = {
        # Documentos
        '.txt': 'Textos',
        '.doc': 'Documentos Word',
        '.docx': 'Documentos Word',
        '.pdf': 'PDFs',
        '.xls': 'Hojas de Cálculo',
        '.xlsx': 'Hojas de Cálculo',
        '.ppt': 'Presentaciones',
        '.pptx': 'Presentaciones',
        '.odt': 'Documentos',
        '.rtf': 'Documentos',
        
        # Imágenes
        '.jpg': 'Imágenes',
        '.jpeg': 'Imágenes',
        '.png': 'Imágenes',
        '.gif': 'Imágenes',
        '.bmp': 'Imágenes',
        '.svg': 'Imágenes',
        '.ico': 'Imágenes',
        '.webp': 'Imágenes',
        
        # Videos
        '.mp4': 'Videos',
        '.avi': 'Videos',
        '.mov': 'Videos',
        '.wmv': 'Videos',
        '.flv': 'Videos',
        '.mkv': 'Videos',
        '.webm': 'Videos',
        
        # Música
        '.mp3': 'Música',
        '.wav': 'Música',
        '.flac': 'Música',
        '.aac': 'Música',
        '.ogg': 'Música',
        '.wma': 'Música',
        
        # Archivos comprimidos
        '.zip': 'Archivos Comprimidos',
        '.rar': 'Archivos Comprimidos',
        '.7z': 'Archivos Comprimidos',
        '.tar': 'Archivos Comprimidos',
        '.gz': 'Archivos Comprimidos',
        
        # Programación
        '.py': 'Código Python',
        '.js': 'Código JavaScript',
        '.html': 'Código HTML',
        '.css': 'Código CSS',
        '.json': 'Archivos JSON',
        '.xml': 'Archivos XML',
        '.c': 'Código C',
        '.cpp': 'Código C++',
        '.java': 'Código Java',
        '.php': 'Código PHP',
        '.rb': 'Código Ruby',
        '.go': 'Código Go',
        '.rs': 'Código Rust',
        
        # Ejecutables
        '.exe': 'Ejecutables',
        '.msi': 'Instaladores',
        '.bat': 'Scripts Batch',
        '.sh': 'Scripts Shell',
        
        # Otros
        '.csv': 'CSV',
        '.log': 'Archivos Log',
        '.tmp': 'Temporales',
        '.bak': 'Backups',
        '.iso': 'Imágenes ISO',
        '.img': 'Imágenes de Disco',
    }
    
    # Diccionario para contar archivos por categoría
    contador = {}
    archivos_procesados = 0
    archivos_no_clasificados = 0
    
    # Obtener todos los archivos de la carpeta
    try:
        archivos = os.listdir(ruta)
    except PermissionError:
        print(f"\n{ansi_text.RED}❌ Error: No tienes permisos para leer esta carpeta.{ansi_text.RESET}")
        input(f"\n{ansi_text.WHITE}Presiona {ansi_text.GREEN}ENTER{ansi_text.RESET} para continuar...")
        return
    
    if not archivos:
        print(f"\n{ansi_text.YELLOW}⚠️ La carpeta está vacía. No hay archivos para clasificar.{ansi_text.RESET}")
        input(f"\n{ansi_text.WHITE}Presiona {ansi_text.GREEN}ENTER{ansi_text.RESET} para continuar...")
        return
    
    print(f"\n{ansi_text.CYAN}📋 Archivos encontrados: {len(archivos)}{ansi_text.RESET}")
    print(f"{ansi_text.GRAY}Iniciando clasificación...{ansi_text.RESET}\n")
    # Para principiantes: preguntamos si realmente mover los archivos
    confirmar = input(f"{ansi_text.CYAN}¿Deseas mover los archivos ahora? (S/n): {ansi_text.RESET}").strip().lower()
    mover_archivos = (confirmar == "" or confirmar.startswith("s"))

    # Preguntar si mover archivos no clasificados a carpeta 'Otros'
    confirmar_no_clas = input(f"{ansi_text.CYAN}¿Mover archivos no clasificados a carpeta 'Otros'? (s/N): {ansi_text.RESET}").strip().lower()
    mover_no_clasificados = confirmar_no_clas.startswith("s")

    # Ruta absoluta del script para evitar moverlo por accidente
    try:
        ruta_script = os.path.abspath(__file__)
    except NameError:
        ruta_script = None
    
    # Funciones auxiliares para reducir líneas y repetir lógica mínima
    def _preparar_destino(carpeta_destino, archivo_nombre):
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)
            print(f"{ansi_text.GREEN}📁 Creando carpeta: {os.path.basename(carpeta_destino)}{ansi_text.RESET}")
        base, ext = os.path.splitext(archivo_nombre)
        destino = os.path.join(carpeta_destino, archivo_nombre)
        i = 1
        while os.path.exists(destino):
            destino = os.path.join(carpeta_destino, f"{base}_{i}{ext}")
            i += 1
        return destino

    def _procesar_movimiento(ruta_completa, categoria, mover):
        carpeta_destino = os.path.join(ruta, categoria)
        destino = _preparar_destino(carpeta_destino, os.path.basename(ruta_completa))
        if mover:
            shutil.move(ruta_completa, destino)
            print(f"{ansi_text.WHITE}✅ Movido: {os.path.basename(ruta_completa)} → {categoria}{ansi_text.RESET}")
            return True
        else:
            print(f"{ansi_text.GRAY}Simulación: {os.path.basename(ruta_completa)} → {categoria}{ansi_text.RESET}")
            return False

    # Procesar cada archivo (más compacto)
    for archivo in archivos:
        ruta_completa = os.path.join(ruta, archivo)
        if not os.path.isfile(ruta_completa):
            continue
        if ruta_script and os.path.abspath(ruta_completa) == ruta_script:
            print(f"{ansi_text.GRAY}Ignorado: {archivo} (archivo del script){ansi_text.RESET}")
            continue

        _, extension = os.path.splitext(archivo)
        extension = extension.lower()
        categoria = extensiones.get(extension)
        if not categoria:
            archivos_no_clasificados += 1
            print(f"{ansi_text.YELLOW}⚠️ {archivo}: Extensión no clasificada ({extension}){ansi_text.RESET}")
            if not mover_no_clasificados:
                continue
            categoria = 'Otros'

        try:
            moved = _procesar_movimiento(ruta_completa, categoria, mover_archivos)
        except Exception as e:
            print(f"{ansi_text.RED}❌ Error moviendo {archivo}: {e}{ansi_text.RESET}")
            moved = False

        if moved:
            archivos_procesados += 1
            contador[categoria] = contador.get(categoria, 0) + 1
    
    # Mostrar resumen
    print(f"\n{ansi_text.CYAN}{'=' * 60}{ansi_text.RESET}")
    print(f"{ansi_text.YELLOW}📊 RESUMEN DE CLASIFICACIÓN{ansi_text.RESET}")
    print(f"{ansi_text.CYAN}{'=' * 60}{ansi_text.RESET}")
    
    print(f"{ansi_text.WHITE}📁 Archivos procesados: {archivos_procesados}{ansi_text.RESET}")
    print(f"{ansi_text.YELLOW}⚠️ Archivos sin clasificar: {archivos_no_clasificados}{ansi_text.RESET}")
    
    if contador:
        print(f"\n{ansi_text.GREEN}📋 Distribución por categorías:{ansi_text.RESET}")
        for categoria, cantidad in sorted(contador.items()):
            print(f"  {ansi_text.CYAN}• {categoria}:{ansi_text.RESET} {cantidad} archivo(s)")
    
    if archivos_no_clasificados > 0:
        print(f"\n{ansi_text.YELLOW}💡 Sugerencia: Puedes agregar más extensiones al diccionario en el código.{ansi_text.RESET}")
    
    print(f"\n{ansi_text.GREEN}✅ ¡Clasificación completada!{ansi_text.RESET}")
    
    input(f"\n{ansi_text.WHITE}Presiona {ansi_text.GREEN}ENTER{ansi_text.RESET} para continuar...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{ansi_text.RED}Operación cancelada por el usuario{ansi_text.RESET}")
    except Exception as e:
        print(f"{ansi_text.RED}Error inesperado: {e}{ansi_text.RESET}")
        input(f"\n{ansi_text.WHITE}Presiona {ansi_text.GREEN}ENTER{ansi_text.RESET} para continuar...")