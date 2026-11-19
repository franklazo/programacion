# Imprecisión de los decimales

Los `float` se guardan en binario y algunos valores no se representan exactamente:

```python
print(0.1 + 0.2)             # 0.30000000000000004
print(0.1 + 0.2 == 0.3)      # False
```

**Soluciones sencillas:**

```python
print(round(0.1 + 0.2, 2))   # 0.3
```

- Redondea con `round(valor, decimales)` al mostrar resultados.
- Para comparar decimales, evita `==` y usa `math.isclose(a, b)`.
- Para dinero con exactitud existe el módulo `decimal`.
