# ----------------------------------------------------------------------
# Problema 25
# ----------------------------------------------------------------------
#
# Verificar si una palabra o frase es palíndromo
# (ignorando espacios y mayúsculas).
# ----------------------------------------------------------------------

cadena = input("Texto: ")

limpia = ""

for car in cadena.lower():
    if car != " ":
        limpia += car

es_palindromo = True
i, j = 0, len(limpia) - 1  # dos índices que se acercan desde los extremos

while i < j:
    if limpia[i] != limpia[j]:
        es_palindromo = False
        break

    i += 1
    j -= 1

print(f"\"{cadena}\" {'es' if es_palindromo else 'no es'} palíndromo")
