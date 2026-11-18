# ----------------------------------------------------------------------
# Problema 04
# ----------------------------------------------------------------------
#
# Imprimir un rombo.
# ----------------------------------------------------------------------

n = int(input("Altura de la mitad superior: "))

# Mitad superior (incluye la fila más ancha)
for i in range(1, n + 1):
    for _ in range(n - i):
        print(" ", end=" ")
    for _ in range(i * 2 - 1):
        print("*", end=" ")
    print()

# Mitad inferior (empieza en n-1 para no repetir la fila central)
for i in range(n - 1, 0, -1):
    for _ in range(n - i):
        print(" ", end=" ")
    for _ in range(i * 2 - 1):
        print("*", end=" ")
    print()
