# ----------------------------------------------------------------------
# 13. Texto con acentos y emojis
# ----------------------------------------------------------------------
#
# Calcula la longitud de `"canción"` y de un emoji;
# investiga por qué a veces la longitud no es la esperada
# (caracteres vs. bytes).
# ----------------------------------------------------------------------

print(len("canción"))                  # 7
print(len("canción".encode("utf-8")))  # 8 (la "ó" ocupa 2 bytes)

print(len("😃"))                  # 1
print(len("😃".encode("utf-8")))  # 4 bytes

print(len("👨‍👩‍👦"))  # 5 (son 3 emojis unidos por 2 caracteres invisibles)

# Python cuenta CODE POINTS, no lo que se ve ni los bytes.
