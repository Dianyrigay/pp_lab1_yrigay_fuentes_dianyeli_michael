# Alumna: Dianyeli Yrigay 95984910
# Tutor: Octavio
# Division 1E

# PRIMER PARCIAL PROGRAMACIÓN

import re
import json
import csv
import os
import calcular_datos as calcular
import imprimir_datos as imprimir
import solicitar_datos as solicitar
import ordenar_datos as ordenar

def limpiar_consola() -> None:
    """
    limpiar_consola: Borra la pantalla de la consola en Python esperando la entrada del usuario y luego
    llamando al comando 'cls'.
    """
    _ = input('\nPresione una tecla para continuar...')
    os.system('cls')

def leer_archivo(nombre_archivo: str) -> list:
    """
    leer_archivo: Lee un archivo JSON y devuelve una lista de jugadores.

    :param nombre_archivo: String que contiene la ruta y nombre del archivo que desea leer.

    :return: Una lista de jugadores obtenida de un archivo JSON.
    """
    lista_jugadores_json = []

    with open(nombre_archivo) as archivo:
        data = json.load(archivo)
        lista_jugadores_json = data["jugadores"]
    return lista_jugadores_json

def imprimir_jugadores_nombre_key(lista_jugadores_imprimir: list, key_ingresada:str ) -> None or -1:
    """
    imprimir_jugadores_nombre_key: Imprime un encabezado de tabla con la key ingresada y "Nombre",
    y el/los valor/es de la clave de cada jugador de la lista recibida.

    :param lista_jugadores_imprimir: Una lista de diccionarios que contiene datos de jugadores.
    :param key_ingresada: String que representa la clave para imprimir el valor de cada jugador.

    :return: None o un int que es -1 si no se cumple con las validaciones.
    """
    if not lista_jugadores_imprimir:
        return -1

    dato_capitalizado = re.sub(r'_', ' ', key_ingresada).capitalize()
    imprimir.imprimir_tabla_encabezado(['Nombre',dato_capitalizado], '20')
    for jugador in lista_jugadores_imprimir:
        dict_nombre_dato= imprimir.obtener_nombre_dato(jugador, key_ingresada)
        imprimir.imprimir_nombre_dato(jugador['nombre'], dict_nombre_dato[key_ingresada])

def obtener_e_imprimir_jugador_nombre_estadisticas(lista_jugadores: list) -> list or -1:
    """
    obtener_e_imprimir_jugador_nombre_estadisticas: Obtiene e imprime el nombre y las estadísticas de un jugador
    según el índice ingresado por el usuario.

    :param lista_jugadores: Una lista de diccionarios que contiene datos de jugadores.

    :return: Una lista del jugador seleccionado con sus datos exceptuando sus logros.
    Si no se cumple alguna validación retorna un int que es -1
    """
    if not lista_jugadores:
        print("La lista de jugadores está vacía")
        return -1

    indice_ingresado = solicitar.solicitar_valor_indice(lista_jugadores)

    if indice_ingresado == -1:
        return -1

    indice = 0
    lista_data_jugador = []
    imprimir.imprimir_tabla_encabezado(['Nombre', 'Estadísticas'], '20')

    for jugador in lista_jugadores:
        if indice_ingresado == indice:
            dict_data_jugador = {}
            for key, valor in jugador.items():
                if key == 'estadisticas':
                    for estadistica, valor_estadistica in valor.items():
                        dict_data_jugador[estadistica] = valor_estadistica
                    imprimir.imprimir_nombre_dict_formateado(jugador["nombre"], valor)
                elif key != "logros":
                    dict_data_jugador[key] = valor
            lista_data_jugador = [dict_data_jugador]
        indice += 1

    return lista_data_jugador

def exportar_csv(nombre_archivo: str, lista_data_jugador: list) -> bool:
    """
    exportar_csv: Exporta una lista de datos de un jugador a un archivo CSV con un nombre de archivo dado.

    :param nombre_archivo: String que representa el nombre del archivo que se creará o sobrescribirá
    con los datos exportados
    :param lista_data_jugador: Una lista de diccionarios que contienen datos de un jugador.

    :return: Booleano que indica si el archivo CSV se guardó correctamente o no.
    """
    archivo_guardado = False
    if lista_data_jugador:
        with open(nombre_archivo, 'w', newline='') as archivo:
            writer = csv.writer(archivo)

            encabezados = lista_data_jugador[0].keys()
            writer.writerow(encabezados)

            for dato in lista_data_jugador:
                valores = dato.values()
                writer.writerow(valores)
            archivo_guardado = True

    if archivo_guardado:
        print(f"Se creó el archivo: {nombre_archivo}")
    else:
        print(f"Error al crear el archivo: {nombre_archivo}")

    return archivo_guardado

def obtener_jugador_nombre_logros(lista_jugadores: list) -> list or -1:
    """
    obtener_jugador_nombre_logros: Solicita al usuario que ingrese un nombre de jugador y obtiene
    una lista de jugadores que coincidieron con el nombre ingresado.

    :param lista_jugadores: Una lista de diccionarios que contienen datos de jugadores.

    :return: Una lista de los jugadores que coincidieron con el nombre de entrada o -1 si no se
    cumplen las validaciones.
    """
    if not lista_jugadores:
        print("La lista de jugadores está vacía")
        return -1

    lista_jugadores_encontrados = solicitar.solicitar_obtener_nombre_jugador(lista_jugadores)
    return lista_jugadores_encontrados

def calcular_e_imprimir_promedio_puntos_por_partido(lista_jugadores: list) -> None or -1:
    """
    calcular_e_imprimir_promedio_puntos_por_partido: Calcula e imprime el promedio de 'promedio_puntos_por_partido'
    de la lista de jugadores y también ordena la lista por nombre de jugador.

    :param lista_jugadores: Una lista de diccionarios que contiene datos de jugadores.

    :return: None o -1 si no se cumplen las validaciones.
    """
    if not lista_jugadores:
        return -1

    promedio_equipo = calcular.calcular_promedio(lista_jugadores, 'promedio_puntos_por_partido')
    lista_ordenada_nombres = ordenar.quick_sort(lista_jugadores, 'nombre')

    if not lista_ordenada_nombres:
        print("No se pudo ordenar la lista")
        return -1
    if promedio_equipo == -1:
        return -1

    imprimir_jugadores_nombre_key(lista_ordenada_nombres,'promedio_puntos_por_partido')
    print(f"\nPromedio de 'Promedio puntos por partido' del equipo: {promedio_equipo}")

def imprimir_jugador_nombre_salon_fama(lista_jugadores: list) -> None or -1:
    """
    imprimir_jugador_nombre_salon_fama: Solicita un nombre al usuario e imprime una tabla con el/los nombre/s
    que coinciden con el mismo y si son o no miembros del Salón de la Fama del baloncesto.

    :param lista_jugadores: Una lista de diccionarios que contiene datos de jugadores.

    :return: None o -1 si no se cumple con las validaciones.
    """
    if not lista_jugadores:
        return -1
    lista_jugadores_buscados = obtener_jugador_nombre_logros(lista_jugadores)
    if lista_jugadores_buscados == -1:
        return -1

    imprimir.imprimir_tabla_encabezado(['Nombre', 'Es miembro del Salón de la Fama del baloncesto'], '20')
    for jugador in lista_jugadores_buscados:
        es_miembro = False
        if 'Miembro del Salon de la Fama del Baloncesto' in jugador['logros']:
            es_miembro = True

        es_miembro = str(es_miembro)
        imprimir.imprimir_datos_tabla([jugador["nombre"], es_miembro], '20')

def calcular_jugador_dato_max_key(lista_jugadores: list, key_ingresada:str ) -> list or -1:
    """
    calcular_jugador_dato_max_key: Calcula y obtiene el jugador con el maximo valor de la key ingresada por
    la lista de jugadores.

    :param lista_jugadores: Una lista de diccionarios que contiene datos de jugadores.

    :return: Una lista de diccionarios con el/los jugador/es con el dato maximo o un entero que es -1
    si no se cumple con las validaciones.
    """
    if not lista_jugadores:
        print(f"La lista está vacía, no es posible realizar la operación")
        return -1

    lista_jugador_dato_max = calcular.calcular_max(lista_jugadores, key_ingresada)

    if lista_jugador_dato_max == -1 or not lista_jugador_dato_max:
        print("No se pudo obtener el máximo")
        return -1

    return lista_jugador_dato_max

def calcular_jugadores_mayor_valor_key(lista_jugadores: list, key_ingresada: str) -> list or -1:
    """
    calcular_jugadores_mayor_valor_key: calcula y obtiene los jugadores que tienen un valor mas alto de la
    key ingresada que el solicitado al usuario.

    :param lista_jugadores: Una lista de diccionarios que contiene datos de jugadores.

    :return: Una lista de diccionarios con los jugadores que tienen mayor valor al ingresado o un entero que es -1
    si no se cumple con las validaciones.
    """
    if not lista_jugadores:
        return -1

    lista_jugadores_mayor_valor = []

    valor_ingresado = solicitar.solicitar_valor_float()
    if valor_ingresado == -1:
        return lista_jugadores_mayor_valor

    lista_jugadores_mayor_valor = calcular.calcular_datos_mayor_a_valor_ingresado(lista_jugadores, key_ingresada, valor_ingresado)

    if not lista_jugadores_mayor_valor:
        print("\nNo existen jugadores que tengan mayor valor que el ingresado")

    return lista_jugadores_mayor_valor

def calcular_e_imprimir_promedio_puntos_por_partido_excluyendo_min(lista_jugadores: list) -> None or -1:
    """
    calcular_e_imprimir_promedio_puntos_por_partido_excluyendo_min: Calcula e imprime el promedio de puntos
    por juego de un equipo, excluyendo al jugador con el 'promedio_puntos_por_partido' más bajo.

    :param lista_jugadores: Una lista de diccionarios que contiene datos de jugadores.

    :return: None o un entero que es -1.
    """
    if not lista_jugadores:
        return -1
    lista_jugadores_copia = lista_jugadores.copy()
    lista_min_puntos_partido = calcular.calcular_min(lista_jugadores,'promedio_puntos_por_partido')
    if not lista_min_puntos_partido:
        print("No se pudo obtener el jugador con minimo puntos por partido")
        return -1

    for jugador_min_puntos in lista_min_puntos_partido:
        nombre_jugador_min = jugador_min_puntos["nombre"]
        lista_jugadores_copia.remove(jugador_min_puntos)
    promedio_equipo = calcular.calcular_promedio(lista_jugadores_copia, 'promedio_puntos_por_partido')

    if promedio_equipo == -1:
        print("No se pudo obtener el promedio del equipo")
        return -1

    print(f"Excluyendo a {nombre_jugador_min}")
    print(f"\nEl promedio de 'Promedio puntos por partido' del equipo es: {promedio_equipo}")

def calcular_jugador_mayor_logros_obtenidos(lista_jugadores: list) -> None or -1:
    """
    calcular_jugador_mayor_logros_obtenidos: Calcula el jugador con el mayor número
    de logros obtenidos de una lista de jugadores.

    :param lista_jugadores: Una lista de diccionarios que contiene datos de jugadores.

    :return: Una lista que contiene el/los jugador/es con la mayor cantidad de logros o
    un entero que es -1.
    """
    if not lista_jugadores:
        return -1

    lista_jugador_mayor_logros = []
    mayor_cantidad_logros = None
    for jugador in lista_jugadores:
        if 'logros' in jugador:
            if mayor_cantidad_logros is None or len(jugador["logros"]) > mayor_cantidad_logros:
                lista_jugador_mayor_logros = [jugador]
                mayor_cantidad_logros = len(jugador["logros"])
            elif len(jugador["logros"]) == mayor_cantidad_logros:
                lista_jugador_mayor_logros.append(jugador)

    return lista_jugador_mayor_logros

def calcular_imprimir_jugadores_tiros_campo_mayor_valor(lista_jugadores: list) -> None or -1:
    """
    calcular_imprimir_jugadores_tiros_campo_mayor_valor: Calcula e imprime los jugadores con un
    'porcentaje_tiros_de_campo' superior a un valor dado y los ordena alfabeticamente por su posición.

    :param lista_jugadores: Una lista de diccionarios que contiene datos de jugadores, cada diccionario
    representa un jugador.

    :return: None o un entero que es -1.
    """
    lista_ordenada = ordenar.quick_sort(lista_jugadores, 'posicion')
    lista_jugadores_mayor_valor = calcular_jugadores_mayor_valor_key(lista_ordenada,'porcentaje_tiros_de_campo')

    if lista_jugadores_mayor_valor == -1:
        return -1

    imprimir.imprimir_tabla_encabezado(['Nombre', 'Porcentaje tiros de campo', 'Posición'], '30')
    for jugador in lista_jugadores_mayor_valor:
        estadisticas = jugador["estadisticas"]
        for key, valor in estadisticas.items():
            if key == 'porcentaje_tiros_de_campo':
                porcentaje_tiros_de_campo = str(valor)
        nombre = jugador["nombre"]
        posicion = jugador["posicion"]
        imprimir.imprimir_datos_tabla([nombre, porcentaje_tiros_de_campo, posicion], '30')

def calcular_obtener_posicion_ranking_jugadores(lista_jugadores: list) -> list or -1:
    """
    calcular_obtener_posicion_ranking_jugadores: Calcula y exporta las posiciones de cada jugador
    en el ranking de puntos, rebotes, asistencias y robos.

    :param lista_jugadores: Una lista de diccionarios que contiene datos de jugadores, cada diccionario
    representa un jugador.

    :return: Una lista de diccionarios con las posiciones de cada jugador en el ranking.
    Si no se cumple con las validaciones, devuelve -1.
    """
    if not lista_jugadores:
        print("La lista de jugadores está vacía")
        return -1

    lista_ordenada_puntos = ordenar.quick_sort_dicts(lista_jugadores, 'puntos_totales', False)
    lista_ordenada_rebotes = ordenar.quick_sort_dicts(lista_jugadores, 'rebotes_totales', False)
    lista_ordenada_asistencias = ordenar.quick_sort_dicts(lista_jugadores, 'asistencias_totales', False)
    lista_ordenada_robos = ordenar.quick_sort_dicts(lista_jugadores, 'robos_totales', False)

    lista_ranking_jugadores = []
    for jugador in lista_jugadores:
        dict_posiciones_jugador = {}
        for i in range(len(lista_ordenada_puntos)):
            if jugador["nombre"] == lista_ordenada_puntos[i]["nombre"]:
                dict_posiciones_jugador['Jugador'] = lista_ordenada_puntos[i]["nombre"]
                dict_posiciones_jugador['Puntos'] = i + 1
                break

        for i in range(len(lista_ordenada_rebotes)):
            if jugador["nombre"] == lista_ordenada_rebotes[i]["nombre"]:
                dict_posiciones_jugador['Rebotes'] = i + 1
                break

        for i in range(len(lista_ordenada_asistencias)):
            if jugador["nombre"] == lista_ordenada_asistencias[i]["nombre"]:
                dict_posiciones_jugador['Asistencias'] = i + 1
                break

        for i in range(len(lista_ordenada_robos)):
            if jugador["nombre"] == lista_ordenada_robos[i]["nombre"]:
                dict_posiciones_jugador['Robos'] = i + 1
                break
        lista_ranking_jugadores.append(dict_posiciones_jugador)

    if not lista_ranking_jugadores:
        print("No se pudo obtener la posición de los juagdores en el ranking")

    return lista_ranking_jugadores

def calcular_cantidad_jugadores_por_posicion(lista_jugadores: list):
    if not lista_jugadores:
        print("La lista se encuentra vacía")
        return -1

    dict_podision_cantidad = {}
    for jugador in lista_jugadores:
        for key, valor in jugador.items():
            if key == 'posicion':
                if valor in dict_podision_cantidad:
                    dict_podision_cantidad[valor] +=1
                else:
                    dict_podision_cantidad[valor] = 1
    return dict_podision_cantidad

# Mostrar la lista de jugadores ordenadas por la cantidad de All-Star de forma descendente. La salida por pantalla debe tener un formato similar a este:
# Michael Jordan (14 veces All Star)
# Magic Johnson (12 veces All-Star)
def obtener_jugadores_cantidad_all_star(lista_jugadores: list):
    lista_jugadores_all_star = []

    regex = r'^([0-9]+) veces All-Star$'
    for jugador in lista_jugadores:
        dict_nombre_cantidad_all_star = {}
        for key, valor in jugador.items():
            if type(valor) == type(list()):
                for elemento in valor:
                    elemento_valido = re.search(regex, elemento)
                    if bool(elemento_valido):
                        cantidad = elemento_valido.group(1)
                        cantidad = int(cantidad)
                        dict_nombre_cantidad_all_star["nombre"] = jugador["nombre"]
                        dict_nombre_cantidad_all_star["logros"] = cantidad
                        lista_jugadores_all_star.append(dict_nombre_cantidad_all_star)


    lista_jugadores_all_star = ordenar.quick_sort(lista_jugadores_all_star, 'logros', False)
    for jugador in lista_jugadores_all_star:
            jugador['logros'] = str(jugador['logros'])
            jugador['logros'] += ' veces All-Star'

    return lista_jugadores_all_star


def obtener_mayores_estadisticas_por_valor(lista_jugadores: list):
    jugadores_mejores_estadisticas = []
    for jugador in lista_jugadores:
        for key, valor in jugador['estadisticas'].items():
            jugadores_dato_max = calcular.calcular_max(lista_jugadores, key)
            for jugador_max in jugadores_dato_max:
                jugadores_mejores_estadisticas.append(jugador_max)
                imprimir.imprimir_datos_tabla([jugador_max["nombre"],key, str(jugador_max['estadisticas'][key])], '40')
        break

    return jugadores_mejores_estadisticas

def obtener_jugador_mejores_estadisticas(lista_jugadores: list):
    if not lista_jugadores:
        return -1

    max_jugador_estadisticas = None
    max_valor = 0
    for jugador in lista_jugadores:
        estadistica_total = 0
        for estadistica in jugador["estadisticas"].values():
            estadistica_total += estadistica
        if max_jugador_estadisticas is None or estadistica_total > max_valor:
            max_jugador_estadisticas = jugador

    nombre = max_jugador_estadisticas["nombre"]
    print(f"Jugador con mayores estadisticas: {nombre}")




