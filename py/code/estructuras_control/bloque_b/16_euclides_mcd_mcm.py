# ----------------------------------------------------------------------
# Problema 16
# ----------------------------------------------------------------------
#
# Calcular el máximo común divisor (algoritmo de Euclides)
# y el mínimo común múltiplo.
# ----------------------------------------------------------------------

a = int(input("m: "))
b = int(input("n: "))

x, y = a, b

while y != 0:
    x, y = y, x % y  # Euclides: (a, b) → (b, a mod b)

mcd = x
mcm = a * b // mcd

print(f"MCD({a}, {b}): {mcd}")
print(f"MCM({a}, {b}): {mcm}")
