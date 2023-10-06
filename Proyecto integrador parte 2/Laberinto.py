from readchar import readkey, key

print ("Presiona una tecla. Para salir, presiona la tecla de flecha hacia arriba (UP).")

while True:
    # Lee un caracter del teclado
    tecla = readkey()

    # Verifica si la tecla es la flecha hacia arriba (UP)
    if tecla == key.UP:
        break

    # Imprime la tecla presionada
    print("Tecla presionada:", tecla)

print("Programa finalizado.")