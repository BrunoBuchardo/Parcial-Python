import os
from Inputs import *
from Funciones import *

cantidad_participantes = 5
cantidad_jurados = 3

def cargar_nombres(matriz):
    """
    Carga los nombres de los participantes en la matriz.

    Parámetros:
        matriz (list[list]): Matriz donde se almacenan los nombres y puntajes.
                             La primera columna de cada fila corresponde al nombre del participante.

    Retorna:
        None
    """
    for i in range(len(matriz)):
        matriz[i][0] = ingresar_nombre(f"Ingresá el nombre del participante {i + 1}: ")

def cargar_puntajes(matriz):
    """
    Carga los puntajes de cada jurado para todos los participantes.

    Parámetros:
        matriz (list[list]): Matriz con los datos de los participantes.
                             Las columnas 1 a 3 de cada fila se utilizan para los puntajes de los jurados.

    Retorna:
        None
    """
    for i in range(len(matriz)):
        print(f"Participante: {matriz[i][0]}")
        for j in range(1, cantidad_jurados + 1):
            matriz[i][j] = ingresar_entero(f"Puntaje jurado {j}: ", 1, 10)

def main():
    matriz = crear_matriz(cantidad_participantes, cantidad_jurados + 1)
    nombres_cargados = False
    puntajes_cargados = False

    while True:
        print("\n--- MENÚ DE COMPETENCIA DE BAILE ---")
        print("1. Cargar nombres")
        print("2. Cargar puntajes")
        print("3. Mostrar puntuaciones")
        print("4. Promedio > 4")
        print("5. Promedio > 7")
        print("6. Promedio por jurado")
        print("7. Jurado más estricto")
        print("8. Buscar participante")
        print("9. Top 3")
        print("10. Orden alfabético")
        print("11. Mostrar ganador")
        print("12. Desempatar")
        print("0. Salir")

        opcion = ingresar_entero("Elegí una opción: ", 0, 12)

        if opcion == 0:
            break
        elif opcion == 1:
            cargar_nombres(matriz)
            nombres_cargados = True
            print("NOMBRES CARGADOS CORRECTAMENTE")
        elif opcion == 2 and nombres_cargados:
            cargar_puntajes(matriz)
            puntajes_cargados = True
            print("PUNTAJES CARGADOS CORRECTAMENTE")
        elif not nombres_cargados or not puntajes_cargados:
            print("Primero debés cargar los nombres y puntajes.")
        elif opcion == 3:
            mostrar_participantes(matriz)
        elif opcion == 4:
            lista = filtrar_por_promedio(matriz, 4)
            if len(lista) == 0:
                print("No hay participantes con promedio mayor a 4.")
            else:
                mostrar_participantes(lista)
        elif opcion == 5:
            lista = filtrar_por_promedio(matriz, 7)
            if len(lista) == 0:
                print("No hay participantes con promedio mayor a 7.")
            else:
                mostrar_participantes(lista)
        elif opcion == 6:
            promedios = calcular_promedios_jurado(matriz)
            for i in range(len(promedios)):
                print(f"Promedio del Jurado {i+1} = {promedios[i]}")
        elif opcion == 7:
            promedios = calcular_promedios_jurado(matriz)
            estrictos = jurado_mas_estricto(promedios)
            print("Jurado(s) más estricto(s):", estrictos)
        elif opcion == 8:
            nombre = ingresar_nombre("Ingresá el nombre a buscar: ")
            resultado = buscar_participante(matriz, nombre)
            if resultado is None:
                print("Participante no encontrado.")
            else:
                mostrar_participantes([resultado])
        elif opcion == 9:
            top = ordenar_top_3(matriz)
            print("--- TOP 3 ---")
            mostrar_participantes(top)
        elif opcion == 10:
            ordenados = ordenar_alfabeticamente(matriz)
            mostrar_participantes(ordenados)
        elif opcion == 11:
            ganadores = determinar_ganadores(matriz)
            if len(ganadores) == 1:
                print("Ganador:", ganadores[0][0])
            else:
                print("Hay empate entre:")
                mostrar_participantes(ganadores)
        elif opcion == 12:
            ganadores = determinar_ganadores(matriz)
            if len(ganadores) == 1:
                print("No hay empate.")
            else:
                elegido = elegir_aleatorio(ganadores)
                print("Ganador por desempate:", elegido[0])

    input("Toque cualquier boton para continuar...")
    os.system("cls")
main()
