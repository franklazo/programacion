# ----------------------------------------------------------------------
# Problema 08
# ----------------------------------------------------------------------
#
# Dados tres lados, clasificar el triángulo
# (equilátero, isósceles, escaleno)
# y verificar primero que sea un triángulo válido.
# ----------------------------------------------------------------------

a = float(input("Lado a: "))
b = float(input("Lado b: "))
c = float(input("Lado c: "))

# 1) ¿Es un triángulo válido?
if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("No forma un triángulo válido")
# 2) Clasificación
elif a == b == c:
    print("Equilátero")
elif a == b or a == c or b == c:
    print("Isósceles")
else:
    print("Escaleno")
