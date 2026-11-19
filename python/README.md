# Curso de Python

Programación general desde cero

## Fase 1: Fundamentos

- [Primeros pasos](modulo-01/primeros-pasos.md)
- [Datos y operaciones básicas](modulo-02/datos-y-operaciones-basicas.md)

### Módulo 3. Control de flujo
- Condicionales: `if`, `elif`, `else`
- Bucles `while` y `for`, con `range()`
- `break`, `continue` y bucles anidados
- Patrones comunes: contadores, acumuladores, validación de entradas

**Mini proyecto:** juego de adivinar un número.

---

## Fase 2: Estructuras de datos y organización del código

### Módulo 4. Colecciones
- Listas: crear, modificar, recorrer, ordenar
- Tuplas y cuándo usarlas
- Diccionarios: pares clave-valor, recorrido y búsqueda
- Conjuntos (`set`) y operaciones entre ellos
- Comprensiones de listas y diccionarios
- Elegir la estructura adecuada para cada problema

**Mini proyecto:** agenda de contactos en consola.

### Módulo 5. Funciones
- Definir y llamar funciones
- Parámetros, valores por defecto y argumentos con nombre
- `return` y múltiples valores de retorno
- Alcance de variables (local vs. global)
- `*args` y `**kwargs`
- Funciones lambda
- Escribir funciones pequeñas con una sola responsabilidad
- Docstrings

**Mini proyecto:** refactorizar la agenda usando funciones.

### Módulo 6. Módulos y librería estándar
- Importar módulos y crear los tuyos
- Organizar un proyecto en varios archivos
- Librería estándar esencial: `math`, `random`, `datetime`, `collections`, `itertools`, `pathlib`
- Entornos virtuales (`venv`) e instalación de paquetes con `pip`
- Archivo `requirements.txt`

**Mini proyecto:** generador de contraseñas seguras.

---

## Fase 3: Trabajar con el mundo exterior

### Módulo 7. Archivos y persistencia
- Leer y escribir archivos de texto
- Manejo de rutas con `pathlib`
- Formatos CSV y JSON
- Guardar y cargar el estado de tu programa
- Introducción a SQLite con el módulo `sqlite3`

**Mini proyecto:** agenda que guarda sus datos entre ejecuciones.

### Módulo 8. Errores y depuración
- Tipos de errores: sintaxis, ejecución, lógicos
- `try`, `except`, `else`, `finally`
- Lanzar tus propias excepciones con `raise`
- Depurar con `print`, con el depurador del editor y con `pdb`
- Introducción al módulo `logging`

**Mini proyecto:** añadir manejo de errores robusto a tus programas anteriores.

### Módulo 9. Herramientas de línea de comandos
- Argumentos con `argparse`
- Variables de entorno
- Ejecutar comandos del sistema con `subprocess`
- Automatizar tareas: renombrar archivos, organizar carpetas, hacer copias de seguridad
- Programas que se ejecutan automáticamente (cron / Programador de tareas)

**Mini proyecto:** organizador automático de la carpeta de descargas.

---

## Fase 4: Programación orientada a objetos

### Módulo 10. Clases y objetos
- Qué problema resuelven las clases
- Atributos, métodos y `__init__`
- Encapsulación y propiedades (`@property`)
- Métodos especiales: `__str__`, `__repr__`, `__eq__`
- Herencia y composición (y por qué suele preferirse la composición)
- `dataclasses`

**Mini proyecto:** gestor de inventario o biblioteca con clases.

### Módulo 11. Conceptos intermedios del lenguaje
- Iteradores y generadores (`yield`)
- Decoradores
- Gestores de contexto (`with`)
- Anotaciones de tipo (*type hints*) básicas
- Expresiones regulares con `re`

**Mini proyecto:** analizador de logs que extrae información con expresiones regulares.

---

## Fase 5: Construir aplicaciones propias

### Módulo 12. Internet y APIs
- Cómo funciona la web a nivel básico (HTTP, JSON)
- Consumir APIs con `requests`
- *Web scraping* básico con `BeautifulSoup`
- Buenas prácticas: límites de uso y respeto a los términos de los sitios

**Mini proyecto:** panel en consola con el clima o datos de una API pública.

### Módulo 13. Interfaces para tus herramientas
Elige **una** de estas dos rutas (o ambas, si te interesa):
- **Interfaz gráfica de escritorio:** `tkinter` (ya incluida en Python) o `customtkinter`
- **Aplicación web sencilla:** `Flask` o `Streamlit` para exponer tu herramienta en el navegador

**Mini proyecto:** darle interfaz gráfica a una de tus herramientas anteriores.

### Módulo 14. Calidad y mantenimiento
- Pruebas automáticas con `pytest`
- Estructura de un proyecto personal
- Control de versiones con Git y GitHub (lo básico: *commit*, historial, recuperar versiones)
- Documentar con un `README`
- Empaquetar y distribuir tu programa (por ejemplo con PyInstaller)

**Mini proyecto:** poner pruebas a un proyecto anterior y subirlo a GitHub.

---

## Fase 6: Proyecto final

### Módulo 15. Tu propia aplicación
Elige algo que realmente quieras usar y pasa por todo el ciclo:
1. Definir el problema y el alcance mínimo
2. Diseñar las estructuras de datos y las funciones o clases
3. Implementar por partes
4. Probar y corregir
5. Darle una interfaz
6. Documentar y compartir

**Ideas:** gestor de gastos personales, organizador de recetas, seguidor de hábitos, automatizador de un proceso repetitivo de tu vida diaria, un juego sencillo.

---

## Consejos para sacarle partido

- **Programa a diario**, aunque sean 30 minutos. La constancia pesa más que las sesiones largas.
- **Escribe el código tú mismo**, no solo lo copies. Y equivócate: depurar es parte del aprendizaje.
- **Haz los mini proyectos aunque parezcan simples.** Ahí es donde se fija lo aprendido.
- **Aplícalo a tus propias necesidades** en cuanto puedas; la motivación se sostiene mucho mejor así.
- **Usa la documentación oficial** (docs.python.org) como complemento, y aprende a buscar errores.
- Si usas una IA como apoyo, pídele explicaciones y pistas antes que soluciones completas.

---

Si quieres, puedo convertir este temario en un **plan semanal con ejercicios concretos** por módulo, o ajustarlo si ya sabes algo de programación o tienes una idea de proyecto en mente.

---

Desarrolla el contenido de la sesión 1, punto por punto y de manera concisa 😃
Dame una lista de problemas/ejercicios imprescindibles conocer/resolver para esta sesión, sólo los necesarios, antes de pasar a la siguiente sesión 🤠
Las soluciones de los ejercicios por favor 😎
Las soluciones de la práctica por favor 😎
