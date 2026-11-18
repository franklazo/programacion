# ----------------------------------------------------------------------
# Problema 07
# ----------------------------------------------------------------------
#
# Encontrar todos los números de tres cifras que cumplan una condición
# (por ejemplo, que sean iguales a la suma de los cubos de sus dígitos).
# ----------------------------------------------------------------------

for n in range(100, 1000):  # 0 a 999
    copia = n
    suma_cubos = 0

    while copia > 0:
        digito = copia % 10  # último dígito
        suma_cubos += digito ** 3
        copia = copia // 10  # quitar el último dígito

    if suma_cubos == n:
        print(n)
