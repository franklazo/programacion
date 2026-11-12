# ----------------------------------------------------------------------
# 11. Iniciales
# ----------------------------------------------------------------------
#
# Dado un nombre completo de tres palabras,
# muestra slo las iniciales en mayúscula.
# ----------------------------------------------------------------------

nombre = "ana maría lópez"

partes = nombre.split()   # sin argumento separa por espacios
iniciales = partes[0][0] + partes[1][0] + partes[2][0]

print(iniciales.upper())  # AML

# `partes[0][0]` significa "de la primera palabra, la primera letra".
