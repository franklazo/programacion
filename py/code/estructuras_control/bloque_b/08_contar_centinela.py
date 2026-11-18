# ----------------------------------------------------------------------
# Problema 08
# ----------------------------------------------------------------------
#
# Contar cuántos números positivos, negativos y ceros se ingresaron
# (terminar con un valor centinela).
# ----------------------------------------------------------------------

CENTINELA = 999
positivos = negativos = ceros = 0

while True:
    numero = int(input("Número (999 para terminar): "))

    if numero == CENTINELA:
        break
    elif numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        ceros += 1

print(f"Positivos: {positivos}, Negativos: {negativos}, Ceros: {ceros}")
