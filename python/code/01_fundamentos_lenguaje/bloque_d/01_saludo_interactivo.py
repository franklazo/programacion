# ----------------------------------------------------------------------
# 01. Saludo interactivo
# ----------------------------------------------------------------------
#
# Pide el nombre y la edad y responde: "Hola, X. En 10 años tendrás Y".
# ----------------------------------------------------------------------

nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Cuántos años tienes? "))

print(f"Hola, {nombre}. En 10 años tendrás {edad + 10}")
