# ----------------------------------------------------------------------
# Problema 05
# ----------------------------------------------------------------------
#
# Verificar si una persona es mayor de edad,
# y clasificarla por rango (niño, adolescente, adulto, adulto mayor).
# ----------------------------------------------------------------------

edad = int(input("Edad: "))

if edad < 0:
    print("Edad inválida")
else:
    if edad < 12:
        categoria = "Niño"
    elif edad < 18:
        categoria = "Adolescente"
    elif edad < 65:
        categoria = "Adulto"
    else:
        categoria = "Adulto mayor"

    print(categoria)
    print("Mayor de edad" if edad >= 18 else "Menor de edad")
