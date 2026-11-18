# ----------------------------------------------------------------------
# Problema 13
# ----------------------------------------------------------------------
#
# Convertir un número decimal a binario (con divisiones sucesivas).
# ----------------------------------------------------------------------

numero = int(input("Número: "))

copia = numero
binario = ""

if copia == 0:
    binario = "0"

while copia > 0:
    binario = f"{copia % 2}{binario}"
    copia //= 2

print(f"{numero} en binario es {binario}")
