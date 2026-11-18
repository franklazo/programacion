# ----------------------------------------------------------------------
# Problema 11
# ----------------------------------------------------------------------
#
# Invertir un número (123 → 321).
# ----------------------------------------------------------------------

numero = int(input("Número: "))

copia = numero
invertido = 0

while copia > 0:
    invertido = invertido * 10 + copia % 10
    copia //= 10

print(f"{numero} invertido es {invertido}")
# 12300 → 321 (los ceros iniciales se pierden)
