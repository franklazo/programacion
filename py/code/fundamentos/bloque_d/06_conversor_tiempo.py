# ----------------------------------------------------------------------
# 06. Conversor de tiempo
# ----------------------------------------------------------------------
#
# Dado un número de segundos, muestra horas, minutos y segundos
# (ejemplo: 3725 s → 1 h 2 min 5 s).
# ----------------------------------------------------------------------

total = int(input("Segundos: "))

horas = total // 3600
resto = total % 3600
minutos = resto // 60
segundos = resto % 60

# Solución alternativa
# horas, resto = divmod(total, 3600)
# minutos, segundos = divmod(resto, 60)

print(f"{total} s = {horas} h {minutos} min {segundos} s")
