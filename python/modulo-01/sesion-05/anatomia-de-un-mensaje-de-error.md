# Anatomía de un mensaje de error

```python
print("Hola)
```

```text
  File "saludo.py", line 1
    print("Hola)
          ^
SyntaxError: unterminated string literal (detected at line 1)
```

| Parte                      | Qué te dice                                               |
| :---                       | :---                                                      |
| `File "saludo.py", line 1` | Archivo y línea donde Python detectó el problema          |
| La línea de código con `^` | Dónde se detuvo (el fallo real puede estar un poco antes) |
| `SyntaxError: ...`         | **Tipo** de error y descripción                           |
