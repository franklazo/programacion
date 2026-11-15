# ----------------------------------------------------------------------
# 01. Longitud y acceso
# ----------------------------------------------------------------------
#
# Dada una palabra, muestra su longitud, su primera letra, su última
# letra y su letra central.
# ----------------------------------------------------------------------

palabra = "teclado"

print(len(palabra))                # 7
print(palabra[0])                  # t  (primera)
print(palabra[-1])                 # o  (última)
print(palabra[len(palabra) // 2])  # l  (central)

# La central sólo es única si la longitud es impar.
# En una con longitud par hay dos centrales: `len // 2 - 1` y `len // 2`.
