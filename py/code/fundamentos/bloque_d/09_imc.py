# ----------------------------------------------------------------------
# 09. IMC
# ----------------------------------------------------------------------
#
# Pide peso y estatura y muestra el índice de masa corporal.
# ----------------------------------------------------------------------

peso = float(input("Peso (kg): "))
estatura = float(input("Estatura (m): "))

imc = peso / estatura ** 2

print(f"Tu IMC es: {imc:.1f}")
