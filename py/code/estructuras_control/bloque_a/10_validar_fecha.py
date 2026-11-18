# ----------------------------------------------------------------------
# Problema 10
# ----------------------------------------------------------------------
#
# Validar una fecha (día, mes, año),
# considerando los días de cada mes y los años bisiestos.
# ----------------------------------------------------------------------

dia = int(input("Día: "))
mes = int(input("Mes: "))
anio = int(input("Año: "))

es_bisiesto = (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0

if anio < 1 or mes < 1 or mes > 12 or dia < 1:
    valida = False
else:
    if mes in (1, 3, 5, 7, 8, 10, 12):
        max_dias = 31
    elif mes in (4, 6, 9, 11):
        max_dias = 30
    else:  # febrero
        max_dias = 29 if es_bisiesto else 28

    valida = dia <= max_dias

print("Fecha válida" if valida else "Fecha inválida")
