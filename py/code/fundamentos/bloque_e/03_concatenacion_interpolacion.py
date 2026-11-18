# ----------------------------------------------------------------------
# 03. Concatenación e interpolación
# ----------------------------------------------------------------------
#
# Construye la misma frase con tres técnicas distintas (concatenar
# con `+`, formateo y plantillas/interpolación).
# ----------------------------------------------------------------------

nombre = "Ana"
edad = 25

# 1) Concatenación (hay que convertir el número a texto)
print("Me llamo " + nombre + " y tengo " + str(edad) + " años")

# 2) Método format
print("Me llamo {} y tengo {} años".format(nombre, edad))

# 3) f-string (interpolación), la más legible
print(f"Me llamo {nombre} y tengo {edad} años")
