# Temario de programación

El contenido de este temario fue generado por [Claude](https://claude.ai/).

Este temario te lleva de cero a construir por tu cuenta utilidades y herramientas personales: gestores de información, herramientas para tu sistema operativo, juegos sencillos y soluciones a problemas abstractos. Cada tema aplica igual en Python, JavaScript, Java, C#, Go, etc.; solo cambia la sintaxis. No busca formar a un especialista ni preparar para un equipo de desarrollo: esos temas aparecen solo como opcionales.

**Cómo está organizado:** las etapas 0 a 6 son el núcleo del lenguaje, la 7 introduce cómo dar interfaz a tus programas y una sección final reúne temas opcionales para explorar hacia dónde especializarte.

---

## Etapa 0: Preparación y mentalidad

1. **Qué es programar**: algoritmos, instrucciones, máquina y lenguaje.
2. **Cómo se ejecuta un programa**: compilado vs. interpretado vs. híbrido; código fuente, bytecode, binario.
3. **Cómo funciona una computadora por dentro (versión ligera)**: CPU, memoria, bytes, sistemas numéricos (binario, hexadecimal) y por qué `0.1 + 0.2` no da exactamente `0.3`.
4. **Entorno de trabajo**: editor/IDE, terminal básica, instalación del lenguaje, ejecutar un archivo.
5. **Pensamiento computacional**: descomposición de problemas, abstracción, patrones, pseudocódigo y diagramas de flujo.
6. **Leer errores**: tipos de error (sintaxis, ejecución, lógica) y cómo interpretar un mensaje de error.
7. **Aprender a aprender**: formular buenas búsquedas, leer documentación oficial y usar asistentes de IA para aprender (pedir explicaciones y revisar tu código, sin copiar sin entender).

---

## Etapa 1: Fundamentos del lenguaje

1. **Sintaxis básica**: instrucciones, comentarios, indentación/bloques, convenciones de nombres.
2. **Variables y constantes**: declaración, asignación, alcance básico.
3. **Tipos de datos primitivos**: enteros, decimales, booleanos, caracteres, texto, nulo/vacío.
4. **Tipos y conversión**: qué es un tipo, conversión (casting) entre tipos; tipado estático vs. dinámico a nivel introductorio.
5. **Operadores**: aritméticos, comparación, lógicos, asignación, precedencia.
6. **Entrada y salida**: leer del usuario, imprimir, formatear texto.
7. **Cadenas de texto**: concatenación, interpolación, métodos comunes, inmutabilidad, codificación (Unicode/UTF-8).
8. **Git básico**: `init`, `add`, `commit`, `log`, repositorio remoto y `.gitignore`. Desde el primer mini proyecto, versiona tu código.

### 🛠 Mini proyecto 1

Calculadora básica por consola (suma, resta, multiplicación, división) y un conversor de unidades (°C ↔ °F, km ↔ millas). Súbelo a un repositorio.

---

## Etapa 2: Control de flujo

1. **Condicionales**: `if / else if / else`, condiciones anidadas, operador ternario.
2. **Selección múltiple**: `switch/match`.
3. **Bucles**: `while`, `for`, `for-each`/iteración sobre colecciones, `do-while` donde exista.
4. **Control de bucles**: `break`, `continue`, bucles anidados, bucles infinitos y cómo evitarlos.
5. **Lógica booleana**: tablas de verdad, evaluación en cortocircuito, valores "truthy/falsy".
6. **Patrones algorítmicos básicos**: contadores, acumuladores, banderas (flags), búsqueda del máximo/mínimo.
7. **Depuración (debugging)**: breakpoints, ejecución paso a paso, inspección de variables, traza de ejecución.

### 🛠 Mini proyecto 2

Juego de adivinar el número y un validador de contraseñas con reglas (longitud, mayúsculas, números). Depura al menos un error real con el debugger.

---

## Etapa 3: Funciones y modularidad

1. **Funciones**: definición, llamada, parámetros, valores de retorno.
2. **Parámetros avanzados**: valores por defecto, argumentos nombrados, número variable de argumentos.
3. **Alcance (scope)**: local vs. global, ciclo de vida de variables.
4. **Recursión**: caso base, caso recursivo, pila de llamadas, cuándo conviene y cuándo no.
5. **Buenas prácticas**: funciones pequeñas, un propósito por función, nombres descriptivos, documentación.
6. **Módulos y paquetes**: dividir código en archivos, importar/exportar, librería estándar, gestores de dependencias.

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
7. **Mutabilidad, copias y referencias**: paso por valor vs. por referencia, copias superficiales vs. profundas, qué se copia realmente y qué no.
8. **Funciones como valores**: callbacks, funciones anónimas/lambdas, closures (introducción), funciones de orden superior.
9. **Transformaciones funcionales**: map, filter, reduce, comprensiones de lista.
10. **Elegir la estructura adecuada** según el problema.

### 🛠 Mini proyecto 4

Gestor de contactos en memoria (agregar, buscar, editar, eliminar) y un contador de frecuencia de palabras en un texto.

---

## Etapa 5: Manejo de errores, archivos y datos

1. **Excepciones**: `try / catch / finally`, lanzar errores propios, jerarquía de errores.
2. **Programación defensiva**: validar entradas, precondiciones, valores límite.
3. **Archivos y carpetas**: abrir, leer, escribir y cerrar archivos de texto, rutas relativas y absolutas, liberación segura de recursos; listar carpetas, copiar, mover y renombrar archivos.
4. **Formatos de datos**: CSV, JSON, XML, YAML; serialización y deserialización.
5. **Fechas y horas**: formatos, zonas horarias, cálculos entre fechas, errores típicos.
6. **Argumentos de línea de comandos y variables de entorno**, y cómo manejar secretos (claves, contraseñas) sin subirlos a Git.
7. **Logging**: niveles de registro, diferencia con imprimir en pantalla.
8. **Pruebas unitarias básicas**: escribir y ejecutar tus primeras pruebas sobre funciones sencillas.
9. **Expresiones regulares (introducción)**: búsqueda, extracción y validación simples.

### 🛠 Mini proyecto 5

Gestor de tareas (to-do) por consola con persistencia en archivo JSON, fechas límite, manejo de errores, argumentos de línea de comandos y algunas pruebas unitarias.

---

## Etapa 6: Programación orientada a objetos (POO)

1. **Clases y objetos**: atributos, métodos, constructores.
2. **Los cuatro pilares**: encapsulación, abstracción, herencia, polimorfismo.
3. **Modificadores de acceso**: público, privado, protegido.
4. **Miembros estáticos vs. de instancia**.
5. **Interfaces y clases abstractas**.
6. **Composición vs. herencia**: cuándo preferir cada una.
7. **Métodos especiales**: igualdad, representación en texto, comparación, iteración.
8. **Genéricos/plantillas** *(opcional)*: donde el lenguaje los tenga.
9. **Diseño de clases cohesivas y principios SOLID** *(opcional, introducción)*.
10. **Otros paradigmas**: programación funcional, imperativa, declarativa; cuándo cada una aporta.

### 🛠 Mini proyecto 6

Sistema de biblioteca o inventario con clases (Libro, Usuario, Préstamo), herencia, persistencia en archivo y pruebas unitarias de las clases principales.

> **Punto de decisión:** al terminar la etapa 6 ya dominas el lenguaje a nivel general. Es buen momento para decidir hacia dónde orientarte (web, datos, automatización, móvil, sistemas, etc.). Después, el temario se puede extender con un bloque propio para ese campo; mientras decides, la sección de temas opcionales te deja probar varios.

---

## Etapa 7: Formas de dar interfaz a tu aplicación (introducción)

1. **Aplicaciones de consola bien hechas**: menús, mensajes claros y ayuda.
2. **Interfaz gráfica de escritorio sencilla (introducción)**: ventanas, botones y eventos con una librería del lenguaje.
3. **Nociones de web**: qué son HTML, CSS y JavaScript, y cómo una página puede mostrar los datos de tu programa.
4. **Separar lógica e interfaz**: tu código principal no debe depender de cómo se muestra.

### 🛠 Mini proyecto 7

Tomar uno de tus proyectos anteriores (por ejemplo, el gestor de tareas o contactos) y darle una segunda interfaz: una GUI sencilla o una página web básica, reutilizando la misma lógica.

---

## Temas opcionales según tus intereses

Esta sección no es obligatoria: elige solo lo que te sirva para lo que quieras construir. Los temas generales sirven en cualquier camino; los demás apuntan a un campo de especialización.

### Temas generales

1. **Introducción breve a bases de datos (SQLite)**: qué es una tabla, consultas básicas (SELECT, INSERT, UPDATE, DELETE) y cuándo conviene usar una base de datos en vez de un archivo JSON.
2. **Automatización y herramientas del sistema operativo**: scripting en terminal, tareas programadas, atajos y utilidades de uso diario. El manejo básico de archivos y carpetas ya se vio en la etapa 5.
3. **Entornos, dependencias y empaquetado**: entornos virtuales, instalar librerías externas y distribuir tu utilidad para usarla en otro equipo. Sirve para aislar las librerías de cada proyecto y evitar conflictos entre ellos.
4. **Consumir una API pública (introducción)**: qué es HTTP y JSON en la práctica, y cómo traer datos (clima, divisas) a tus programas.
5. **Base mínima para trabajo en equipo**: Git con ramas y pull requests, pruebas automatizadas, linters, README y revisión de código, solo como idea general por si algún día quieres integrarte a un equipo.

### Temas que apuntan a un campo

1. **Algoritmos y computación científica** *(apunta a: ciencia y datos)*: notación Big O a nivel intuitivo, búsqueda lineal y binaria, ordenamientos simples, árboles y grafos (recorridos BFS y DFS). Es la puerta de entrada al cálculo numérico, las simulaciones y el análisis de datos, y sirve para resolver problemas abstractos.
2. **Juegos sencillos** *(apunta a: videojuegos)*: estado del juego, entrada del usuario y bucle de juego (game loop), apoyándote en la interfaz gráfica de la etapa 7.
3. **Desarrollo web (profundización)** *(apunta a: web)*: partiendo de las nociones de la etapa 7, cómo funciona un servidor web, crear una API sencilla y conectar una página con ella.
4. **Desarrollo móvil (introducción)** *(apunta a: apps móviles)*: qué cambia al programar para Android o iOS (pantallas táctiles, permisos, ciclo de vida de la app) y qué opciones hay para empezar.

### 🛠 Mini proyecto opcional

Elige uno según lo que hayas visto: una utilidad que automatice una tarea de tu sistema (por ejemplo, ordenar o renombrar archivos), un juego sencillo (ahorcado o snake) o llevar tu gestor de tareas a SQLite.

---

## Cómo usar este temario

- Las etapas **0 a 6** dan el dominio general del lenguaje; la **7** introduce cómo dar interfaz a tus apps, y los temas opcionales del final permiten profundizar según lo que quieras construir. Cuando decidas un campo de especialización, el temario se puede extender.
- **Criterio para avanzar:** no pases a la siguiente etapa hasta que su mini proyecto funcione sin mirar una solución. Si te atascas, usa la depuración y la documentación primero, y la ayuda externa después.
- **Tiempo orientativo** (a un ritmo de 5 a 8 horas por semana):
  - Etapas 0 a 2: 4 a 6 semanas
  - Etapas 3 y 4: 4 a 6 semanas
  - Etapa 5: 3 a 4 semanas
  - Etapa 6: 4 a 5 semanas
  - Etapa 7: 2 a 3 semanas, más 1 a 2 semanas por cada tema opcional que elijas
- Los **mini proyectos se versionan en Git** desde la etapa 1: tu repositorio será tu portafolio al terminar.
- **Hazlo tuyo:** al terminar cada mini proyecto, añade una función que tú realmente usarías. Así practicas con herramientas que te sirven de verdad.
- **Hábito constante:** practica con frecuencia (katas, proyectos propios, retos semanales) y acostúmbrate a leer código ajeno y documentación oficial.

opciones:

- [x] A
- [ ] B
- [ ] C
