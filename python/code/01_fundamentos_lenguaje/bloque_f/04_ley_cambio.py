# ----------------------------------------------------------------------
# 04. Ley del cambio
# ----------------------------------------------------------------------
#
# Dado un precio y el dinero entregado,
# calcula el vuelto y el desglose en billetes y monedas.
# ----------------------------------------------------------------------

print("\n=== Ley del cambio ===\n")

precio = int(input("Precio (entero): "))
pagado = int(input("Dinero entregado (entero): "))

vuelto = pagado - precio

billetes_100, resto = divmod(vuelto, 100)
billetes_50, resto = divmod(resto, 50)
billetes_20, resto = divmod(resto, 20)
billetes_10, resto = divmod(resto, 10)
monedas_5, resto = divmod(resto, 5)
monedas_2, resto = divmod(resto, 2)
monedas_1 = resto

print(f"\nVuelto total: {vuelto}")
print(f"Billetes de 100: {billetes_100}")
print(f"Billetes de 50:  {billetes_50}")
print(f"Billetes de 20:  {billetes_20}")
print(f"Billetes de 10:  {billetes_10}")
print(f"Monedas de 5:    {monedas_5}")
print(f"Monedas de 2:    {monedas_2}")
print(f"Monedas de 1:    {monedas_1}\n")
