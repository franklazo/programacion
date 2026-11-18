# ----------------------------------------------------------------------
# Problema 17
# ----------------------------------------------------------------------
#
# Mostrar la secuencia de Fibonacci hasta el término N.
# ----------------------------------------------------------------------

n = int(input("Ingresa N: "))

anterior, actual = 0, 1

for _ in range(n):
    print(anterior, end=" ")
    anterior, actual = actual, anterior + actual
