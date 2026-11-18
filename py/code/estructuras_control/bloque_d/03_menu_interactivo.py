# ----------------------------------------------------------------------
# Problema 03
# ----------------------------------------------------------------------
#
# Menú interactivo que se repite hasta que el usuario elija "Salir".
# ----------------------------------------------------------------------

while True:
    print("\n--- MENÚ ---")
    print("1. Saludar")
    print("2. Tabla de multiplicar")
    print("3. Salir")

    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        nombre = input("¿Cómo te llamas? ")
        print(f"¡Hola, {nombre}!")

    elif opcion == "2":
        n = input("¿De qué número? ").strip()
        if n.isdigit():
            for i in range(1, 11):
                print(f"{n} x {i} = {int(n) * i}")
        else:
            print("Número no válido.")

    elif opcion == "3":
        print("¡Hasta pronto!")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
