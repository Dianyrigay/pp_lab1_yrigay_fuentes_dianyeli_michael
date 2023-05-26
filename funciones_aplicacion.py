# Alumna: Dianyeli Yrigay 95984910
# Division 1E

# PARCIAL PROGRAMACIÓN

import operaciones_numericas as operacion
import imprimir_datos as imprimir
import solicitar_datos as solicitar
import re
import json
import csv

def leer_archivo(nombre_archivo: str) -> list:
    """
    leer_archivo: Carga los datos del archivo json, almacenandolos en una lista. El modo de apertura
    del archivo es de solo lectura

    Recibe: :param nombre_archivo: String que contiene la ruta y nombre del archivo que se desea leer.

    Retorna: La lista obtenida del archivo json
    """
    lista = []

    with open(nombre_archivo) as archivo:
        data = json.load(archivo)
        lista = data["jugadores"]
    return lista

lista_jugadores = leer_archivo('dt.json')

def obtener_nombre_dato(jugador: dict, key_ingresada: str) -> dict:
    """
    obtener_nombre_dato: Obtiene el nombre del jugador y el valor de la key ingresada.

    Recibe: :param jugador: Diccionario que contiene los datos de un jugador.
            :param key_ingresada: String que hace referencia al dato del que se desea obtener el valor.

    Retorna: Un diccionario que contiene como keys el nombre y el dato pasado por parametro, si el jugador es
    de tipo 'dict'; caso contrario retorna -1.
    """
    dict_nombre_dato = {}

    if type(jugador) != type(dict()):
        return -1

    if 'nombre' not in jugador and key_ingresada not in jugador:
        return -1

    dict_nombre_dato["nombre"] = jugador["nombre"]
    dict_nombre_dato[key_ingresada] = jugador[key_ingresada]
    return dict_nombre_dato

def imprimir_jugadores_posicion(lista_jugadores: list) -> None:
    """
    imprimir_jugadores_posicion: Imprime por consola los nombres de los jugadores y la posición de los mismos.

    Recibe: :param lista_jugadores: Lista de diccionarios que contiene datos de jugadores.

    No retorna datos.
    """
    if not lista_jugadores:
        return -1

    print("Nombre:".ljust(20), "- Posición:")
    for jugador in lista_jugadores:
        imprimir.imprimir_nombre_dato(jugador, 'posicion')

def imprimir_nombre_indice(lista_jugadores: list) -> None:
    """
    imprimir_nombre_indice: Imprime en consola los nombres de los jugadores y el indice de los mismos
    si la lista no está vacía, sino imprime que la misma esta vacía.

    Recibe: :param lista_jugadores: Lista de diccionarios que contiene datos de jugadores.

    No retorna datos.
    """
    if not lista_jugadores:
        print("Lista vacía")

    indice = 0
    for jugador in lista_jugadores:
        if 'nombre' in jugador:
            nombre = jugador['nombre']
        mensaje = f"\t{indice} - {nombre}"
        indice += 1
        print(mensaje)

def obtener_e_imprimir_jugador_nombre_estadisticas(lista_jugadores: list) -> list:
    """
    obtener_e_imprimir_jugador_nombre_estadisticas: Reutiliza la función 'imprimir_nombre_indice'
    y 'solicitar_dato' para solicitar al usuario que ingrese el índice de un jugador, almacena el nombre,
    la posición y las estadisticas en una lista e imprime estos datos en consola.

    Recibe: :param lista_jugadores: Lista de diccionarios que contiene datos de jugadores.

    Retorna: Una lista que contiene el nombre, posición y las estadisticas del jugador solicitado.
             -1 si la lista esta vacía o en caso de que el usuario no desee continuar con la búsqueda.
    """
    if not lista_jugadores:
        return -1

    condicion_valida = False
    imprimir_nombre_indice(lista_jugadores)

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
            imprimir.imprimir_nombre_dato(jugador, 'estadisticas')
        indice += 1

    return lista_data_jugador

def exportar_csv(nombre_archivo: str, data_jugador: list) -> bool:
    """
    exportar_csv: Escribe un archivo csv y si ya existe lo sobreescribe, con los datos de la lista que haya
    recibido por parámetro, valida si se creo el archivo correctamente.

    Recibe: :param nombre_archivo: String que contiene la ruta y nombre del archivo que se desea guardar.
            :param data_jugador: Una lista de diccionarios que contiene datos de un jugador.

    Retorna: Un booleano que es True si el archivo se guardo correctamente y False si el archivo no pudo
    ser guardado.
    """
    archivo_guardado = False
    if data_jugador:
        with open(nombre_archivo, 'w', newline='') as archivo:
            writer = csv.writer(archivo)

            encabezados = data_jugador[0].keys()
            writer.writerow(encabezados)

            for dato in data_jugador:
                valores = dato.values()
                writer.writerow(valores)
            archivo_guardado = True

    if archivo_guardado:
        print(f"Se creó el archivo: {nombre_archivo}")
    else:
        print(f"Error al crear el archivo: {nombre_archivo}")

    return archivo_guardado

def obtener_jugador_nombre_logros(lista_jugadores: list) -> list:
    """
    obtener_jugador_nombre_logros: Reutiliza la función 'imprimir_nombre_indice'
    y 'solicitar_dato' para solicitar al usuario que ingrese el nombre de un jugador, usando
    la función 'obtener_nombre_dato' guarda el nombre y los logros en un diccionario.

    Recibe: :param lista_jugadores: Lista de diccionarios que contiene datos de jugadores.

    Retorna: Un diccionario que contiene el nombre y los logros del jugador solicitado.
             -1 si la lista esta vacía o en caso de que el usuario no desee continuar con la búsqueda.
    """
    if not lista_jugadores:
        return -1

    nombre_valido = False
    imprimir_nombre_indice(lista_jugadores)
    lista_jugadores_validos = []

    while not lista_jugadores_validos:
        nombre_buscado = solicitar.solicitar_dato('nombre')

        if nombre_buscado == '-1':
            print("\nIngrese una nueva opción del menú")
            return -1

        for jugador in lista_jugadores:
            regex = r'\b'+ nombre_buscado + r'\b'+ r'|\b[a-zA-Z]{1,}'+ nombre_buscado + r'\b'+ r'|\b'+ nombre_buscado + r'+[a-zA-Z]{1,}\b'
            nombre_jugador = jugador['nombre'].lower()
            nombre_valido = re.search(regex, nombre_jugador)
            nombre_valido = bool(nombre_valido)
            if nombre_valido:
                lista_jugadores_validos.append(jugador)
    return lista_jugadores_validos

def calcular_e_imprimir_promedio_puntos_por_partido(lista_jugadores: list) -> None:
    if not lista_jugadores:
        return -1
    promedio_equipo = operacion.calcular_promedio(lista_jugadores, 'promedio_puntos_por_partido')
    imprimir.ordenar_imprimir_dato(lista_jugadores, 'promedio_puntos_por_partido', 'nombre')
    print(f"\nPromedio de 'Promedio puntos por partido' del equipo: {promedio_equipo}")

def imprimir_jugador_nombre_salon_fama(lista_jugadores: list) -> None:
    lista_jugadores_buscados = obtener_jugador_nombre_logros(lista_jugadores)
    if type(lista_jugadores_buscados) != type(list()):
        return -1

    for jugador in lista_jugadores_buscados:
        if 'Miembro del Salon de la Fama del Baloncesto' in jugador['logros']:
            print("Nombre:".ljust(20),"- Es miembro:")
            imprimir.imprimir_nombre_dato(jugador, 'Miembro del Salon de la Fama del Baloncesto')

def calcular_imprimir_jugador_mayor_cantidad_rebotes(lista_jugadores: list) -> None:
    if not lista_jugadores:
        return -1
    imprimir.calcular_imprimir_dato(lista_jugadores, 'max', 'rebotes_totales')

def calcular_imprimir_jugador_mayor_porcentaje_tiros_campo(lista_jugadores: list) -> None:
    if not lista_jugadores:
        return -1
    imprimir.calcular_imprimir_dato(lista_jugadores, 'max', 'porcentaje_tiros_de_campo')

def calcular_imprimir_jugador_mayor_cantidad_asistencias(lista_jugadores: list) -> None:
    if not lista_jugadores:
        return -1
    imprimir.calcular_imprimir_dato(lista_jugadores, 'max', 'asistencias_totales')

def calcular_imprimir_jugadores_puntos_por_partido_mayor_valor(lista_jugadores: list) -> None:
    if not lista_jugadores:
        return -1

    valor_ingresado = solicitar.solicitar_valor_float()
    if valor_ingresado == -1:
        return -1
    existe_valor_mayor = imprimir.calcular_imprimir_jugadores_mayor_valor(lista_jugadores,'promedio_puntos_por_partido', valor_ingresado)
    if not existe_valor_mayor:
        print("\nNo existen jugadores que tengan más puntos por partido que ese valor")

def calcular_imprimir_jugadores_rebotes_partido_mayor_valor(lista_jugadores: list) -> None:
    if not lista_jugadores:
        return -1

    valor_ingresado = solicitar.solicitar_valor_float()
    if valor_ingresado == -1:
        return -1
    existe_valor_mayor = imprimir.calcular_imprimir_jugadores_mayor_valor(lista_jugadores,'promedio_rebotes_por_partido', valor_ingresado)
    if not existe_valor_mayor:
        print("\nNo existen jugadores que tengan más rebotes por partido que ese valor")

def calcular_imprimir_jugadores_asistencias_partido_mayor_valor(lista_jugadores: list) -> None:
    if not lista_jugadores:
        return -1

    valor_ingresado = solicitar.solicitar_valor_float()
    if valor_ingresado == -1:
        return -1
    existe_valor_mayor = imprimir.calcular_imprimir_jugadores_mayor_valor(lista_jugadores,'promedio_asistencias_por_partido', valor_ingresado)
    if not existe_valor_mayor:
        print("\nNo existen jugadores que tengan más asistencias por partido que ese valor")

def calcular_imprimir_jugador_mayor_robos_totales(lista_jugadores: list) -> None:
    if not lista_jugadores:
        return -1
    imprimir.calcular_imprimir_dato(lista_jugadores, 'max', 'robos_totales')

def calcular_imprimir_jugador_mayor_bloqueos_totales(lista_jugadores: list) -> None:
    if not lista_jugadores:
        return -1
    imprimir.calcular_imprimir_dato(lista_jugadores, 'max', 'bloqueos_totales')

def calcular_imprimir_jugadores_tiros_libres_mayor_valor(lista_jugadores: list) -> None:
    if not lista_jugadores:
        return -1

    valor_ingresado = solicitar.solicitar_valor_float()
    if valor_ingresado == -1:
        return -1
    existe_valor_mayor = imprimir.calcular_imprimir_jugadores_mayor_valor(lista_jugadores,'porcentaje_tiros_libres', valor_ingresado)
    if not existe_valor_mayor:
        print("\nNo existen jugadores que tengan más asistencias por partido que ese valor")

def aplicacion_jugadores():
    """
    aplicacion_jugadores: reutiliza la funcion 'mostrar_menu' para obtener la opcion elegida, de acuerdo a esta
    llama a una función para aplicar la lógica correspondiente.

    No recibe parámetros

    No retorna datos
    """
    flag_guardar_archivo = False
    while True:
        opcion = imprimir.imprimir_menu()
        opcion_valida = re.search(r'2', str(opcion))
        if bool(opcion_valida):
            flag_guardar_archivo = True
        match opcion:
            case 1:
                imprimir_jugadores_posicion(lista_jugadores)
            case 2:
                lista_data_jugador = obtener_e_imprimir_jugador_nombre_estadisticas(lista_jugadores)
                if lista_data_jugador != -1:
                    nombre_jugador = lista_data_jugador[0]['nombre'].lower()
                    nombre_jugador = re.sub(r" ", "_", nombre_jugador)
            case 3:
                if flag_guardar_archivo and lista_data_jugador != -1:
                    exportar_csv(f'jugador_{nombre_jugador}.csv', lista_data_jugador)
                else:
                    print("Debe haber ingresado la opción 2 anteriormente para poder guardar el archivo")
            case 4:
                lista_jugadores_logros = obtener_jugador_nombre_logros(lista_jugadores)
                if lista_jugadores_logros != -1:
                    for jugador in lista_jugadores_logros:
                        imprimir.imprimir_nombre_dato(jugador, 'logros')
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
                pass
            case 16:
                pass
            case 17:
                pass
            case 18:
                pass
            case 19:
                pass
            case 20:
                pass
            case 23:
                pass
            case 0:
                break
            case _:
                print("Opción no válida")