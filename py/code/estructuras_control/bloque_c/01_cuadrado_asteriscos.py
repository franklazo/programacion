# ----------------------------------------------------------------------
# Problema 01
# ----------------------------------------------------------------------
#
# Imprimir un cuadrado de asteriscos de N×N.
# ----------------------------------------------------------------------

n = int(input("Tamaño: "))

for fila in range(n):
    for col in range(n):
        print("*", end=" ")  # end=" " evita el salto de línea
    print()                  # salto de línea al terminar la fila
