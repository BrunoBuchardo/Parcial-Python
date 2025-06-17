def ingresar_entero(mensaje, minimo, maximo):
    """
    Solicita al usuario que ingrese un número entero dentro de un rango determinado.

    Parámetros:
        mensaje (str): Mensaje mostrado al usuario.
        minimo (int): Valor mínimo aceptado.
        maximo (int): Valor máximo aceptado.

    Retorna:
        int: Número ingresado por el usuario que cumple con la validación.
    """
    while True:
        valor = input(mensaje)
        if es_entero(valor):
            valor = convertir_entero(valor)
            if minimo <= valor <= maximo:
                return valor
        print(f"Ingresá un número entre {minimo} y {maximo}.")

def es_entero(cadena):
    """
    Verifica si una cadena representa un número entero válido (positivo o negativo).

    Parámetros:
        cadena (str): Cadena a evaluar.

    Retorna:
        bool: True si es un entero válido, False si no lo es.
    """
    digitos = "0123456789"
    if cadena == "":
        return False
    if cadena[0] == "-":
        cadena = cadena[1:]
    for caracter in cadena:
        if caracter not in digitos:
            return False
    return True

def convertir_entero(cadena):
    """
    Convierte una cadena numérica en un número entero sin usar la función int().

    Parámetros:
        cadena (str): Cadena que representa un número entero.

    Retorna:
        int: Número entero resultante de la conversión.
    """
    negativo = False
    if cadena[0] == "-":
        negativo = True
        cadena = cadena[1:]
    numero = 0
    for caracter in cadena:
        numero = numero * 10 + (ord(caracter) - ord("0"))
    if negativo:
        numero = -numero
    return numero

def ingresar_nombre(mensaje):
    """
    Solicita al usuario ingresar un nombre válido (mínimo 3 letras, solo letras y espacios).

    Parámetros:
        mensaje (str): Mensaje que se muestra al usuario.

    Retorna:
        str: Nombre ingresado que cumple con la validación.
    """
    while True:
        nombre = input(mensaje)
        if validar_nombre(nombre):
            return nombre
        print("Ingresá un nombre válido (solo letras y espacios, mínimo 3 caracteres).")

def validar_nombre(nombre):
    """
    Valida si un nombre contiene al menos 3 caracteres, y solo letras o espacios.

    Parámetros:
        nombre (str): Nombre a validar.

    Retorna:
        bool: True si es un nombre válido, False si no.
    """
    if contar_caracteres(nombre) < 3:
        return False
    for caracter in nombre:
        if not (es_letra(caracter) or caracter == " "):
            return False
    return True

def contar_caracteres(cadena):
    """
    Cuenta cuántos caracteres hay en una cadena.

    Parámetros:
        cadena (str): Cadena a contar.

    Retorna:
        int: Número de caracteres.
    """
    contador = 0
    for _ in cadena:
        contador += 1
    return contador

def es_letra(caracter):
    """
    Verifica si un carácter es una letra (mayúscula o minúscula).

    Parámetros:
        caracter (str): Carácter a verificar.

    Retorna:
        bool: True si es una letra, False si no lo es.
    """
    return ("A" <= caracter <= "Z") or ("a" <= caracter <= "z")
