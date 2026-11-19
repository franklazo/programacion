# Asignación con `=` y reasignación

El `=` **no significa "igual"**: significa "guarda el valor de la derecha en el nombre de la izquierda". Python evalúa primero la derecha.

```python
puntos = 10
puntos = 15          # reasignación: ahora vale 15
puntos = puntos + 5  # primero calcula 15 + 5, luego lo guarda
print(puntos)        # 20
```

Una variable puede cambiar de tipo al reasignarla (Python es de tipado dinámico):

```python
dato = 5        # int
dato = "cinco"  # ahora es str
```
