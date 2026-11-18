# Número variable de argumentos

```python
def mostrar_suma(*numeros):  # argumentos como tupla
    print(sum(numeros))

def mostrar_datos(**datos):  # argumentos como diccionario
    print(datos)
```

```python
mostrar_suma(1, 2, 3, 4)              # (1, 2, 3, 4)
mostrar_datos(nombre="Ana", edad=25)  # {'nombre': 'Ana', 'edad': 25}
```
