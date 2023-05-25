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
        dict_nombre_posicion = obtener_nombre_dato(jugador, 'posicion')
        if dict_nombre_posicion == -1:
            print(f"El jugador no es válido para realizar esta operación")
            return -1
        nombre = dict_nombre_posicion["nombre"]
        posicion = dict_nombre_posicion['posicion']
        print(nombre.ljust(20), "-", posicion)


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
    y 'solicitar_dato' para solicita al usuario que ingrese el índice de un jugador, almacena el nombre
    y las estadisticas en una lista e imprime estos datos en consola.

    Recibe: :param lista_jugadores: Lista de diccionarios que contiene datos de jugadores.

    Retorna: Una lista que contiene el nombre y las estadisticas del jugador solicitado. 
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
        regex = r'^[0-11]+$'
        condicion_valida = re.search(regex, indice_jugador)
        condicion_valida = bool(condicion_valida)

    indice_jugador = int(indice_jugador)

    if indice_jugador == -1:
        print("\nIngrese una nueva opción del menú")
        return -1

    indice = 0
    for jugador in lista_jugadores:
        if indice_jugador == indice:
            nombre = jugador['nombre']

            dict_data_jugador = {}
            print(f"\nNombre: {nombre}")
            for dato,valor in jugador.items():
                if dato == 'estadisticas':
                    print("Estadísticas:")
                    for estadistica, valor_estadistica in valor.items():
                        dict_data_jugador[estadistica] = valor_estadistica
                        print(f"{estadistica} : {valor_estadistica} | ", end="")
                elif dato != "logros":
                    dict_data_jugador[dato] = valor
            print("\n")
            lista_data_jugador = [dict_data_jugador]
        indice += 1
    
    return lista_data_jugador

def exportar_csv(nombre_archivo: str, data_jugador: list):
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


def imprimir_jugador_nombre_logros(lista_jugadores: list):
    if not lista_jugadores:
        return -1

    condicion_valida = False
    imprimir_nombre_indice(lista_jugadores)

    while not condicion_valida:
        nombre_buscado = solicitar_dato('nombre')

        if nombre_buscado == '-1':
            mensaje = "\nIngrese una nueva opción del menú"
            return print(mensaje)

        nombre_buscado = nombre_buscado.lower()
        regex = r'\b'+ nombre_buscado + r'\b'+ r'|\b[a-zA-Z]{1,}'+ nombre_buscado + r'\b'+ r'|\b'+ nombre_buscado + r'+[a-zA-Z]{1,}\b'
        for jugador in lista_jugadores:
            nombre_jugador = jugador['nombre'].lower()
            condicion_valida = re.search(regex, nombre_jugador)
            condicion_valida = bool(condicion_valida)
            if condicion_valida:
                dict_nombre_logros = obtener_nombre_dato(jugador,'logros')
                return dict_nombre_logros
                

# Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por
# nombre de manera ascendente.

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
    print("5. ")
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
                    nombre_jugador = lista_data_jugador[0]['nombre']
                    nombre_jugador = re.sub(r" ", "_", nombre_jugador)
            case 3:
                if flag_guardar_archivo and lista_data_jugador != -1:
                    exportar_csv(f'jugador_{nombre_jugador}.csv', lista_data_jugador)
                else:
                    print("Debe haber ingresado la opción 2 anteriormente para poder guardar el archivo")
            case 4:
                dict_nombre_logros = imprimir_jugador_nombre_logros(lista_jugadores)
                nombre = dict_nombre_logros["nombre"]
                logros = dict_nombre_logros["logros"]
                print(f"\nNombre: {nombre}")
                print("Logros:")
                for logro in logros:
                    print(f"{logro} | ", end="")
            case 5:
                pass
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