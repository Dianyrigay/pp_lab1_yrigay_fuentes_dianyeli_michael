import re

def obtener_nombre_dato(dict_datos: dict, key_ingresada: str) -> dict or -1:
    """
    obtener_nombre_dato: Obtiene el nombre y un valor de datos específico de un diccionario,
    basado en una clave dada.

    :param dict_datos: Diccionario que contiene datos
    :param key_ingresada: String que hace referencia a la clave que se busca en el diccionario

    :return: Un diccionario con el nombre y el valor de la clave ingresados como argumentos si se
    cumple con las validaciones, o -1 si no se cumplen con las validaciones.
    """
    if type(dict_datos) != type(dict()):
        print(f"El tipo {type(dict_datos)} no es válido, intente nuevamente")
        return -1

    if 'nombre' not in dict_datos:
        print(f"Nombre no se encuentra en el diccionario recibido.")
        return -1

    dict_nombre_dato = {}
    dato = None
    nombre = dict_datos["nombre"]

    for key_dict_datos, valor_dict_datos in dict_datos.items():
        if key_ingresada in dict_datos and key_dict_datos == key_ingresada:
            if type(valor_dict_datos) == type(str()):
                dato = dict_datos[key_ingresada]
            elif type(valor_dict_datos) == type(dict()):
                dato = valor_dict_datos
            elif type(valor_dict_datos) == type(list()):
                dato = valor_dict_datos
        elif key_ingresada in valor_dict_datos:
            if type(valor_dict_datos) == type(dict()):
                for key, valor in valor_dict_datos.items():
                    if key == key_ingresada:
                        dato = valor
            elif type(valor_dict_datos) == type(list()):
                for elemento in valor_dict_datos:
                    dato = elemento

    if dato == None:
        print(f"No se pudo obtener el valor de {key_ingresada}")
        return -1

    dict_nombre_dato["nombre"] = nombre
    dict_nombre_dato[key_ingresada] = dato
    return dict_nombre_dato

def imprimir_nombre_dato(nombre: str, dato: any) -> None or -1:
    """
    imprimir_dato: formatea el nombre de la key e imprime un encabezado de tabla y el nombre y el valor
    de los datos máximos.

    :param dict_datos: Lista de diccionarios que contienen datos.
    :param key_ingresada: String que representa la key o atributo de los datos de la lista para los que
    queremos calcular el valor máximo.

    :return: None o -1 si no se cumple con las validaciones.
    """
    if dato == None or type(nombre) != type(str()):
        print(f"Los parámetros recibidos no son válidos")
        return -1

    if type(dato) != type(dict()) and type(dato) != type(list()):
        print(nombre.ljust(20), dato)
    elif type(dato) == type(dict()):
        imprimir_nombre_dict_formateado(nombre, dato)
    elif type(dato) == type(list()):
        imprimir_nombre_list_formateada(nombre, dato)
    else:
        print(f"EL tipo de dato {type(dato)} no se puede imprimir")
        return -1

def imprimir_nombre_dict_formateado(nombre: str, diccionario: dict) -> None:
    """
    imprimir_nombre_dict_formateado: Recibe un nombre y un diccionario como entrada y los imprime en
    formato de tabla.

    :param nombre: String que representa un nombre.
    :param diccionario: Diccionario que contiene par de clave-valor.
    """
    i = 0
    for key, valor in diccionario.items():
        if i == 0:
            print(nombre.ljust(20), end="")
            print(f"{key.capitalize()}: ", valor)
        else:
            print("".ljust(20),f"{key.capitalize()}: ", valor)
        i += 1

def imprimir_nombre_list_formateada(nombre: str, lista: list) -> None:
    """
    imprimir_nombre_list_formateada: Recibe un nombre y una lista como entrada y los imprime en
    formato de tabla.

    :param nombre: String que representa un nombre.
    :param lista: Lista de elementos que se imprimirán de forma formateada
    """
    i = 0
    for elemento in lista:
        if i == 0:
            print(nombre.ljust(20), end="")
            print(f"{elemento.capitalize()}")
        else:
            print("".ljust(20),f"{elemento.capitalize()}")
        i += 1

def imprimir_nombre_indice_jugadores(lista_jugadores: list) -> None or -1:
    """
    imprimir_nombre_indice_jugadores: Imprime el índice y el nombre de cada jugador en una lista de jugadores.

    :param lista_jugadores: Una lista de diccionarios, donde cada diccionario contiene datos sobre un jugador.

    :return: Si la lista está vacía, devuelve -1. De lo contrario, la función imprime el índice y el nombre de
      cada jugador en la lista y devuelve None.
    """
    if not lista_jugadores:
        print("Lista de jugadores vacía")
        return -1

    indice = 0
    for jugador in lista_jugadores:
        if 'nombre' in jugador:
            nombre = jugador['nombre']
        mensaje = f"\t{indice} - {nombre}"
        indice += 1
        print(mensaje)

def imprimir_tabla_encabezado(lista_titulos_encabezado: list, longitud: str) -> None or -1:
    """
    imprimir_tabla_encabezado: Imprime un encabezado de tabla con títulos de una lista dada y una longitud específica
    para cada título.

    :param lista_titulos_encabezado: Una lista de cadenas que representan los títulos que se imprimirán
    como encabezados en una tabla.
    :param longitud: String que representa la longitud de los títulos de los encabezados en caracteres.

    :return: None si los parámetros de entrada son válidos o -1 si no se cumple con las validaciones.
    """
    if not lista_titulos_encabezado:
        print("No existen titulos en la lista para encabezar")
        return -1

    longitud_valida = re.search(r'^[1-9]$|1[0-9]$|^2[0-9]$|^3[0-9]$|^4[0-9]$|50', longitud)
    if not bool(longitud_valida):
        print("La longitud debe ser menor a 50")
        return -1

    longitud = int(longitud)
    print("\n")
    for titulo in lista_titulos_encabezado:
        encabezado = titulo.ljust(longitud)
        print(encabezado, end='')
    print("\n")

def imprimir_datos_tabla(lista_datos_fila: list, longitud: str)-> None or -1:
    """
    imprimir_datos: Imprime una fila en la tabla con datos de una lista dada y una longitud específica
    para cada fila.

    :param lista_datos_fila: Una lista de cadenas que representan los datos que se imprimirán
    como filas en una tabla.
    :param longitud: String que representa la longitud de los datos de las filas en caracteres.

    :return: None si los parámetros de entrada son válidos o -1 si no se cumple con las validaciones.
    """
    if not lista_datos_fila:
        print("No existen datos en la lista para encabezar")
        return -1

    longitud_valida = re.search(r'^[1-9]$|1[0-9]$|^2[0-9]$|^3[0-9]$|^4[0-9]$|50', longitud)
    if not bool(longitud_valida):
        print("La longitud debe ser menor a 50")
        return -1

    longitud = int(longitud)
    for titulo in lista_datos_fila:
        fila = titulo.ljust(longitud)
        print(fila, end="")
    print("")