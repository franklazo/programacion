# Formato de salida

```python
# Enteros
print(f"{25:5d}")    # ancho mínimo        =    25
print(f"{25:05d}")   # relleno con ceros   = 00025
print(f"{1234:,d}")  # separador de miles  = 1,234
```

```python
# Flotantes
print(f"{12.5:.2f}")     # decimales           = 12.50
print(f"{0.85:.1%}")     # porcentaje          = 85.0%
print(f"{1234.5:,.0f}")  # separador de miles  = 1,234
```

```python
print(f"|{'Ana':<10}|")  # alineación derecha    = |Ana       |
print(f"|{'Ana':^10}|")  # alineación centro     = |   Ana    |
print(f"|{'Ana':>10}|")  # alineación izquierda  = |       Ana|
```
