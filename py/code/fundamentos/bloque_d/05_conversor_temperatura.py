# ----------------------------------------------------------------------
# 05. Conversor de temperatura
# ----------------------------------------------------------------------
#
# °C a °F, y luego K a °C.
# ----------------------------------------------------------------------

celsius = float(input("Grados Celsius: "))
fahrenheit = celsius * 9 / 5 + 32

print(f"{celsius} ºC = {fahrenheit:.1f} ºF")

kelvin = float(input("Grados Kelvin: "))
print(f"{kelvin} K = {kelvin - 273.15:.2f} ºC")
