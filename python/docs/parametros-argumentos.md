# Parámetros y argumentos

```python
def saludar(nombre):              # parámetro único
    print(f"Hola {nombre}")

def presentar(nombre, edad):      # varios parámetros
    print(f"{nombre} tiene {edad} años")
```

```python
saludar("Ana")                    # argumento único
presentar("Ana", 20)              # argumentos por posición
presentar(edad=20, nombre="Ana")  # argumentos por nombre
```
