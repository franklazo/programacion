# ----------------------------------------------------------------------
# Problema 01
# ----------------------------------------------------------------------
#
# FizzBuzz: del 1 al 100, imprimir "Fizz" si es múltiplo de 3,
# "Buzz" si lo es de 5, "FizzBuzz" si de ambos,
# y el número en otro caso.
# ----------------------------------------------------------------------

for i in range(1, 101):
    if i % 15 == 0:  # múltiplo de 3 y de 5
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
