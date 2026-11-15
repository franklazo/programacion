# ----------------------------------------------------------------------
# Problema 05
# ----------------------------------------------------------------------
#
# Juego de adivinar el número con pistas "mayor/menor"
# y conteo de intentos.
# ----------------------------------------------------------------------

import random

secreto = random.randint(1, 100)
intentos = 0
adivinado = False

print("Generé un número entre 1 y 100. ¡Intenta adivinarlo!")

while not adivinado:
    texto = input("Tu número: ").strip()

    if not texto.isdigit():
        print("Ingresa un número entero válido.")
        continue

    numero = int(texto)
    intentos += 1

    if numero < secreto:
        print("Más alto ↑")
    elif numero > secreto:
        print("Más bajo ↓")
    else:
        adivinado = True
        print(f"¡Correcto! Lo lograste en {intentos} intentos.")
