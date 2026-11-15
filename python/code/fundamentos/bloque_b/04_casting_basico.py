# ----------------------------------------------------------------------
# 04. Casting básico
# ----------------------------------------------------------------------
#
# Convierte `"123"` a entero, `3.99` a entero (¿trunca o redondea?),
# y `7` a texto.
# ----------------------------------------------------------------------

print(int("123"))   # 123
print(int(3.99))    # 3    → trunca, NO redondea
print(str(7))       # "7"

# Detalles adicionales
print(int(-3.99))   # -3   → trunca hacia cero
print(round(3.99))  # 4    → redondea
print(round(2.5))   # 2    → redondeo "bancario" (al par más cercano,
print(round(3.5))   # 4      para reducir el sesgo estadístico)
