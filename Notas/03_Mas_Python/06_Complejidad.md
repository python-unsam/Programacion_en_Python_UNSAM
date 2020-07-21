[Contenidos](../Contenidos.md) \| [Anterior (6 Algoritmos de búsqueda)](06_5_BSec_BBin_Viejo.md) \| [Próximo (8 Figuritas)](07_NumPy_Arrays.md)

# 3.7 Complejidad de algoritmos

### Resumen de algoritmos de Búsqueda

1. La búsqueda de un elemento en una secuencia es un
algoritmo básico pero importante. El problema que intenta resolver puede
plantearse de la siguiente manera: Dada una secuencia de valores y un
valor, devolver el índice del valor en la secuencia, si se encuentra, de no
encontrarse el valor en la secuencia señalizarlo apropiadamente.

2. Una de las formas de resolver el problema es mediante la **búsqueda lineal**, que consiste en ir revisando uno a uno los elementos de
la secuencia y comparándolos con el elemento a buscar.  Este algoritmo no
requiere que la secuencia se encuentre ordenada, la cantidad de comparaciones
que realiza es proporcional a `len(secuencia)`.

3. Cuando la secuencia sobre la que se quiere buscar está ordenada, se
puede utilizar el algoritmo de **búsqueda binaria**.  Al estar ordenada
la secuencia, se puede desacartar en cada paso la mitad de los elementos,
quedando entonces con una eficiencia algorítmica proporcional a
`log2(len(secuencia))`.

El análisis del comportamiento de un algoritmo puede ser muy engañoso
si se tiene en cuenta el mejor caso, por eso suele ser mucho más
ilustrativo tener en cuenta el **peor caso**.  En algunos casos
particulares podrá ser útil tener en cuenta, además, el **caso promedio**.


### Insertar un elemento en una lista
Uno de los problemas de la búsqueda binaria es que requiere que la lista esté ordenada. Si la lista se encuentra ordenada podemos mantener el orden evitando adjuntar nuevos elementos de forma desordenada.

Escribí una función `insertar(l,e)` que recibe una lista ordenada *l* y un elemento y *e*. Si el elemento se encuentra en la lista solamente devuelve su posición; si no se encuentra en la lista, lo inserta en la posición correcta para mantener el orden. En ambos casos debe devolver su posición.

Usá la función `busqueda_binaria(l,e)` del [Ejercicio 3.13](../03_Mas_Python/06_5_BSec_BBin_Viejo.md#ejercicio-313-búsqueda-binaria) para determinar si $e$ se encuentra en $l$.

[Contenidos](../Contenidos.md) \| [Anterior (6 Algoritmos de búsqueda)](06_5_BSec_BBin_Viejo.md) \| [Próximo (8 Figuritas)](07_NumPy_Arrays.md)

