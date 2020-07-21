[Contenidos](../Contenidos.md) \| [Anterior (7 Entorno de desarrollo integrado)](07_IDE.md) \| [Próximo (9 Cierre de la segunda clase)](10_CierreClase.md)

# 2.8 Listas y búsqueda lineal

En esta sección seguiremos usando Python, pero nos concentraremos en la parte algorítmica. Vas a escribir funciones sencillas (y no tanto) que realicen operaciones de bajo nivel sobre listas.

Este es un curso de Python y de algoritmos. Python es un lenguaje de alto nivel. Esto significa que con pocas instrucciones permite realizar operaciones muy complejas. Los lenguajes de bajo nivel están más cerca del lenguaje del procesador y programar en ellos por ejemplo, un análisis de datos, es mucho más tedioso.

Sin embargo, entre las cosas que trae resueltas Python hay algunos algoritmos que nos interesa que vuelvas a escribir vos, por motivos didácticos. En lo que sigue te vamos a pedir en algunas ocasiones que no uses toda la potencia y simpleza de Python sino que te arremangues y escribas algunas funciones desde los primeros rudimentos.

Queremos mostrarte en ejemplos concretos cómo distintas maneras de resolver  un mismo problema pueden dar lugar a algoritmos con eficiencias muy diferentes. A veces una es mejor para un uso y la otra para otro uso. En concreto, vamos a profundizar en el problema de la búsqueda y en el problema del ordenamiento, que son dos problemas elementales que ilustran conceptos centrales del desarrollo de algoritmos. 

El uso adecuado de estos conceptos puede hacer la diferencia entre un algoritmo que termina el procesamiento en unos pocos minutos o uno que hay que dejar corriendo dos dias (y rezar para que no corte la electricidad mientras corre).


## Búsqueda lineal

### El problema de la búsqueda

Presentamos ahora uno de los problemas más clásicos de la computación, el
problema de la búsqueda, que se puede enunciar de la siguiente manera:

**Problema:** Dada una lista `lista` y un valor `e` devolver el índice de `e`
en `lista` si `e` está en `lista`, y -1 si `e` no está en `lista`.

Este problema tiene una solución muy sencilla en Python: se puede usar el método `index()` de las listas.

Probá esa solución:

```python
>>> [1, 3, 5, 7].index(5)
2
>>> [1, 3, 5, 7].index(20)
Traceback (most recent call last):

  File "<ipython-input-177-1bcce50c5c91>", line 1, in <module>
    [1, 3, 5, 7].index(20)

ValueError: 20 is not in list
```

Vemos que usar la función `index()` resuelve nuestro problema si el
valor buscado está en la lista, pero si el valor no está no sólo no devuelve
un -1, sino que se produce un error.

El problema es que para poder aplicar la función `index()` debemos
estar seguros de que el valor está en la lista, y para averiguar eso Python
nos provee del operador `in`:

```python
>>> 5 in [1, 3, 5, 7]
True
>>> 20 in [1, 3, 5, 7]
False
```

Si llamamos a la función `index()` sólo cuando el
resultado de `in` es verdadero, y devolvemos -1 cuando el
resultado de `in` es falso, estaremos resolviendo el problema
planteado usando sólo funciones provistas por Python:

```python
def busqueda_con_index(lista, e):
    '''Busca un elemento e en la lista.

    Si e está en lista devuelve el índice,
    de lo contrario devuelve -1.
    '''
    if e in lista:
        pos = lista.index(e)
    else:
        pos = -1
    return pos
```

Probemos la función `busqueda_con_index()`:

```python
>>> busqueda_con_index([1, 4, 54, 3, 0, -1], 1)
0
>>> busqueda_con_index([1, 4, 54, 3, 0, -1], -1)
5
>>> busqueda_con_index([1, 4, 54, 3, 0, -1], 3)
3
>>> busqueda_con_index([1, 4, 54, 3, 0, -1], 44)
-1
>>> busqueda_con_index([], 0)
-1
```

### ¿Cuántas comparaciones hace este programa?

Es decir, ¿cuánto esfuerzo computacional requiere
este programa? ¿Cuántas veces compara el valor que buscamos con los datos de
la lista? No lo sabemos porque no sabemos cómo están implementadas las
operaciones `in` e `index()`. La pregunta queda planteada
por ahora pero daremos un método para averiguarlo más adelante.

###  Búsqueda lineal

Nos interesa estudiar formas alternativas de programar la búsqueda usando operaciones más elementales, y no las primitivas `in` e `index()` de nuestro lenguaje de alto nivel. Aceptemos entonces que no vamos a usar ni `in` ni `index()`. En cambio, podemos usar ciclos y comparaciones.

iterar sobre los índices y elementos de una lista, y hacer comparaciones elementales.

Consideremos la siguiente solución: iterar sobre los índices y elementos de una lista de manera de comparar el elemento `e` buscado con cada uno de los elementos de la lista y devolver la posición
donde lo encontremos, en caso de encontrarlo.
Si llegamos al final de la lista sin haber salido antes de la función es
porque el valor de `e` no está en la lista, y en ese caso
devolvemos -1.

En esta solución lo ideal es usar `enumerate` (ver la [Sección 2.6](../02_Datos/06_Secuencias.md#la-función-enumerate)) ya que dentro de la iteración necesitamos tener acceso tanto al valor del elemento (para ver si es igual al buscado) como a su índice (es el valor que tenemos que devolver).

Primero hagámoslo sin usarlo y luego lo agregamos para entender su ventaja. En ambos casos necesitamos una variable `i` que cuente en cada momento en qué posición de la lista estamos parados.  Si no usamos `enumerate`, debemos inicializar `i` en 0 antes de entrar en el ciclo e incrementarla en 1 en cada paso.

El programa nos queda entonces como se muestra a continuación:

```python
def busqueda_lineal(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    i = 0     
    for z in lista:  # recorremos los elementos de la lista
        if z == e:   # si entontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
        i += 1       
    return pos
```

La versión con `enumerate` es mucho más elegante:
```python
def busqueda_lineal(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si entontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    return pos
```

Y ahora lo probamos:

```python
>>> busqueda_lineal([1, 4, 54, 3, 0, -1], 44)
-1
>>> busqueda_lineal([1, 4, 54, 3, 0, -1], 3)
3
>>> busqueda_lineal([1, 4, 54, 3, 0, -1], 0)
4
>>> busqueda_lineal([], 42)
-1
```

###  ¿Cuántas comparaciones hace este programa?

Volvemos a preguntarnos lo mismo que en la sección anterior, pero con el nuevo
programa: ¿cuánto esfuerzo computacional requiere este programa?, ¿cuántas
veces compara el valor que buscamos con los datos de la lista? Ahora podemos
analizar el código de `busqueda_lineal`:

El ciclo recorre uno a uno los elementos de la lista, y en el cuerpo de ese ciclo, se compara cada elemento con el valor buscado. En el caso de encontrarlo
se devuelve la posición. Si el valor no está en la lista, se recorrerá la lista entera, haciendo una comparación por cada elemento.

O sea que si el valor está en la posición *p* de la lista se hacen *p*
comparaciones. En el *peor caso*, si el valor no está, se hacen
tantas comparaciones como elementos tenga la lista.

En resúmen: Si la lista crece, la cantidad de comparaciones
para encontrar un valor arbitrario crecerá en forma proporcional al tamaño de
la lista. Por lo tanto diremos que:

**El algoritmo de búsqueda lineal tiene un comportamiento *proporcional a la longitud de la lista involucrada*, o que es un algoritmo *lineal*.**

## Ejercicios


### Ejercicio 2.26: Búsquedas de un elemento
Creá el archivo `busqueda_en_listas.py` para guardar tu código de este ejercicio y el siguiente.

En este primer ejercicio tenés que escribir una función `buscar_u_elemento()` que reciba una lista y un elemento y devuelva la posición de la última aprición de ese elemento en la lista (o -1 si el elemento no pertenece a la lista).

Por ejemplo:
```pyton 
>>> buscar_u_elemento([1,2,3,2,3,4],1)
0
>>> buscar_u_elemento([1,2,3,2,3,4],2)
3
>>> buscar_u_elemento([1,2,3,2,3,4],3)
4
>>> buscar_u_elemento([1,2,3,2,3,4],5)
-1

```

Agregale a tu programa `busqueda_en_listas.py` una función `buscar_n_elemento()` que reciba una lista desordenada y un elemento y devuelva la cantidad de veces que aparece el elemento en la lista.


### Ejercicio 2.27: Búsqueda del máximo
Agergale a tu archivo una función `maximo()` que busque el elemento máximo de una lista de números positivos. Python tiene el comando `max` que ya hace esto, pero como práctica te propomenos que completes el siguiente código:

```python
def maximo(lista):
    '''devuelve el máximo de una lista 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = 0 # Lo inicializo en 0
    for e in lista: # Recorro la lista y voy guardando el mayor
        ...
    return m
```

Probalo con estos ejemplos:
```pyton 
>>> maximo([1,2,7,2,3,4])
7
>>> maximo([1,2,3,4])
4
>>> maximo([-5,4])
4
>>> maximo([-5,-4])
0
```

¿Por qué falla en el último caso? ¿Por qué anda en el caso anterior? 
¿Cómo se puede inicializar m para que la función ande también con números negativos? Corregilo y guarda la version mejorada en el archivo `busqueda_en_listas.py`.

## Ejercitación con iteradores y listas

### Ejercicio 2.28: Invertir una lista
Escribí una función `invertir_lista(lista)` que dada una lista devuelva otra que tenga los mismos elementos en el orden inverso. Es decir, el que era el primer elemento de la lista de entrada deberá ser el último de la lista de salida y análogamente con los demás elementos.


```python
def invertir_lista(lista):
    invertida = []
    for e in lista: # Recorro la lista
        ... #agrego el elemento e al principio de la lista invertida
    return invertida
```

Guardá la función en el archivo `invlista.py` y probarla con las siguientes listas:
`[1,2,3,4,5]`
`['Bogotá', 'Rosario', 'Santiago', San Fernando', 'San Miguel']`

### Ejercicio 2.29: Invertir una lista *in place*
En el ejercicio anterior creaste una nueva lista conteniendo los elementos de una lista dada en orden inverso. En este ejercicio te pedimos que inviertas los elementos de una lista pero sin crear una nueva lista ni listas auxiliares. Es decir, te pedimos que escribas una función `invertir_lista_inplace(lista)` que, dada una lista, invierta la misma lista *en el lugar* (en inglés, *in place*), sin usar listas nuevas.)

### Ejercicio 2.30: Tablas de multiplicar
Escribí un programa `tablamult.py` que imprima de forma prolija las tablas de
multiplicar del 1 al 9 usando f-strings. Si podés, evitá usar la multiplicación, usando sólo sumas alcanza.


### Ejercicio 2.31: Propagación
Imaginate una fila con varios fósforos uno al lado del otro. Los fósforos pueden estar en tres estados: nuevos, prendidos fuego o ya gastados (carbonizado).
Representaremos esta situación con una lista *L* con un elemento por fósforo, que en cada posición tiene un 0 (nuevo), un 1 (encendido) o un -1 (carbonizado). 
El fuego se propaga inmediatamente de un fósforo encendido a cualquier fósoforo nuevo que tenga a su lado. Los fósforos carbonizados no se encienden nuevamente.

Escribí una función llamada `propagar` que reciba un vector con 0, 1 y -1 y devuelva un vector en el que los 1 se propagaron a sus vecinos con 0. Guardalo en un archivo `propaga.py`.

Por ejemplo:
```python
>>> propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
[ 0, 0, 0,-1, 1, 1, 1, 1,-1, 1, 1, 1, 1]
>>> propagar([ 0, 0, 0, 1, 0, 0])
[ 1, 1, 1, 1, 1, 1]
```

![Propagación](./fosforos.jpg) Propagación análoga a la del Ejercicio


[Contenidos](../Contenidos.md) \| [Anterior (7 Entorno de desarrollo integrado)](07_IDE.md) \| [Próximo (9 Cierre de la segunda clase)](10_CierreClase.md)

