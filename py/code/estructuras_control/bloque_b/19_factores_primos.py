# ----------------------------------------------------------------------
# Problema 19
# ----------------------------------------------------------------------
#
# Descomponer un número en sus factores primos.
# ----------------------------------------------------------------------

numero = int(input("Número: "))

copia = numero
divisor = 2

while copia > 1:
    if copia % divisor == 0:
        print(divisor, end=" ")

    while copia % divisor == 0:  # divide cuantas veces sea posible
        copia //= divisor

    divisor += 1
