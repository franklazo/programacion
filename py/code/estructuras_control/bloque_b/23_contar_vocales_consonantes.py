# ----------------------------------------------------------------------
# Problema 23
# ----------------------------------------------------------------------
#
# Contar vocales y consonantes de una frase.
# ----------------------------------------------------------------------

frase = input("Frase: ")

vocales = consonantes = 0

for car in frase.lower():
    if car in "aeiouáéíóúü":
        vocales += 1
    elif car.isalpha():  # es letra pero no vocal
        consonantes += 1

print(f"Vocales: {vocales}, Consonantes: {consonantes}")
