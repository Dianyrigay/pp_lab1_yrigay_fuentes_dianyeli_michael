import operaciones_numericas as operacion
import re
import ordenar_datos as ordenar

def imprimir_menu() -> int:
      """
      mostrar_menu: Imprime por consola el menú de opciones, solicita al usuario que ingrese una opción
      y valida la misma.

      No recibe parámetros.

      Retorna: Un entero que es la opción ingresada si es válida, caso contrario retorna -1.
      """
      print("\n----------------------------------------------------")
      print("Menú de opciones:")
      print("1. Mostrar la lista de todos los jugadores del Dream Team.")
      print("2. Buscar jugador por índice y mostrar sus estadísticas completas.")
      print("3. Exportar archivo CSV con las estadisticas del jugador del punto 2.")
      print("4. Buscar jugador por nombre y mostrar sus logros.")
      print("5. Calcular y mostrar el promedio de puntos por partido del equipo del Dream Team ordenado por nombre de manera ascendente.")
      print("6. Buscar jugador por nombre y mostrar si es miembro del Salón de la Fama del baloncesto.")
      print("7. Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.")
      print("8. Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.")
      print("9. Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.")
      print("10. Ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.")
      print("11. Ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor.")
      print("12. Ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor.")
      print("13. ")
      print("14. ")
      print("15. ")
      print("16. ")
      print("17. ")
      print("18. ")
      print("19. ")
      print("20. ")
      print("23. ")
      print("0. Salir del programa")
      opcion = input("\nIngrese la opción deseada: ")
      print("\n----------------------------------------------------")
      opcion_valida = re.search(r'^[1-9]$|^1[0-9]$|^20$', opcion)
      if not bool(opcion_valida):
          return -1
      opcion = int(opcion)
      return opcion

def imprimir_nombre_dato(jugador: dict, key_ingresada: str) -> None:
    """
    imprimir_nombre_dato: Esta función toma un diccionario que representa a un jugador y una clave, e imprime el nombre del
    jugador y el valor asociado con la clave, o imprime el nombre del jugador y los valores asociados
    con la clave si es un diccionario o una lista.

    Recibe: :param jugador: Diccionario que representa a un jugador, con claves para su nombre y varias estadísticas o logros
            :param key_ingresada: String que representa la clave o atributo que el usuario quiere recuperar del diccionario del
                                  jugador

    :return: Si se llama a la función con una entrada no válida (una clave que no pertenece al diccionario como primer argumento o
    una clave que no existe en el diccionario), devolverá -1. Si la función se llama con éxito,
    imprimirá información sobre el nombre del jugador y los datos solicitados.
    """
    if type(jugador) != type(dict()):
        return -1

    if 'nombre' not in jugador:
        return -1

    nombre = jugador["nombre"]
    for valor_jugador in jugador.values():
        if key_ingresada in jugador:
            if type(valor_jugador) == type(str()):
                dato = jugador[key_ingresada]
        if key_ingresada in valor_jugador:
            if type(valor_jugador) == type(dict()):
                for key, valor in valor_jugador.items():
                    if key == key_ingresada:
                        dato = valor
            if type(valor_jugador) == type(list()):
                for elemento in valor_jugador:
                    if key_ingresada in elemento:
                        dato = elemento
                    dato = elemento

    if type(dato) == type(str()) or type(dato) == type(int()) or type(dato) == type(float()):
        print(nombre.ljust(20), "-", dato)
    if type(dato) == type(dict()):
        print("\nNombre: ".ljust(20), nombre)
        print("Estadísticas:")
        for key, valor in dato.items():
            print("".ljust(20),f"{key.capitalize()}: ", valor)
    if type(dato) == type(list()):
        print("\nNombre: ".ljust(20), nombre)
        print("Logros:")
        for elemento in dato:
            print("".ljust(20),f"{elemento.capitalize()}")

def calcular_imprimir_dato(lista_jugadores: list, calculo: str, key_ingresada: str) -> None:
    if calculo != 'max' and calculo != 'min':
        return -1

    dato_max_min = operacion.calcular_max_min_dato(lista_jugadores, calculo, key_ingresada)
    if dato_max_min == -1:
      return -1

    dato_capitalizado = re.sub(r'_', ' ', key_ingresada).capitalize()
    print("Nombre:".ljust(20), f"- {dato_capitalizado}:")
    imprimir_nombre_dato(dato_max_min, key_ingresada)

def ordenar_imprimir_dato(lista_jugadores: list, key_imprimir: str, key_ordenar: str)-> None:
    if not lista_jugadores:
        return -1
    lista_ordenada = ordenar.quick_sort(lista_jugadores, key_ordenar)
    dato_capitalizado = re.sub(r'_', ' ', key_imprimir).capitalize()
    print("Nombre:".ljust(20), f"- {dato_capitalizado}:")
    for jugador in lista_ordenada:
        imprimir_nombre_dato(jugador, key_imprimir)

def calcular_imprimir_jugadores_mayor_valor(lista_jugadores:list , key_ingresada: str, valor_ingresado: float) -> None:
    # lista_jugadores_mayor_valor = []
    existe_valor_mayor = False
    for jugador in lista_jugadores:
        for valor_jugador in jugador.values():
            if type(valor_jugador) == type(dict()) and key_ingresada in valor_jugador:
                if type(valor_jugador[key_ingresada]) == type(int()) or type(valor_jugador[key_ingresada]) == type(float()):
                        for key, valor in valor_jugador.items():
                            if key == key_ingresada and valor > valor_ingresado:
                                # lista_jugadores_mayor_valor.append(jugador)
                                imprimir_nombre_dato(jugador, key_ingresada)
                                existe_valor_mayor = True
    return existe_valor_mayor