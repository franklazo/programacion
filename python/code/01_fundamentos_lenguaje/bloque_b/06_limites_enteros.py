# ----------------------------------------------------------------------
# 06. Límites de los enteros
# ----------------------------------------------------------------------
#
# Investiga el valor máximo de un entero en tu lenguaje y qué ocurre al
# superarlo (desbordamiento u otro comportamiento).
# ----------------------------------------------------------------------

import sys

# En Python los enteros no tienen límite fijo,
# crecen según la memoria disponible.

print(2 ** 100)   # 1267650600228229401496703205376
print(2 ** 1000)  # un número de 302 dígitos, sin problema

# Los decimales (float) sí tienen un límite.

print(sys.float_info.max)  # 1.7976931348623157e+308
print(1e308 * 10)          # inf  → "infinito", no error
