# ----------------------------------------------------------------------
# 11. Velocidad media
# ----------------------------------------------------------------------
#
# Con distancia y tiempo, calcula la velocidad y conviértela de km/h
# a m/s.
# ----------------------------------------------------------------------

distancia_km = float(input("Distancia (km): "))
tiempo_h = float(input("Tiempo (horas): "))

velocidad_kmh = distancia_km / tiempo_h
velocidad_ms = velocidad_kmh * 1000 / 3600  # equivale a dividir entre 3.6

print(f"{velocidad_kmh:.2f} km/h = {velocidad_ms:.2f} m/s")
