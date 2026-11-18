# ----------------------------------------------------------------------
# 12. Códigos de carácter
# ----------------------------------------------------------------------
#
# Obtén el código Unicode de `'A'` y `'a'`,
# y el carácter correspondiente al código 97.
# Entiende por qué un carácter es en el fondo un número.
# ----------------------------------------------------------------------

print(ord("A"))            # 65
print(ord("a"))            # 97
print(chr(97))             # a
print(chr(ord("a") - 32))  # A

# La diferencia entre minúscula y mayúscula es 32.
