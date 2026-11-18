# ----------------------------------------------------------------------
# Problema 26
# ----------------------------------------------------------------------
#
# Contar cuántas veces aparece un carácter en una cadena.
# ----------------------------------------------------------------------

cadena = input("Texto: ")
buscado = input("Carácter buscado: ")

cuenta = 0

for car in cadena.lower():
    if car == buscado.lower():
        cuenta += 1

print(f"'{buscado}' aparece {cuenta} veces en \"{cadena}\"")
