# ----------------------------------------------------------------------
# 03. Lógicos con tabla de verdad
# ----------------------------------------------------------------------
#
# Construye a mano la tabla de `AND`, `OR` y `NOT` y verifícala con
# código para todas las combinaciones de `true/false`.
# ----------------------------------------------------------------------

#  A  B    A and B  A or B  not A
# --------------------------------
#  T  T       T       T       F
#  T  F       F       T       F
#  F  T       F       T       T
#  F  F       F       F       T

a, b = True, True
print(f"{a and b}   {a or b}   {not a}")

a, b = True, False
print(f"{a and b}  {a or b}   {not a}")

a, b = False, True
print(f"{a and b}  {a or b}   {not a}")

a, b = False, False
print(f"{a and b}  {a or b}  {not a}")
