# Codificación

```python
# Unicode: Puntos de código
# Número único que se le asigna a un carácter

ord("ñ")  # obtener entero        = 241
chr(241)  # convertir a carácter  = 'ñ'
```

```python
# Codificación predeterminada UTF-8
# Cómo se almacenan los caracteres en bytes

"ñ".encode()          # b'\xc3\xb1'
b'\xc3\xb1'.decode()  # ñ

# Unicode 241 (ñ) en binario:        11   110001
# Plantilla binaria en UTF-8:  110xxxxx 10xxxxxx  (2 bytes)
# Codificación UTF-8 para ñ:   11000011 10110001  (0xc3 0xb1)
```
