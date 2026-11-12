# ----------------------------------------------------------------------
# 02. División entera vs. decimal
# ----------------------------------------------------------------------
#
# Calcula `7 / 2`, `7 // 2` (o su equivalente) y `7 % 2`. Entiende en
# qué lenguajes cambia el resultado según los tipos.
# ----------------------------------------------------------------------

print(7 / 2)   # 3.5  → división real
print(7 // 2)  # 3    → división entera (cociente)
print(7 % 2)   # 1    → módulo (resto)

# Con negativos
print(-7 // 2)  # -4  (Python redondea hacia abajo)
print(-7 % 2)   # 1    
