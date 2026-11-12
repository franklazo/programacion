# ----------------------------------------------------------------------
# 03. Reloj digital
# ----------------------------------------------------------------------
#
# Dados segundos desde medianoche,
# muestra la hora en formato `HH:MM:SS` con ceros a la izquierda.
# ----------------------------------------------------------------------

print("\n=== Reloj digital ===\n")

segundos_totales = int(input("Segundos desde medianoche: "))

# % 86400 (segundos de un día) evita horas mayores a 23
segundos_totales %= 86400

horas = segundos_totales // 3600
minutos = (segundos_totales % 3600) // 60
segundos = segundos_totales % 60

print(f"\nHora: {horas:02d}:{minutos:02d}:{segundos:02d}\n")
