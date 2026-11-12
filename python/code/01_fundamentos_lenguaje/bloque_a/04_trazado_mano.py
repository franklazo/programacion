# ----------------------------------------------------------------------
# 04. Trazado a mano
# ----------------------------------------------------------------------
#
# Predice, sin ejecutar, el valor final de cada variable y luego
# verifica.
#
#   x = 3
#   y = x
#   x = x + 2
#   y = y * x
# ----------------------------------------------------------------------

x = 3      # se crea `x` (`y` no existe)
y = x      # `y` recibe una copia del valor de `x`
x = x + 2  # se calcula `3 + 2` y se guarda en `x` (`y` no cambia)
y = y * x  # se calcula `3 * 5` y se guarda en `y` (`x` no cambia)

print(x)   # verificar x = 5
print(y)   # verificar y = 15
