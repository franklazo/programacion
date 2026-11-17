# Parámetros con valores por defecto

```python
def saludar(nombre, saludo="Hola"):  # `saludo` se puede omitir en la llamada
    print(f"{saludo} {nombre}")
```

```python
saludar("Ana")                 # Hola Ana
saludar("Ana", "Buenos días")  # Buenos días Ana
```
