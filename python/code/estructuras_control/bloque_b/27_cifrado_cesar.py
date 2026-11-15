# ----------------------------------------------------------------------
# Problema 27
# ----------------------------------------------------------------------
#
# Cifrado César: desplazar cada letra N posiciones.
# ----------------------------------------------------------------------

texto = input("Texto: ")
desplazamiento = int(input("Desplazamiento: "))

cifrado = ""

for c in texto:
    if "a" <= c <= "z":
        cifrado += chr((ord(c) - ord("a") + desplazamiento) % 26 + ord("a"))
    elif "A" <= c <= "Z":
        cifrado += chr((ord(c) - ord("A") + desplazamiento) % 26 + ord("A"))
    else:
        cifrado += c  # espacios y símbolos no se modifican

print(f"Original: {texto}")
print(f"Cifrado:  {cifrado}")

# Para descifrar: usar -desplazamiento (el % 26 maneja los negativos)
