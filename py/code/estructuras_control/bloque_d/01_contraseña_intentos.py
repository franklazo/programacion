# ----------------------------------------------------------------------
# Problema 01
# ----------------------------------------------------------------------
#
# Pedir una contraseña hasta que sea correcta,
# con un máximo de 3 intentos.
# ----------------------------------------------------------------------

CLAVE = "python123"
MAX_INTENTOS = 3

intentos = 0
acceso = False

while intentos < MAX_INTENTOS and not acceso:
    intento = input("Contraseña: ")
    intentos += 1

    if intento == CLAVE:
        acceso = True
    else:
        print(f"Incorrecta. Intentos restantes: {MAX_INTENTOS - intentos}")

if acceso:
    print("Acceso concedido")
else:
    print("Cuenta bloqueada")
