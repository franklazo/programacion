# ----------------------------------------------------------------------
# Problema 02
# ----------------------------------------------------------------------
#
# Pedir un número dentro de un rango (por ejemplo, 1 a 10)
# y repetir hasta que sea válido.
# ----------------------------------------------------------------------

minimo, maximo = 1, 10

while True:
    texto = input(f"Ingresa un número entre {minimo} y {maximo}: ").strip()

    if texto.isdigit():
        numero = int(texto)

        if minimo <= numero <= maximo:
            break
        print("Fuera de rango.")

    else:
        print("Eso no es un número entero válido.")

print(f"Número aceptado: {numero}")
