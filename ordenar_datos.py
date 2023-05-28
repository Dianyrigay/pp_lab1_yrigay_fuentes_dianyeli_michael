import re
import imprimir_datos as imprimir

def quick_sort(lista:list, key_ingresada: str, ascendente:bool = True)->list:
    """
    quick_sort: Realiza una clasificación rápida en una lista de diccionarios según una key
    y un orden específico.

    :param lista: Una lista de diccionarios que contiene datos.
    :param key_ingresada: String que representa la key por la que se desea ordenar.
    :param ascendente: Booleano opcional para saber si el orden debe ser ascendente (True) o
    descendente (False). Por default es True

    :return: Una lista ordenada, bajo la key especificada y el orden recibido por parámetro.
    """

    i = 0
    lista_de = []
    lista_iz = []
    if(len(lista)<=1):
        return lista

    pivot_encontrado = False
    while not pivot_encontrado:
      if key_ingresada in lista[i]:
          pivot = lista[i]
          pivot_encontrado = True
      i += 1

    for dato in lista[i:]:
        if key_ingresada in dato and key_ingresada in pivot:
            if ascendente and dato[key_ingresada] > pivot[key_ingresada] or \
              not ascendente and dato[key_ingresada] < pivot[key_ingresada]:
                lista_de.append(dato)
            else:
                lista_iz.append(dato)

    lista_iz = quick_sort(lista_iz, key_ingresada, ascendente)
    lista_iz.append(pivot)
    lista_de = quick_sort(lista_de, key_ingresada, ascendente)

    lista_iz.extend(lista_de)
    lista_ordenada = lista_iz
    return lista_ordenada

def quick_sort_dicts(lista:list, key_ingresada: str, ascendente:bool = True)->list:
    """
    quick_sort: Realiza una clasificación rápida en una lista de diccionarios
    según una key y un orden específico. Ordena los datos que estan dentro de un diccionario
    del diccionario de la lista.

    :param lista: Una lista de diccionarios que contiene datos.
    :param key_ingresada: String que representa la key por la que se desea ordenar.
    :param ascendente: Booleano opcional para saber si el orden debe ser ascendente (True) o
    descendente (False). Por default es True

    :return: Una lista ordenada, bajo la key especificada y el orden recibido por parámetro.
    """

    lista_de = []
    lista_iz = []
    if(len(lista)<=1):
        return lista

    pivot_encontrado = False

    for elemento in lista:
        for key_elemento, valor_elemento in elemento.items():
            if key_ingresada in valor_elemento:
                if not pivot_encontrado:
                    pivot = elemento
                    pivot_encontrado = True
                else:
                    if type(valor_elemento) == type(dict()):
                        if ascendente and valor_elemento[key_ingresada] > pivot[key_elemento][key_ingresada] or \
                                not ascendente and valor_elemento[key_ingresada] < pivot[key_elemento][key_ingresada]:
                            lista_de.append(elemento)
                        else:
                            lista_iz.append(elemento)

    lista_iz = quick_sort_dicts(lista_iz, key_ingresada, ascendente)
    lista_iz.append(pivot)
    lista_de = quick_sort_dicts(lista_de, key_ingresada, ascendente)

    lista_iz.extend(lista_de)
    lista_ordenada = lista_iz
    return lista_ordenada