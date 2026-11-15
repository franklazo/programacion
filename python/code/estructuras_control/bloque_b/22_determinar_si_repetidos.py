# ----------------------------------------------------------------------
# Problema 22
# ----------------------------------------------------------------------
#
# Determinar si en una serie de números
# hay alguno repetido consecutivamente (uso de bandera).
# ----------------------------------------------------------------------

num = int(input("Número (0 para terminar): "))

hay_repetido = False
bandera = num

while num != 0:
    num = int(input("Número (0 para terminar): "))

    if num == bandera:
        hay_repetido = True

    bandera = num

print(f"{'Hay' if hay_repetido else 'No hay'} números repetidos consecutivamente")
