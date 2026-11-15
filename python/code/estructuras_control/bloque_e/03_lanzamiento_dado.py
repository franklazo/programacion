# ----------------------------------------------------------------------
# Problema 03
# ----------------------------------------------------------------------
#
# Simular lanzamientos de un dado N veces
# y contar cuántas veces salió cada cara.
# ----------------------------------------------------------------------

import random

n = int(input("¿Cuántos lanzamientos? "))

c1 = c2 = c3 = c4 = c5 = c6 = 0

for _ in range(n):
    dado = random.randint(1, 6)

    if dado == 1:
        c1 += 1
    elif dado == 2:
        c2 += 1
    elif dado == 3:
        c3 += 1
    elif dado == 4:
        c4 += 1
    elif dado == 5:
        c5 += 1
    else:
        c6 += 1

print(f"1: {c1}  2: {c2}  3: {c3}  4: {c4}  5: {c5}  6: {c6}")
