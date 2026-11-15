# ----------------------------------------------------------------------
# Problema 24
# ----------------------------------------------------------------------
#
# Invertir una cadena sin funciones predefinidas.
# ----------------------------------------------------------------------

cadena = input("Texto: ")

invertida = ""

for car in cadena:
    invertida = car + invertida  # cada letra nueva va al principio

print(invertida)
