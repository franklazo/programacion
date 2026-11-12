# ----------------------------------------------------------------------
# Mini proyecto 1
# ----------------------------------------------------------------------
#
# Calculadora básica por consola (suma, resta, multiplicación, división)
# Conversor de unidades (°C ↔ °F, km ↔ millas)
# ----------------------------------------------------------------------

# --- Constantes ---
MILLA_EN_KM = 1.609344


# --- Encabezado ---
print("=" * 40)
print("CALCULADORA Y CONVERSOR DE UNIDADES".center(40))
print("=" * 40)


# --- Parte 1: Calculadora ---
print("\n[1] CALCULADORA\n")

a = float(input("Primer número: "))
b = float(input("Segundo número: "))

print(f"\n{a} + {b}  = {a + b}")
print(f"{a} - {b}  = {a - b}")
print(f"{a} * {b}  = {a * b}")
print(f"{a} / {b}  = {a / b:.4f}")
print(f"{a} // {b} = {a // b}    (división entera)")
print(f"{a} % {b}  = {a % b}    (residuo)")


# --- Parte 2: Conversión de temperatura ---
print("\n[2] TEMPERATURA\n")

celsius = float(input("Temperatura en ºC: "))
fahrenheit_de_c = celsius * 9 / 5 + 32
print(f"{celsius} ºC = {fahrenheit_de_c:.2f} ºF")

fahrenheit = float(input("\nTemperatura en ºF: "))
celsius_de_f = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit} ºF = {celsius_de_f:.2f} ºC")


# --- Parte 3: Conversión de distancia ---
print("\n[3] DISTANCIA\n")

km = float(input("Distancia en km: "))
print(f"{km} km = {km / MILLA_EN_KM:.2f} millas")

millas = float(input("\nDistancia en millas: "))
print(f"{millas} millas = {millas * MILLA_EN_KM:.2f} km")


# --- Fin del programa ---
print("\n" + "=" * 40)
print("¡Fin del programa!".center(40))
print("=" * 40)
