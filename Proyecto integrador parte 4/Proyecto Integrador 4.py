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
import readchar

def convertir_laberinto(laberinto):
    return [list(fila) for fila in laberinto.split("\n")]

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_mapa(mapa):
    for fila in mapa:
        print(''.join(fila))

def main_loop(mapa, posicion_inicial, posicion_final):
    px, py = posicion_inicial

    while (px, py) != posicion_final:
        limpiar_pantalla()
        mapa[px][py] = 'P'
        mostrar_mapa(mapa)
        mapa[px][py] = '.'

        tecla = readchar.readkey()
        if tecla == '\x1b[A' and px > 0 and mapa[px - 1][py] != '#':
            px -= 1  # Tecla de flecha hacia arriba
        elif tecla == '\x1b[B' and px < len(mapa) - 1 and mapa[px + 1][py] != '#':
            px += 1  # Tecla de flecha hacia abajo
        elif tecla == '\x1b[D' and py > 0 and mapa[px][py - 1] != '#':
            py -= 1  # Tecla de flecha hacia la izquierda
        elif tecla == '\x1b[C' and py < len(mapa[0]) - 1 and mapa[px][py + 1] != '#':
            py += 1  # Tecla de flecha hacia la derecha
    print("¡Ganaste!")

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

mapa = convertir_laberinto(laberinto)
posicion_inicial = (0, 0)
posicion_final = (len(mapa) - 1, len(mapa[0]) - 1)
main_loop(mapa, posicion_inicial, posicion_final)
