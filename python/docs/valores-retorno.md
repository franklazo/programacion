# Valores de retorno

```python
def sumar(a, b):
    return a + b         # valor único

def mostrar_mensaje():
    print("Hola")        # sin valor de retorno

def operaciones(a, b):
    return a + b, a - b  # tupla de valores
```

```python
sumar(20, 30)            # 50
mostrar_mensaje()        # None
operaciones(70, 50)      # (120, 20)
```
