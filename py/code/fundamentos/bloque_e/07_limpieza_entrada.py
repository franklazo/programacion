# ----------------------------------------------------------------------
# 07. Limpieza de entrada
# ----------------------------------------------------------------------
#
# Dado `"   Hola Mundo   "`, elimina espacios extremos
# y conviértelo a minúsculas.
# ----------------------------------------------------------------------

entrada = "   Hola Mundo   "

limpio = entrada.strip().lower()

print(limpio)         # hola mundo
print(f"[{limpio}]")  # [hola mundo] (mostrar que ya no hay espacios)
