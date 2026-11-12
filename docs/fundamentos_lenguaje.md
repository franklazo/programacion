# Fundamentos del lenguaje

## Bloque A

Salida, variables y asignación:

1. **Hola mundo personalizado**: imprime tu nombre, edad y ciudad en tres líneas distintas.
1. **Una sola línea**: imprime los mismos tres datos en una sola línea separados por comas, sin escribir el texto "a mano" tres veces (usa variables).
1. **Intercambio de variables**: dadas `a = 5` y `b = 9`, intercámbialas (a) con una variable auxiliar y (b) sin ella.
1. **Trazado a mano**: predice, sin ejecutar, el valor final de cada variable y luego verifica.

    ```text
    x = 3
    y = x
    x = x + 2
    y = y * x
    ```

1. **Constantes**: define el valor de π y el IGV como constantes y úsalos en un cálculo, sin repetir el número en el código.
1. **Caracteres especiales**: imprime comillas dobles, comillas simples, una barra invertida y un salto de línea dentro de un texto.

## Bloque B

Tipos de datos y conversiones:

1. **Descubre el tipo**: imprime el tipo de `42`, `42.0`, `"42"`, `true`, `'4'` y el resultado de `7 / 2`. Explica cada uno.
1. **División entera vs. decimal**: calcula `7 / 2`, `7 // 2` (o su equivalente) y `7 % 2`. Entiende en qué lenguajes cambia el resultado según los tipos.
1. **Suma de textos vs. números**: ¿qué ocurre con `"5" + "3"` y con `5 + 3`? ¿Y con `"5" + 3`? Documenta el comportamiento de tu lenguaje.
1. **Casting básico**: convierte `"123"` a entero, `3.99` a entero (¿trunca o redondea?), y `7` a texto.
1. **Error de precisión**: calcula `0.1 + 0.2` y explica por qué no da exactamente `0.3`. (Representación binaria de flotantes.)
1. **Límites de los enteros**: investiga el valor máximo de un entero en tu lenguaje y qué ocurre al superarlo (desbordamiento u otro comportamiento).
1. **Booleanos desde comparaciones**: imprime el resultado de `5 > 3`, `5 == 5.0`, `"a" == "A"` y `5 != 5`.
1. **Valor vacío**: declara una variable sin valor (nulo/vacío) e intenta usarla en una suma. Lee el error con calma.

## Bloque C

Operadores y expresiones:

1. **Precedencia**: evalúa a mano y luego en código `2 + 3 * 4`, `(2 + 3) * 4`, `2 ** 3 ** 2` (o equivalente) y `10 - 4 - 3`.
1. **Operadores de asignación compuesta**: dado `n = 10`, aplica `+= 5`, `*= 2`, `-= 3`, `%= 4` y registra el valor en cada paso.
1. **Lógicos con tabla de verdad**: construye a mano la tabla de `AND`, `OR` y `NOT` y verifícala con código para todas las combinaciones de `true/false`.
1. **Cortocircuito**: razona por qué `false AND (1/0 > 0)` no produce error en la mayoría de lenguajes.
1. **Pares e impares sin condicionales**: obtén `n % 2` para varios `n` y observa el patrón.
1. **Último y primeros dígitos**: dado un entero de 4 cifras, obtén su último dígito (`% 10`) y sus dos primeros (`// 100`).
1. **Descomposición de un número**: dado `n = 4729`, imprime cada dígito por separado usando solo división entera y módulo.

## Bloque D

Entrada y salida con cálculo:

1. **Saludo interactivo**: pide el nombre y la edad y responde: "Hola, X. En 10 años tendrás Y".
1. **Suma de dos números**: pide dos números al usuario y muestra su suma.
1. **Promedio de tres notas**: pide tres notas y muestra el promedio con 2 decimales.
1. **Área y perímetro**: para un rectángulo, un círculo y un triángulo (base y altura), pidiendo los datos al usuario.
1. **Conversor de temperatura**: °C a °F, y luego K a °C.
1. **Conversor de tiempo**: dado un número de segundos, muestra horas, minutos y segundos (ejemplo: 3725 s → 1 h 2 min 5 s).
1. **Cambio de monedas**: dado un monto en centavos, calcula cuántas monedas de 50, 20, 10, 5 y 1 se necesitan (versión sin condicionales: usa división entera y resto en cadena).
1. **Interés simple y compuesto**: capital, tasa y años como entradas; muestra el monto final.
1. **IMC**: pide peso y estatura y muestra el índice de masa corporal.
1. **Propina y total**: cuenta, porcentaje de propina y número de comensales; muestra cuánto paga cada uno.
1. **Velocidad media**: con distancia y tiempo, calcula la velocidad y conviértela de km/h a m/s.
1. **Hipotenusa**: teorema de Pitágoras con entrada del usuario (necesitas raíz cuadrada: practica importar una función de la librería estándar).

## Bloque E

Cadenas de texto:

1. **Longitud y acceso**: dada una palabra, muestra su longitud, su primera letra, su última letra y su letra central.
1. **Mayúsculas y minúsculas**: convierte un texto a mayúsculas, a minúsculas y a "tipo título".
1. **Concatenación e interpolación**: construye la misma frase con tres técnicas distintas (concatenar con `+`, formateo y plantillas/interpolación).
1. **Sub-cadenas (slicing)**: dado `"programación"`, extrae los primeros 3 caracteres, los últimos 4 y los del medio.
1. **Invertir una cadena** (sin usar el método de inversión, o usándolo y después buscando otra forma).
1. **Reemplazar y contar**: reemplaza todas las `a` por `*` y cuenta cuántas veces aparece una letra o palabra.
1. **Limpieza de entrada**: dado `"   Hola Mundo   "`, elimina espacios extremos y conviértelo a minúsculas.
1. **Inmutabilidad**: intenta cambiar un carácter de una cadena por índice y observa qué pasa; luego logra el cambio de otra manera.
1. **Repetición y formato**: imprime una línea de 30 guiones sin escribirlos uno por uno, y un texto centrado en un ancho de 40 caracteres.
1. **Separar y unir**: separa `"ana,luis,marta"` por comas, y vuelve a unirlo con guiones.
1. **Iniciales**: dado un nombre completo de tres palabras, muestra sólo las iniciales en mayúscula.
1. **Códigos de carácter**: obtén el código Unicode de `'A'` y `'a'`, y el carácter correspondiente al código 97. Entiende por qué un carácter es en el fondo un número.
1. **Texto con acentos y emojis**: calcula la longitud de `"canción"` y de un emoji; investiga por qué a veces la longitud no es la esperada (caracteres vs. bytes).
1. **Formato de factura**: imprime una tabla alineada con producto, cantidad y precio usando formateo de texto con anchos fijos.

## Bloque F

Problemas integradores:

1. **Boleta simple**: pide producto, precio unitario y cantidad; muestra subtotal, IGV y total con formato de moneda.
1. **Generador de usuario**: dado nombre y apellido, genera un usuario tipo `inicial + apellido` en minúsculas y un correo `usuario@dominio.com`.
1. **Reloj digital**: dados segundos desde medianoche, muestra la hora en formato `HH:MM:SS` con ceros a la izquierda.
1. **Ley del cambio**: dado un precio y el dinero entregado, calcula el vuelto y el desglose en billetes y monedas.
1. **Mensaje personalizado**: pide nombre, ciudad y hobby, y construye un párrafo corto que combine los tres datos con buen formato.
1. **Calculadora de edad aproximada**: dado el año de nacimiento y el año actual, calcula edad, años hasta los 100 y días vividos aproximados.
1. **Conversor de bases**: convierte un número a binario y hexadecimal con las funciones del lenguaje, y luego intenta explicar cómo se hace a mano.
