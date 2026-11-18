# ----------------------------------------------------------------------
# Problema 08
# ----------------------------------------------------------------------
#
# Mostrar todas las tablas de multiplicar del 1 al 10
# en formato de cuadrícula.
# ----------------------------------------------------------------------

# Encabezado de columnas
print("    ", end="")
for j in range(1, 11):
    print(f"{j:4}", end="")
print()
print("    " + "-" * 40)

# Filas
for i in range(1, 11):
    print(f"{i:2} |", end="")

    for j in range(1, 11):
        print(f"{i * j:4}", end="")

    print()
