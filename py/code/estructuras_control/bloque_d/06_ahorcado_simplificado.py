# ----------------------------------------------------------------------
# Problema 06
# ----------------------------------------------------------------------
#
# Juego del ahorcado simplificado.
# ----------------------------------------------------------------------

import random

palabras = ["python", "bucle", "variable", "funcion", "algoritmo"]
palabra = random.choice(palabras)

adivinadas = ""
vidas = 6

while vidas > 0:
    # Construir la palabra con guiones
    mostrado = ""

    for letra in palabra:
        if letra in adivinadas:
            mostrado += letra + " "
        else:
            mostrado += "_ "

    print(f"\n{mostrado}    (vidas: {vidas})")

    # ¿Ganó?
    if "_" not in mostrado:
        print("¡Ganaste!")
        break

    entrada = input("Letra: ").lower().strip()

    if len(entrada) != 1 or not entrada.isalpha():
        print("Ingresa una sola letra.")
        continue

    if entrada in adivinadas:
        print("Ya probaste esa letra.")
        continue

    adivinadas += entrada

    if entrada not in palabra:
        vidas -= 1
        print("Esa letra no está.")
else:
    print(f"\nPerdiste. La palabra era: {palabra}")
