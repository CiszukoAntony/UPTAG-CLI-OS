#Anteriormente Esta funcion aceptaba numeros negativos a la hora de recibir el valor a convertir
#Ahora no los acepta y avisa al usuario de este error
def validar_entrada(mensaje, limite, tipo):
    """
    Recibe la entrada de datos que ingrese el usuario, valida si el dato entra en los requerimientos y retorna este dato
    
    PARAMETROS
    ----------
    
    Mensaje
        Es el mensaje que le indica al usuario que debe de ingresar
    
    Parametro1
        Establece el limite de valores(numero) que puede ingresar el usuario (el minimo)
    
    Parametro2
        Establece el limite de valores(numero) que puede ingresar el usuario (el maximo)
    
    Tipo
        Le indica a la funcion que si va a usar limites o no
            1 si va a usar el limite para un rango de numeros
            2 si no va usar ese rango de numeros
    
    Retorna
    ----------
    La entrada del usuario ya validada
    """
    print("-"*100)
    while True:
        try:
        
            if tipo == 1:
                entrada = int(input(mensaje))
        
                if 1 <= entrada <= limite:
                    break
        
                else:
                    print("-"*100+"\n"+"ERROR","\nPor favor, ingrese un numero valido", "(1", "-", str(limite) + ")","\n"+"-"*100)
                    entrada = "f"
        
            elif tipo == 2:
                entrada = float(input(mensaje))
                if entrada >= 0:
                    break
        
                elif entrada == "c":
                    break
                else:
                    print("-"*100+"\n"+"ERROR","\nPor favor, ingrese un numero psitivo valido valido","\n"+"-"*100)
                    entrada = "f"
        
        except ValueError:
            print("-"*100+"\n"+"ERROR","\nPor favor, ingrese un numero valido","\n"+"-"*100)
            entrada = "f"
            
        if entrada != "f":
            print("-"*100)
            break
    return entrada

#Antes esta funcion mostraba los resultados
#Viendo que era algo innecesario para ser una funcion fue cambiada para darle un mejor uso y darle al usuario informacion extra
def devolver_cadena(cadena, cadenaIs, cadenaAn, cadenacon):
    """
    Cambia el valor entero del dato de tipo entero a una cadena de caracteres, sean nombres o sufijos
    
    PARAMETROS
    ----------
    cadena
        el valor de esta variable va a ser cambiado por una cadena de testo segun su valor
        
    cadenaIs
        es la lista de cadenas de caracteres del sistema internacional (nombres o sufijos) cual se utilizara para intercambiar el valor de dato
            tambien sirve de limite para asignar las cadenas de texto del sistema anglosajon
    
    cadenaAn
        es la lista de cadenas de caracteres del sistema anglosajon (nombres o sufijos) cual se utilizara para intercambiar el valor de dato
    
    cadenacon
        si esta cadena no esta vacia, va a buscar en esta cadena 

    Retorna
    ----------
        retorna el dato con su cadena asignada
    """

    #Apartir de aqui, se van cambiando los valores numericos por cadenas de texto, que estan guardadas dentro de arreglos
    if cadenacon == None:
        if cadena > len(cadenaIs):
            cadena = cadenaAn[cadena - len(cadenaIs) - 1]


        else:
            cadena = cadenaIs[cadena - 1]
    else:
        cadena=cadenacon[cadena - 1]
    return cadena


def convertir_unidadis(valor_final, unidad1, unidad2, unidad):
    """
    Recibe el valor ingresado por el usuario y lo transforma, dentro del sistema internacional, segun sus indicaciones(parametros)
    
    PARAMETROS
    ----------
    
    valor_final
        Es el valor ingresado por el usuario
    
    unidad1
        Es la unidad asignada al valor, utilizada para poder convertirlo a la unidad2
    
    unidad2
        Es una condicion para establecer si el valor a sido convertido o no
    
    unidad
        es un arreglo con un conjunto de valores, valores los cuales se acceden gracias a la unidad1 y unidad2
            los valores del arreglos deben ser digitos (flotantes)
            
            Los valores de los arreglos deben de estar ordenados correctamente(segun el sistema internacional)
            
            La cantidad de datos maxima debe ser igual a la cantidad maxima del dato de la unidad1 y unidad2
    Retorna
    ----------
    La el valor ingresado por el usuario pero ya convertido a la unidad que eligio
    
    """
    unidad1 = unidad[unidad1 - 1]

    unidad2 = unidad[unidad2 - 1]

    while unidad1 != unidad2:
    
        if unidad1 > unidad2:
            unidad1 = unidad1 / 10
            valor_final = valor_final * 10
    
        elif unidad1 < unidad2:
            unidad1 = unidad1 * 10
            valor_final = valor_final / 10
    
    return valor_final


def convertir_unidadan(valor_final, unidad1, unidad2, unidad):
    """
    Recibe el valor ingresado por el usuario y lo transforma segun sus indicaciones(parametros)
    
    PARAMETROS
    ----------
    
    valor_final
        Es el valor ingresado por el usuario
    
    unidad1
        Es la unidad asignada al valor, utilizada para poder convertirlo a la unidad2
    
    unidad2
        Es una condicion para establecer si el valor a sido convertido o no
    
    unidad
        es un arreglo con un conjunto de valores, valores los cuales se acceden gracias a la unidad1 y unidad2
            los valores del arreglos deben ser digitos (flotantes)
            
            Los valores de los arreglos deben de estar ordenados correctamente(segun el sistema anglosajon)
            
            La cantidad de datos maxima debe ser menor a diferencia de la que puede ser el maximo que tiene unidad1 y unidad2 en uno
            por ejemplo, unidad1 y unidad2 pueden tener un maximo de 4 opciones
            y la cantidad de datos dentro del arreglo debe ser menor en 1, 3.
    Retorna
    ----------
    La el valor ingresado por el usuario pero ya convertido a la unidad que eligio
    
    """
    unidad1 = unidad1 - 1
    unidad2 = unidad2 - 1

    while unidad1 != unidad2:
    
        if unidad1 > unidad2:
            unidad1 = unidad1 - 1
            valor_final = valor_final * unidad[unidad1]

        elif unidad1 < unidad2:
            valor_final = valor_final / unidad[unidad1]
            unidad1 = unidad1 + 1

    return valor_final

#encuentra la posicion de la unidad que se le indique, dentro de la lista de unidades que se le indique
def encontrar_posicion(lista, valor):
    """
    Encuentra la posicion de un valor dentro de una lista
    
    PARAMETROS
    ----------
    Lista
        la lista en la que va a buscar el valor
    valor
        el valor a buscar

    Retorna
    ----------
        la posicion del valor encontrado
    """
    for i in range(0,len(lista)):
        posicion=lista[i]
    
        if posicion == valor:
            return i+1
    
def encontrarCadenaMayor(lista):
    """
    Encuentra la cadena de caracteres más grande
    
    PARAMETROS
    ----------
    Lista
        la lista en la que va a buscar la cadena de caracteres más grande

    Retorna
    ----------
        la posicion del valor encontrado
    """
    cadenaMayor=lista[0]
    
    for i in range(0,len(lista)):
        if len(lista[i]) > len(cadenaMayor):
            cadenaMayor=lista[i]
    
    return cadenaMayor
    
def igualarCadena(lista,cadenaMayor):
    """
    Iguala la longitud de una cadena agregandole una cantidad de espacios de acuerdo con la diferencia que tiene con la referencia, cadenaMayor.
    
    PARAMETROS
    ----------
    Lista
        la lista que se usara para cambiar las longitudes del las cadenas

    Retorna
    ----------
        la lista con sus valores igualados a la longitud de la cadenaMayor
    """
    cadenaMayor=cadenaMayor+" "*10
    
    for i in range(0,len(lista)):
    
        if len(lista[i])<len(cadenaMayor):
            dif=len(cadenaMayor)-len(lista[i])
            lista[i]=lista[i]+" "*dif
    
    return  lista
    
def main():
    """
    El menu y centro de datos y operaciones del convertidor de unidades de longitud
    
    PARAMETROS
    ----------
        ninguna

    Retorna
    ----------
        ninguno
    """
    #unidades del sistema internacional (kilometro, hectometro, decametro, metro, decimetro, centimetro, milimetro)
    unidadis = [10 ** 3, 10 ** 2, 10 ** 1, 10 ** 0, 10 ** -1, 10 ** -2, 10 ** -3]
    nombreIs = ["Kilometros", "Hectometros","Decametros","Metros","Decimetros","Centimetros","Milimetros"]
    sufijoIs = ["km", "hm", "dam", "m", "dm", "cm", "mm"]
        
    #unidades del sistema anglosajon (pulgada, pies, yardas, millas)
    unidadan = [1000,12, 3, 5.5, 4, 10, 8, 3]
    nombreAn = ["Mil","Pulgadas", "Pies", "Yardas", "Rod", "Cadena", "Furlong", "Millas", "Leguas"]
    sufijoAn = ["mil","in", "f", "yd", "rd", "ch", "fur", "mi","legua"]
        
    #valores de conversion entre los dos sistemas 
    #para pulgada, pies y yardas los valores estan convertidos en centimetros
    #para millas lo el valor esta convertido en kilometros
    unidadcon = [0.00254,2.54, 30.48, 91.44, 5.0292, 20.1168, 201.168, 1.60934, 4.828032]
    nombrecon = ["mm","cm", "cm", "cm", "m", "m", "m","km","km"]        
    #establesco el limite que se utilizara como parametro más adelante
    #amentandolo en dos para que tambien acepte la ultima unidad del sistema anglosajon y el numero de salida
    limite_is=len(nombreIs)
    limite_an=limite_is+(len(nombreAn))
    limite_op = len(nombreIs) + len(nombreAn) + 1
    
    #Para el menu visual, necesitaremos hacer que cada nombre tenga la misma longitud para que las dos columnas esten a la misma distancia
    #Y saber que lista es mayor para el numero de veces se tendra que añadir el valor de las columnas en sus filas
    cadenaMayor=encontrarCadenaMayor(lista=[encontrarCadenaMayor(nombreIs),encontrarCadenaMayor(nombreAn)])
    
    listaUnidades=nombreIs+nombreAn
    
    listaUnidades=igualarCadena(listaUnidades,cadenaMayor)
    
    #agrega la enunemaracion de las opciones
    for i in range(0,len(listaUnidades)):
        if i < 9:
            listaUnidades[i]="( 0"+str(i+1)+". )"+listaUnidades[i]
        else:
            listaUnidades[i]="( "+str(i+1)+". )"+listaUnidades[i]
            
    limiteMayor=len(encontrarCadenaMayor(lista=[nombreIs,nombreAn]))
    
    listaUnidad=""
    
    #crea el menu reutilisable de opciones y unidades
    for i in range(0,limiteMayor+1):
            
        if i < len(nombreIs):
            listaUnidad=listaUnidad+listaUnidades[i]

        else:
            listaUnidad=listaUnidad+" "*len(listaUnidades[0])
            
        if i+limite_is < len(listaUnidades):
            listaUnidad=listaUnidad+listaUnidades[i+limite_is]
                
        elif i+limite_is == len(listaUnidades):
            if limite_op < 9:
                listaUnidad=listaUnidad+"( 0"+str(limite_op)+". )"+"salir"
            else:
                listaUnidad=listaUnidad+"( "+str(limite_op)+". )"+"salir"
        
        listaUnidad=listaUnidad+"\n"
    listaUnidad=listaUnidad+"-"*100+"\n"
    
    while True:    
        
                
        print("-"*100)
        print(" "*30+"Convertidor de unidades de longitud\n")
        

        unidadEntrada = sufijoEntrada = nombreEntrada = validar_entrada(mensaje=listaUnidad+"Seleccione la unidad que quiere convertir: ", limite=limite_op, tipo=1)
        
        print("-"*100)
        if unidadEntrada == limite_op:
            print("\n"+"-"*100)
            print("\n"+"/"*41+"Programa finalizado"+"/"*40)
            print("\n"+"-"*100)
            break
        
        nombreEntrada = devolver_cadena(cadena= nombreEntrada, cadenaIs= nombreIs, cadenaAn= nombreAn, cadenacon= None)
        sufijoEntrada = devolver_cadena(cadena= sufijoEntrada, cadenaIs= sufijoIs, cadenaAn= sufijoAn, cadenacon= None)
    

        unidadSalida = sufijoSalida = nombreSalida = validar_entrada(mensaje=listaUnidad+"\nDe "+nombreEntrada+" a cual otra unidad la desea convertir: ", limite=limite_op, tipo=1)
        
        print("-"*100)
        if unidadSalida == limite_op:
            print("\n"+"-"*100)
            print("\n"+"/"*41+"Programa finalizado"+"/"*40)
            print("\n"+"-"*100)
            break
        
        nombreSalida = devolver_cadena(cadena= nombreSalida, cadenaIs= nombreIs, cadenaAn= nombreAn, cadenacon= None)
        sufijoSalida = devolver_cadena(cadena= sufijoSalida, cadenaIs= sufijoIs, cadenaAn= sufijoAn, cadenacon= None)
        
        
        while True:
            valor = valorEntrada = validar_entrada(mensaje="\nIngrese el valor que quieres convertir de "+nombreEntrada+" a "+nombreSalida+": ",
                                    limite=None,tipo=2)
            print("-"*100)
        
            #evalua sí el programa requiere llamar cual funcion o usar cual proceso 
            #o si el requisito de igualda entre unidades elegidas por el usuario se cumple
            if unidadEntrada==unidadSalida:
                valorFinal= valor
        
            #conversion interna (sistema internacional)
            elif (1 <= unidadEntrada <= limite_is) and (1 <= unidadSalida <= limite_is):
                valorFinal = convertir_unidadis(valor_final=valor, unidad1=unidadEntrada, unidad2=unidadSalida, unidad=unidadis)

            #conversion interna (sistema anglosajon)
            elif ( (limite_is+1) <= unidadEntrada <= limite_an) and ( (limite_is+1) <= unidadSalida <= limite_an):
                valorFinal = convertir_unidadan(valor_final=valor, unidad1=(unidadEntrada - limite_is), unidad2=(unidadSalida - limite_is), unidad=unidadan)

            #conversion cruzada o mixta (sistema internacional a sistema anglosajon)
            elif (1 <= unidadEntrada <= limite_is) and ( (limite_is+1) <= unidadSalida <= limite_an):
            
            
                if sufijoEntrada != nombrecon[unidadSalida -(limite_is) -1]:
                    #haremos la conversion en el mismo sistema basandose en la posicion de la unidad salida, buscando a partir del nombre que unidad hay que convertirla ntes de convertirlo al otro sistema
                    unidadinter = encontrar_posicion(sufijoIs, valor=devolver_cadena(cadena= unidadSalida -(limite_is) , cadenaIs= None, cadenaAn= None, cadenacon= nombrecon))
                
                    valor = convertir_unidadis(valor_final=valor, unidad1=unidadEntrada, unidad2=unidadinter, unidad=unidadis)
                    
        
                valorFinal = valor / unidadcon[unidadSalida -(limite_is) -1]

            #conversion cruzada o mixta (sistema anglosajon a sistema internacional)
            elif ((limite_is+1) <= unidadEntrada <= limite_an) and (1 <= unidadSalida <= limite_is) :
            
                #dependiendo de la unidad, esta se puede transformar en alguna de las diferentes unidades del sistema internacional
                #esto es para preparar la conversion dentro del sistema internacional
                valorFinal = valor * unidadcon[unidadEntrada - (limite_is) -1]
                
                unidadinter=encontrar_posicion(lista=sufijoIs,valor=devolver_cadena(cadena=unidadEntrada - (limite_is),cadenaIs= None, cadenaAn= None, cadenacon= nombrecon))   
             
                if unidadinter != unidadSalida:
                    valorFinal = convertir_unidadis(valor_final=valorFinal, unidad1=unidadinter, unidad2=unidadSalida, unidad=unidadis)
        
            print("De "+nombreEntrada+" a "+nombreSalida+".","\n\n"+str(valorEntrada) + sufijoEntrada, "es igual a", str(valorFinal) + sufijoSalida)  
        
            opcion = validar_entrada(mensaje="""1|Convertir Otro Valor
2|Ir al Menu
----------------------------------------------------------------------------------------------------
Seleccione una de las siguientes opciones: """, limite=2, tipo=1)
        
            if opcion == 2:
                break
