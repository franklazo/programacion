print(int("12"))      # 12
print(int("12.5"))    # ValueError
print(float("1,5"))   # ValueError
print(bool("False"))  # True
print(str(None))      # "None"

# Cómo arreglar los dos errores:
# int(float("12.5"))              # 12
# float("1,5".replace(",", "."))  # 1.5
