# ----------------------------------------------------------------------
# Problema 03
# ----------------------------------------------------------------------
#
# Imprimir una pirámide centrada.
# ----------------------------------------------------------------------

n = int(input("Altura: "))

for i in range(1, n + 1):
    for _ in range(n - i):      # espacios a la izquierda
        print(" ", end=" ")
    for _ in range(i * 2 - 1):  # asteriscos (1, 3, 5)
        print("*", end=" ")
    print()
