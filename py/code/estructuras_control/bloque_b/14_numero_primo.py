# ----------------------------------------------------------------------
# Problema 14
# ----------------------------------------------------------------------
#
# Verificar si un número es primo.
# ----------------------------------------------------------------------

numero = int(input("Número: "))

es_primo = numero > 1  # 0, 1 y negativos no son primos
i = 2

while i * i <= numero:    # basta probar hasta la raíz cuadrada
    if numero % i == 0:
        es_primo = False
        break             # salida anticipada: ya no hace falta seguir
    i += 1

print(f"{numero} {'es' if es_primo else 'no es'} primo")
