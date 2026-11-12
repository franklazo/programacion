# ----------------------------------------------------------------------
# 03. Intercambio de variables
# ----------------------------------------------------------------------
#
# Dadas `a = 5` y `b = 9`, intercámbialas...
# (a) con una variable auxiliar y
# (b) sin ella.
# ----------------------------------------------------------------------

a = 5
b = 9

# (a) Con variable auxiliar
aux = a
a = b
b = aux

print(a, b)  # 9 5


# (b) Sin variable auxiliar, con aritmética
a, b = 5, 9

a = a + b    # a = 14
b = a - b    # b = 14 - 9 = 5
a = a - b    # a = 14 - 5 = 9

print(a, b)  # 9 5


# (c) La forma idiomática de Python (desempaquetado de tuplas)
a, b = 5, 9
a, b = b, a

print(a, b)  # 9 5
