# ----------------------------------------------------------------------
# 03. Suma de textos vs. números
# ----------------------------------------------------------------------
#
# ¿Qué ocurre con `"5" + "3"` y con `5 + 3`? ¿Y con `"5" + 3`?
# Documenta el comportamiento de tu lenguaje.
# ----------------------------------------------------------------------

print("5" + "3")  # 53  → concatenación
print(5 + 3)      # 8   → suma
print("5" + 3)    # TypeError

# Resolver error
print(int("5") + 3)  # 8   → suma
print("5" + str(3))  # 53  → concatenación
