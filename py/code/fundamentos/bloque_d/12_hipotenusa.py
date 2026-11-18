# ----------------------------------------------------------------------
# 12. Hipotenusa
# ----------------------------------------------------------------------
#
# Teorema de Pitágoras con entrada del usuario (necesitas raíz
# cuadrada: practica importar una función de la librería estándar).
# ----------------------------------------------------------------------

import math

cateto_a = float(input("Cateto a: "))
cateto_b = float(input("Cateto b: "))

hipotenusa = math.sqrt(cateto_a ** 2 + cateto_b ** 2)

# Solución alternativa
# hipotenusa = math.hypot(cateto_a, cateto_b)

print(f"La hipotenusa mide: {hipotenusa:.2f}")
