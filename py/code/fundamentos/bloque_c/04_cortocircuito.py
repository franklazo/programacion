# ----------------------------------------------------------------------
# 04. Cortocircuito
# ----------------------------------------------------------------------
#
# Razona por qué `false AND (1 / 0 > 0)` no produce error en la mayoría
# de lenguajes.
# ----------------------------------------------------------------------

print(False and (1 / 0 > 0))   # False  → no da error
print(True or (1 / 0 > 0))     # True   → no da error

# print(True and (1 / 0 > 0))  # ZeroDivisionError
# print(False or (1 / 0 > 0))  # ZeroDivisionError

# Python evalúa de izquierda a derecha y se
# detiene cuando el resultado ya es seguro.
