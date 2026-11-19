# `None`: ausencia de valor

- Representa "todavía no hay nada" o "no aplica".
- No es lo mismo que `0`, `""` ni `False`.

```python
resultado = None
print(resultado)         # None
print(type(resultado))   # <class 'NoneType'>
```

Para comprobarlo se usa `is None`:

```python
print(resultado is None)  # True
```
