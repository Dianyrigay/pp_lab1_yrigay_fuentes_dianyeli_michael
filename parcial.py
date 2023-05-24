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

"""
leer_archivo: Carga los datos del archivo json, almacenandolos en una lista. El modo de apertura
del archivo es de solo lectura

Recibe: :param nombre_archivo: String que contiene la ruta y nombre del archivo que se desea leer.

Retorna: La lista obtenida del archivo json
"""
def leer_archivo(nombre_archivo: str) -> list:
  lista = []

  with open(nombre_archivo) as archivo:
      data = json.load(archivo)
      lista = data["jugadores"]
  return lista

lista_jugadores = leer_archivo('dt.json')

def obtener_nombre_dato(jugador: dict, key_ingresada: str) -> str:
    if not lista_jugadores:
        return -1

    if 'nombre' in jugador and key_ingresada in jugador:
        nombre = jugador["nombre"]
        dato = jugador[key_ingresada]
        mensaje = f"{nombre} - {dato}"
        return mensaje

def obtener_jugadores_posicion(lista_jugadores: list) -> None:
    for jugador in lista_jugadores:
        print(obtener_nombre_dato(jugador, 'posicion'))

"""
solicitar_indice: Muestra al usuario la lista de indices con los nombres de los jugadores y solicita que
ingrese un índice, validando el mismo.

Recibe :param lista_jugadores: Una lista de diccionarios que contiene datos de jugadores

Retorna: Un entero que es el índice ingresado si es válido, caso contrario retorna -1.
"""
def solicitar_condicion(lista_jugadores: list, condicion: str):
    condicion_valida = False
    primer_ingreso = True

    if not lista_jugadores:
        return -1


    while not condicion_valida:
        if primer_ingreso:
            obtener_nombre_indice(lista_jugadores)
            condicion_ingresada = input(f"\nIngrese {condicion} del jugador que desea buscar: ")
            primer_ingreso = False

        if condicion == 'indice':
            regex = r'^[0-11]+$'
            condicion_valida = re.search(regex, condicion_ingresada)
            condicion_valida = bool(condicion_valida)
            if not condicion_valida:
              condicion_ingresada = input("El indice es inválido, intente nuevamente o presione 's' para salir: ")
            if condicion_ingresada == 's':
                return -1

    return condicion_ingresada

def solicitar_condicion(condicion: str) -> str:
    condicion_ingresada = input(f"\nIngrese {condicion} del jugador que desea buscar (o ingrese '-1' para salir): ")
    return condicion_ingresada

def obtener_nombre_indice(lista_jugadores: list) -> None:
    if not lista_jugadores:
        return -1

    indice = 0
    for jugador in lista_jugadores:
        if 'nombre' in jugador:
            nombre = jugador["nombre"]
        mensaje = f"{indice} - {nombre}"
        indice += 1
        print(mensaje)

def obtener_nombre_estadisticas(lista_jugadores: list):
    if not lista_jugadores:
        return -1

    condicion_valida = False
    obtener_nombre_indice(lista_jugadores)

    while not condicion_valida:
        indice_jugador = solicitar_condicion('indice')
        if indice_jugador == '-1':
            break
        regex = r'^[0-11]+$'
        condicion_valida = re.search(regex, indice_jugador)
        condicion_valida = bool(condicion_valida)

    indice_jugador = int(indice_jugador)

    if indice_jugador == -1:
        mensaje = "\nIngrese una nueva opción del menú"
        return print(mensaje)

    indice = 0
    for jugador in lista_jugadores:
        if indice_jugador == indice:
          print(obtener_nombre_dato(jugador, 'estadisticas'))
        indice += 1

# Después de mostrar las estadísticas de un jugador seleccionado por el usuario, permite al usuario
# guardar las estadísticas de ese jugador en un archivo CSV. El archivo CSV debe contener los
# siguientes campos: nombre, posición, temporadas, puntos totales, promedio de puntos por partido,
# rebotes totales, promedio de rebotes por partido, asistencias totales, promedio de asistencias por
# partido, robos totales, bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y
# porcentaje de tiros triples.

def obtener_nombre_logros(lista_jugadores: list):
    if not lista_jugadores:
        return -1

    condicion_valida = False
    obtener_nombre_indice(lista_jugadores)

    while not condicion_valida:
        nombre_buscado = solicitar_condicion('nombre')

        if nombre_buscado == '-1':
            mensaje = "\nIngrese una nueva opción del menú"
            return print(mensaje)

        nombre_buscado = nombre_buscado.lower()
        regex = r'\b'+ nombre_buscado + r'\b'
        for jugador in lista_jugadores:
            nombre_jugador = jugador['nombre'].lower()
            condicion_valida = re.search(regex, nombre_jugador)
            if bool(condicion_valida):
                return print(obtener_nombre_dato(jugador,'logros'))

# Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por
# nombre de manera ascendente.

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
def quick_sort(lista_jugadores:list, key: str, ascendente:bool = True)->list:
    i = 0
    lista_de = []
    lista_iz = []
    if(len(lista_jugadores)<=1):
        return lista_jugadores

    pivot_encontrado = False
    while not pivot_encontrado:
      if key in lista_jugadores[i]:
          pivot = lista_jugadores[i]
          pivot_encontrado = True
      i += 1

    for dato in lista_jugadores[i:]:
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



"""
mostrar_menu: Imprime por consola el menú de opciones, solicita al usuario que ingrese una opción
y valida la misma.

No recibe parámetros.

Retorna: Un entero que es la opción ingresada si es válida, caso contrario retorna -1.
"""
def mostrar_menu() -> int:
    print("----------------------------------------------------")
    print("Menú de opciones:")
    print("1. Mostrar la lista de todos los jugadores del Dream Team.")
    print("2. Buscar jugador por índice y mostrar sus estadísticas completas")
    print("3. ")
    print("4. Buscar jugador por nombre y mostrar sus logros")
    print("5. ")
    print("6. ")
    print("7. ")
    print("0. Salir del programa")
    opcion = input("\nIngrese la opción deseada: ")
    print("----------------------------------------------------")
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
                obtener_jugadores_posicion(lista_jugadores)
            case 2:
                obtener_nombre_estadisticas(lista_jugadores)
            case 3:
                if flag_guardar_archivo:
                    pass
                else:
                    print("Debe haber ingresado la opción 2 anteriormente para poder guardar el archivo")
            case 4:
                obtener_nombre_logros(lista_jugadores)
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