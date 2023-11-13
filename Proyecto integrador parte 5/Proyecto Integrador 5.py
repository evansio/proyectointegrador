import os
from readchar import readkey,key
from pydantic import BaseModel
import random

class NotFileError(Exception):
    pass

class Juego(BaseModel):
    mapa: list | None
    laberinto: str | None
    posicion_inicial: tuple | None
    posicion_final: tuple | None

    def convertir_laberinto(self,laberinto) -> None:
        self.mapa = [list(fila.strip()) for fila in self.laberinto.split("\n")]

    def limpiar_pantalla(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_mapa(self, mapa) -> None:
        for fila in self.mapa:
            print(''.join(fila))

    def main_loop(self, laberinto, posicion_inicial, posicion_final = None) -> None:
        
        
        px, py = posicion_inicial
        while (px, py) != posicion_final:
            self.limpiar_pantalla()
            self.mapa[px][py] = 'P'
            self.mostrar_mapa(self.mapa)
            self.mapa[px][py] = '.'

            tecla = readkey()
            if tecla == key.UP and px > 0 and self.mapa[px - 1][py] != '#':
                px -= 1  # Flecha arriba
            elif tecla == key.DOWN and px < len(self.mapa) - 1 and self.mapa[px + 1][py] != '#':
                px += 1  # Flecha abajo
            elif tecla == key.LEFT and py > 0 and self.mapa[px][py - 1] != '#':
                py -= 1  # Flecha izquierda
            elif tecla == key.RIGHT and py < len(self.mapa[0]) - 1 and self.mapa[px][py + 1] != '#':
                py += 1  # Flecha derecha

        # Verificar si la nueva posición es válida
        while True:
            nueva_px = px
            nueva_py = py
            tecla = readkey()
            if tecla == key.UP:
                nueva_py -= 1
            elif tecla == key.DOWN:
                nueva_py += 1
            elif tecla == key.LEFT:
                nueva_px -= 1
            elif tecla == key.RIGHT:
                nueva_px += 1
            else:
                pass

            if 0 <= nueva_px < len(self.mapa[0]) and 0 <= nueva_py < len(self.mapa) and self.mapa[nueva_py][nueva_px] != "#":
                # Actualizar la posición y restaurar la posición anterior
                px, py = nueva_px, nueva_py
            else:
                continue
            print ("¡Haz logrado salir del Laberinto, nos vemos en el siguiente módulo!")

class JuegoArchivo():
    def __init__(self):
        laberinto = self.leer_archivo()
        self.juego = Juego(posicion_inicial=(0,0),laberinto=laberinto,mapa=None,posicion_final = None)
    
    def leer_archivo(self) -> str:
        path = "C:\\Users\\thelo\\Desktop\\adaschool\\Proyecto integrador parte 5\\mapas"
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
        if os.path.exists(path):
            mapas = os.listdir(path)
            laberinto = list()
            if len(mapas) > 0:
                mapa = random.choice(mapas)
                with open(path+'/'+mapa,"r") as archivo:
                    laberinto = archivo.read()
            else:
                raise NotFileError("No hay archivos en la carpeta mapas, se cargara elmapa por defecto")
        return laberinto.strip()
    
    def iniciar_juego(self):
        self.juego.convertir_laberinto(self.juego.laberinto)
        self.juego.main_loop(self.juego.mapa,self.juego.posicion_inicial,posicion_final=(len(self.juego.mapa) - 1, len(self.juego.mapa[0]) - 1))

Jugar = JuegoArchivo()
Jugar.iniciar_juego()
