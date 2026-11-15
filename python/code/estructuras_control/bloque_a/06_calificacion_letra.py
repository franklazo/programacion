# ----------------------------------------------------------------------
# Problema 06
# ----------------------------------------------------------------------
#
# Calcular una calificación con letra (A, B, C, D, F)
# a partir de una nota numérica.
# ----------------------------------------------------------------------

nota = float(input("Nota (0-100): "))

if nota < 0 or nota > 100:
    print("Nota fuera de rango")
elif nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
elif nota >= 60:
    print("D")
else:
    print("F")
