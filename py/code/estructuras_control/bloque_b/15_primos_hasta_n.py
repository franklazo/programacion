# ----------------------------------------------------------------------
# Problema 15
# ----------------------------------------------------------------------
#
# Listar todos los primos hasta N
# (y luego optimizar: ¿hasta dónde basta probar divisores?).
# ----------------------------------------------------------------------

n = int(input("Ingresa N: "))

for candidato in range(2, n + 1):
    i = 2

    while i * i <= candidato:
        if candidato % i == 0:
            break
        i += 1
    else:
        print(candidato, end=" ")
