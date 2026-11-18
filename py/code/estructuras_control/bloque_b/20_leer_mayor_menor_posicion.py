# ----------------------------------------------------------------------
# Problema 20
# ----------------------------------------------------------------------
#
# Leer N números y mostrar el mayor, el menor
# y la posición de cada uno.
# ----------------------------------------------------------------------

n = int(input("Ingresa N: "))

if n > 0:
    num = int(input("Número: "))
    mayor = menor = num
    pos_mayor = pos_menor = 1

    for i in range(2, n + 1):
        num = int(input("Número: "))

        if num > mayor:
            mayor = num
            pos_mayor = i

        if num < menor:
            menor = num
            pos_menor = i

    print(f"Mayor: {mayor} (posición {pos_mayor})")
    print(f"Menor: {menor} (posición {pos_menor})")

else:
    print("No se ingresaron números")
