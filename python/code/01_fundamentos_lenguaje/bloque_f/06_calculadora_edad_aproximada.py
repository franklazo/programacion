# ----------------------------------------------------------------------
# 06. Calculadora de edad aproximada
# ----------------------------------------------------------------------
#
# Dado el año de nacimiento y el año actual,
# calcula edad, años hasta los 100 y días vividos aproximados.
# ----------------------------------------------------------------------

print("\n=== Calculadora de edad aproximada ===\n")

anio_nacimiento = int(input("Año de nacimiento: "))
anio_actual = int(input("Año actual: "))

edad = anio_actual - anio_nacimiento
anios_para_100 = 100 - edad
dias_vividos = int(edad * 365.25)  # 365.25 compensa los años bisiestos

print(f"\nEdad aproximada: {edad} años")
print(f"Años que faltan para los 100: {anios_para_100}")
print(f"Días vividos (aprox.): {dias_vividos:,}\n")
