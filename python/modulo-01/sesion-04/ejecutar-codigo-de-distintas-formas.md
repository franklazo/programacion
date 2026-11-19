# Ejecutar código de distintas formas

**Objetivo:** moverte con comodidad entre el editor y la terminal.

1. [Qué es la terminal y por qué te sirve](que-es-la-terminal-y-por-que-te-sirve.md)
1. [Comandos básicos de navegación](comandos-basicos-de-navegacion.md)
1. [Ejecutar un archivo con `python archivo.py`](ejecutar-un-archivo-con-python-archivo-py.md)

## 4. El modo interactivo (REPL)
- **REPL** significa *Read, Evaluate, Print, Loop*: Python lee una instrucción, la ejecuta, muestra el resultado y espera la siguiente.
- Para abrirlo, escribe `python` (o `python3`) sin nombre de archivo. Verás el símbolo `>>>`.
- Pruébalo:
  ```python
  >>> 2 + 3
  5
  >>> print("Hola")
  Hola
  >>> 10 / 4
  2.5
  ```
- Para salir: `exit()` o `Ctrl + Z` y Enter en Windows (`Ctrl + D` en macOS y Linux).
- **Ojo:** lo que escribes aquí **no se guarda**. Al salir, desaparece.

## 5. ¿Archivo o REPL?

| Usa el **REPL** cuando... | Usa un **archivo** cuando... |
|---|---|
| Quieres probar algo rápido | Escribes un programa completo |
| Dudas de cómo funciona una instrucción | Quieres guardarlo y reutilizarlo |
| Haces cálculos sueltos | El código tiene varias líneas o pasos |

**Regla práctica:** experimenta en el REPL y, cuando algo funcione, pásalo a un archivo.

## Práctica
1. Abre la terminal y navega hasta tu carpeta `modulo-01`.
2. Ejecuta los tres programas de la sesión 3 con `python archivo.py`.
3. Abre el REPL y prueba `2 + 3`, `10 / 4` y `print("Hola")`.
4. Sal del REPL con `exit()`.

## Comprobación
- ✅ Puedes moverte entre carpetas con `cd`.
- ✅ Ejecutas cualquiera de tus archivos desde la terminal.
- ✅ Abres y cierras el REPL sin ayuda.
- ✅ Sabes cuándo usar el REPL y cuándo un archivo.

¿Seguimos con el desarrollo de la sesión 5? 🚀
