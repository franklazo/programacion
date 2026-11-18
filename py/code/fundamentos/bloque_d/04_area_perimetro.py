# ----------------------------------------------------------------------
# 04. Área y perímetro
# ----------------------------------------------------------------------
#
# Para un rectángulo, un círculo y un triángulo (base y altura),
# pidiendo los datos al usuario.
# ----------------------------------------------------------------------

import math

# Rectángulo
base_r = float(input("Base del rectángulo: "))
alto_r = float(input("Altura del rectángulo: "))

print(f"Rectángulo -> área: {base_r * alto_r:.2f}, perímetro: {2 * (base_r + alto_r):.2f}")


# Círculo
radio = float(input("Radio del círculo: "))

print(f"Círculo -> área: {math.pi * radio ** 2:.2f}, perímetro: {2 * math.pi * radio:.2f}")


# Triángulo
base_t = float(input("Base del triángulo: "))
alto_t = float(input("Altura del triángulo: "))
lado2 = float(input("Segundo lado: "))
lado3 = float(input("Tercer lado: "))

print(f"Triángulo -> área: {base_t * alto_t / 2:.2f}, perímetro: {base_t + lado2 + lado3:.2f}")
