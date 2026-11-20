# Forma 1: con variable auxiliar
a = 10
b = 20

auxiliar = a  # guardo el valor de a
a = b         # a toma el valor de b
b = auxiliar  # b toma el valor guardado

print(a, b)   # 20 10


# Forma 2: asignación múltiple (la forma "pythónica")
a = 10
b = 20

a, b = b, a

print(a, b)   # 20 10
