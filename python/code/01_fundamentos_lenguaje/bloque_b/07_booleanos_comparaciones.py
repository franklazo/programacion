# ----------------------------------------------------------------------
# 07. Booleanos desde comparaciones
# ----------------------------------------------------------------------
#
# Imprime el resultado de `5 > 3`, `5 == 5.0`, `"a" == "A"` y `5 != 5`.
# ----------------------------------------------------------------------

print(5 > 3)       # True
print(5 == 5.0)    # True
print("a" == "A")  # False
print(5 != 5)      # False

# `==` compara valores, no tipos
# Textos distinguen entre mayúsculas y minúsculas,
# para ignorarlas:

print("a".lower() == "A".lower())  # True
