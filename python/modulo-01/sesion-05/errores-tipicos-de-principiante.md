# Errores típicos de principiante

**`SyntaxError`: escribiste algo que Python no puede interpretar**

```python
print("Hola)        # faltan comillas de cierre
print("Hola"        # falta el paréntesis de cierre
```

Revisa comillas, paréntesis y dos puntos.

**`NameError`: usaste un nombre que Python no conoce**

```python
prin("Hola")        # 'prin' no existe
Print("Hola")       # Python distingue mayúsculas y minúsculas
```

Revisa ortografía y mayúsculas.

**`IndentationError`: espacios inesperados al inicio de la línea**

```python
print("Hola")
    print("Adiós")  # esta sangría no corresponde
```

Por ahora, todas tus líneas deben empezar en la columna 0.
