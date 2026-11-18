# ----------------------------------------------------------------------
# Problema 01
# ----------------------------------------------------------------------
#
# Imprimir los números de 1 a N, y luego de N a 1.
# ----------------------------------------------------------------------

# Números del 1 a N
n = int(input("Ingresa N: "))

for i in range(1, n + 1):
    print(i, end=" ")

print()

# Números de N a 1
i = n

while i >= 1:
    print(i, end=" ")
    i -= 1
