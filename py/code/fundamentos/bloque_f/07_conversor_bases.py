# ----------------------------------------------------------------------
# 07. Conversor de bases
# ----------------------------------------------------------------------
#
# Convierte un número a binario y hexadecimal
# con las funciones del lenguaje,
# y luego intenta explicar cómo se hace a mano.
# ----------------------------------------------------------------------

print("\n=== Conversor de bases ===\n")

n = int(input("Número entero entre 0 y 255: "))

# A) Con las funciones del lenguaje
print(f"\nBinario (bin): {bin(n)}  →  {n:08b}")
print(f"Hexadecimal (hex): {hex(n)}  →  {n:02X}")

# B) A mano, para 8 bits. Cada bit es: (n // 2 ** k) % 2
#    Se divide por la potencia de 2 de esa posición y se toma el resto de 2.
b7 = (n // 2 ** 7) % 2
b6 = (n // 2 ** 6) % 2
b5 = (n // 2 ** 5) % 2
b4 = (n // 2 ** 4) % 2
b3 = (n // 2 ** 3) % 2
b2 = (n // 2 ** 2) % 2
b1 = (n // 2 ** 1) % 2
b0 = (n // 2 ** 0) % 2

print(f"\nBinario a mano: {b7}{b6}{b5}{b4}{b3}{b2}{b1}{b0}")

# Hexadecimal a mano: cada dígito hex vale 16 posibilidades (4 bits).
digitos = "0123456789ABCDEF"  # una cadena se usa como tabla de búsqueda

digito_alto = n // 16
digito_bajo = n % 16

print(f"Hexadecimal a mano: {digitos[digito_alto]}{digitos[digito_bajo]}\n")
