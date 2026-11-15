# ----------------------------------------------------------------------
# Problema 13
# ----------------------------------------------------------------------
#
# Convertir un número del 1 al 7 en el día de la semana,
# y uno del 1 al 12 en el nombre del mes.
# ----------------------------------------------------------------------

# Número a día de la semana
n = int(input("Número (1-7): "))

match n:
    case 1: print("Lunes")
    case 2: print("Martes")
    case 3: print("Miércoles")
    case 4: print("Jueves")
    case 5: print("Viernes")
    case 6: print("Sábado")
    case 7: print("Domingo")
    case _: print("Número fuera de rango")

# Número a día de la semana
n = int(input("Número (1-12): "))

match n:
    case 1: print("Enero")
    case 2: print("Febrero")
    case 3: print("Marzo")
    case 4: print("Abril")
    case 5: print("Mayo")
    case 6: print("Junio")
    case 7: print("Julio")
    case 8: print("Agosto")
    case 9: print("Septiembre")
    case 10: print("Octubre")
    case 11: print("Noviembre")
    case 12: print("Diciembre")
    case _: print("Número fuera de rango")
