# Valores verdaderos y falsos (*truthy* y *falsy*)

Al usar `bool()` o una condición, Python trata estos valores como **falsos**:

- `False`
- `None`
- `0` y `0.0`
- `""` (cadena vacía)
- Colecciones vacías: `[]`, `()`, `{}`

**Todo lo demás es verdadero**, incluido `"0"`, `" "` y `-1`.

```python
bool(0)        # False
bool("")       # False
bool("hola")   # True
bool(-5)       # True

nombre = ""
if not nombre:
    print("No escribiste tu nombre")
```
