import re

def calcular_max(lista: list, key_ingresada: str) -> dict:
    """
    calcular_max : Compara entre los elementos de la lista para obtener el dato (diccionario)
    que contiene el mayor valor de la key ingresada por parámetro

    Recibe: :param lista: Una lista de diccionarios que contiene datos
            :param key_ingresada: Hace referencia al dato del que se desea buscar el máximo

    Retorna: Un diccionario que contiene los datos del maximo valor encontrado de la key ingresada,
    en caso que se cumpla con las validaciones. Caso contrario retorna -1
    """
    if not lista:
        return -1

    i = 0
    maximo_obtenido = False

    for elemento in lista:
        for key_elemento, valor_elemento in elemento.items():
            if type(valor_elemento) == type(dict()):
                if key_ingresada in valor_elemento and not maximo_obtenido:
                    dato_maximo = lista[i]
                    maximo = dato_maximo[key_elemento][key_ingresada]
                    maximo_obtenido = True

                if maximo_obtenido:
                    for key, valor in valor_elemento.items():
                        if key == key_ingresada:
                            if (valor > maximo):
                                maximo = valor
                                dato_maximo = elemento
            i += 1

    if not maximo_obtenido:
        print(f"El dato '{key_ingresada}' no existe o no es válido para realizar la operación")
        return -1

    return dato_maximo

def calcular_min(lista: list, key_ingresada: str) -> dict:
    """
    calcular_min : Compara entre los elementos de la lista para obtener el dato (diccionario)
    que contiene el menor valor de la key ingresada por parámetro

    Recibe: :param lista: Una lista de diccionarios que contiene datos
            :param key_ingresada: Hace referencia al dato del que se desea buscar el mínimo

    Retorna: Un diccionario que contiene los datos del mínimo valor encontrado de la key ingresada,
    en caso que se cumpla con las validaciones. Caso contrario retorna -1
    """
    if not lista:
        return -1

    i = 0
    minimo_obtenido = False

    for elemento in lista:
        for key_elemento, valor_elemento in elemento.items():
            if type(valor_elemento) == type(dict()):
                if key_ingresada in valor_elemento and not minimo_obtenido:
                    dato_minimo = lista[i]
                    minimo = dato_minimo[key_elemento][key_ingresada]
                    minimo_obtenido = True

                if minimo_obtenido:
                    for key, valor in valor_elemento.items():
                        if key == key_ingresada:
                            if (valor < minimo):
                                minimo = valor
                                dato_minimo = elemento
        i += 1

    if not minimo_obtenido:
        print(f"El dato '{key_ingresada}' no existe en la lista")
        return -1

    return dato_minimo

def calcular_max_min_dato(lista_jugadores: list, calculo: str, key_ingresada: str) -> dict:
    """
    calcular_max_min_dato : Verifica que el calculo recibido sea 'maximo' o 'minimo' para llamar
    a las funciones 'calcular_max' o 'calcular_min' respectivamente y obtener el valor deseado
    de la key ingresada por parámetro.

    Recibe: :param lista: Una lista de diccionarios que contiene datos
            :param calculo: Hace refencia al cálculo que se desea buscar, el mismo puede ser 'maximo'
                            o 'minimo'.
            :param key_ingresada: Hace referencia al dato del que se desea buscar el mínimo

    Retorna: Un diccionario que contiene los datos del calculo y key deseados en caso que se cumpla
    con las validaciones. Caso contrario retorna -1
    """
    if not lista_jugadores:
        return -1

    calculo_valido = re.search(r'max|min', calculo)
    if bool(calculo_valido):
        if calculo == 'max':
            dato_dict = calcular_max(lista_jugadores, key_ingresada)
        else:
            dato_dict = calcular_min(lista_jugadores, key_ingresada)
    else:
        print(f"El calculo {calculo} no es válido")
        return -1

    return dato_dict

def calcular_promedio(lista_jugadores: list, key_ingresada: str) -> float:
    """
    calcular_promedio : Suma los valores de la key ingresada por parámetro y acumula la cantidad de
    veces que aparece esa key en la lista para obtener el promedio de los valores de la key.

    Recibe: :param lista: Una lista de diccionarios que contiene datos de jugadores
            :param key_ingresada: Hace referencia al dato del que se desea buscar el promedio

    Retorna: Un float que es el promedio obtenido en caso que se cumpla con las validaciones.
    Caso contrario retorna -1
    """
    if not lista_jugadores:
        return -1

    promedio = 0
    suma_valores = 0
    cantidad_key_en_lista = 0

    for jugador in lista_jugadores:
        for dato_jugador, valor_jugador in jugador.items():
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

def calcular_datos_mayor_a_valor_ingresado(lista: list, key_ingresada: str, valor_ingresado: float):
    lista_datos_mayor_valor = []
    for elemento in lista:
        for valor_elemento in elemento.values():
            if type(valor_elemento) == type(dict()) and key_ingresada in valor_elemento:
                if type(valor_elemento[key_ingresada]) == type(int()) or type(valor_elemento[key_ingresada]) == type(float()):
                        for key, valor in valor_elemento.items():
                            if key == key_ingresada and valor > valor_ingresado:
                                lista_datos_mayor_valor.append(elemento)
    return lista_datos_mayor_valor
