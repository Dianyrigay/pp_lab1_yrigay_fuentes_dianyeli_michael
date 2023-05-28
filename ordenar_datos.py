import re
import imprimir_datos as imprimir

def quick_sort(lista:list, key: str, ascendente:bool = True)->list:
    """
    quick_sort: Realiza una clasificación rápida en una lista de diccionarios
    según una key específica y un orden de clasificación.

    :param lista: una lista de diccionarios que se ordenarán según el valor de una key específica en
    cada diccionario
    :param key: String que representa la key o atributo de los objetos de la lista que se utilizará para ordenarlos
    :param ascendente: Booleano opcional que determina si la clasificación se debe realizar en orden
    ascendente (True) o descendente (False). Por default es True

    :return: Una lista ordenada basada en el algoritmo de clasificación rápida, bajo la key
    especificada y el orden recibido por parámetro.
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

def ordenar_imprimir_dato(lista: list, key_imprimir: str, key_ordenar: str)-> None or -1:
    """
    ordenar_imprimir_dato: Toma una lista, una key para imprimir y una key para ordenar, y luego
    ordena la lista por la key de clasificación e imprime el nombre del jugador y los datos
    especificados.

    :param lista: Una lista de diccionarios que contiene datos.
    :param key_imprimir: String que representa la key de los datos que se imprimirán para cada
    dato de la lista.
    :param key_ordenar: String que representa la key para ordenar la lista por sus valores.

    :return: None si cumple con las validaciones, caso contrario devuelve -1.
    """
    if not lista:
        return -1

    lista_ordenada = quick_sort(lista, key_ordenar)

    if not lista_ordenada:
        print("No se pudo ordear la lista")
        return -1

    dato_capitalizado = re.sub(r'_', ' ', key_imprimir).capitalize()
    imprimir.imprimir_tabla_encabezado(['Nombres',dato_capitalizado], '20')
    for elemento in lista_ordenada:
        imprimir.imprimir_obtener_nombre_dato(elemento, key_imprimir)