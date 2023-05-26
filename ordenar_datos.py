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