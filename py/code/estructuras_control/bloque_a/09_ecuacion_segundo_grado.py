# ----------------------------------------------------------------------
# Problema 09
# ----------------------------------------------------------------------
#
# Resolver una ecuación de segundo grado analizando el discriminante
# (dos raíces, una raíz, sin raíces reales).
# ----------------------------------------------------------------------

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if a == 0:
    print("No es cuadrática (a no puede ser 0)")
else:
    discriminante = b ** 2 - 4 * a * c

    if discriminante > 0:
        x1 = (-b + discriminante ** 0.5) / (2 * a)
        x2 = (-b - discriminante ** 0.5) / (2 * a)
        print(f"Dos raíces reales: {x1} y {x2}")
    elif discriminante == 0:
        x = -b / (2 * a)
        print(f"Una raíz doble: {x}")
    else:
        print("No tiene raíces reales")
