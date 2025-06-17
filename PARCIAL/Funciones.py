def crear_matriz(filas:int, columnas:int) -> list:
    """
    Crea una matriz con la cantidad de filas y columnas dadas.
    La primera columna se reserva para los nombres (None), el resto se inicializa en 0.

    Parámetros:
        filas (int): Número de participantes.
        columnas (int): Número total de columnas (1 para nombre + jurados).

    Retorna:
        list[list]: Matriz inicializada.
    """
    matriz = []
    for _ in range(filas):
        fila = [None] + [0] * (columnas - 1)
        matriz = matriz + [fila]
    return matriz

def calcular_promedio(puntajes):
    """
    Calcula el promedio entero de una lista de puntajes.

    Parámetros:
        puntajes (list[int]): Lista de puntajes.

    Retorna:
        int: Promedio entero de los puntajes.
    """
    total = 0
    for valor in puntajes:
        total += valor
    return total // len(puntajes)

def mostrar_participantes(matriz):
    """
    Muestra por pantalla los nombres, puntajes y promedios de los participantes.

    Parámetros:
        matriz (list[list]): Matriz con nombres y puntajes.
    """
    for fila in matriz:
        promedio = calcular_promedio(fila[1:])
        print(f"NOMBRE PARTICIPANTE: {fila[0]}")
        for j in range(1, len(fila)):
            print(f"PUNTAJE JURADO {j}: {fila[j]}")
        print(f"PUNTAJE PROMEDIO: {promedio:.2f}/10")
        print("-----------------------------------")

def filtrar_por_promedio(matriz, minimo):
    """
    Filtra los participantes con promedio mayor a un valor mínimo.

    Parámetros:
        matriz (list[list]): Matriz con datos.
        minimo (int): Promedio mínimo deseado.

    Retorna:
        list[list]: Participantes que cumplen la condición.
    """
    filtrados = []
    for fila in matriz:
        if calcular_promedio(fila[1:]) > minimo:
            filtrados = filtrados + [fila]
    return filtrados

def calcular_promedios_jurado(matriz):
    """
    Calcula el promedio de puntajes por jurado.

    Parámetros:
        matriz (list[list]): Matriz con puntajes.

    Retorna:
        list[int]: Promedio de cada jurado.
    """
    cantidad = len(matriz)
    columnas = len(matriz[0]) - 1
    suma_jurados = [0] * columnas
    for fila in matriz:
        for j in range(columnas):
            suma_jurados[j] += fila[j + 1]
    promedios = [suma_jurados[i] // cantidad for i in range(columnas)]
    return promedios

def jurado_mas_estricto(promedios):
    """
    Determina qué jurado(s) tienen el promedio más bajo.

    Parámetros:
        promedios (list[int]): Promedios por jurado.

    Retorna:
        list[int]: Lista con número(s) de jurado(s) más estricto(s), empezando desde 1.
    """
    minimo = promedios[0]
    posiciones = [1]
    for i in range(1, len(promedios)):
        if promedios[i] < minimo:
            minimo = promedios[i]
            posiciones = [i + 1]
        elif promedios[i] == minimo:
            posiciones = posiciones + [i + 1]
    return posiciones

def buscar_participante(matriz, nombre):
    """
    Busca un participante por su nombre exacto.

    Parámetros:
        matriz (list[list]): Matriz con datos.
        nombre (str): Nombre a buscar.

    Retorna:
        list or None: Fila del participante o None si no se encuentra.
    """
    for fila in matriz:
        if fila[0] == nombre:
            return fila
    return None

def ordenar_top_3(matriz):
    """
    Ordena la matriz por promedio descendente y devuelve los 3 mejores.

    Parámetros:
        matriz (list[list]): Datos de los participantes.

    Retorna:
        list[list]: Lista con los tres mejores participantes.
    """
    copia = [fila for fila in matriz]
    for i in range(len(copia) - 1):
        for j in range(len(copia) - i - 1):
            if calcular_promedio(copia[j][1:]) < calcular_promedio(copia[j + 1][1:]):
                auxiliar = copia[j]
                copia[j] = copia[j + 1]
                copia[j + 1] = auxiliar
    return [copia[0], copia[1], copia[2]]

def ordenar_alfabeticamente(matriz):
    """
    Ordena la matriz alfabéticamente por nombre.

    Parámetros:
        matriz (list[list]): Matriz con datos.

    Retorna:
        list[list]: Copia ordenada alfabéticamente.
    """
    copia = [fila for fila in matriz]
    for i in range(len(copia) - 1):
        for j in range(len(copia) - i - 1):
            if copia[j][0] > copia[j + 1][0]:
                auxiliar = copia[j]
                copia[j] = copia[j + 1]
                copia[j + 1] = auxiliar
    return copia

def determinar_ganadores(matriz):
    """
    Determina el/los participante/s con mayor promedio.

    Parámetros:
        matriz (list[list]): Datos de los participantes.

    Retorna:
        list[list]: Lista de ganadores (puede haber empate).
    """
    maximo = calcular_promedio(matriz[0][1:])
    ganadores = [matriz[0]]
    for i in range(1, len(matriz)):
        promedio_actual = calcular_promedio(matriz[i][1:])
        if promedio_actual > maximo:
            maximo = promedio_actual
            ganadores = [matriz[i]]
        elif promedio_actual == maximo:
            ganadores = ganadores + [matriz[i]]
    return ganadores

def elegir_aleatorio(lista):
    """
    Realiza un desempate aleatorio basado en la suma de valores ASCII de los nombres.

    Parámetros:
        lista (list[list]): Lista de participantes empatados.

    Retorna:
        list: Participante seleccionado.
    """
    total = 0
    for fila in lista:
        nombre = fila[0]
        for caracter in nombre:
            total += ord(caracter)
    indice = total % len(lista)
    return lista[indice]
