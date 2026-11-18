# ----------------------------------------------------------------------
# Problema 08
# ----------------------------------------------------------------------
#
# Cuenta regresiva con formato de tiempo (horas:minutos:segundos).
# ----------------------------------------------------------------------

import time

total = int(input("Segundos de la cuenta regresiva: "))

while total >= 0:
    horas = total // 3600
    minutos = (total % 3600) // 60
    segundos = total % 60

    print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")

    time.sleep(1)  # espera 1 segundo
    total -= 1

print("¡Tiempo!")
