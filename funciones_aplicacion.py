# Alumna: Dianyeli Yrigay 95984910
# Tutor: Octavio
# Division 1E

# PRIMER PARCIAL PROGRAMACIÓN

import re
import json
import csv
import os
import calcular_datos as operacion
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

def imprimir_jugadores_nombre_posicion(lista_jugadores: list) -> None or -1:
    """
    imprimir_jugadores_nombre_posicion: Toma una lista de jugadores e imprime sus nombres y posiciones en un
    formato de tabla.

    :param lista_jugadores: Lista de diccionarios, donde cada diccionario contiene información sobre un jugador.

    :return: Si la lista de entrada está vacía, la función devuelve un entero que es -1. De lo contrario, devuelve None.
    """
    if not lista_jugadores:
        return -1

    imprimir.imprimir_tabla_encabezado(['Nombre:', 'Posición:'], '20')

    for jugador in lista_jugadores:
        imprimir.imprimir_obtener_nombre_dato(jugador, 'posicion')

def obtener_e_imprimir_jugador_nombre_estadisticas(lista_jugadores: list) -> list or -1:
    """
    obtener_e_imprimir_jugador_nombre_estadisticas: Obtiene e imprime el nombre y las estadísticas de un jugador
    seleccionado de una lista de jugadores según su índice.

    :param lista_jugadores: Una lista de diccionarios que contiene datos de jugadores, cada diccionario
    representa un jugador.

    :return: Una lista que contiene un diccionario con las estadísticas, el nombre y la posición del jugador
    seleccionado de la lista de jugadores. Si la lista de jugadores está vacía o el usuario ingresa '-1' como índice
    del jugador, la función devuelve un entero que es -1.
    """
    if not lista_jugadores:
        print("La lista de jugadores está vacía")
        return -1

    condicion_valida = False
    imprimir.imprimir_nombre_indice_jugadores(lista_jugadores)

    while not condicion_valida:
        indice_jugador = solicitar.solicitar_dato('indice')
        if indice_jugador == '-1':
            break
        condicion_valida = re.search(r'^[0-9]$|^1[0-1]$', indice_jugador)
        condicion_valida = bool(condicion_valida)

    indice_jugador = int(indice_jugador)

    if indice_jugador == -1:
        print("\nIngrese una nueva opción del menú")
        return -1

    indice = 0
    for jugador in lista_jugadores:
        if indice_jugador == indice:
            dict_data_jugador = {}
            for dato,valor in jugador.items():
                if dato == 'estadisticas':
                    for estadistica, valor_estadistica in valor.items():
                        dict_data_jugador[estadistica] = valor_estadistica
                elif dato != "logros":
                    dict_data_jugador[dato] = valor
            lista_data_jugador = [dict_data_jugador]
            imprimir.imprimir_tabla_encabezado(['Nombre:', 'Estadísticas:'], '20')
            imprimir.imprimir_obtener_nombre_dato(jugador, 'estadisticas')
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
    obtener_jugador_nombre_logros: Toma una lista de jugadores y solicita al usuario que ingrese el nombre
    de un jugador reutilizando la funcion 'solicitar_obtener_nombre_jugador', luego devuelve una lista de jugadores
    cuyos nombres coinciden con el nombre de entrada.

    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores, donde cada
    diccionario contiene datos sobre un jugador.

    :return: Una lista de diccionarios que contienen información sobre jugadores cuyos nombres coinciden
    con lo ingresado por el usuario. Devuelve un entero que es -1 si el usuario ingresa "-1" indicando que desea volver al menu,
    o si no se encontraron nombres fuera de las validaciones realizadas.
    """
    if not lista_jugadores:
        return -1

    lista_jugadores_validos = solicitar.solicitar_obtener_nombre_jugador(lista_jugadores)

    return lista_jugadores_validos

def obtener_e_imprimir_jugador_nombre_logros(lista_jugadores: list) -> None or -1:
    """
    obtener_e_imprimir_jugador_nombre_logros: obtiene e imprime el nombre y los logros de los jugadores
    de una lista que se obtiene reutilizando la función 'obtener_jugador_nombre_logros'.

    :param lista_jugadores: Una lista de diccionarios que contiene datos de jugadores, cada diccionario
    representa un jugador.

    :return: None o un entero que es -1 si no se cumplieron las validaciones.
    """
    lista_jugadores_logros = obtener_jugador_nombre_logros(lista_jugadores)

    if lista_jugadores_logros != -1:
        imprimir.imprimir_tabla_encabezado(['Nombre:', 'Logros:'], '20')
        for jugador in lista_jugadores_logros:
            imprimir.imprimir_obtener_nombre_dato(jugador, 'logros')

def calcular_e_imprimir_promedio_puntos_por_partido(lista_jugadores: list) -> None or -1:
    """
    calcular_e_imprimir_promedio_puntos_por_partido: calcula e imprime el promedio de 'promedio_puntos_por_partido'
    de la lista de jugadores y también ordena la lista por nombre de jugador.

    :param lista_jugadores: Una lista de diccionarios que contiene datos de jugadores, cada diccionario
    representa un jugador.

    :return: Si la lista de entrada `lista_jugadores` está vacía, la función devuelve un entero que es -1. De lo
    contrario, None.
    """
    if not lista_jugadores:
        return -1

    promedio_equipo = operacion.calcular_promedio(lista_jugadores, 'promedio_puntos_por_partido')
    ordenar.ordenar_imprimir_dato(lista_jugadores, 'promedio_puntos_por_partido', 'nombre')
    print(f"\nPromedio de 'Promedio puntos por partido' del equipo: {promedio_equipo}")

def imprimir_jugador_nombre_salon_fama(lista_jugadores: list) -> None or -1:
    """
    imprimir_jugador_nombre_salon_fama: imprime una tabla de jugadores de baloncesto y si son o no miembros
    del Salón de la Fama del baloncesto.

    :param lista_jugadores: Una lista de diccionarios que contiene datos de jugadores, cada diccionario
    representa un jugador.

    :return: Si el tipo de `lista_jugadores_buscados` no es una lista, la función devuelve un entero que es
    -1. De lo contrario, devuelve None.
    """
    if not lista_jugadores:
        return -1
    lista_jugadores_buscados = obtener_jugador_nombre_logros(lista_jugadores)
    if type(lista_jugadores_buscados) != type(list()):
        return -1

    imprimir.imprimir_tabla_encabezado(['Nombre', 'Es miembro del Salón de la Fama del baloncesto'], '20')
    for jugador in lista_jugadores_buscados:
        es_miembro = False
        if 'Miembro del Salon de la Fama del Baloncesto' in jugador['logros']:
            es_miembro = True

        es_miembro = str(es_miembro)
        imprimir.imprimir_datos_tabla([jugador["nombre"], es_miembro], '20')

def calcular_imprimir_jugador_mayor_cantidad_rebotes(lista_jugadores: list) -> None or -1:
    """
    calcular_imprimir_jugador_mayor_cantidad_rebotes: Calcula e imprime el jugador con el total de 'rebotes_totales'
    más alto de una lista de jugadores.

    :param lista_jugadores: Una lista de diccionarios que contiene datos de jugadores, cada diccionario
    representa un jugador.

    :return: None o un entero que es -1.
    """
    if not lista_jugadores:
        return -1
    operacion.calcular_max_imprimir_dato(lista_jugadores, 'rebotes_totales')

def calcular_imprimir_jugador_mayor_porcentaje_tiros_campo(lista_jugadores: list) -> None or -1:
    """
    calcular_imprimir_jugador_mayor_porcentaje_tiros_campo: Calcula e imprime el jugador con el total de 'porcentaje_tiros_de_campo'
    más alto de una lista de jugadores.

    :param lista_jugadores: Una lista de diccionarios que contiene datos de jugadores, cada diccionario
    representa un jugador.

    :return: None o un entero que es -1.
    """
    if not lista_jugadores:
        return -1
    operacion.calcular_max_imprimir_dato(lista_jugadores, 'porcentaje_tiros_de_campo')

def calcular_imprimir_jugador_mayor_cantidad_asistencias(lista_jugadores: list) -> None or -1:
    """
    calcular_imprimir_jugador_mayor_cantidad_asistencias: Calcula e imprime el jugador con el total de 'asistencias_totales'
    más alto de una lista de jugadores.

    :param lista_jugadores: Una lista de diccionarios que contiene datos de jugadores, cada diccionario
    representa un jugador.

    :return: None o un entero que es -1.
    """
    if not lista_jugadores:
        return -1
    operacion.calcular_max_imprimir_dato(lista_jugadores, 'asistencias_totales')

def calcular_imprimir_jugadores_puntos_por_partido_mayor_valor(lista_jugadores: list) -> None or -1:
    """
    calcular_imprimir_jugadores_puntos_por_partido_mayor_valor: calcula e imprime los jugadores que
    tienen un 'promedio_puntos_por_partido' más alto que un valor dado.

    :param lista_jugadores: Una lista de diccionarios que contiene datos de jugadores, cada diccionario
    representa un jugador.

    :return: None o un entero que es -1.
    """
    if not lista_jugadores:
        return -1

    valor_ingresado = solicitar.solicitar_valor_float()
    if valor_ingresado == -1:
        return -1
    existe_valor_mayor = operacion.calcular_imprimir_jugadores_mayor_valor(lista_jugadores,'promedio_puntos_por_partido', valor_ingresado)
    if not existe_valor_mayor:
        print("\nNo existen jugadores que tengan más puntos por partido que ese valor")

def calcular_imprimir_jugadores_rebotes_partido_mayor_valor(lista_jugadores: list) -> None or -1:
    """
    calcular_imprimir_jugadores_rebotes_partido_mayor_valor: calcula e imprime los jugadores que
    tienen un 'promedio_rebotes_por_partido' más alto que un valor dado.

    :param lista_jugadores: Una lista de diccionarios que contiene datos de jugadores, cada diccionario
    representa un jugador.

    :return: None o un entero que es -1.
    """
    if not lista_jugadores:
        return -1

    valor_ingresado = solicitar.solicitar_valor_float()
    if valor_ingresado == -1:
        return -1
    existe_valor_mayor = operacion.calcular_imprimir_jugadores_mayor_valor(lista_jugadores,'promedio_rebotes_por_partido', valor_ingresado)
    if not existe_valor_mayor:
        print("\nNo existen jugadores que tengan más rebotes por partido que ese valor")

def calcular_imprimir_jugadores_asistencias_partido_mayor_valor(lista_jugadores: list) -> None or -1:
    """
    calcular_imprimir_jugadores_asistencias_partido_mayor_valor: calcula e imprime los jugadores que
    tienen un 'promedio_asistencias_por_partido' más alto que un valor dado.

    :param lista_jugadores: Una lista de diccionarios que contiene datos de jugadores, cada diccionario
    representa un jugador.

    :return: None o un entero que es -1.
    """
    if not lista_jugadores:
        return -1

    valor_ingresado = solicitar.solicitar_valor_float()
    if valor_ingresado == -1:
        return -1
    existe_valor_mayor = operacion.calcular_imprimir_jugadores_mayor_valor(lista_jugadores,'promedio_asistencias_por_partido', valor_ingresado)
    if not existe_valor_mayor:
        print("\nNo existen jugadores que tengan más asistencias por partido que ese valor")

def calcular_imprimir_jugador_mayor_robos_totales(lista_jugadores: list) -> None or -1:
    """
    calcular_imprimir_jugador_mayor_robos_totales: Calcula e imprime el jugador con el total de 'robos_totales'
    más alto de una lista de jugadores.

    :param lista_jugadores: Una lista de diccionarios que contiene datos de jugadores, cada diccionario
    representa un jugador.

    :return: None o un entero que es -1.
    """
    if not lista_jugadores:
        return -1
    operacion.calcular_max_imprimir_dato(lista_jugadores, 'robos_totales')

def calcular_imprimir_jugador_mayor_bloqueos_totales(lista_jugadores: list) -> None or -1:
    """
    calcular_imprimir_jugador_mayor_bloqueos_totales: Calcula e imprime el jugador con el total de 'bloqueos_totales'
    más alto de una lista de jugadores.

    :param lista_jugadores: Una lista de diccionarios que contiene datos de jugadores, cada diccionario
    representa un jugador.

    :return: None o un entero que es -1.
    """
    if not lista_jugadores:
        return -1
    operacion.calcular_max_imprimir_dato(lista_jugadores, 'bloqueos_totales')

def calcular_imprimir_jugadores_tiros_libres_mayor_valor(lista_jugadores: list) -> None or -1:
    """
    calcular_imprimir_jugadores_tiros_libres_mayor_valor: calcula e imprime los jugadores que
    tienen un 'porcentaje_tiros_libres' más alto que un valor dado.

    :param lista_jugadores: Una lista de diccionarios que contiene datos de jugadores, cada diccionario
    representa un jugador.

    :return: None o un entero que es -1.
    """
    if not lista_jugadores:
        return -1

    valor_ingresado = solicitar.solicitar_valor_float()
    if valor_ingresado == -1:
        return -1
    existe_valor_mayor = operacion.calcular_imprimir_jugadores_mayor_valor(lista_jugadores,'porcentaje_tiros_libres', valor_ingresado)
    if not existe_valor_mayor:
        print("\nNo existen jugadores que tengan mayor porcentaje de tiros libres que ese valor")

def calcular_e_imprimir_promedio_puntos_por_partido_excluyendo_min(lista_jugadores: list) -> None or -1:
    """
    calcular_e_imprimir_promedio_puntos_por_partido_excluyendo_min: Calcula e imprime el promedio de puntos
    por juego de un equipo, excluyendo al jugador con el 'promedio_puntos_por_partido' más bajo.

    :param lista_jugadores: Una lista de diccionarios que contiene datos de jugadores, cada diccionario
    representa un jugador.

    :return: None o un entero que es -1.
    """
    if not lista_jugadores:
        return -1
    lista_jugadores_copia = lista_jugadores.copy()
    lista_min_puntos_partido = operacion.calcular_min(lista_jugadores,'promedio_puntos_por_partido')
    if not lista_min_puntos_partido:
        print("No se pudo obtener el jugador con minimo puntos por partido")
        return -1

    for jugador_min_puntos in lista_min_puntos_partido:
        nombre_jugador_min = jugador_min_puntos["nombre"]
        lista_jugadores_copia.remove(jugador_min_puntos)
    promedio_equipo = operacion.calcular_promedio(lista_jugadores_copia, 'promedio_puntos_por_partido')

    if promedio_equipo == -1:
        print("No se pudo obtener el promedio del equipo")
        return -1

    print(f"Excluyendo a {nombre_jugador_min}")
    print(f"\nEl promedio de 'Promedio puntos por partido' del equipo es: {promedio_equipo}")

def calcular_imprimir_jugador_mayor_logros_obtenidos(lista_jugadores: list) -> None or -1:
    """
    calcular_imprimir_jugador_mayor_logros_obtenidos: Calcula e imprime el jugador con el mayor número
    de logros obtenidos de una lista de jugadores.

    :param lista_jugadores: Una lista de diccionarios que contiene datos de jugadores, cada diccionario
    representa un jugador.

    :return: None o un entero que es -1.
    """
    if not lista_jugadores:
        return -1
    mayor_cantidad_obtenida = False
    for jugador in lista_jugadores:
        if 'logros' in jugador:
            if not mayor_cantidad_obtenida:
                jugador_mayor_logros = jugador
                mayor_cantidad_logros = len(jugador["logros"])
                mayor_cantidad_obtenida = True
            else:
                if len(jugador["logros"]) > mayor_cantidad_logros:
                    jugador_mayor_logros = jugador
                    mayor_cantidad_logros = len(jugador["logros"])
    imprimir.imprimir_tabla_encabezado(['Nombre', 'Logros'], '20')
    imprimir.imprimir_obtener_nombre_dato(jugador_mayor_logros,'logros')

def calcular_imprimir_jugadores_tiros_triples_mayor_valor(lista_jugadores: list) -> None or -1:
    """
    calcular_imprimir_jugadores_tiros_triples_mayor_valor: calcula e imprime los jugadores que
    tienen un 'porcentaje_tiros_triples' más alto que un valor dado.

    :param lista_jugadores: Una lista de diccionarios que contiene datos de jugadores, cada diccionario
    representa un jugador.

    :return: None o un entero que es -1.
    """
    if not lista_jugadores:
        return -1

    valor_ingresado = solicitar.solicitar_valor_float()
    if valor_ingresado == -1:
        return -1
    existe_valor_mayor = operacion.calcular_imprimir_jugadores_mayor_valor(lista_jugadores,'porcentaje_tiros_triples', valor_ingresado)
    if not existe_valor_mayor:
        print("\nNo existen jugadores que tengan mayor porcentaje de tiros triples que ese valor")

def calcular_imprimir_jugador_mayor_temporadas(lista_jugadores: list) -> None or -1:
    """
    calcular_imprimir_jugador_mayor_temporadas: Calcula e imprime el/los jugador/es con mayor número de temporadas
    de una lista de jugadores.

    :param lista_jugadores: Una lista de diccionarios que contiene datos de jugadores, cada diccionario
    representa un jugador.

    :return: None o un entero que es -1.
    """
    if not lista_jugadores:
        return -1
    operacion.calcular_max_imprimir_dato(lista_jugadores, 'temporadas')

def calcular_imprimir_jugadores_tiros_campo_mayor_valor(lista_jugadores: list) -> None or -1:
    """
    calcular_imprimir_jugadores_tiros_campo_mayor_valor: Calcula e imprime los jugadores con un
    'porcentaje_tiros_de_campo' superior a un valor dado y los ordena alfabeticamente por su posición.

    :param lista_jugadores: Una lista de diccionarios que contiene datos de jugadores, cada diccionario
    representa un jugador.

    :return: None o un entero que es -1.
    """
    lista_ordenada = ordenar.quick_sort(lista_jugadores, 'posicion')
    valor_ingresado = solicitar.solicitar_valor_float()

    if valor_ingresado == -1:
        return -1

    lista_jugadores_mayor_valor = operacion.calcular_datos_mayor_a_valor_ingresado(lista_ordenada,'porcentaje_tiros_de_campo', valor_ingresado)

    if not lista_jugadores_mayor_valor:
        print("\nNo existen jugadores que tengan mayor porcentaje de tiros de campo que ese valor")
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

def aplicacion_jugadores(lista_jugadores: list):
    """
    aplicacion_jugadores: Imprime el menú y administra datos de la lista de jugadores de
    baloncesto. Permite al usuario realizar varias operaciones con la lista.

    :param lista_jugadores: Una lista de diccionarios que contiene datos de jugadores, cada diccionario
    representa un jugador.
    """
    flag_guardar_archivo = False
    while True:

        opcion = imprimir.imprimir_menu()
        opcion_valida = re.search(r'2', str(opcion))
        if bool(opcion_valida):
            flag_guardar_archivo = True
        match opcion:
            case 1:
                imprimir_jugadores_nombre_posicion(lista_jugadores)
            case 2:
                lista_data_jugador = obtener_e_imprimir_jugador_nombre_estadisticas(lista_jugadores)
                if lista_data_jugador != -1:
                    nombre_jugador = lista_data_jugador[0]['nombre'].lower()
                    nombre_jugador = re.sub(r" ", "_", nombre_jugador)
            case 3:
                if flag_guardar_archivo and lista_data_jugador != -1:
                    exportar_csv(f'jugador_{nombre_jugador}.csv', lista_data_jugador)
                else:
                    print("Debe haber completado la opción 2 anteriormente para poder guardar el archivo")
            case 4:
                obtener_e_imprimir_jugador_nombre_logros(lista_jugadores)
            case 5:
                calcular_e_imprimir_promedio_puntos_por_partido(lista_jugadores)
            case 6:
                imprimir_jugador_nombre_salon_fama(lista_jugadores)
            case 7:
                calcular_imprimir_jugador_mayor_cantidad_rebotes(lista_jugadores)
            case 8:
                calcular_imprimir_jugador_mayor_porcentaje_tiros_campo(lista_jugadores)
            case 9:
                calcular_imprimir_jugador_mayor_cantidad_asistencias(lista_jugadores)
            case 10:
                calcular_imprimir_jugadores_puntos_por_partido_mayor_valor(lista_jugadores)
            case 11:
                calcular_imprimir_jugadores_rebotes_partido_mayor_valor(lista_jugadores)
            case 12:
                calcular_imprimir_jugadores_asistencias_partido_mayor_valor(lista_jugadores)
            case 13:
                calcular_imprimir_jugador_mayor_robos_totales(lista_jugadores)
            case 14:
                calcular_imprimir_jugador_mayor_bloqueos_totales(lista_jugadores)
            case 15:
                calcular_imprimir_jugadores_tiros_libres_mayor_valor(lista_jugadores)
            case 16:
                calcular_e_imprimir_promedio_puntos_por_partido_excluyendo_min(lista_jugadores)
            case 17:
                calcular_imprimir_jugador_mayor_logros_obtenidos(lista_jugadores)
            case 18:
                calcular_imprimir_jugadores_tiros_triples_mayor_valor(lista_jugadores)
            case 19:
                calcular_imprimir_jugador_mayor_temporadas(lista_jugadores)
            case 20:
                calcular_imprimir_jugadores_tiros_campo_mayor_valor(lista_jugadores)
            case 23:
                lista_ranking_jugadores = calcular_obtener_posicion_ranking_jugadores(lista_jugadores)
                exportar_csv('posicion_ranking_jugadores.csv', lista_ranking_jugadores)
            case 0:
                break
            case _:
                print("Opción no válida")
        limpiar_consola()