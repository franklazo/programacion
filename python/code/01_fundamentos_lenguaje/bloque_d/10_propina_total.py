# ----------------------------------------------------------------------
# 10. Propina y total
# ----------------------------------------------------------------------
#
# Cuenta, porcentaje de propina y número de comensales; muestra cuánto
# paga cada uno.
# ----------------------------------------------------------------------

cuenta = float(input("Total de la cuenta: "))
porcentaje = float(input("Propina (%): "))
comensales = int(input("Número de comensales: "))

# Separar el cálculo en pasos con nombres claros
# vuelve el código legible y fácil de depurar.

propina = cuenta * porcentaje / 100
total = cuenta + propina
por_persona = total / comensales

print(f"Cada persona paga: {por_persona:.2f}")
