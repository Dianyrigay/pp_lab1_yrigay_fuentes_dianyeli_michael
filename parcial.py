# Alumna: Dianyeli Yrigay 95984910
# Division 1E

# PARCIAL PROGRAMACIÓN

"""
name_funcion:

Recibe:

Retorna:
"""
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

def quick_sort(lista:list, key: str, ascendente:bool = True)->list:
    """
    quick_sort: Ordena una lista de diccionarios por el dato 'key' pasado por parámetro de
    forma ascendente por defecto o descendente si se desea.

    Recibe: :param lista: Una lista de diccionarios que contiene datos
            :param key: String que representa la key por la que se desea ordenar la lista
            :param ascendente: Booleano que indica si el ordenamiento debe ser ascendente o
                            descendente (por defecto es True)

    Retorna: Una lista de diccionarios ordenada si se cumple con las validaciones, caso contrario
    retorna -1.
    """
    i = 0
    lista_de = []
    lista_iz = []
    if(len(lista)<=1):
        return lista

    pivot_encontrado = False
    while not pivot_encontrado:
      if key in lista[i]:
          pivot = lista[i]
          pivot_encontrado = True
      i += 1

    for dato in lista[i:]:
        if key in dato and key in pivot:
            if ascendente and dato[key] > pivot[key] or \
               not ascendente and dato[key] < pivot[key]:
                lista_de.append(dato)
            else:
                lista_iz.append(dato)

    lista_iz = quick_sort(lista_iz, key, ascendente)
    lista_iz.append(pivot)
    lista_de = quick_sort(lista_de, key, ascendente)

    lista_iz.extend(lista_de)
    lista_ordenada = lista_iz
    return lista_ordenada

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

def imprimir_nombre_dato(jugador: dict, key_ingresada: str) -> None:
    if type(jugador) != type(dict()):
        return -1

    if 'nombre' not in jugador:
        return -1

    nombre = jugador["nombre"]
    for dato_jugador, valor_jugador in jugador.items():
        if key_ingresada in jugador:
            if type(valor_jugador) == type(str()):
                dato = jugador[key_ingresada]
        if key_ingresada in valor_jugador:
            if type(valor_jugador) == type(dict()):
                for key, valor in valor_jugador.items():
                    if key == key_ingresada:
                        dato = valor
            if type(valor_jugador) == type(list()):
                for elemento in valor_jugador.items():
                    dato = elemento

    if type(dato) == type(str()) or type(dato) == type(int()) or type(dato) == type(float()):
        print(nombre.ljust(20), "-", dato)
    if type(dato) == type(dict()):
        print("\nNombre: ".ljust(20), nombre)
        print("Estadísticas:")
        for key, valor in dato.items():
            print(" ".ljust(20),f"{key.capitalize()}: ", valor)
    if type(dato) == type(list()):
        print("\nNombre: ".ljust(20), nombre)
        print("Logros:")
        for elemento in dato:
            print(" ".ljust(20),f"{elemento.capitalize()}")

def solicitar_dato(dato: str) -> str:
    """
    solicitar_dato: Solicita al usuario por consola que ingrese un dato de un jugador.

    Recibe :param dato: String que hace referencia al dato que el usuario debe ingresar.

    Retorna: Un string que es el dato del jugador a buscar o -1 si el usuario se arrepiente de la búsqueda.
    """
    dato_ingresado = input(f"\nIngrese {dato} del jugador que desea buscar (o ingrese '-1' para salir del submenú): ")
    return dato_ingresado

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
        imprimir_nombre_dato(jugador, 'posicion')

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

def obtener_e_imprimir_jugador_nombre_estadisticas(lista_jugadores: list):
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
        indice_jugador = solicitar_dato('indice')
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
            imprimir_nombre_dato(jugador, 'estadisticas')
        indice += 1

    return lista_data_jugador

def exportar_csv(nombre_archivo: str, data_jugador: list):
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

def obtener_jugador_nombre_logros(lista_jugadores: list):
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

    condicion_valida = False
    imprimir_nombre_indice(lista_jugadores)

    while not condicion_valida:
        nombre_buscado = solicitar_dato('nombre')

        if nombre_buscado == '-1':
            print("\nIngrese una nueva opción del menú")
            return -1

        nombre_buscado = nombre_buscado.lower()
        regex = r'\b'+ nombre_buscado + r'\b'+ r'|\b[a-zA-Z]{1,}'+ nombre_buscado + r'\b'+ r'|\b'+ nombre_buscado + r'+[a-zA-Z]{1,}\b'
        for jugador in lista_jugadores:
            nombre_jugador = jugador['nombre'].lower()
            condicion_valida = re.search(regex, nombre_jugador)
            condicion_valida = bool(condicion_valida)
            if condicion_valida:
                dict_nombre_logros = obtener_nombre_dato(jugador,'logros')
                imprimir_nombre_dato(jugador,'logros')
                return dict_nombre_logros

# Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por
# nombre de manera ascendente.
def calcular_e_imprimir_promedio_puntos_por_partido(lista_jugadores: list) -> float:
    if not lista_jugadores:
        return -1

    promedio_equipo = calcular_promedio(lista_jugadores, 'promedio_puntos_por_partido')

    lista_ordenada_nombres = quick_sort(lista_jugadores, 'nombre')
    print("Nombre:".ljust(20), "- Promedio puntos por partido:")
    for jugador in lista_ordenada_nombres:
        imprimir_nombre_dato(jugador, 'promedio_puntos_por_partido')

    print(f"\nPromedio de 'Promedio puntos por partido' del equipo: {promedio_equipo}")

"""
mostrar_menu: Imprime por consola el menú de opciones, solicita al usuario que ingrese una opción
y valida la misma.

No recibe parámetros.

Retorna: Un entero que es la opción ingresada si es válida, caso contrario retorna -1.
"""
def mostrar_menu() -> int:
    print("\n----------------------------------------------------")
    print("Menú de opciones:")
    print("1. Mostrar la lista de todos los jugadores del Dream Team.")
    print("2. Buscar jugador por índice y mostrar sus estadísticas completas.")
    print("3. Exportar archivo CSV con las estadisticas del jugador del punto 2.")
    print("4. Buscar jugador por nombre y mostrar sus logros.")
    print("5. Calcular y mostrar el promedio de puntos por partido del equipo del Dream Team,")
    print("   ordenado por nombre de manera ascendente")
    print("6. ")
    print("7. ")
    print("0. Salir del programa")
    opcion = input("\nIngrese la opción deseada: ")
    print("\n----------------------------------------------------")
    opcion_valida = re.search(r'^[1-9]$|^1[0-9]$|^20$', opcion)
    if not bool(opcion_valida):
        return -1
    opcion = int(opcion)
    return opcion

"""
main: reutiliza la funcion 'mostrar_menu' para obtener la opcion elegida, de acuerdo a esta
llama a una función para aplicar la lógica correspondiente.

No recibe parámetros

No retorna datos
"""
def main():
    flag_guardar_archivo = False
    while True:
        opcion = mostrar_menu()
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
                obtener_jugador_nombre_logros(lista_jugadores)
            case 5:
                calcular_e_imprimir_promedio_puntos_por_partido(lista_jugadores)
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 0:
                break
            case _:
                print("Opción no válida")

main()