# Temario general de programación

Este temario es independiente del lenguaje. Cada tema aplica igual en Python, JavaScript, Java, C#, Go, etc.; solo cambia la sintaxis.

---

## Etapa 0: Preparación y mentalidad

1. **Qué es programar**: algoritmos, instrucciones, máquina y lenguaje.
2. **Cómo se ejecuta un programa**: compilado vs. interpretado vs. híbrido; código fuente, bytecode, binario.
3. **Entorno de trabajo**: editor/IDE, terminal básica, instalación del lenguaje, ejecutar un archivo.
4. **Pensamiento computacional**: descomposición de problemas, abstracción, patrones, pseudocódigo y diagramas de flujo.
5. **Leer errores**: tipos de error (sintaxis, ejecución, lógica) y cómo interpretar un mensaje de error.

---

## Etapa 1: Fundamentos del lenguaje

1. **Sintaxis básica**: instrucciones, comentarios, indentación/bloques, convenciones de nombres.
2. **Variables y constantes**: declaración, asignación, alcance básico.
3. **Tipos de datos primitivos**: enteros, decimales, booleanos, caracteres, texto, nulo/vacío.
4. **Tipado**: estático vs. dinámico, fuerte vs. débil, conversión (casting) entre tipos.
5. **Operadores**: aritméticos, comparación, lógicos, asignación, precedencia.
6. **Entrada y salida**: leer del usuario, imprimir, formatear texto.
7. **Cadenas de texto**: concatenación, interpolación, métodos comunes, inmutabilidad, codificación (Unicode/UTF-8).

### 🛠 Mini proyecto 1

Calculadora básica por consola (suma, resta, multiplicación, división) y un conversor de unidades (°C ↔ °F, km ↔ millas).

---

## Etapa 2: Control de flujo

1. **Condicionales**: `if / else if / else`, condiciones anidadas, operador ternario.
2. **Selección múltiple**: `switch/match`.
3. **Bucles**: `while`, `for`, `for-each`/iteración sobre colecciones, `do-while` donde exista.
4. **Control de bucles**: `break`, `continue`, bucles anidados, bucles infinitos y cómo evitarlos.
5. **Lógica booleana**: tablas de verdad, evaluación en cortocircuito, valores "truthy/falsy".
6. **Patrones algorítmicos básicos**: contadores, acumuladores, banderas (flags), búsqueda del máximo/mínimo.

### 🛠 Mini proyecto 2

Juego de adivinar el número, y un validador de contraseñas con reglas (longitud, mayúsculas, números).

---

## Etapa 3: Funciones y modularidad

1. **Funciones**: definición, llamada, parámetros, valores de retorno.
2. **Parámetros avanzados**: valores por defecto, argumentos nombrados, número variable de argumentos.
3. **Alcance (scope)**: local vs. global, ciclo de vida de variables, closures (introducción).
4. **Paso por valor vs. por referencia**: qué se copia realmente y qué no.
5. **Recursión**: caso base, caso recursivo, pila de llamadas, cuándo conviene y cuándo no.
6. **Funciones como valores**: callbacks, funciones anónimas/lambdas, funciones de orden superior.
7. **Buenas prácticas**: funciones pequeñas, un propósito por función, nombres descriptivos, documentación.
8. **Módulos y paquetes**: dividir código en archivos, importar/exportar, librería estándar, gestores de dependencias.

### 🛠 Mini proyecto 3

Generador de contraseñas aleatorias con módulos separados, y una función recursiva para Fibonacci/factorial comparada con su versión iterativa.

---

## Etapa 4: Estructuras de datos fundamentales

1. **Arreglos/listas**: acceso por índice, recorrido, inserción, eliminación, ordenamiento, slicing.
2. **Matrices (arreglos multidimensionales)**.
3. **Diccionarios/mapas/hash maps**: pares clave-valor, búsqueda por clave, iteración.
4. **Conjuntos (sets)**: unicidad, unión, intersección, diferencia.
5. **Tuplas/registros/structs**: datos agrupados e inmutabilidad.
6. **Pilas y colas**: LIFO/FIFO y sus usos reales.
7. **Mutabilidad vs. inmutabilidad**: copias superficiales vs. profundas.
8. **Transformaciones funcionales**: map, filter, reduce, comprensiones de lista.
9. **Elegir la estructura adecuada** según el problema.

### 🛠 Mini proyecto 4

Gestor de contactos en memoria (agregar, buscar, editar, eliminar) y un contador de frecuencia de palabras en un texto.

---

## Etapa 5: Manejo de errores y archivos

1. **Excepciones**: `try / catch / finally`, lanzar errores propios, jerarquía de errores.
2. **Programación defensiva**: validar entradas, precondiciones, valores límite.
3. **Archivos de texto**: abrir, leer, escribir, cerrar, rutas relativas y absolutas, liberación segura de recursos.
4. **Formatos de datos**: CSV, JSON, XML, YAML; serialización y deserialización.
5. **Argumentos de línea de comandos y variables de entorno**.
6. **Logging**: niveles de registro, diferencia con imprimir en pantalla.
7. **Expresiones regulares**: sintaxis básica, búsqueda, extracción y validación.

### 🛠 Mini proyecto 5

Gestor de tareas (to-do) por consola con persistencia en archivo JSON, con manejo de errores y argumentos de línea de comandos.

---

## Etapa 6: Programación orientada a objetos (POO)

1. **Clases y objetos**: atributos, métodos, constructores.
2. **Los cuatro pilares**: encapsulación, abstracción, herencia, polimorfismo.
3. **Modificadores de acceso**: público, privado, protegido.
4. **Miembros estáticos vs. de instancia**.
5. **Interfaces y clases abstractas**.
6. **Composición vs. herencia**: cuándo preferir cada una.
7. **Métodos especiales**: igualdad, representación en texto, comparación, iteración.
8. **Genéricos/plantillas** (donde el lenguaje los tenga).
9. **Principios SOLID** (introducción) y diseño de clases cohesivas.
10. **Otros paradigmas**: programación funcional, imperativa, declarativa; cuándo cada una aporta.

### 🛠 Mini proyecto 6

Sistema de biblioteca o inventario con clases (Libro, Usuario, Préstamo), herencia y persistencia en archivo.

---

## Etapa 7: Algoritmos y estructuras avanzadas

1. **Análisis de complejidad**: notación Big O, tiempo vs. espacio.
2. **Búsqueda**: lineal, binaria.
3. **Ordenamiento**: burbuja, inserción, selección, merge sort, quick sort.
4. **Listas enlazadas** (simples y dobles).
5. **Árboles**: binarios, árboles de búsqueda, recorridos (inorden, preorden, postorden).
6. **Grafos**: representación, recorridos BFS y DFS, camino más corto (conceptos).
7. **Heaps y colas de prioridad**.
8. **Tablas hash**: colisiones y cómo funcionan por dentro.
9. **Técnicas algorítmicas**: divide y vencerás, programación dinámica, backtracking, algoritmos voraces (greedy), dos punteros, ventana deslizante.
10. **Resolución de problemas**: practicar con ejercicios tipo LeetCode/HackerRank.

### 🛠 Mini proyecto 7

Buscador de rutas en un laberinto o mapa (BFS/DFS) y un visualizador por consola de algoritmos de ordenamiento comparando tiempos.

---

## Etapa 8: Herramientas profesionales

1. **Control de versiones con Git**: commit, ramas, merge, resolución de conflictos, pull requests, GitHub/GitLab.
2. **Depuración (debugging)**: breakpoints, inspección de variables, traza de ejecución.
3. **Pruebas automatizadas**: unitarias, de integración, TDD, mocks, cobertura.
4. **Entornos y dependencias**: entornos virtuales/aislados, archivos de dependencias, versionado semántico.
5. **Calidad de código**: linters, formateadores, revisión de código (code review), refactorización.
6. **Documentación**: comentarios útiles, README, docstrings, documentación de API.
7. **Terminal avanzada**: scripting, pipes, automatización de tareas.
8. **Empaquetado y distribución** de tu código.

### 🛠 Mini proyecto 8

Retomar un proyecto anterior y llevarlo a nivel profesional: repositorio en Git, pruebas unitarias, linter, README y empaquetado instalable.

---

## Etapa 9: Concurrencia, redes y datos

1. **Procesos vs. hilos**: concurrencia vs. paralelismo.
2. **Programación asíncrona**: async/await, promesas/futuros, event loop.
3. **Problemas de concurrencia**: condiciones de carrera, bloqueos (locks), deadlocks.
4. **Fundamentos de redes**: modelo cliente-servidor, TCP/IP, HTTP, DNS, sockets.
5. **APIs REST**: métodos HTTP, códigos de estado, consumir una API, autenticación (tokens, OAuth a nivel conceptual).
6. **Crear una API sencilla** con un framework del lenguaje.
7. **Bases de datos relacionales**: SQL (SELECT, INSERT, UPDATE, DELETE, JOIN), normalización, índices, transacciones.
8. **Bases de datos no relacionales**: documentos, clave-valor; cuándo usarlas.
9. **ORMs** y acceso a datos desde el código.

### 🛠 Mini proyecto 9

API REST de un sistema de notas o tareas con base de datos, y un script que consuma una API pública (clima, divisas) de forma asíncrona.

---

## Etapa 10: Arquitectura, seguridad y despliegue

1. **Patrones de diseño**: Singleton, Factory, Observer, Strategy, Decorator, MVC.
2. **Arquitectura de software**: capas, monolito vs. microservicios, principios de diseño limpio.
3. **Seguridad básica**: validación de entradas, inyección SQL, XSS, manejo de contraseñas (hashing), secretos y variables de entorno, principio de mínimo privilegio.
4. **Rendimiento**: profiling, caché, optimización con criterio.
5. **Contenedores**: Docker a nivel básico.
6. **CI/CD**: automatizar pruebas y despliegues.
7. **Despliegue en la nube**: conceptos de servidores, hosting y servicios gestionados.
8. **Observabilidad**: logs, métricas, monitoreo.

### 🛠 Proyecto integrador final

Aplicación completa de tu elección (por ejemplo, gestor de finanzas personales o plataforma de reservas) con:

- Backend con API y base de datos
- Pruebas automatizadas
- Contenerización con Docker
- Pipeline de CI/CD
- Despliegue público y documentación

---

## Etapa 11 (transversal): Hábitos de un programador sólido

- **Leer código ajeno** y documentación oficial con soltura.
- **Estimar y planificar** tareas; metodologías ágiles (Scrum/Kanban) a nivel conceptual.
- **Aprender un segundo lenguaje** de otro paradigma para consolidar los conceptos.
- **Contribuir a código abierto** o revisar proyectos de terceros.
- **Practicar de forma constante**: katas, proyectos propios, retos semanales.

---

## Notas

El contenido de este temario fue generado por [Claude](https://claude.ai/).

### Cómo usar este temario

- Las etapas **0 a 6** dan el dominio general del lenguaje; las **7 a 10** te llevan a nivel de desarrollador completo.
- No avances de etapa sin terminar su mini proyecto: ahí se consolida lo aprendido.
- Al terminar la etapa 6, es buen momento para decidir una especialización (web, datos, automatización, móvil, sistemas, etc.).
