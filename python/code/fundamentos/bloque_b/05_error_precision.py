# ----------------------------------------------------------------------
# 05. Error de precisión
# ----------------------------------------------------------------------
#
# Calcula `0.1 + 0.2` y explica por qué no da exactamente `0.3`.
# (Representación binaria de flotantes.)
# ----------------------------------------------------------------------

import math
from decimal import Decimal

print(0.1 + 0.2)         # 0.30000000000000004
print(0.1 + 0.2 == 0.3)  # False

# Los números se guardan en binario y así como 1/3 no es exacto
# en decimal, los decimales no son exactos en binario,
# por ello se guardan de forma aproximada.

# Manejo de decimales:

# 1. Comparar con tolerancia
print(math.isclose(0.1 + 0.2, 0.3))          # True

# 2. Redondear al mostrar o comparar
print(round(0.1 + 0.2, 2) == 0.3)            # True

# 3. Decimal para precisión exacta (dinero)
print(Decimal("0.1") + Decimal("0.2"))       # 0.3
