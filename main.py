import funciones_parcial as funcion
import menu_parcial as menu

lista_jugadores = funcion.leer_archivo('dt.json')
menu.aplicacion_jugadores(lista_jugadores)

