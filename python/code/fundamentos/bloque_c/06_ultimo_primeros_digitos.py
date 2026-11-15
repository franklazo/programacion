# ----------------------------------------------------------------------
# 06. Último y primeros dígitos
# ----------------------------------------------------------------------
#
# Dado un entero de 4 cifras, obtén su último dígito (`% 10`) y sus dos
# primeros (`// 100`).
# ----------------------------------------------------------------------

n = 4729

ultimo = n % 10          # 9
primeros_dos = n // 100  # 47

print(ultimo)            # 9
print(primeros_dos)      # 47


# Enteros negativos
n = -4729

ultimo = abs(n) % 10          # 9
primeros_dos = abs(n) // 100  # 47

print(ultimo)                 # 9
print(primeros_dos)           # 47
