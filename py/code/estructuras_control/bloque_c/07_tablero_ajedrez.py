# ----------------------------------------------------------------------
# Problema 07
# ----------------------------------------------------------------------
#
# Imprimir un tablero de ajedrez con `#` y espacios.
# ----------------------------------------------------------------------

n = int(input("Tamaño del tablero: "))

for fila in range(n):
    for col in range(n):
        if (fila + col) % 2 == 0:
            print("  ", end="")
        else:
            print("##", end="")
    print()
