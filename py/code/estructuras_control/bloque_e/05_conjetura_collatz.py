# ----------------------------------------------------------------------
# Problema 05
# ----------------------------------------------------------------------
#
# Conjetura de Collatz: aplicar la regla hasta llegar a 1
# y contar los pasos.
# ----------------------------------------------------------------------

n = int(input("Número inicial (entero positivo): "))

if n <= 0:
    print("Debe ser positivo.")

else:
    pasos = 0

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        pasos += 1

    print(f"Llegó a 1 en {pasos} pasos")
