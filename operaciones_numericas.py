import re
import imprimir_datos as imprimir

def calcular_max(lista: list, key_ingresada: str) -> dict or -1:
    """
    calcular_max: Calcula el valor máximo de una key específica en una lista de diccionarios y devuelve
    una lista de todos los valores máximos encontrados.

    :param lista: Una lista de diccionarios que contienen datos.
    :param key_ingresada: String que representa la key que se utilizará para buscar el valor máximo
    dentro de los diccionarios en la lista de entrada.

    :return: Diccionario o -1 si no se cumplen las validaciones.
    """
    if not lista:
        return -1

    lista_maximos = []
    dato_maximo = None

    for elemento in lista:
        for valor_elemento in elemento.values():
            if type(valor_elemento) == type(dict()) and key_ingresada in valor_elemento:
                if dato_maximo is None or valor_elemento[key_ingresada] > dato_maximo:
                    dato_maximo = valor_elemento[key_ingresada]
                    lista_maximos = [elemento]
                elif valor_elemento[key_ingresada] == dato_maximo:
                    lista_maximos.append(elemento)

    if dato_maximo is None:
        print(f"No se pudo obtener un valor maximo. Maximo: {dato_maximo}")

    return lista_maximos

def calcular_min(lista: list, key_ingresada: str) -> dict or -1:
    """
    calcular_min: Calcula el valor mínimo de una key específica en una lista de diccionarios y devuelve
    una lista de todos los valores mínimos encontrados.

    :param lista: Una lista de diccionarios que contienen datos.
    :param key_ingresada: String que representa la key que se utilizará para buscar el valor mínimo
    dentro de los diccionarios en la lista de entrada.

    :return: Diccionario o -1 si no se cumplen las validaciones.
    """
    if not lista:
        return -1

    lista_minimos = []
    dato_minimo = None

    for elemento in lista:
        for valor_elemento in elemento.values():
            if type(valor_elemento) == type(dict()) and key_ingresada in valor_elemento:
                if dato_minimo is None or valor_elemento[key_ingresada] < dato_minimo:
                    dato_minimo = valor_elemento[key_ingresada]
                    lista_minimos = [elemento]
                elif valor_elemento[key_ingresada] == dato_minimo:
                    lista_minimos.append(elemento)

    if dato_minimo is None:
        print(f"No se pudo obtener un valor minimo. Minimo: {dato_minimo}")

    return lista_minimos

def calcular_promedio(lista: list, key_ingresada: str) -> float or -1:
    """
    calcular_promedio: Calcula el valor promedio de una key específica en una lista de diccionarios.

    :param lista: Lista de diccionarios que que contiene datos.
    :param key_ingresada: String que representa la clave (o atributo) de los datos de los que queremos
    calcular el promedio.

    :return: Float que es el promedio calculado de la key recibido en la lista de diccionarios. Si no
    se cumple con las validaciones, la función devuelve -1.
    """
    if not lista:
        return -1

    promedio = 0
    suma_valores = 0
    cantidad_key_en_lista = 0

    for jugador in lista:
        for valor_jugador in jugador.values():
            if type(valor_jugador) == type(str()) and key_ingresada in jugador:
                if type(jugador[key_ingresada]) == type(int()) or type(jugador[key_ingresada]) == type(float()):
                    if key == key_ingresada:
                        suma_valores += valor_jugador
                        cantidad_key_en_lista += 1
            if type(valor_jugador) == type(dict()) and key_ingresada in valor_jugador:
                if type(valor_jugador[key_ingresada]) == type(int()) or type(valor_jugador[key_ingresada]) == type(float()):
                        for key, valor in valor_jugador.items():
                            if key == key_ingresada:
                                suma_valores += valor
                                cantidad_key_en_lista += 1

    if cantidad_key_en_lista == 0:
        print(f"El dato '{key_ingresada}' no se encuentra o no es válido para realizar la operación")
        return -1

    promedio = suma_valores / cantidad_key_en_lista

    return promedio

def calcular_max_imprimir_dato(lista: list, key_ingresada: str) -> None or -1:
    """
    calcular_max_imprimir_dato: calcula el valor máximo de una key determinada en una lista,
    formatea el nombre de la key e imprime un encabezado de tabla y el nombre y el valor de los datos máximos.

    :param lista: Lista de diccionarios que contienen datos.
    :param key_ingresada: String que representa la key o atributo de los datos de la lista para los que
    queremos calcular el valor máximo.

    :return: None o -1 si no se cumple con las validaciones.
    """
    if not lista:
        print(f"La lista está vacía, no es posible realizar la operación")
        return -1

    lista_dato_max = calcular_max(lista, key_ingresada)

    if lista_dato_max == -1 or not lista_dato_max:
        print("No se pudo obtener el máximo")
        return -1

    dato_capitalizado = re.sub(r'_', ' ', key_ingresada).capitalize()
    imprimir.imprimir_tabla_encabezado(['Nombre', dato_capitalizado], '20')
    for dato_max in lista_dato_max:
        imprimir.imprimir_obtener_nombre_dato(dato_max, key_ingresada)

def calcular_datos_mayor_a_valor_ingresado(lista: list, key_ingresada: str, valor_ingresado: float) -> list or -1:
    """
    calcular_datos_mayor_a_valor_ingresado: Toma una lista de diccionarios, una key y un valor, y devuelve una
    nueva lista con todos los diccionarios que tienen un valor mayor que el valor de entrada para la key dada.

    :param lista: Lista de diccionarios que contienen datos.
    :param key_ingresada: String que representa la key del diccionario de la lista que queremos comparar con el valor_ingresado.
    :param valor_ingresado: Float que representa al valor introducido por el usuario para compararlo con los valores del
    diccionario.

    :return: Lista de diccionarios donde el valor de la key es mayor que el valor ingresado por el usuario.
    Si la lista de entrada está vacía, la función devuelve -1.
    """
    if not lista:
        print("La lista está vacía")
        return -1

    lista_datos_mayor_valor = []
    for elemento in lista:
        for valor_elemento in elemento.values():
            if type(valor_elemento) == type(dict()) and key_ingresada in valor_elemento:
                if type(valor_elemento[key_ingresada]) == type(int()) or type(valor_elemento[key_ingresada]) == type(float()):
                        for key, valor in valor_elemento.items():
                            if key == key_ingresada and valor > valor_ingresado:
                                lista_datos_mayor_valor.append(elemento)
    return lista_datos_mayor_valor

def calcular_imprimir_jugadores_mayor_valor(lista_jugadores:list , key_ingresada: str, valor_ingresado: float) -> None or -1:
    """
    calcular_imprimir_jugadores_mayor_valor: Toma una lista de jugadores y un par clave-valor y devuelve una lista
    de jugadores cuyo valor para la key dada es mayor que el valor de entrada e imprime sus nombres.

    :param lista_jugadores: Lista de diccionarios que contiene datos de jugadores, cada diccionario representa un
    jugador
    :param key_ingresada: String que representa la key (atributo) del jugador que la función usará para comparar
    con el parámetro value_ingresado
    :param valor_ingresado: Float que representa al valor ingresado por el usuario para comparar con los valores de los
    jugadores en la lista

    :return: Booleano que es True si hay jugadores en la lista con un valor mayor que el valor de entrada e imprime sus
    nombres y valores. Si no hay tales jugadores, la función devuelve Falso
    """
    lista_jugadores_mayor_valor = calcular_datos_mayor_a_valor_ingresado(lista_jugadores, key_ingresada, valor_ingresado)

    if not lista_jugadores_mayor_valor:
        existe_valor_mayor = False
        return existe_valor_mayor

    existe_valor_mayor = True
    for jugador in lista_jugadores_mayor_valor:
        imprimir.imprimir_obtener_nombre_dato(jugador, key_ingresada)
    return existe_valor_mayor