# ----------------------------------------------------------------------
# 14. Formato de factura
# ----------------------------------------------------------------------
#
# Imprime una tabla alineada con producto,
# cantidad y precio usando formateo de texto con anchos fijos.
# ----------------------------------------------------------------------

print(f"{'Producto':<15}{'Cant.':>6}{'Precio':>10}")
print("-" * 31)
print(f"{'Manzana':<15}{3:>6}{1.5:>10.2f}")
print(f"{'Leche':<15}{2:>6}{4.25:>10.2f}")
print(f"{'Pan integral':<15}{1:>6}{3.0:>10.2f}")
