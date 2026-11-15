# ----------------------------------------------------------------------
# 05. Constantes
# ----------------------------------------------------------------------
#
# Define el valor de π y el IGV como constantes y úsalos en un cálculo,
# sin repetir el número en el código.
# ----------------------------------------------------------------------

import math

# Por convención, las constantes van en MAYÚSCULAS
PI = 3.14159
IGV = 0.18

radio = 5
area = PI * radio ** 2
print(f"Área del círculo: {area:.2f}")  # 78.54

precio = 100
precio_final = 100 * (1 + IGV)
print(f"Precio con IGV: {precio_final:.2f}")  # 118.00

# Python ya trae π con más precisión
print(math.pi)   # 3.141592653589793
