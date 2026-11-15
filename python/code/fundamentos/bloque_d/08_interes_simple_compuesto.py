# ----------------------------------------------------------------------
# 08. Interés simple y compuesto
# ----------------------------------------------------------------------
#
# Capital, tasa y años como entradas; muestra el monto final.
# ----------------------------------------------------------------------

capital = float(input("Capital inicial: "))
tasa = float(input("Tasa anual (%): ")) / 100
anyos = int(input("Años: "))

simple = capital * (1 + tasa * anyos)
compuesto = capital * (1 + tasa) ** anyos

print(f"Monto con interés simple:    {simple:,.2f}")
print(f"Monto con interés compuesto: {compuesto:,.2f}")
