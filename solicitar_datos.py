import re
import imprimir_datos as imprimir
def solicitar_dato(dato: str) -> str:
    """
    solicitar_dato: Solicita al usuario por consola que ingrese un dato de un jugador.

    Recibe :param dato: String que hace referencia al dato que el usuario debe ingresar.

    Retorna: Un string que es el dato del jugador a buscar o -1 si el usuario se arrepiente de la búsqueda.
    """
    dato_ingresado = input(f"\nIngrese un {dato} (o ingrese '-1' para salir del submenú): ")
    return dato_ingresado

def solicitar_valor_float() -> float:
    valor_valido = False

    while not valor_valido:
        valor_ingresado = solicitar_dato('valor')
        if valor_ingresado == '-1':
            break
        valor_valido = re.search(r'^[0-9]{1,}$|^[0-9]{1,}.[0-9]{1,}$', valor_ingresado)
        valor_valido = bool(valor_valido)

    if valor_ingresado == '-1':
        print("\nIngrese una nueva opción del menú")
        return -1

    valor_ingresado = float(valor_ingresado)
    return valor_ingresado
