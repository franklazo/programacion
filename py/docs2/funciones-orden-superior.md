# Funciones de orden superior

```python
def aplicar(func, valor):  # función como argumento (callback)
    return func(valor)

aplicar(len, "python")     # 6
```

```python
def crear_potencia(exp):
    def potencia(base):
        return base ** exp
    return potencia        # devuelve una función

cubo = crear_potencia(3)   # permite crear nuevas funciones
cubo(2)                    # 8
```
