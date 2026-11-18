# ----------------------------------------------------------------------
# Problema 18
# ----------------------------------------------------------------------
#
# Verificar si un número es perfecto o de Armstrong.
# ----------------------------------------------------------------------

numero = int(input("Número: "))

suma_divisores = 0

for i in range(1, numero // 2 + 1):  # ningún divisor propio supera n/2
    if numero % i == 0:
        suma_divisores += i

print(f"{numero} {'es' if suma_divisores == numero else 'no es'} perfecto")

# Primero se cuentan los dígitos;
# luego se suma cada dígito elevado a esa cantidad
copia = numero
cantidad = 0

while copia > 0:
    copia //= 10
    cantidad += 1

copia = numero
suma = 0

while copia > 0:
    digito = copia % 10
    potencia = 1

    for _ in range(cantidad):
        potencia *= digito

    suma += potencia
    copia //= 10

print(f"{numero} {'es' if suma == numero else 'no es'} un número de Armstrong")
