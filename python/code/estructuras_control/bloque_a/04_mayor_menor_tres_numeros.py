# ----------------------------------------------------------------------
# Problema 04
# ----------------------------------------------------------------------
#
# Dados tres números, mostrar el mayor y el menor
# sin usar funciones predefinidas.
# ----------------------------------------------------------------------

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

mayor = a
menor = a

if b > mayor:
    mayor = b
if c > mayor:
    mayor = c

if b < menor:
    menor = b
if c < menor:
    menor = c

print(f"Mayor: {mayor} | Menor: {menor}")
