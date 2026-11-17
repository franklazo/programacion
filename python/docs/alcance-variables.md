# Alcance de las variables

```python
x = 10        # alcance global

def mostrar():
    y = 5     # alcance local (función)
    print(x)  # 10

def aumentar():
    global x  # permite modificar (mala práctica)
    x += 5    # 15
```
