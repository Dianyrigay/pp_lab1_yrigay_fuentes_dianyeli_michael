import re
import imprimir_datos as imprimir

def solicitar_dato(dato: str) -> str:
    """
    solicitar_dato: Solicita al usuario que ingrese un tipo específico de datos y devuelve
    la entrada como una cadena.

    :param dato: String que representa un tipo de dato, que va a ser el solicitado al usuario.

    :return: String que son los datos introducidos por el usuario.
    """
    dato_ingresado = input(f"\nIngrese un {dato} (o ingrese '-1' para salir del submenú): ")
    return dato_ingresado

def solicitar_valor_float() -> float or -1:
    """
    solicitar_valor_float: Solicita al usuario que ingrese un valor flotante válido y lo devuelve.

    :return: Float que es valor ingresado por el usuario, sino devuelve un entero que es -1, en caso
    que el usuario no desee continuar con la operación.
    """
    valor_valido = False

    while not valor_valido:
        valor_ingresado = solicitar_dato('valor')
        if valor_ingresado == '-1':
            break
        valor_valido = re.search(r'^[0-9]{1,}$|^[0-9]{1,}\.[0-9]{1,}$', valor_ingresado)
        valor_valido = bool(valor_valido)

    if valor_ingresado == '-1':
        print("\nIngrese una nueva opción del menú")
        return -1

    valor_ingresado = float(valor_ingresado)
    return valor_ingresado

def solicitar_valor_indice(lista_jugadores: list) -> int or -1:
    """
    solicitar_valor_indice: Solicita al usuario que ingrese un valor entero válido y lo devuelve.

    :return: int que es valor ingresado por el usuario, sino devuelve un entero que es -1, en caso
    que el usuario no desee continuar con la operación.
    """
    valor_valido = False
    imprimir.imprimir_nombre_indice_jugadores(lista_jugadores)

    while not valor_valido:
        indice_ingresado = solicitar_dato('indice')
        if indice_ingresado == '-1':
            break
        valor_valido = re.search(r'^[0-9]$|^1[0-1]$', indice_ingresado)
        valor_valido = bool(valor_valido)

    if indice_ingresado == '-1':
        print("\nIngrese una nueva opción del menú")
        return -1

    indice_ingresado = int(indice_ingresado)
    return indice_ingresado

def solicitar_obtener_nombre_jugador(lista_jugadores: list) -> list or -1:
    """
    solicitar_obtener_nombre_jugador: Busca el nombre de un jugador en una lista de jugadores y devuelve una lista de
    jugadores que coinciden con el nombre de entrada ingresado por el usuario.

    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores, donde cada
    diccionario contiene datos sobre un jugador.

    :return: Una lista de diccionarios que contienen información sobre jugadores cuyos nombres coinciden
    con la entrada proporcionada por el usuario, o -1 si no se cumple con las validaciones.
    """
    if not lista_jugadores:
        print("Lista de jugadores vacía")
        return -1

    nombre_valido = False
    imprimir.imprimir_nombre_indice_jugadores(lista_jugadores)
    lista_jugadores_validos = []
    while not lista_jugadores_validos:
        nombre_buscado = solicitar_dato('nombre').lower()

        if nombre_buscado == '-1':
            print("\nIngrese una nueva opción del menú")
            return -1

        for jugador in lista_jugadores:
            regex = r'\b([a-zA-Z]+)?'+ nombre_buscado + r'( [a-zA-Z]+)?|'+ nombre_buscado + r'([a-zA-Z]+)?\b'
            nombre_jugador = jugador['nombre'].lower()
            nombre_valido = re.search(regex, nombre_jugador)
            nombre_valido = bool(nombre_valido)
            if nombre_valido:
                lista_jugadores_validos.append(jugador)

    if not lista_jugadores_validos:
        print(f"No se pudieron encontrar jugadores que coincidan con {nombre_buscado}")
        return -1

    return lista_jugadores_validos
