# ----------------------------------------------------------------------
# Problema 10
# ----------------------------------------------------------------------
#
# Sumar los dígitos de un número.
# ----------------------------------------------------------------------

numero = int(input("Número: "))

copia = numero
suma = 0

while copia > 0:
    suma += copia % 10  # %10 obtiene el último dígito
    copia //= 10

print(f"La suma de los dígitos de {numero} es {suma}")
