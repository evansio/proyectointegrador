import os
from readchar import readkey, key
from pydantic import BaseModel
import random

class NotFileError(Exception):
    pass

class Juego(BaseModel):
    mapa: list | None
    posicion_inicial: tuple | None
    posicion_final: tuple | None

    def convertir_laberinto(self, laberinto):
        self.mapa = [list(fila) for fila in laberinto.split("\n")]

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_mapa(self):
        for fila in self.mapa:
            print(''.join(fila))

    def main_loop(self):
        px, py = self.posicion_inicial

        while (px, py) != self.posicion_final:
            self.limpiar_pantalla()
            self.mapa[px][py] = 'P'
            self.mostrar_mapa()
            self.mapa[px][py] = '.'

            tecla = readkey()
            nueva_px, nueva_py = px, py

            if tecla == key.UP and py > 0 and self.mapa[py - 1][px] != '#':
                nueva_py -= 1
            elif tecla == key.DOWN and py < len(self.mapa) - 1 and self.mapa[py + 1][px] != '#':
                nueva_py += 1
            elif tecla == key.LEFT and px > 0 and self.mapa[py][px - 1] != '#':
                nueva_px -= 1
            elif tecla == key.RIGHT and px < len(self.mapa[0]) - 1 and self.mapa[py][px + 1] != '#':
                nueva_px += 1

            if 0 <= nueva_px < len(self.mapa[0]) and 0 <= nueva_py < len(self.mapa) and self.mapa[nueva_py][nueva_px] != "#":
                px, py = nueva_px, nueva_py
            else:
                continue

        print("¡Ganaste!")

class JuegoArchivo:
    def __init__(self, path_mapas):
        self.path_mapas = path_mapas
        self.juego = Juego()

    def leer_archivo(self):
        laberinto = ""
        if os.path.exists(self.path_mapas):
            mapas = os.listdir(self.path_mapas)
            if len(mapas) > 0:
                mapa_elegido = random.choice(mapas)
                with open(os.path.join(self.path_mapas, mapa_elegido), "r") as archivo:
                    laberinto = archivo.read()
            else:
                raise NotFileError("No hay archivos en la carpeta mapas, se cargará el mapa por defecto")
        return laberinto

    def iniciar_juego(self):
        self.juego.posicion_inicial = (0, 0)
        self.juego.posicion_final = (0, 0)
        self.juego.convertir_laberinto(self.leer_archivo())
        self.juego.main_loop()

if __name__ == "__main__":
    juego_archivo = JuegoArchivo(path_mapas="C:\\Users\\thelo\\Desktop\\adaschool\\Proyecto integrador parte 5\\mapas")
    juego_archivo.iniciar_juego()
