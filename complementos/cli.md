# Temario de Python orientado a aplicaciones CLI

Está pensado para avanzar en orden. Los bloques 1 a 5 son la base que sirve para cualquier especialización (web, datos, automatización, DevOps, IA). Los bloques 6 a 8 son los que hacen que tus programas sean realmente herramientas de terminal.

---

## Bloque 0: Preparación del entorno

- Instalar Python (versiones, cómo verificar con `python --version`)
- Usar la terminal: navegar carpetas, crear/mover/borrar archivos, variables de entorno básicas
- Editor o IDE (VS Code, PyCharm) y configuración básica
- Ejecutar scripts (`python archivo.py`) y usar el intérprete interactivo (REPL)
- Entornos virtuales (`venv`) y por qué existen
- `pip`: instalar, listar y desinstalar paquetes

---

## Bloque 1: Fundamentos del lenguaje

1. Sintaxis básica, indentación y comentarios
2. Variables y asignación
3. Tipos básicos: `int`, `float`, `str`, `bool`, `None`
4. Operadores aritméticos, de comparación y lógicos
5. Entrada y salida: `print()` e `input()`
6. Conversión de tipos (casting)
7. Cadenas de texto: indexado, slicing, métodos (`split`, `strip`, `replace`, `join`…)
8. f-strings y formateo de texto
9. Condicionales: `if`, `elif`, `else`
10. Bucles: `for`, `while`, `break`, `continue`, `range()`

**🛠 Mini proyecto 1:** Calculadora interactiva en terminal (suma, resta, multiplicación, división, con menú que se repite hasta que el usuario salga).

---

## Bloque 2: Estructuras de datos

1. Listas: creación, métodos, slicing, iteración
2. Tuplas e inmutabilidad
3. Diccionarios: claves/valores, métodos, iteración
4. Conjuntos (`set`) y operaciones entre conjuntos
5. Comprensiones de listas, diccionarios y conjuntos
6. Desempaquetado de secuencias (`a, b = ...`, `*resto`)
7. Copias superficiales vs. profundas
8. Ordenamiento (`sorted`, `sort`, `key=`)
9. Funciones útiles: `len`, `sum`, `min`, `max`, `enumerate`, `zip`, `any`, `all`

**🛠 Mini proyecto 2:** Gestor de tareas en memoria (agregar, listar, marcar como hecha, eliminar), usando listas de diccionarios.

---

## Bloque 3: Funciones y organización del código

1. Definir funciones, parámetros y `return`
2. Argumentos posicionales, por nombre y valores por defecto
3. `*args` y `**kwargs`
4. Alcance de variables (local, global, `nonlocal`)
5. Funciones como objetos (pasarlas como argumento)
6. Funciones `lambda`
7. Docstrings y *type hints* (anotaciones de tipo)
8. Módulos: `import`, `from … import`, alias
9. Paquetes y estructura de carpetas de un proyecto
10. El bloque `if __name__ == "__main__":` (clave para CLI)
11. Biblioteca estándar: `math`, `random`, `datetime`, `collections`, `itertools`

**🛠 Mini proyecto 3:** Generador de contraseñas aleatorias, dividido en funciones y módulos, con reglas configurables (longitud, símbolos, números).

---

## Bloque 4: Manejo de archivos y errores

1. Leer y escribir archivos de texto (`open`, modo `r/w/a`)
2. Context managers (`with`)
3. `pathlib` para manejar rutas (en lugar de concatenar strings)
4. Trabajar con CSV (`csv`)
5. Trabajar con JSON (`json`): serializar y deserializar
6. Excepciones: `try`, `except`, `else`, `finally`
7. Tipos de excepciones comunes y cómo lanzar las tuyas (`raise`)
8. Validación de datos de entrada
9. Introducción a `logging` (en lugar de usar solo `print` para depurar)
10. Depuración básica: leer un *traceback*, `breakpoint()`/`pdb`

**🛠 Mini proyecto 4:** Gestor de tareas con persistencia: guarda y carga las tareas desde un archivo JSON, con manejo de errores si el archivo no existe o está corrupto.

---

## Bloque 5: Programación orientada a objetos (POO)

1. Clases, objetos, atributos y métodos
2. `__init__` y `self`
3. Métodos especiales (`__str__`, `__repr__`, `__eq__`, `__len__`)
4. Atributos de clase vs. de instancia
5. Herencia y `super()`
6. Encapsulamiento y propiedades (`@property`)
7. `@classmethod` y `@staticmethod`
8. Composición vs. herencia
9. `dataclasses`
10. Excepciones personalizadas (clases que heredan de `Exception`)

**🛠 Mini proyecto 5:** Agenda de contactos con clases (`Contacto`, `Agenda`), búsqueda por nombre y guardado en JSON.

---

## Bloque 6: Fundamentos de aplicaciones CLI

1. Qué es una aplicación CLI: comandos, argumentos, opciones y banderas (*flags*)
2. `sys.argv` y sus limitaciones
3. `argparse`: argumentos posicionales, opcionales, tipos, valores por defecto, `choices`, `--help`
4. Subcomandos (`git commit`, `git push` como modelo mental)
5. Códigos de salida (`sys.exit`, éxito vs. error)
6. Flujos estándar: `stdin`, `stdout`, `stderr`
7. Redirección y *pipes* (`|`, `>`, `<`) y cómo hacer que tu programa los soporte
8. Variables de entorno (`os.environ`) y archivos `.env`
9. Archivos de configuración (JSON, TOML con `tomllib`, INI con `configparser`)
10. Manejo de rutas y del sistema de archivos (`os`, `shutil`, `glob`)
11. Ejecutar otros programas con `subprocess`
12. Manejo de `Ctrl+C` (`KeyboardInterrupt`) y salidas limpias

**🛠 Mini proyecto 6:** Organizador de archivos: recibe una carpeta como argumento y mueve los archivos a subcarpetas según su extensión, con opciones `--dry-run` y `--verbose`.

---

## Bloque 7: CLIs con mejor experiencia de usuario

1. Frameworks modernos: **Click** y/o **Typer** (comparar con `argparse`)
2. Colores y formato en terminal con **Rich** (tablas, barras de progreso, paneles)
3. Mensajes de error claros y ayuda bien redactada
4. Entrada interactiva: confirmaciones, menús, *prompts* (`questionary`, `prompt_toolkit`, o los de Click/Typer)
5. Barras de progreso y *spinners*
6. Salida en múltiples formatos (`--json`, tabla, texto plano)
7. Detectar si la salida es una terminal o un *pipe* (`sys.stdout.isatty()`)
8. Autocompletado en shell (conceptos básicos)
9. Convenciones de CLI: `-h/--help`, `-v/--verbose`, `--version`, `-q/--quiet`

**🛠 Mini proyecto 7:** Gestor de tareas "profesional" con Typer o Click, subcomandos (`add`, `list`, `done`, `remove`), salida con tablas de Rich y almacenamiento en archivo.

---

## Bloque 8: Datos, red y persistencia

1. Peticiones HTTP con `requests` o `httpx`
2. Consumir APIs REST: JSON, *headers*, autenticación con tokens, códigos de estado
3. Manejo de errores de red, *timeouts* y reintentos
4. Expresiones regulares (`re`)
5. SQLite con `sqlite3`: crear tablas, insertar, consultar, actualizar
6. Introducción a SQL básico (`SELECT`, `INSERT`, `UPDATE`, `DELETE`, `WHERE`)
7. Variables de entorno para guardar claves de API de forma segura
8. Introducción a *web scraping* (`BeautifulSoup`), con ética y respeto a `robots.txt`
9. Programación asíncrona: concepto de `async/await` (solo introducción)

**🛠 Mini proyecto 8:** CLI de clima o cotizaciones: consulta una API pública, muestra el resultado con Rich y guarda un historial de consultas en SQLite.

---

## Bloque 9: Calidad, pruebas y distribución

1. Pruebas con `pytest`: asserts, fixtures, parametrización
2. Probar CLIs (`CliRunner` de Click/Typer, `capsys`)
3. *Mocking* de archivos, red y tiempo
4. Formateo y *linting*: `ruff`, `black`
5. Análisis estático de tipos con `mypy`
6. Estructura de un proyecto moderno: `pyproject.toml`, carpeta `src/`
7. Gestores de dependencias y entornos: `pip` + `venv`, `uv`, `poetry` (conocer las opciones)
8. Definir *entry points* (`[project.scripts]`) para instalar tu CLI como comando
9. Empaquetar y publicar (TestPyPI), versionado semántico
10. Control de versiones con **Git** y GitHub
11. Escribir un buen `README` y documentar el uso

**🛠 Mini proyecto 9 (integrador):** Toma cualquiera de los proyectos anteriores, agrégale pruebas, configúralo como paquete instalable con `pip install .` y súbelo a GitHub con un README claro.

---

## Bloque 10: Temas intermedios-avanzados (para explorar y descubrir tu camino)

Aquí ya empiezas a probar áreas distintas y notar cuál te atrae más:

1. Iteradores, generadores y `yield`
2. Decoradores (cómo los usan Click, Typer y pytest por dentro)
3. Context managers personalizados
4. Concurrencia: hilos (`threading`), procesos (`multiprocessing`) y `asyncio`
5. Patrones de diseño básicos aplicados a CLIs (comandos, plugins, fábricas)
6. Rendimiento: *profiling* (`cProfile`), estructuras eficientes
7. Seguridad básica: no ejecutar entradas no confiables, manejo de secretos, `shlex`
8. Docker básico para distribuir tus herramientas

**🛠 Mini proyecto 10:** Herramienta de línea de comandos con *plugins* o que procese muchos archivos o URLs en paralelo (por ejemplo, un verificador de enlaces rotos concurrente).

---

## Pruebas de especialización (después del Bloque 8 o 9)

Para que descubras qué te gusta, prueba un mini proyecto corto de cada área:

| Área | Qué probar | Herramientas para explorar |
|---|---|---|
| **Automatización / scripting** | Renombrar archivos, enviar reportes por correo | `pathlib`, `smtplib`, `schedule` |
| **Datos / análisis** | Analizar un CSV y sacar estadísticas | `pandas`, `matplotlib` |
| **Web / backend** | Una API sencilla | `FastAPI`, `Flask` |
| **DevOps / sistemas** | Script que monitorea disco o servicios | `psutil`, `subprocess`, `paramiko` |
| **Ciberseguridad** | Escáner de puertos educativo, validador de hashes | `socket`, `hashlib` |
| **IA / ML** | Clasificador simple o uso de una API de LLM | `scikit-learn`, SDKs de APIs |

---

## Resumen de la ruta

| Etapa | Bloques | Resultado |
|---|---|---|
| **Principiante** | 0, 1, 2 | Escribes scripts simples |
| **Básico sólido** | 3, 4, 5 | Organizas código y manejas archivos y errores |
| **CLI funcional** | 6, 7 | Construyes herramientas de terminal reales |
| **Integración** | 8, 9 | Consumes APIs, usas bases de datos y publicas proyectos |
| **Exploración** | 10 + pruebas | Eliges una especialización con criterio |

**Consejo:** no hace falta dominar un bloque al 100 % antes de pasar al siguiente. Con entender lo esencial y hacer el mini proyecto es suficiente; vuelves a lo que necesites cuando el proyecto lo pida.
