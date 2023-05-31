from funciones_parcial import *

def imprimir_menu() -> int or -1:
    """
    imprimir_menu: Imprime un menú con diferentes opciones y devuelve la opción seleccionada por el
    usuario como un número entero.

    :return: Un número entero que representa la opción seleccionada por el usuario en el menú. Si el
    usuario ingresa una opción no válida, la función devuelve -1.
    """
    print("\n----------------------------------------------------")
    print("Menú de opciones:")
    print("1. Mostrar la lista de todos los jugadores del Dream Team con Nombre y Posición.")
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
    print("13. Calcular y mostrar el jugador con la mayor cantidad de robos totales.")
    print("14. Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.")
    print("15. Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.")
    print("16. Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.")
    print("17. Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos.")
    print("18. Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.")
    print("19. Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas.")
    print("20. Ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.")
    print("23. Calcular de cada jugador cuál es su posición en cada uno de los siguientes ranking: Puntos, Rebotes, Asistencias, Robos. Exportar csv")
    print("24. Determinar la cantidad de jugadores que hay por cada posición.")
    print("25. Mostrar la lista de jugadores ordenadas por la cantidad de All-Star de forma descendente.")
    print("26. Determinar qué jugador tiene las mejores estadísticas en cada valor.")
    print("27. Determinar qué jugador tiene las mejores estadísticas de todos.")
    print("0. Salir del programa")
    opcion = input("\nIngrese la opción deseada: ")
    print("\n----------------------------------------------------")
    opcion_valida = re.search(r'^[0-9]$|^1[0-9]$|^20$|^2[3-7]$', opcion)
    if not bool(opcion_valida):
        return -1
    opcion = int(opcion)
    return opcion

def aplicacion_jugadores(lista_jugadores: list):
    """
    aplicacion_jugadores: Imprime el menú y administra datos de la lista de jugadores de
    baloncesto. Permite al usuario realizar varias operaciones con la lista.

    :param lista_jugadores: Una lista de diccionarios que contiene datos de jugadores, cada diccionario
    representa un jugador.
    """
    flag_guardar_archivo = False
    while True:

        opcion = imprimir_menu()
        opcion_valida = re.search(r'2', str(opcion))
        if bool(opcion_valida):
            flag_guardar_archivo = True
        match opcion:
            case 1:
                imprimir_jugadores_nombre_key(lista_jugadores, 'posicion')
            case 2:
                lista_data_jugador = obtener_e_imprimir_jugador_nombre_estadisticas(lista_jugadores)
                if lista_data_jugador != -1 or lista_data_jugador:
                    nombre_jugador = lista_data_jugador[0]['nombre'].lower()
                    nombre_jugador = re.sub(r" ", "_", nombre_jugador)
            case 3:
                if flag_guardar_archivo and lista_data_jugador != -1:
                    exportar_csv(f'jugador_{nombre_jugador}.csv', lista_data_jugador)
                else:
                    print("Debe haber completado la opción 2 anteriormente para poder guardar el archivo")
            case 4:
                lista_jugadores_encontrados = obtener_jugador_nombre_logros(lista_jugadores)
                imprimir_jugadores_nombre_key(lista_jugadores_encontrados, 'logros')
            case 5:
                calcular_e_imprimir_promedio_puntos_por_partido(lista_jugadores)
            case 6:
                imprimir_jugador_nombre_salon_fama(lista_jugadores)
            case 7:
                lista_dato_max = calcular_jugador_dato_max_key(lista_jugadores, 'rebotes_totales')
                imprimir_jugadores_nombre_key(lista_dato_max, 'rebotes_totales')
            case 8:
                lista_dato_max = calcular_jugador_dato_max_key(lista_jugadores, 'porcentaje_tiros_de_campo')
                imprimir_jugadores_nombre_key(lista_dato_max, 'porcentaje_tiros_de_campo')
            case 9:
                lista_dato_max = calcular_jugador_dato_max_key(lista_jugadores, 'asistencias_totales')
                imprimir_jugadores_nombre_key(lista_dato_max, 'asistencias_totales')
            case 10:
                lista_jugadores_mayor_valor = calcular_jugadores_mayor_valor_key(lista_jugadores, 'promedio_puntos_por_partido')
                imprimir_jugadores_nombre_key(lista_jugadores_mayor_valor, 'promedio_puntos_por_partido')
            case 11:
                lista_jugadores_mayor_valor = calcular_jugadores_mayor_valor_key(lista_jugadores, 'promedio_rebotes_por_partido')
                imprimir_jugadores_nombre_key(lista_jugadores_mayor_valor, 'promedio_rebotes_por_partido')
            case 12:
                lista_jugadores_mayor_valor = calcular_jugadores_mayor_valor_key(lista_jugadores, 'promedio_asistencias_por_partido')
                imprimir_jugadores_nombre_key(lista_jugadores_mayor_valor, 'promedio_asistencias_por_partido')
            case 13:
                lista_dato_max = calcular_jugador_dato_max_key(lista_jugadores, 'robos_totales')
                imprimir_jugadores_nombre_key(lista_dato_max, 'robos_totales')
            case 14:
                lista_dato_max = calcular_jugador_dato_max_key(lista_jugadores, 'bloqueos_totales')
                imprimir_jugadores_nombre_key(lista_dato_max, 'bloqueos_totales')
            case 15:
                lista_jugadores_mayor_valor = calcular_jugadores_mayor_valor_key(lista_jugadores, 'porcentaje_tiros_libres')
                imprimir_jugadores_nombre_key(lista_jugadores_mayor_valor, 'porcentaje_tiros_libres')
            case 16:
                calcular_e_imprimir_promedio_puntos_por_partido_excluyendo_min(lista_jugadores)
            case 17:
                lista_jugador_mayor_logros = calcular_jugador_mayor_logros_obtenidos(lista_jugadores)
                imprimir_jugadores_nombre_key(lista_jugador_mayor_logros,'logros')
            case 18:
                lista_jugadores_mayor_valor = calcular_jugadores_mayor_valor_key(lista_jugadores, 'porcentaje_tiros_triples')
                imprimir_jugadores_nombre_key(lista_jugadores_mayor_valor, 'porcentaje_tiros_triples')
            case 19:
                lista_dato_max = calcular_jugador_dato_max_key(lista_jugadores, 'temporadas')
                imprimir_jugadores_nombre_key(lista_dato_max, 'temporadas')
            case 20:
                calcular_imprimir_jugadores_tiros_campo_mayor_valor(lista_jugadores)
            case 23:
                lista_ranking_jugadores = calcular_obtener_posicion_ranking_jugadores(lista_jugadores)
                exportar_csv('posicion_ranking_jugadores.csv', lista_ranking_jugadores)
            case 24:
                dict_posicion_cantidad = calcular_cantidad_jugadores_por_posicion(lista_jugadores)
                for key, valor in dict_posicion_cantidad.items():
                    imprimir.imprimir_datos_tabla([key, str(valor)], '20')
            case 25:
                lista_jugadores_all_star = obtener_jugadores_cantidad_all_star(lista_jugadores)
                for jugador in lista_jugadores_all_star:
                    imprimir.imprimir_datos_tabla([jugador["nombre"], jugador["logros"]], '30')
            case 26:
                jugadores_mejores_estadisticas = obtener_mayores_estadisticas_por_valor(lista_jugadores)
            case 27:
                obtener_jugador_mejores_estadisticas(lista_jugadores)
            case 0:
                break
            case _:
                print("Opción no válida")
        limpiar_consola()