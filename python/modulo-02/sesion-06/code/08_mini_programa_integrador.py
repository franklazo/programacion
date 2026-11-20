TASA_IVA = 0.18  # constante por convención (MAYÚSCULAS)
precio = 200

iva = precio * TASA_IVA      # 36.0
precio_final = precio + iva  # 236.0

print(iva)
print(precio_final)
