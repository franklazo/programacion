# Closures

```python
# Función interna que "recuerda" las variables
# de la función que la envolvió
def crear_multiplicador(n):
    def multiplicar(x):
        return x * n             # variable envolvente `n`
    return multiplicar

doble = crear_multiplicador(2)   # doble(5)   → 10
triple = crear_multiplicador(3)  # triple(5)  → 15
```

```python
def crear_contador():
    cuenta = 0
    def incrementar():
        nonlocal cuenta  # modificar variable envolvente
        cuenta += 1
        return cuenta
    return incrementar

c = crear_contador()     # c(), c(), c()  → 1, 2, 3
```
