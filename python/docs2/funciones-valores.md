# Funciones como valores

```python
# Funciones son objetos de primera clase
def saludar(nombre):
    return f"Hola, {nombre}"

otro_nombre = saludar  # guardar en variable
otro_nombre("Ana")     # Hola, Ana
```
