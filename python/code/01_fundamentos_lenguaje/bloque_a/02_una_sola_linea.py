# ----------------------------------------------------------------------
# 02. Una sola línea
# ----------------------------------------------------------------------
#
# Imprime los mismos tres datos en una sola línea separados por comas,
# sin escribir el texto "a mano" tres veces (usa variables).
# ----------------------------------------------------------------------

nombre = "Ana"
edad = 25
ciudad = "Cusco"

# Opción 1: f-string (interpolación)
print(f"{nombre}, {edad}, {ciudad}")

# Opción 2: print con varios argumentos y separador
print(nombre, edad, ciudad, sep=", ")

# Opción 3: concatenación (exige convertir la edad a texto)
print(nombre + ", " + str(edad) + ", " + ciudad)
