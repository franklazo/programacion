# ----------------------------------------------------------------------
# Problema 07
# ----------------------------------------------------------------------
#
# Calcular el promedio de N números ingresados por el usuario.
# ----------------------------------------------------------------------

cantidad = int(input("Cantidad: "))

suma = 0

for i in range(1, cantidad + 1):
    numero = int(input(f"Número {i}: "))
    suma += numero

promedio = suma / cantidad

print(f"Promedio: {promedio}")
