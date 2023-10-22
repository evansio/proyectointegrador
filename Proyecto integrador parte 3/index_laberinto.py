#Proyecto Integrador - Parte 3
"""En esta sección del proyecto integrador, abordaremos la manipulación de la terminal.

El objetivo es comenzar con un número inicializado en 0, y en un bucle, esperar la entrada de la tecla 'n' del teclado. Por cada vez que se presiona 'n', se borrará la terminal y se imprimirá el nuevo número, incrementándolo hasta llegar a 50.

Para llevar a cabo la operación de limpiar la terminal antes de mostrar el nuevo contenido, se ha creado una función específica. Se utiliza la instrucción os.system('cls' en sistemas Windows o 'clear' en otros sistemas) para lograr esto. Es necesario importar la biblioteca os."""
import os
from readchar import readkey

def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_numero(numero):
    print(numero)

numero = 0

while True:
    print("Presiona la tecla 'n' para aumentar el número.")
    tecla = readkey()
    
    if tecla == 'n':
        numero += 1
        limpiar_terminal()
        imprimir_numero(numero)
        
        if numero == 50:
            print("¡Has alcanzado el número 50!")
            break
    else:
        limpiar_terminal()
        print("No has presionado la tecla 'n'.")