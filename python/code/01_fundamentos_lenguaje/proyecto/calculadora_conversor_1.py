# ----------------------------------------------------------------------
# Mini proyecto 1 (+ opcionales 1)
# ----------------------------------------------------------------------
#
# Calculadora básica por consola (suma, resta, multiplicación, división)
# Conversor de unidades (°C ↔ °F, km ↔ millas)
# Menú interactivo (bucles y condicionales)
# Validación de la división entre cero (condicionales)
# ----------------------------------------------------------------------

# --- Constantes ---
MILLA_EN_KM = 1.609344


# --- Encabezado ---
print("\n" + "=" * 40)
print("CALCULADORA Y CONVERSOR DE UNIDADES".center(40))
print("=" * 40)


# --- Menú interactivo ---
while True:
    print("\n---- MENÚ ----\n")
    print("1) Calculadora")
    print("2) °C → °F")
    print("3) °F → °C")
    print("4) km → millas")
    print("5) millas → km")
    print("0) Salir")

    opcion = input("\nElige una opción: ")

    # --- Fin del programa ---
    if opcion == "0":
        print("\n" + "=" * 40)
        print("¡Fin del programa!".center(40))
        print("=" * 40 + "\n")
        break

    # --- Calculadora ---
    elif opcion == "1":
        a = float(input("\nPrimer número: "))
        b = float(input("Segundo número: "))
        op = input("Operación (+, -, *, /, //, %): ")

        if op == "+":
            print(f"\n{a} + {b} = {a + b}")

        elif op == "-":
            print(f"\n{a} - {b} = {a - b}")

        elif op == "*":
            print(f"\n{a} * {b} = {a * b}")

        elif op == "/":
            if b == 0:
                print("\nError: no se puede dividir entre cero.")
            else:
                print(f"\n{a} / {b} = {a / b:.4f}")

        elif op == "//":
            if b == 0:
                print("\nError: no se puede dividir entre cero.")
            else:
                print(f"\n{a} // {b} = {a // b}")

        elif op == "%":
            if b == 0:
                print("\nError: no se puede dividir entre cero.")
            else:
                print(f"\n{a} % {b} = {a % b}")

        else:
            print("\nOperación no válida.")

    # --- Conversión de temperatura ---
    elif opcion == "2":
        celsius = float(input("\nGrados ºC: "))
        fahrenheit = celsius * 9 / 5 + 32
        print(f"{celsius} ºC = {fahrenheit:.2f} ºF")

    elif opcion == "3":
        fahrenheit = float(input("\nGrados ºF: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"{fahrenheit} ºF = {celsius:.2f} ºC")

    # --- Conversión de distancia ---
    elif opcion == "4":
        km = float(input("\nKilómetros: "))
        print(f"{km} km = {km / MILLA_EN_KM:.2f} millas")

    elif opcion == "5":
        mi = float(input("\nMillas: "))
        print(f"{mi} millas = {mi * MILLA_EN_KM:.2f} km")

    # --- Opción no válida ---
    else:
        print("Opción no válida, intenta de nuevo.")
