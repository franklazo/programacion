# ----------------------------------------------------------------------
# Problema 02
# ----------------------------------------------------------------------
#
# Imprimir un triángulo rectángulo de asteriscos
# (creciente y decreciente).
# ----------------------------------------------------------------------

n = int(input("Altura: "))

# Creciente
for i in range(1, n + 1):
    for _ in range(i):  # fila i → i asteriscos
        print("*", end=" ")
    print()

print()

# Decreciente
for i in range(n, 0, -1):
    for _ in range(i):
        print("*", end=" ")
    print()
