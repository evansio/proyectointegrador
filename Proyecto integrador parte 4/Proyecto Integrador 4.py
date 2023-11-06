'''
Proyecto integrador parte 4

    Implementar una función que reciba el mapa de un laberinto en forma de cadena, y lo convierta a matriz de caracteres.
        Utiliza el siguiente mapa:

        laberinto = """..###################
        ....#...............#
        #.#.#####.#########.#
        #.#...........#.#.#.#
        #.#####.#.###.#.#.#.#
        #...#.#.#.#.....#...#
        #.#.#.#######.#.#####
        #.#...#.....#.#...#.#
        #####.#####.#.#.###.#
        #.#.#.#.......#...#.#
        #.#.#.#######.#####.#
        #...#...#...#.#.#...#
        ###.#.#####.#.#.###.#
        #.#...#.......#.....#
        #.#.#.###.#.#.###.#.#
        #...#.#...#.#.....#.#
        ###.#######.###.###.#
        #.#.#.#.#.#...#.#...#
        #.#.#.#.#.#.#.#.#.#.#
        #.....#.....#.#.#.#.#
        ###################.."""

Los puntos inicial y final deben ser dados al crear el juego, usar las coordenadas (0,0) para el inicio y (len(mapa)-1, len(mapa[0])-1) para el final.
Recuerdo: Para separar por filas usar split("\n") y para convertir una cadena a una lista de caracteres usar list(cadena).

Escribir una función que limpie la pantalla y muestre la matriz (recibe el mapa en forma de matriz)
Implementar el main loop en una función (recibe el mapa en forma de matriz)

recibir: mapa List[List[str]], posicion inicial Tuple[int, int], posicion final Tuple[int, int].
definir dos variavles px y py que contienen las coordenadas del jugador, iniciar como los valores de la posición incial
procesar mientras (px, py) no coincida con la coordenada final.
asignar el caracter P en el mapa a las coordenadas (px, py) en todo momento.
leer del teclado las teclas de flechas, antes de actualizar la posición, verificar si esta posición tentativa:
No se sale del mapa
No es una pared
Si la nueva posición es válida, actualizar (px, py), poner el caracter P en esta nueva coordenada y restaurar la anterior a .
mostrar


'''

import os
import msvcrt

def convertir_mapa_a_matriz(laberinto):
    # Dividir el laberinto en filas
    filas = laberinto.split("\n")
    matriz = [list(fila) for fila in filas]
    return matriz

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_loop(mapa, posicion_inicial, posicion_final):
    px, py = posicion_inicial
    while (px, py) != posicion_final:
        mapa[py][px] = "P"
        mostrar_mapa(mapa)
        
        # Leer la tecla presionada
        key = msvcrt.getch().decode('utf-8')
        
        # Calcula la nueva posición tentativa
        nueva_px, nueva_py = px, py
        if key == "w":
            nueva_py -= 1
        elif key == "s":
            nueva_py += 1
        elif key == "a":
            nueva_px -= 1
        elif key == "d":
            nueva_px += 1
        
        # Verificar si la nueva posición es válida
        if 0 <= nueva_px < len(mapa[0]) and 0 <= nueva_py < len(mapa) and mapa[nueva_py][nueva_px] != "#":
            # Actualizar la posición y restaurar la posición anterior
            mapa[py][px] = "."
            px, py = nueva_px, nueva_py
        else:
            continue

def mostrar_mapa(mapa):
    limpiar_pantalla()
    for fila in mapa:
        print("".join(fila))

laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

mapa = convertir_mapa_a_matriz(laberinto)
posicion_inicial = (0, 0)
posicion_final = (len(mapa[0]) - 1, len(mapa) - 1)

main_loop(mapa, posicion_inicial, posicion_final)
