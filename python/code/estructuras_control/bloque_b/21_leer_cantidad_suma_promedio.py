# ----------------------------------------------------------------------
# Problema 21
# ----------------------------------------------------------------------
#
# Leer números hasta que el usuario ingrese 0
# y mostrar cuántos fueron, su suma y su promedio.
# ----------------------------------------------------------------------

cantidad = 0
suma = 0

num = int(input("Número (0 para terminar): "))

while num != 0:
    cantidad += 1
    suma += num

    num = int(input("Número (0 para terminar): "))

if cantidad > 0:
    promedio = suma / cantidad
    print(f"Cantidad: {cantidad}, Suma: {suma}, Promedio: {promedio:.2f}")
else:
    print("No se ingresó ningún número")
