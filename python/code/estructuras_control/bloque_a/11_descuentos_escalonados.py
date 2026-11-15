# ----------------------------------------------------------------------
# Problema 11
# ----------------------------------------------------------------------
#
# Calcular el precio final de una compra con descuentos escalonados
# (por ejemplo, 5% desde 100, 10% desde 500).
# ----------------------------------------------------------------------

total = float(input("Total de la compra: "))

if total < 0:
    print("Monto inválido")
else:
    if total >= 500:
        descuento = 0.10
    elif total >= 100:
        descuento = 0.05
    else:
        descuento = 0.0

    final = total * (1 - descuento)

    print(f"Descuento: {descuento * 100:.0f}%")
    print(f"Total a pagar: {final:.2f}")
