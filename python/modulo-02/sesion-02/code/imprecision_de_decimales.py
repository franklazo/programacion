# import math

a = 0.1 + 0.2
b = 0.1 * 3

print(a)              # 0.30000000000000004
print(b)              # 0.30000000000000004

print(round(a, 2))    # 0.3
print(round(b, 2))    # 0.3

# Comparación correcta:
# print(a == 0.3)                # False
# print(math.isclose(a, 0.3))    # True
