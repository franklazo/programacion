# ----------------------------------------------------------------------
# Problema 03
# ----------------------------------------------------------------------
#
# Dados dos números, mostrar el mayor (y detectar si son iguales).
# ----------------------------------------------------------------------

a = float(input("Primer número: "))
b = float(input("Segundo número: "))

if a > b:
    print(f"El mayor es {a}")
elif a < b:
    print(f"El mayor es {b}")
else:
    print("Son iguales")
