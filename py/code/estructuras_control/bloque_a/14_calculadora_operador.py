# ----------------------------------------------------------------------
# Problema 14
# ----------------------------------------------------------------------
#
# Calculadora: dados dos números y un operador (`+ - * /`),
# realizar la operación, controlando la división entre cero.
# ----------------------------------------------------------------------

a = float(input("Primer número: "))
op = input("Operador (+ - * /): ").strip()
b = float(input("Segundo número: "))

match op:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        if b == 0:
            print("Error: No se puede dividir entre cero")
        else:
            print(a / b)
    case _:
        print("Operador no válido")
