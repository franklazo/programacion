# ----------------------------------------------------------------------
# Proyecto 02
# ----------------------------------------------------------------------
#
# Juego de adivinar el número, y un validador de contraseñas con reglas
# (longitud, mayúsculas, números).
# ----------------------------------------------------------------------

import random


MAX_INTENTOS = 7
MINIMO = 1
MAXIMO = 100
LONGITUD_MINIMA = 8
ESPECIALES = "!@#$%^&*()-_=+[]{};:,.<>?/"


while True:
    print("\n--- MENÚ PRINCIPAL ---\n")
    print("1. Adivinar el número")
    print("2. Validador de contraseñas")
    print("3. Salir\n")

    opcion = input("Elige una opción: ").strip()


    # -------------------------------------------------------------------------
    # OPCIÓN 1: ADIVINA EL NÚMERO
    # -------------------------------------------------------------------------
    if opcion == "1":
        secreto = random.randint(MINIMO, MAXIMO)
        intentos = 0
        acertado = False

        print(f"\nPensé un número entre {MINIMO} y {MAXIMO}.")
        print(f"Tienes {MAX_INTENTOS} intentos.")

        while intentos < MAX_INTENTOS and not acertado:
            # Validación de la entrada: no gasta intentos si es inválida
            while True:
                clave = input(f"\nIntento {intentos + 1}/{MAX_INTENTOS}: ").strip()

                if not clave.isdigit():
                    print("  Ingresa solo números entero positivos.")
                    continue

                numero = int(clave)

                if numero < MINIMO or numero > MAXIMO:
                    print(f"  El número debe estar entre {MINIMO} y {MAXIMO}.")
                    continue

                break

            intentos += 1

            if numero == secreto:
                acertado = True
            elif numero < secreto:
                print("  Muy bajo. Prueba con uno mayor.")
            else:
                print("  Muy alto. Prueba con uno menor.")

        if acertado:
            print(f"\n¡Correcto! Lo adivinaste en {intentos} intento(s).")
        else:
            print(f"\nSe acabaron los intentos. El número era {secreto}.")


    # -------------------------------------------------------------------------
    # OPCIÓN 2: VALIDADOR DE CONTRASEÑAS
    # -------------------------------------------------------------------------
    elif opcion == "2":
        print("\nReglas de la contraseña:")
        print(f"  - Al menos {LONGITUD_MINIMA} caracteres")
        print("  - Al menos una mayúscula y una minúscula")
        print("  - Al menos un número")
        print("  - Al menos un carácter especial")
        print("  - Sin espacios")
        print("(Escribe 'salir' para volver al menú)")

        while True:
            clave = input("\nContraseña: ")

            if clave.lower() == "salir":
                break

            tiene_mayuscula = False
            tiene_minuscula = False
            tiene_numero = False
            tiene_especial = False
            tiene_espacio = False

            for caracter in clave:
                if caracter.isupper():
                    tiene_mayuscula = True

                elif caracter.islower():
                    tiene_minuscula = True

                elif caracter.isdigit():
                    tiene_numero = True

                elif caracter in ESPECIALES:
                    tiene_especial = True

                elif caracter == " ":
                    tiene_espacio = True

            # Se acumulan TODOS los errores para informarlos juntos
            errores = ""

            if len(clave) < LONGITUD_MINIMA:
                errores += f"\n  - Debe tener al menos {LONGITUD_MINIMA} caracteres."
            if not tiene_mayuscula:
                errores += "\n  - Falta una letra mayúscula."
            if not tiene_minuscula:
                errores += "\n  - Falta una letra minúscula."
            if not tiene_numero:
                errores += "\n  - Falta un número."
            if not tiene_especial:
                errores += "\n  - Falta un carácter especial."
            if tiene_espacio:
                errores += "\n  - No puede contener espacios."

            if errores == "":
                print("✅ Contraseña válida.")
                break
            else:
                print("❌ Contraseña no válida:", end="")
                print(errores)


    # -------------------------------------------------------------------------
    # OPCIÓN 3: SALIR
    # -------------------------------------------------------------------------
    elif opcion == "3":
        print("¡Hasta pronto!\n")
        break

    else:
        print("Opción no válida. Elige 1, 2 o 3.")
