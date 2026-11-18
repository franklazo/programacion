# ----------------------------------------------------------------------
# Problema 05
# ----------------------------------------------------------------------
#
# Calcular la potencia `base^exp` sin usar el operador de potencia.
# ----------------------------------------------------------------------

base = int(input("Base: "))
exponente = int(input("Exponente: "))

potencia = base

for _ in range(exponente):
    potencia *= base

print(f"{base}^{exponente} = {potencia}")
