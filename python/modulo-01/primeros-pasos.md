# Primeros pasos

---

1. [Entender qué vas a hacer](sesion-01/entender-que-vas-a-hacer.md)
1. [Preparar tu entorno](sesion-02/preparar-tu-entorno.md)
1. [Tu primer programa](sesion-03/tu-primer-programa.md)

## Sesión 3. Tu primer programa (60 min)

**Objetivo:** escribir, guardar y ejecutar código por primera vez.

**Temas**
- Crear un archivo `.py`
- La función `print()` y cómo mostrar texto
- Texto entre comillas simples y dobles
- Varias instrucciones: el orden de ejecución, de arriba abajo
- Comentarios con `#`: para qué sirven y cuándo usarlos
- Ejecutar el archivo desde el editor

**Práctica:** tres programas cortos:
1. Imprimir "Hola, mundo"
2. Imprimir tu nombre y una frase sobre por qué quieres aprender Python
3. Imprimir un pequeño dibujo con texto (arte ASCII), con comentarios que expliquen cada parte

**Comprobación:** ejecutas tus archivos sin ayuda y entiendes por qué la salida aparece en ese orden.

---

## Sesión 4. Ejecutar código de distintas formas (45-60 min)

**Objetivo:** moverte con comodidad entre el editor y la terminal.

**Temas**
- Qué es la terminal y por qué te va a servir (la usarás mucho más adelante)
- Comandos básicos de navegación: `cd`, `ls` (o `dir` en Windows), `pwd`
- Ejecutar un archivo con `python archivo.py`
- El modo interactivo (REPL): abrirlo con `python` y probar instrucciones sueltas
- Cuándo conviene usar el REPL (experimentar) y cuándo un archivo (programas completos)

**Práctica:** ejecutar los programas de la sesión 3 desde la terminal, y luego usar el REPL para probar `print("...")` y operaciones simples como `2 + 3`.

**Comprobación:** puedes ejecutar cualquiera de tus archivos desde la terminal y sabes salir del REPL (`exit()`).

---

## Sesión 5. Errores y mini proyecto (60-90 min)

**Objetivo:** perder el miedo a los errores y cerrar el módulo con un programa propio.

**Temas**
- Los errores son normales y útiles: no significan que lo hagas mal
- Anatomía de un mensaje de error: tipo, línea y descripción
- Errores típicos de principiante: `SyntaxError` (comillas o paréntesis sin cerrar), `NameError` (nombre mal escrito), `IndentationError` (espacios inesperados)
- Estrategia de lectura: empezar por la **última línea** del mensaje y luego mirar el número de línea
- Cómo buscar un error en internet usando su mensaje

**Práctica 1, errores a propósito:** introduce adrede cada uno de los tres errores anteriores, lee el mensaje y corrígelos.

**Práctica 2, mini proyecto:** programa que te saluda por tu nombre. Por ahora, el nombre va escrito dentro del código (en el módulo 2 lo pedirás con `input()`). Debe incluir:
- Un saludo personalizado
- Al menos dos líneas más con información tuya
- Comentarios que expliquen qué hace cada bloque

**Comprobación final del módulo**
- Instalaste Python y un editor
- Ejecutas programas desde el editor y desde la terminal
- Usas `print()` y comentarios
- Sabes interpretar un mensaje de error sencillo

---

## Resumen

| Sesión | Tema | Duración |
|---|---|---|
| 1 | Qué es programar y qué es Python | 45-60 min |
| 2 | Instalación y editor | 60-90 min |
| 3 | `print()`, comentarios y primer programa | 60 min |
| 4 | Terminal y modo interactivo | 45-60 min |
| 5 | Errores y mini proyecto | 60-90 min |

Si ya tienes Python instalado o algo de práctica, puedes fusionar las sesiones 1 y 2, o saltarte la 1. ¿Quieres que prepare el mismo desglose para el Módulo 2?
