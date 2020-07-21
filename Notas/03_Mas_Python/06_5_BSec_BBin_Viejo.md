[Contenidos](../Contenidos.md) \| [Anterior (5 Búsqueda binaria)](05_BusqBinaria.md) \| [Próximo (7 Complejidad de algoritmos)](06_Complejidad.md)

# 3.6 Algoritmos de búsqueda




## Búsqueda sobre listas ordenadas

Si podemos suponer que la lista está previamente ordenada,
¿podemos encontrar una manera más eficiente de buscar elementos sobre ella?

En principio hay una modificación muy simple que podemos hacer sobre el
algoritmo de búsqueda lineal: si estamos buscando el elemento *e* en una
lista que está ordenada de menor a mayor, en cuanto encontremos algún elemento
mayor a *e* podemos estar seguros de que *e* no está en la lista, por lo que no
es necesario continuar recorriendo el resto.

### Ejercicio 3.11: Búsqueda lineal sobre listas ordenadas.Modificar la búsqueda lineal para el caso de listas ordenadas.
En el peor caso, ¿cuál es nuestra nueva hipótesis sobre comportamiento del
algoritmo? ¿Es realmente más eficiente?}

### Búsqueda binaria

¿Podemos hacer algo mejor? Trataremos de aprovechar el hecho de que la lista
está ordenada y vamos a hacer algo distinto: nuestro espacio de búsqueda se
irá achicando a segmentos cada vez menores de la lista original.
La idea es descartar segmentos de la lista donde el valor seguro que no puede
estar:

1. Consideramos como segmento inicial de búsqueda a la lista completa.

2. Analizamos el punto medio del segmento (el valor central); si es el valor
buscado, devolvemos el índice del punto medio.

3. Si el valor central es mayor al buscado, podemos descartar el segmento
que está desde el punto medio hacia la a derecha.

4. Si el valor central es menor al buscado, podemos descartar el segmento
que está desde el punto medio hacia la izquierda.

5. Una vez descartado el segmento que no nos interesa, volvemos a analizar
el segmento restante, de la misma forma.

6. Si en algún momento el segmento a analizar tiene longitud 0
significa que el valor buscado no se encuentra en la lista.


Para señalar la porción del segmento que se está analizando a cada paso,
utilizaremos dos variables (`izq` y `der`) que
contienen la posición de inicio y la posición de fin del segmento que se
está considerando. De la misma manera usaremos la varible `medio`
para contener la posición del punto medio del segmento.

A continuación ilustramos qué pasa cuando se busca
el valor 18 en la lista `[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]`.

![Búsqueda Binaria](./bbin.png)
Ejemplo de una búsqueda usando el algoritmo de búsqueda binaria.
Como no se encontró al valor buscado, devuelve -1.

En el archivo `bbin.py` mostramos una posible implementación de
este algoritmo, incluyendo una instrucción de depuración (debug) con `print` para verificar su funcionamiento.

A continuación varias ejecuciones de prueba:

```python
>>> busqueda_binaria([1, 3, 5], 0)
[DEBUG] izq: 0 der: 2 medio: 1
[DEBUG] izq: 0 der: 0 medio: 0
-1
>>> busqueda_binaria([1, 3, 5], 1)
[DEBUG] izq: 0 der: 2 medio: 1
[DEBUG] izq: 0 der: 0 medio: 0
0
>>> busqueda_binaria([1, 3, 5], 2)
[DEBUG] izq: 0 der: 2 medio: 1
[DEBUG] izq: 0 der: 0 medio: 0
-1
>>> busqueda_binaria([1, 3, 5], 3)
[DEBUG] izq: 0 der: 2 medio: 1
1
>>> busqueda_binaria([1, 3, 5], 5)
[DEBUG] izq: 0 der: 2 medio: 1
[DEBUG] izq: 2 der: 2 medio: 2
2
>>> busqueda_binaria([1, 3, 5], 6)
[DEBUG] izq: 0 der: 2 medio: 1
[DEBUG] izq: 2 der: 2 medio: 2
-1
>>> busqueda_binaria([], 0)
-1
>>> busqueda_binaria([1], 1)
[DEBUG] izq: 0 der: 0 medio: 0
0
>>> busqueda_binaria([1], 3)
[DEBUG] izq: 0 der: 0 medio: 0
-1
```

**Pregunta**: En la línea `medio = (izq + der) // 2` efectuamos la división usando el operador `//` en lugar de `/`. ¿Qué pasa su usáramos `/`?

### ¿Cuántas comparaciones hace este programa?

Para responder esto pensemos en el peor caso, es decir, que se descartaron
varias veces partes del segmento para finalmente llegar a un segmento vacío y
el valor buscado no se encontraba en la lista.

En cada paso el segmento se divide por la mitad y se desecha una de esas
mitades, y en cada paso se hace una comparación con el valor buscado. Por lo
tanto, la cantidad de comparaciones que hacen con el valor buscado es
aproximadamente igual a la cantidad de pasos necesarios para llegar a un
segmento de tamaño 1.
Veamos el caso más sencillo para razonar, y supongamos que la longitud de la
lista es una potencia de 2, es decir `len(lista)`*= 2^k*:

1. Luego del primer paso, el segmento a tratar es de tamaño *2^k*.
2. Luego del segundo paso, el segmento a tratar es de tamaño *2^(k-1)*.
3. Luego del tercer paso, el segmento a tratar es de tamaño *2^(k-2)*.
...
4. Luego del paso *k*, el segmento a tratar es de tamaño *2^(k-k)=1*.


Por lo tanto este programa hace aproximadamente *k* comparaciones con el valor
buscado cuando `len(lista)`*= 2^k*.
Pero si despejamos *k* de la ecuación anterior, podemos ver que este programa
realiza aproximadamente `log2(len(lista)` comparaciones.

Cuando `len(lista)` no es una potencia de 2 el razonamiento es menos
prolijo, pero también vale que este programa realiza aproximadamente
`log2(len(lista))` comparaciones. Concluimos entonces que:

### Comparción entre ambos métodos

Veamos un ejemplo para entender cuánto más eficiente es la búsqueda binaria.
Supongamos que tenemos una lista con un millón de elementos.

1. El algoritmo de búsqueda lineal hará una cantidad de operaciones proporcional a un millón; es decir que en el peor caso hará 1,000,000 comparaciones, y en un caso promedio, 500,000 comparaciones.
2. El algoritmo de búsqueda binaria hará como máximo *log2(1,000,000)*
comparaciones, o sea ¡no más que 20 comparaciones!.

*Conclusión*: Si una lista está previamente ordenada, podemos utilizar el
algoritmo de búsqueda binaria, cuyo comportamiento es proporcional al
*logaritmo* de la cantidad de elementos de la lista, y por lo tanto
muchísimo más eficiente que la búsqueda lineal, espcialmente si la lista es larga.




\newpage
\section{Ejercicios}

\extractionlabel{guia}
\begin{ejercicio}
Escribir una función que reciba una lista desordenada y un elemento, que:
\begin{partes}
\item Busque todos los elementos coincidan con el pasado por parámetro y
devuelva la cantidad de coincidencias encontradas.
\item Busque la primera coincidencia del elemento en la lista y devuelva su
posición.
\item Utilizando la función anterior, busque todos los elementos que coincidan
con el pasado por parámetro y devuelva una lista con las posiciones.
\end{partes}
\end{ejercicio}


\extractionlabel{guia}
\begin{ejercicio}
Escribir una función que reciba una lista de números no ordenada, que:
\begin{partes}
\item Devuelva el valor máximo.
\item Devuelva una tupla que incluya el valor máximo y su posición.
\item ¿Qué sucede si los elementos son cadenas de caracteres?
\end{partes}
{\bf Nota:} no utilizar !lista.sort()!
\end{ejercicio}


\extractionlabel{guia}
\begin{ejercicio}
{\bf Agenda simplificada} \\
Escribir una función que reciba una cadena a buscar y una lista de tuplas
(nombre\_completo, telefono), y busque dentro de la lista, todas las
entradas que contengan en el nombre completo la cadena recibida (puede
ser el nombre, el apellido o sólo una parte de cualquiera de ellos).
Debe devolver una lista con todas las tuplas encontradas.
\end{ejercicio}


\extractionlabel{guia}
\begin{ejercicio}
{\bf Sistema de facturación simplificado} \\
Se cuenta con una lista ordenada de productos, en la que uno consiste en
una tupla de (identificador, descripción, precio), y una lista de los
productos a facturar, en la que cada uno consiste en una tupla de
(identificador, cantidad). \\
Se desea generar una factura que incluya la cantidad, la descripción, el
precio unitario y el precio total de cada producto comprado, y al final
imprima el total general. \\
Escribir una función que reciba ambas listas e imprima por
pantalla la factura solicitada.
\end{ejercicio}


\extractionlabel{guia}
\begin{ejercicio}
Escribir una función que reciba una lista ordenada y un elemento. Si el
elemento se encuentra en la lista, debe encontrar su posición mediante
búsqueda binaria y devolverlo.  Si no se encuentra, debe agregarlo a la
lista en la posición correcta y devolver esa nueva posición. (No utilizar
!lista.sort()!.)
\end{ejercicio}


\newpage
\begin{subappendices}
\section{Filtros, transformaciones y acumulaciones}

Supongamos que manejamos una librería, y disponemos de una base de datos con el
inventario. Cada entrada del inventario está compuesta por el título del libro,
el autor, la cantidad disponible y el precio. Por ejemplo:

\begin{center}
\small
\rowcolors[]{2}{}{light-gray}
\begin{tabular}{p{8cm} p{3cm} r r}
{\bf Título} & {\bf Autor} & {\bf Cantidad} & {\bf Precio} \\
\hline
The Art of Computer Programming, Volumes 1-4 & Donald Knuth & 12 & 179.62 \\
Concrete Mathematics: A Foundation for Computer Science & Donald Knuth & 5 & 54.77 \\
The Pragmatic Programmer: From Journeyman to Master & Andrew Hunt, David Thomas & 3 & 33.17 \\
Clean Code: A Handbook of Agile Software Craftsmanship & Robert C. Martin & 7 & 38.99 \\
Code Complete: A Practical Handbook of Software Construction & Steve McConnell & 0 & 29.97 \\
Learning Python & Mark Lutz & 4 & 40.95 \\
\ldots & \ldots & \ldots & \ldots \\ \hline
\end{tabular}
\end{center}

Podemos representar nuestro inventario en Python utilizando una lista de
tuplas:

```python
inventario = [
    ('The Art of Computer Programming, Volumes 1-4',
     'Donald Knuth', 12, 179.62),
    ('Concrete Mathematics: A Foundation for Computer Science',
     'Donald Knuth', 5, 54.77),
    ('The Pragmatic Programmer: From Journeyman to Master',
     'Andrew Hunt and David Thomas', 3, 33.17),
    ...
]
```

Una vez que disponemos de nuestro inventario en una estructura de datos,
podemos sacar todo tipo de
reportes: la cantidad total de libros, el valor total del
inventario, el precio promedio por libro, etc.

Veamos un ejemplo simple: supongamos que queremos obtener la cantidad total de
libros de un autor determinado. Podemos diseñar un algoritmo muy simple:

```python
def total_libros_autor(inventario, autor_buscado):
    total = 0
    for titulo, autor, cantidad, precio in inventario:
        if autor == autor_buscado:
            total += cantidad
    return total
```

Otro ejemplo: queremos obtener la cantidad de títulos de los cuales no hay
suficiente stock (menos de 5 unidades):

```python
def cantidad_poco_stock(inventario):
    total = 0
    for titulo, autor, cantidad, precio in inventario:
        if cantidad < 5:
            total += 1
    return total
```

¿Y si quisiéramos obtener la lista de títulos cuyo precio supera los \$100?

```python
def titulos_caros(inventario):
    titulos = []
    for titulo, autor, cantidad, precio in inventario:
        if precio > 100:
            titulos.append(titulo)
    return titulos
```

Acabamos de ``inventar'' tres algoritmos para resolver tres problemas
diferentes\ldots\ pero ¿son realmente diferentes? ¿No tienen nada en común?

Si observamos con detenimiento, los tres algoritmos comparten un mismo esquema:

\begin{codigo-nohl-sn}
def f(L):
    inicializar acumulador
    por cada elemento en el la lista L:
        si se cumple alguna condición:
            hacer algún cálculo en base al elemento y acumular
    devolver acumulador
\end{codigo-nohl-sn}

Y este esquema en el fondo puede pensarse como una composición de tres
problemas más simples:

\begin{enumerate}
    \item A partir de una lista, \emph{filtrar} la lista según una condición
        determinada y obtener una lista con los elementos que pasan la
        condición.
    \item A partir de una lista, aplicar una \emph{transformación} a cada elemento
        y obtener una lista con los resultados.
    \item A partir de una lista, \emph{acumular} los elementos según un
        criterio determinado.
\end{enumerate}

% TODO: dibujo

Por ejemplo, podemos repensar nuestro primer algoritmo, que nos permitía calcular
la cantidad total de libros de un determinado autor, como:

\begin{enumerate}
    \item A partir del inventario, \emph{filtrar} según el autor:
        el resultado será una lista que contiene los libros del autor buscado.
    \item A partir de la lista obtenida, \emph{transformar} cada una de las tuplas
        `(titulo, autor, cantidad, precio)` para descartar todo menos la
        `cantidad`. Es decir, nos quedamos con una lista de números
        enteros, donde cada número representa una cantidad de libros.
    \item A partir de la lista obtenida, \emph{acumular} los elementos sumando uno
        a uno.
\end{enumerate}

Una ventaja de pensar el algoritmo de esta manera es que Python nos provee una
forma muy fácil de implementar filtros y transformaciones: las \emph{listas por
comprensión}.

\subsection{Listas por comprensión}

Concentrémonos en el filtro según el autor propuesto en el ejemplo anterior.
Una forma de implementarlo es:

```python
def filtrar_autor(inventario, autor_buscado):
    filtrado = []
    for libro in inventario:
        if libro[2] == autor_buscado:
            filtrado.append(libro)
    return filtrado
```

En Python podemos obtener el mismo resultado utilizando una \emph{lista por
comprensión}:

```python
def filtrar_autor(inventario, autor_buscado):
    return (@[libro for libro in inventario if libro[2] == autor_buscado]@)
```

Lo que vemos aquí es una sintaxis especial, que nos permite crear una lista
filtrando una secuencia según una condición:

```python
(@[@)<variable> (@for@) <variable> (@in@) <secuencia> (@if@) <condicion>(@]@)
```

Para aplicar la transformación propuesta (quedándonos únicamente con las
cantidades), podríamos implementarlo de esta manera:

```python
def obtener_cantidades(inventario):
    cantidades = []
    for titulo, autor, cantidad, precio in inventario:
        cantidades.append(cantidad)
    return cantidades
```

Pero en este caso también podemos obtener el mismo resultado con una lista por
comprensión:

```python
def obtener_cantidades(inventario):
    return (@[cantidad for titulo, autor, cantidad, precio in inventario]@)
```

En este caso la sintaxis utilizada es un poco diferente:

```python
(@[@)<expresión> (@for@) <variable> (@in@) <secuencia>(@]@)
```

Opcionalmente podemos combinar el filtro y la transformación en una única lista
por comprensión:

```python
def cantidades_autor(inventario, autor_buscado):
    return [
        cantidad
        for titulo, autor, cantidad, precio in inventario
        if autor == autor_buscado
    ]
```

\begin{observacion}
Es decir que la sintaxis general de las listas por comprensión es:
```python
(@[@)<expresión> (@for@) <variable> (@in@) <secuencia> (@if@) <condicion>(@]@)
```
\end{observacion}

Volviendo a nuestro problema inicial: obtener la cantidad total de libros del
autor; ya tenemos una forma de filtrar y transformar, y lo único que nos falta
es la acumulación. Pero recordemos que ya conocíamos una forma simple de
acumular sumando elementos: ¡la función `sum`!

```python
def total_libros_autor(inventario, autor_buscado):
    return sum([
        cantidad
        for titulo, autor, cantidad, precio in inventario
        if autor == autor_buscado
    ])
```

Planteemos ahora las soluciones para los otros dos problemas utilizando
filtros, transformaciones y acumulaciones. Nuestro segundo problema era obtener
la cantidad de títulos de los cuales no hay suficiente stock.

\begin{enumerate}
    \item Filtramos según la cantidad de stock, quedándonos con los libros
        para los cuales `cantidad < 5`.
    \item No es necesario aplicar una transformación.
    \item Solo necesitamos la cantidad de títulos, y eso es simplemente la
        cantidad de elementos de la lista producida en el paso anterior. Es
        decir que nuestra función de acumulación es `len`.
\end{enumerate}

```python
def cantidad_poco_stock(inventario):
    return len([libro for libro in inventario if libro[3] < 5])
```

Nuestro tercer problema era obtener la lista de títulos cuyo precio supera los
\$100.

\begin{enumerate}
    \item Filtramos según el precio, quedándonos con la lista de libros con
        `precio > 100`.
    \item Transformamos cada tupla quedándonos únicamente con el `titulo`.
    \item No es necesario aplicar una acumulación.
\end{enumerate}

```python
def titulos_caros(inventario):
    return [
        titulo
        for titulo, autor, cantidad, precio in inventario
        if precio > 100
    ]
```

Comparando estas soluciones con las primeras tres soluciones
propuestas, vemos que son dos estilos de programación diferentes:

\begin{itemize}
    \item Las primeras soluciones corresponden a un estilo más \emph{procedural} e
        \emph{imperativo}. Cuando pensamos en este estilo nos concentramos en
        dar órdenes para especificar \emph{cómo} queremos que la computadora
        resuelva el problema, paso por paso.
    \item Las soluciones planteadas utilizando filtros, transformaciones y
        acumulaciones corresponden a un estilo más \emph{funcional} y
        \emph{declarativo}, en el cual dividimos el problema en sub-problemas
        más simples, y nos concentramos en especificar cómo es el flujo de datos.
\end{itemize}

La discusión acerca de si uno de los dos estilos es ``mejor'' que el otro queda
fuera del alcance de este apunte, pero en general se considera que el uso de
listas por comprensión es \emph{idiomático} en Python. Es decir, los
programadores Python experimentados van a preferir leer y escribir código que
utilice listas por comprensión en lugar de implementar los filtros y
transformaciones a mano.

Por último, observamos que las listas por comprensión ofrecen una alternativa
sintáctica a las funciones `map` y `filter`, explicadas en el
Apéndice~\ref{map-filter}. Dejamos como ejercicio implementar las funciones
`total_libros_autor`, `cantidad_poco_stock` y `titulos_caros` en términos de
`map` y `filter`.
\end{subappendices}

-----------------------------------------
-----------
---------

### Ejercicio 3.12: Búsqueda secuencial
Búsqueda secuencial `b_sec.py`

### Ejercicio 3.13: Búsqueda binaria
Búsqueda binaria `b_bin.py`



[Contenidos](../Contenidos.md) \| [Anterior (5 Búsqueda binaria)](05_BusqBinaria.md) \| [Próximo (7 Complejidad de algoritmos)](06_Complejidad.md)

