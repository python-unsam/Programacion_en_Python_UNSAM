[Contenidos](../Contenidos.md) \| [Anterior (3 Productores, consumidores, cañerías.)](04_Producers_consumers.md) \| [Próximo (5 Cierre de la novena clase)](06_Cierre.md)

# 9.4 # Mas sobre generadores

Esta sección introduce algunos temas adicionales relacionados con generadores, entre ellas : expresiones generadoras y el módulo `itertools`

### Expresiones generadoras
Una expresión generadora es una lista por comprensión en su "versión generadora", que devuelve un elemento por vez.

```python
>>> a = [1,2,3,4]
>>> b = (2*x for x in a)
>>> b
<generator object at 0x58760>
>>> for i in b:
...   print(i, end=' ')
...
2 4 6 8
>>>
```

¿Cuales son las diferencias entre expresiones generadoras y comprensión de listas? Bueno, las expresiones generadoras ... 

* No construyen una lista
* Construídas para ser iteradas
* Una vez consumidas, no pueden ser reutilizadas.

La sintaxis general es :

```python
(<expression> for i in s if <conditional>)
```
Que puede leerse como .... el valor es <expression> para cada elemento `i` perteneciente a `s` siempre y cuando <conditional> se cumpla.

Las podés usar como argumento de una función.

```python
sum(x*x for x in a)
```

Las podés usar en lugar de cualquier iterable.

```python
>>> a = [1,2,3,4]
>>> b = (x*x for x in a)
>>> c = (-x for x in b)
>>> for i in c:
...   print(i, end=' ')
...
-1 -4 -9 -16
>>>
```

El uso principal de las expresiones generadoras es en código que realiza un cómputo con una serie de elementos pero sólo necesita cada elemento una única vez. Ejemplo: quitar todas las líneas de un programa que sean comentarios:

```python
f = open('unarchivo.txt')
lines = (line for line in f if not line.startswith('#'))
for line in lines:
    ...
f.close()
```

Al usar generadores, tu código ejecuta más rápido y usa menos memoria. Se portan como un filtro en el flujo de datos por un pipeline.

### Motivos para usar generadores

* Muchos problemas se expresan mejor en términos de iteración.
  * Recorrer una colección de items para hacer algún cómputo (buscar, reemplazar, modificar, etc.).
  * Los pipelines de procesamiento resuelven un amplio abanico de problemas.

* Mas eficientes en el uso de memoria.
  * Sólo producís valores cuando los necesitás.
  * Varias ventajas sobre construír una larga lista.
  * Pueden operar sobre datos en pipelines.  

* Un generador facilita la reutilización de código.
  * Separa la propia *iteración* del código que utiliza sus resultados.
  * Podés construír tu propio conjunto de herramientas de iteración y ensamblarlas como necesites en cada caso. 

### El módulo `itertools` 

El módulo `itertools` es una biblioteca con varias funciones útiles para construír generadores e interadores. 

```python
itertools.chain(s1,s2)
itertools.count(n)
itertools.cycle(s)
itertools.dropwhile(predicate, s)
itertools.groupby(s)
itertools.ifilter(predicate, s)
itertools.imap(function, s1, ... sN)
itertools.repeat(s, n)
itertools.tee(s, ncopies)
itertools.izip(s1, ... , sN)
```

Todas estas funciones procesan datos iterativamente, e implementan distintos tipos de patrones de iteración.

Un buen curso (en inglés, del 2014) sobre [Generadores e iteradores] es: (http://www.dabeaz.com/generators/)

## Ejercicios

En ejercicios anteriores escribiste código que vigilaba un archivo (un log) esperando líneas nuevas escritas al final y las presentaba como una secuencia de filas. Este ejercicio continúa aquél, de modo que vas a necesitar `Data/stocksim.py` ejecutándose para esto.

### Ejercicio 9.13: Expresiones generadoras
Fijate este ejemplo de una expresión generadora:

```python
>>> nums = [1, 2, 3, 4, 5]
>>> cuadrados = (x*x for x in nums)
>>> cuadrados
<generator object <genexpr> at 0x109207e60>
>>> for n in cuadrados:
...     print(n)
...
1
4
9
16
25
```

A diferencia de una definición por comprensión de listas, una expresión generadora sólo puede recorrerse una vez. Si intentás recorrerla de nuevo con otro `for`, no obtenés nada.

```python
>>> for n in squares:
...     print(n)
...
>>>
```

### Ejercicio 9.14: Expresiones generadoras como argumentos en funciones.
A veces es útil (y muy claro al leerlo) si pasás una expresión generadora como argumento de una función. A primera vista parece un poco raro, pero probá esto:

```python
>>> nums = [1,2,3,4,5]
>>> sum([x*x for x in nums])    # una lista por comprensión
55
>>> sum(x*x for x in nums)      # una expresión generadora
55
>>>
```

En ese ejemplo, la segunda versión (que usa un generador) requeriría mucha menos memoria que si construyera toda la lista simultáneamente, si la lista fuera grande.

En tu archivo `camion.py` lograste hacer algunos cálculos usando comprensión de listas. Reemplazá esas expresiones por expresiones generadoras.

### Ejercicio 9.15: Código simple
Las expresiones generadoras son a menudo un buen reemplazo para pequeñas funciones generadoras. Por ejemplo, en lugar de escribir una función como esta:

```python
def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row
```

La podrías reemplazar con una expresión así:

```python
rows = (row for row in rows if row['name'] in names)
```

Entonces: copiá el programa `ticker.py` a `ticker_simple.py` y modificá este último para que use funciones generadoras. Preparalos para entregar porque te los pedimos al terminar la clase, junto con ejercicios anteriores.



[Contenidos](../Contenidos.md) \| [Anterior (3 Productores, consumidores, cañerías.)](04_Producers_consumers.md) \| [Próximo (5 Cierre de la novena clase)](06_Cierre.md)

