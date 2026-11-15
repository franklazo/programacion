# ----------------------------------------------------------------------
# Problema 02
# ----------------------------------------------------------------------
#
# Determinar si una cadena de paréntesis está balanceada,
# usando solo un contador por ahora.
# ----------------------------------------------------------------------

texto = input("Escribe una expresión: ")

contador = 0
balanceado = True

for c in texto:
    if c == "(":
        contador += 1

    elif c == ")":
        contador -= 1

        if contador < 0:        # cerró uno que nunca se abrió
            balanceado = False
            break

if contador != 0:               # quedaron paréntesis sin cerrar
    balanceado = False

print(f"{'Balanceada' if balanceado else 'No balanceada'}")
