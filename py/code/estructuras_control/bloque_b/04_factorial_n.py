# ----------------------------------------------------------------------
# Problema 04
# ----------------------------------------------------------------------
#
# Calcular el factorial de N con un bucle.
# ----------------------------------------------------------------------

n = int(input("Ingresa N: "))

factorial = 1

for i in range(2, n + 1):
    factorial *= i

print(f"{n}! = {factorial}")  # 0! y 1! dan 1: el bucle no se ejecuta
