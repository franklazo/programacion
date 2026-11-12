# ----------------------------------------------------------------------
# 07. Descomposición de un número
# ----------------------------------------------------------------------
#
# Dado `n = 4729`, imprime cada dígito por separado usando solo
# división entera y módulo.
# ----------------------------------------------------------------------

n = 4729

millares = n // 1000        # 4
centenas = (n // 100) % 10  # 7
decenas = (n // 10) % 10    # 2
unidades = n % 10           # 9

print(millares)  # 4
print(centenas)  # 7
print(decenas)   # 2
print(unidades)  # 9

# Fórmula general para la cifra en la posición k
# (0 = unidades, 1 = decenas..):
#
#   cifra = (n // 10 ** k) % 10

# Verificación
print(millares * 1000 + centenas * 100 + decenas * 10 + unidades)  # 4729
