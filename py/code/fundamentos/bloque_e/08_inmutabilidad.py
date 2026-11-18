# ----------------------------------------------------------------------
# 08. Inmutabilidad
# ----------------------------------------------------------------------
#
# Intenta cambiar un carácter de una cadena por índice y
# observa qué pasa; luego logra el cambio de otra manera.
# ----------------------------------------------------------------------

palabra = "python"

# cadena[0] = "P"            # TypeError
palabra = "P" + palabra[1:]  # se crea una cadena NUEVA

print(palabra)               # Python
