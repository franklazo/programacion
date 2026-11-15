# ----------------------------------------------------------------------
# Problema 28
# ----------------------------------------------------------------------
#
# Contar palabras de una frase.
# ----------------------------------------------------------------------

frase = input("Texto: ")

palabras = 0
dentro_de_palabra = False  # bandera: ¿estamos en medio de una palabra?

for c in frase:
    if c != " ":
        if not dentro_de_palabra:
            palabras += 1  # empieza una palabra nueva
            dentro_de_palabra = True
    else:
        dentro_de_palabra = False

print(f"La frase tiene {palabras} palabras")
