# ----------------------------------------------------------------------
# 01. Boleta simple
# ----------------------------------------------------------------------
#
# Pide producto, precio unitario y cantidad;
# muestra subtotal, IGV y total con formato de moneda.
# ----------------------------------------------------------------------

print("\n=== Boleta simple ===\n")

IGV = 0.18

producto = input("Producto: ").strip()
precio = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))

subtotal = precio * cantidad
impuesto = subtotal * IGV
total = subtotal + impuesto

print(f"\nProducto: {producto} x {cantidad}")
print(f"{'Subtotal:':<12}{subtotal:>10.2f}")
print(f"{'IGV (18%):':<12}{impuesto:>10.2f}")
print(f"{'Total:':<12}{total:>10.2f}\n")
