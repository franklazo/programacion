# ----------------------------------------------------------------------
# 07. Cambio de monedas
# ----------------------------------------------------------------------
#
# Dado un monto en centavos, calcula cuántas monedas de 50, 20, 10,
# 5 y 1 se necesitan (versión sin condicionales: usa división entera
# y resto en cadena).
# ----------------------------------------------------------------------

monto = int(input("Monto en centavos: "))

m50, monto = divmod(monto, 50)
m20, monto = divmod(monto, 20)
m10, monto = divmod(monto, 10)
m5, monto = divmod(monto, 5)
m1 = monto

print(f"50c: {m50} | 20c: {m20} | 10c: {m10} | 5c: {m5} | 1c: {m1}")
