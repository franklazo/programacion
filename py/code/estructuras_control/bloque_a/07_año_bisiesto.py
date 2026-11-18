# ----------------------------------------------------------------------
# Problema 07
# ----------------------------------------------------------------------
#
# Determinar si un año es bisiesto
# (divisible entre 4, pero no entre 100, salvo que lo sea entre 400).
# ----------------------------------------------------------------------

anio = int(input("Año: "))

if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print("Bisiesto")
else:
    print("No bisiesto")
