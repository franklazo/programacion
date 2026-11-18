# ----------------------------------------------------------------------
# Problema 12
# ----------------------------------------------------------------------
#
# Piedra, papel o tijera:
# dadas las elecciones de dos jugadores, decidir el ganador.
# ----------------------------------------------------------------------

j1 = input("Jugador 1 (piedra/papel/tijera): ").strip().lower()
j2 = input("Jugador 2 (piedra/papel/tijera): ").strip().lower()

opciones = ("piedra", "papel", "tijera")

if j1 not in opciones or j2 not in opciones:
    print("Opción inválida")
elif j1 == j2:
    print("Empate")
elif (j1 == "piedra" and j2 == "tijera") or \
     (j1 == "papel" and j2 == "piedra") or \
     (j1 == "tijera" and j2 == "papel"):
    print("Gana el jugador 1")
else:
    print("Gana el jugador 2")
