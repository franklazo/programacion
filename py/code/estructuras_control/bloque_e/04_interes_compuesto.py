# ----------------------------------------------------------------------
# Problema 04
# ----------------------------------------------------------------------
#
# Interés compuesto:
# ¿en cuántos años se duplica un capital con una tasa dada?
# ----------------------------------------------------------------------

capital = float(input("Capital inicial: "))
tasa = float(input("Tasa de interés anual (%): "))

if capital <= 0 or tasa <= 0:
    print("El capital y la tasa deben ser positivos.")
else:
    saldo = capital
    anios = 0

    while saldo < 2 * capital:
        saldo = saldo * (1 + tasa / 100)
        anios += 1

    print(f"Se duplica en {anios} años (saldo: {saldo:.2f})")
