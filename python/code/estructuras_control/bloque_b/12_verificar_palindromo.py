# ----------------------------------------------------------------------
# Problema 12
# ----------------------------------------------------------------------
#
# Verificar si un número es palíndromo.
# ----------------------------------------------------------------------

numero = int(input("Número: "))

copia = numero
invertido = 0

while copia > 0:
    invertido = invertido * 10 + copia % 10
    copia //= 10

print(f"{numero} {'es' if numero == invertido else 'no es'} palíndromo")
