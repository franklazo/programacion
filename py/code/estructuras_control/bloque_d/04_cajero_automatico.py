# ----------------------------------------------------------------------
# Problema 04
# ----------------------------------------------------------------------
#
# Cajero automático simulado: saldo inicial, depósitos,
# retiros (sin permitir saldo negativo) y consulta.
# ----------------------------------------------------------------------

saldo = 1000

while True:
    print("\n--- CAJERO ---")
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")

    opcion = input("Opción: ").strip()

    if opcion == "1":
        print(f"Saldo actual: ${saldo}")

    elif opcion == "2":
        monto = input("Monto a depositar: ").strip()
        if monto.isdigit() and int(monto) > 0:
            saldo += int(monto)
            print(f"Depósito exitoso. Nuevo saldo: ${saldo}")
        else:
            print("Monto no válido.")

    elif opcion == "3":
        monto = input("Monto a retirar: ").strip()
        if not (monto.isdigit() and int(monto) > 0):
            print("Monto no válido.")
        elif int(monto) > saldo:
            print("Fondos insuficientes.")
        else:
            saldo -= int(monto)
            print(f"Retiro exitoso. Nuevo saldo: ${saldo}")

    elif opcion == "4":
        print("Gracias por usar el cajero.")
        break

    else:
        print("Opción no válida.")
