import operaciones_numericas as operacion
import re
import ordenar_datos as ordenar

def imprimir_menu() -> int or -1:
    """
    imprimir_menu: Imprime un menú con diferentes opciones y devuelve la opción seleccionada por el
    usuario como un número entero.

    :return: Un número entero que representa la opción seleccionada por el usuario en el menú. Si el
    usuario ingresa una opción no válida, la función devuelve -1.
    """
    print("\n----------------------------------------------------")
    print("Menú de opciones:")
    print("1. Mostrar la lista de todos los jugadores del Dream Team con Nombre y Posición.")
    print("2. Buscar jugador por índice y mostrar sus estadísticas completas.")
    print("3. Exportar archivo CSV con las estadisticas del jugador del punto 2.")
    print("4. Buscar jugador por nombre y mostrar sus logros.")
    print("5. Calcular y mostrar el promedio de puntos por partido del equipo del Dream Team ordenado por nombre de manera ascendente.")
    print("6. Buscar jugador por nombre y mostrar si es miembro del Salón de la Fama del baloncesto.")
    print("7. Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.")
    print("8. Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.")
    print("9. Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.")
    print("10. Ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.")
    print("11. Ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor.")
    print("12. Ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor.")
    print("13. Calcular y mostrar el jugador con la mayor cantidad de robos totales.")
    print("14. Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.")
    print("15. Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.")
    print("16. Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.")
    print("17. Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos.")
    print("18. Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.")
    print("19. Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas.")
    print("20. Ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.")
    print("23. ")
    print("0. Salir del programa")
    opcion = input("\nIngrese la opción deseada: ")
    print("\n----------------------------------------------------")
    opcion_valida = re.search(r'^[0-9]$|^1[0-9]$|^20$', opcion)
    if not bool(opcion_valida):
        return -1
    opcion = int(opcion)
    return opcion

def obtener_nombre_dato(dict_datos: dict, key_ingresada: str) -> dict or -1:
    """
    obtener_nombre_dato: Obtiene el nombre y un valor de datos específico de un diccionario,
    basado en una clave dada.

    :param dict_datos: Diccionario que contiene datos
    :param key_ingresada: String que hace referencia a la clave que se busca en el diccionario

    :return: Un diccionario con el nombre y el valor de la clave ingresados como argumentos si se
    cumple con las validaciones, o -1 si el diccionario de entrada no es válido o si la clave no se
    encuentra en el diccionario.
    """
    if type(dict_datos) != type(dict()):
        return -1

    if 'nombre' not in dict_datos:
        print(f"Nombre no se encuentra en el diccionario recibido.")
        return -1

    dict_nombre_dato = {}
    dato = None
    nombre = dict_datos["nombre"]

    for key_dict_datos, valor_dict_datos in dict_datos.items():
        if key_ingresada in dict_datos:
            if type(valor_dict_datos) == type(str()) and key_dict_datos == key_ingresada:
                dato = dict_datos[key_ingresada]
        elif key_ingresada in valor_dict_datos:
            if type(valor_dict_datos) == type(dict()):
                for key, valor in valor_dict_datos.items():
                    if key == key_ingresada:
                        dato = valor
            if type(valor_dict_datos) == type(list()):
                for elemento in valor_dict_datos:
                    if key_ingresada in elemento:
                        dato = elemento
                    dato = elemento
        else:
            print(f"{key_ingresada} no se encuentra en el diccionario recibido.")
            return -1

    dict_nombre_dato["nombre"] = nombre
    dict_nombre_dato[key_ingresada] = dato
    return dict_nombre_dato

def imprimir_nombre_dato(dict_datos: dict, key_ingresada: str) -> None or -1:
    """
    imprimir_nombre_dato: Toma un diccionario y una clave como entrada, recupera el nombre y el valor asociado
    con la clave y los imprime formateados según el tipo de valor.

    :param dict_datos: Diccionario que contiene datos para ser impresos.
    :param key_ingresada: String que hace referencia a la clave de los datos que el usuario desea recuperar
    del diccionario.

    :return: Devuelve None si imprime con éxito el nombre y los datos, o -1 si hay un error.
    """
    if type(dict_datos) != type(dict()):
        print(f"El tipo {type(dict_datos)} no es válido, intente nuevamente")
        return -1

    dict_nombre_dato = obtener_nombre_dato(dict_datos, key_ingresada)

    if dict_nombre_dato == -1:
        print("No se pudo obtener el nombre y el dato solicitado.")
        return -1

    dato = dict_nombre_dato[key_ingresada]
    nombre = dict_nombre_dato['nombre']

    if type(dato) == type(str()) or type(dato) == type(int()) or type(dato) == type(float()):
        print(nombre.ljust(20), dato)
    if type(dato) == type(dict()):
        for key, valor in dato.items():
            print("".ljust(20),f"{key.capitalize()}: ", valor)
    if type(dato) == type(list()):
        for elemento in dato:
            print("".ljust(20),f"{elemento.capitalize()}")

def imprimir_tabla_encabezado(lista_titulos_encabezado: list, longitud: str) -> None or -1:
    """
    imprimir_tabla_encabezado: Imprime un encabezado de tabla con títulos de una lista dada y una longitud específica
    para cada título.

    :param lista_titulos_encabezado: Una lista de cadenas que representan los títulos que se imprimirán
    como encabezados en una tabla.
    :param longitud: La longitud de los títulos de los encabezados en caracteres.

    :return: None si los parámetros de entrada son válidos o -1 si no se cumple con las validaciones.
    """
    if not lista_titulos_encabezado:
        print("No existen titulos en la lista para encabezar")
        return -1

    longitud_valida = re.search(r'^[1-9]$|1[0-9]$|^2[0-9]$|^3[0-9]$|^4[0-9]$|50', longitud)
    if not bool(longitud_valida):
        print("La longitud no debe ser superior a 50")
        return -1

    longitud = int(longitud)

    for titulo in lista_titulos_encabezado:
        encabezado = titulo.ljust(longitud)
        print(encabezado, end='')
    print("\n")

def calcular_imprimir_dato(lista: list, calculo: str, key_ingresada: str) -> None:
    """
    calcular_imprimir_dato: calcula e imprime el valor máximo o mínimo de una key dada en una lista.

    :param lista: Una lista de diccionarios que contiene datos.
    :param calculo: String que indica si se debe calcular el valor máximo o mínimo de una key de
    datos dada en la lista.
    :param key_ingresada: String que representa la clave de la que se desea obtener el cálculo y se utiliza
    para la impresión del resultado.

    :return: Si los datos no cumplen con las validaciones devuelve -1. De lo contrario, la función no
     devuelve None.
    """
    if calculo != 'max' and calculo != 'min':
        print(f"El cálculo {calculo} no es válido")
        return -1

    if not lista:
        print(f"El cálculo {calculo} no es válido")
        return -1
    dato_max_min = operacion.calcular_max_min_dato(lista, calculo, key_ingresada)
    if dato_max_min == -1:
      return -1

    dato_capitalizado = re.sub(r'_', ' ', key_ingresada).capitalize()
    print("Nombre:".ljust(20), f"- {dato_capitalizado}:")
    imprimir_nombre_dato(dato_max_min, key_ingresada)

def ordenar_imprimir_dato(lista: list, key_imprimir: str, key_ordenar: str)-> None or -1:
    """
    ordenar_imprimir_dato: Toma una lista, una key para imprimir y una key para ordenar, y luego
    ordena la lista por la key de clasificación e imprime el nombre del jugador y los datos
    especificados.

    :param lista: Una lista de diccionarios que contiene datos.
    :param key_imprimir: String que representa la key de los datos que se imprimirán para cada
    dato de la lista.
    :param key_ordenar: String que representa la key para ordenar la lista por sus valores.

    :return: None si cumple con las validaciones, caso contrario devuelve -1.
    """
    if not lista:
        return -1
    lista_ordenada = ordenar.quick_sort(lista, key_ordenar)
    dato_capitalizado = re.sub(r'_', ' ', key_imprimir).capitalize()
    print("Nombre:".ljust(20), f"- {dato_capitalizado}:")
    for elemento in lista_ordenada:
        imprimir_nombre_dato(elemento, key_imprimir)
