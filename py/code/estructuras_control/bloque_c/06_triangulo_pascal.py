# ----------------------------------------------------------------------
# Problema 06
# ----------------------------------------------------------------------
#
# Imprimir el triángulo de Pascal.
# ----------------------------------------------------------------------

# Cada valor se calcula a partir del anterior de su fila
# con la fórmula del coeficiente binomial:
# C(n,k+1) = C(n,k)*(n-k)/(k+1)

n = int(input("Filas: "))

for i in range(n):
    # Espacios para centrar (cada número ocupa 4 caracteres)
    for _ in range(n - 1 - i):
        print("  ", end="")

    valor = 1                               # primer valor de cada fila
    for j in range(i + 1):
        print(f"{valor:4}", end="")         # ancho fijo de 4 caracteres
        valor = valor * (i - j) // (j + 1)  # siguiente valor de la fila

    print()
