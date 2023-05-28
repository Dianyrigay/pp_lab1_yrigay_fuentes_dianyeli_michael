import re
def solicitar_dato(dato: str) -> str:
    """
    solicitar_dato: Solicita al usuario que ingrese un tipo específico de datos y devuelve
    la entrada como una cadena.

    :param dato: String que representa un tipo de dato, que va a ser el solicitado al usuario.

    :return: String que son los datos introducidos por el usuario.
    """
    dato_ingresado = input(f"\nIngrese un {dato} (o ingrese '-1' para salir del submenú): ")
    return dato_ingresado

def solicitar_valor_float() -> float or -1:
    """
    solicitar_valor_float: Solicita al usuario que ingrese un valor flotante válido y lo devuelve.

    :return: Float que es valor ingresado por el usuario, sino devuelve un entero que es -1, en caso
    que el usuario no desee continuar con la operación.
    """
    valor_valido = False

    while not valor_valido:
        valor_ingresado = solicitar_dato('valor')
        if valor_ingresado == '-1':
            break
        valor_valido = re.search(r'^[0-9]{1,}$|^[0-9]{1,}\.[0-9]{1,}$', valor_ingresado)
        valor_valido = bool(valor_valido)

    if valor_ingresado == '-1':
        print("\nIngrese una nueva opción del menú")
        return -1

    valor_ingresado = float(valor_ingresado)
    return valor_ingresado
