# ----------------------------------------------------------------------
# Problema 09
# ----------------------------------------------------------------------
#
# Contar los dígitos de un número.
# ----------------------------------------------------------------------

numero = int(input("Número: "))

copia = numero
digitos = 0

if copia == 0:
    digitos = 1  # caso borde: el 0 tiene un dígito

while copia > 0:
    copia //= 10  # quita el último dígito
    digitos += 1

print(f"{numero} tiene {digitos} dígitos")
