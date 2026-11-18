# ----------------------------------------------------------------------
# 04. Sub-cadenas (slicing)
# ----------------------------------------------------------------------
#
# Dado `"programación"`, extrae los primeros 3 caracteres,
# los últimos 4 y los del medio.
# ----------------------------------------------------------------------

palabra = "programación"

print(palabra[:3])    # pro    (3 primeros)
print(palabra[-4:])   # ción   (últimos 4)
print(palabra[3:-3])  # gramac (el medio, sin 3 por cada lado)
