# Conversión entre tipos

| Función   | Qué hace                       | Ejemplo        | Resultado |
| :---      | :---                           | :---           | :---      |
| `int()`   | A entero (trunca, no redondea) | `int(3.9)`     | `3`       |
| `float()` | A decimal                      | `float("2.5")` | `2.5`     |
| `str()`   | A texto                        | `str(42)`      | `"42"`    |
| `bool()`  | A booleano                     | `bool(7)`      | `True`    |

```python
int("25")          # 25
float(3)           # 3.0
str(3.14)          # "3.14"
int("hola")        # ValueError
int("3.7")         # ValueError (primero float, luego int)
int(float("3.7"))  # 3
```

**Regla útil:** para convertir un texto decimal a entero, pasa primero por `float()`.
