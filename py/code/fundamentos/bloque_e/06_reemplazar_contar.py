# ----------------------------------------------------------------------
# 06. Reemplazar y contar
# ----------------------------------------------------------------------
#
# Reemplaza todas las `a` por `*` y
# cuenta cuántas veces aparece una letra o palabra.
# ----------------------------------------------------------------------

texto = "banana"

print(texto.replace("a", "*"))            # b*n*n*
print(texto.count("a"))                   # 3
print("la casa de la playa".count("la"))  # 3

# `.count()` también cuenta palabras o sub-cadenas.
