[Contenidos](../Contenidos.md) \| [Anterior (1 El módulo collections)](01_Collections.md) \| [Próximo (3 Objects)](03_Objects.md)

# 3.2 Compresión de listas

Una tarea que realizamos una y otra vez es procesar los elementos de una lista. En esta sección introducimos la definición de listas por compresión que es una herramienta potente para hacer exactamente eso.

### Crear listas nuevas

La comprensión de listas crea un una nueva lista aplicando una operación a cada elemento de una secuencia.

```python
>>> a = [1, 2, 3, 4, 5]
>>> b = [2*x for x in a ]
>>> b
[2, 4, 6, 8, 10]
>>>
```

Otro ejemplo:

```python
>>> names = ['Edmundo', 'Juana']
>>> a = [name.lower() for name in names]
>>> a
['edmundo', 'juana']
>>>
```

La sintaxis general es : `[ <expresión> for <variable> in <secuencia> ]`.

### Filtros

La comprensión de listas se puede usar para filtrar.

```python
>>> a = [1, -5, 4, 2, -2, 10]
>>> b = [2*x for x in a if x > 0 ]
>>> b
[2, 8, 4, 20]
>>>
```

### Casos de uso

La comprensión de listas es enormemente útil. Por ejemplo, podés recolectar los valores de un campo específico de un diccionario:

```python
frutas = [s['nombre'] for s in cajones]
```

O podés hacer consultas (queries) como si las secuencias fueran bases de datos.

```python
a = [s for s in cajones if s['precio'] > 100 and s['cajones'] > 50 ]
```

También podés combinar la comprensión de listas con reducciones de secuencias:

```python
costo = sum([s['cajones']*s['precio'] for s in cajones])
```

### Sintaxis general

```code
[ <expresión> for <variable> in <secuencia> if <condición>]
```

Lo que significa

```python
resultado = []
for variable in secuencia:
    if condición:
        resultado.append(expresión)
```

### Disgresión histórica

La comprensión de listas viene de la matemática (definición de conjuntos por comprensión).

```code
a = [ x * x for x in s if x > 0 ] # Python

a = { x^2 | x ∈ s, x > 0 }         # Math
```

La mayoría de los programadores no suelen pensar en el costado matemático de esta herramienta. Podemos verla simplemente como una abreviación copada para definir listas.

## Ejercicios

Corré  tu programa `reporte.py` de forma de tener los datos sobre cajones cargados en tu intérprete en modo interactivo. 

Luego, tratá de escribir los comandos adecuados para realizar las operaciones descriptas abajo. Estas operaciones son reducciones, transformaciones y consultas sobre la carga del camión.

### Ejercicio 3.2: Comprensión de listas
Probá un par de comprensión de listas para familiarizarte con la sintaxis.

```python
>>> nums = [1,2,3,4]
>>> cuadrados = [ x * x for x in nums ]
>>> cuadrados
[1, 4, 9, 16]
>>> dobles = [ 2 * x for x in nums if x > 2 ]
>>> dobles
[6, 8]
>>>
```

Observá que estás creando nuevas listas con los datos adecuadamente transformados o filtrados.

### Ejercicio 3.3: Reducción de secuencias
Calculá el costo total de la carga del camión en un solo comando.

```python
>>> camion = leer_camion('Data/camion.csv')
>>> cost = sum([ s['cajones'] * s['precio'] for s in camion ])
>>> cost
44671.15
>>>
```

Luego, usando la variable `precios` calculá también el valor en el mercado de la carga del camión usando una sola línea de código.

```python
>>> value = sum([ s['cajones'] * precios[s['name']] for s in camion ])
>>> value
28686.1
>>>
```

Ambos son ejemplos de aplicación-reducción. La comprensión de listas está aplicando una operación a lo largo de la lista. 

```python
>>> [ s['cajones'] * s['precio'] for s in camion ]
[3220.0000000000005, 4555.0, 12516.0, 10246.0, 3835.1499999999996, 3254.9999999999995, 7044.0]
>>>
```

La función `sum()` luego realiza una reducción del resultaqdo

```python
>>> sum(_)
44671.15
>>>
```

Con este conocimiento algunos ya empiezan su startup de big-data.

### Ejercicio 3.4: Consultas de datos
Probá los siguientes ejemplos de consultas (queries) de datos.

Primero, generá una lista con la info de todas las frutas que tienen más de 100 cajones en el camión.

```python
>>> mas100 = [ s for s in camion if s['cajones'] > 100 ]
>>> mas100
[{'precio': 83.44, 'name': 'Caqui', 'cajones': 150}, {'precio': 51.23, 'name': 'Mandarina', 'cajones': 200}]
>>>
```

Ahora, una con la info sobre cajones de Mandarina y Naranja.

```python
>>> myn = [ s for s in camion if s['name'] in {'Mandarina','Naranja'} ]
>>> myn
[{'precio': 91.1, 'name': 'Naranja', 'cajones': 50}, {'precio': 51.23, 'name': 'Mandarina', 'cajones': 200},
  {'precio': 65.1, 'name': 'Mandarina', 'cajones': 50}, {'precio': 70.44, 'name': 'Naranja', 'cajones': 100}]
>>>
```

O una con la info de las frutas que costaron más de $10000.

```python
>>> cost10k = [ s for s in camion if s['cajones'] * s['precio'] > 10000 ]
>>> cost10k
[{'precio': 83.44, 'name': 'Caqui', 'cajones': 150}, {'precio': 51.23, 'name': 'Mandarina', 'cajones': 200}]
>>>
```

Observá que esta forma de escribir resulta análoga a las consultas a una base de datos SQL.

### Ejercicio 3.5: Extracción de datos
Show how you could build a list of tuples `(name, cajones)` where `name` and `cajones` are taken from `camion`.

```python
>>> name_cajones =[ (s['name'], s['cajones']) for s in camion ]
>>> name_cajones
[('Lima', 100), ('Naranja', 50), ('Caqui', 150), ('Mandarina', 200), ('Durazno', 95), ('Mandarina', 50), ('Naranja', 100)]
>>>
```

If you change the the square brackets (`[`,`]`) to curly braces (`{`, `}`), you get something known as a set comprehension.
This gives you unique or distinct values.

For example, this determines the set of unique cajon names that appear in `camion`:

```python
>>> names = { s['name'] for s in camion }
>>> names
{ 'Lima', 'Durazno', 'Naranja', 'Mandarina', 'Caqui'] }
>>>
```

If you specify `key:value` pairs, you can build a dictionary.
For example, make a dictionary that maps the name of a cajon to the total number of cajones held.

```python
>>> holdings = { name: 0 for name in names }
>>> holdings
{'Lima': 0, 'Durazno': 0, 'Naranja': 0, 'Mandarina': 0, 'Caqui': 0}
>>>
```

This latter feature is known as a **dictionary comprehension**. Let’s tabulate:

```python
>>> for s in camion:
        holdings[s['name']] += s['cajones']

>>> holdings
{ 'Lima': 100, 'Durazno': 95, 'Naranja': 150, 'Mandarina':250, 'Caqui': 150 }
>>>
```

Try this example that filters the `precios` dictionary down to only
those names that appear in the camion:

```python
>>> camion_precios = { name: precios[name] for name in names }
>>> camion_precios
{'Lima': 9.22, 'Durazno': 13.48, 'Naranja': 106.28, 'Mandarina': 20.89, 'Caqui': 35.46}
>>>
```

### Ejercicio 3.6: Extracting Data From CSV Files
Knowing how to use various combinations of list, set, and dictionary
comprehensions can be useful in various forms of data processing.
Here’s an example that shows how to extract selected columns from a
CSV file.

First, read a row of header information from a CSV file:

```python
>>> import csv
>>> f = open('Data/fecha_camion.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> headers
['name', 'date', 'time', 'cajones', 'precio']
>>>
```

Next, define a variable that lists the columns that you actually care about:

```python
>>> select = ['name', 'cajones', 'precio']
>>>
```

Now, locate the indices of the above columns in the source CSV file:

```python
>>> indices = [ headers.index(ncolumna) for ncolumna in select ]
>>> indices
[0, 3, 4]
>>>
```

Finally, read a row of data and turn it into a dictionary using a
dictionary comprehension:

```python
>>> row = next(rows)
>>> record = { ncolumna: row[index] for ncolumna, index in zip(select, indices) }   # dict-comprehension
>>> record
{'precio': '32.20', 'name': 'Lima', 'cajones': '100'}
>>>
```

If you’re feeling comfortable with what just happened, read the rest
of the file:

```python
>>> camion = [ { ncolumna: row[index] for ncolumna, index in zip(select, indices) } for row in rows ]
>>> camion
[{'precio': '91.10', 'name': 'Naranja', 'cajones': '50'}, {'precio': '83.44', 'name': 'Caqui', 'cajones': '150'},
  {'precio': '51.23', 'name': 'Mandarina', 'cajones': '200'}, {'precio': '40.37', 'name': 'Durazno', 'cajones': '95'},
  {'precio': '65.10', 'name': 'Mandarina', 'cajones': '50'}, {'precio': '70.44', 'name': 'Naranja', 'cajones': '100'}]
>>>
```

Oh my, you just reduced much of the `leer_camion()` function to a single statement.

### Commentary

List comprehensions are commonly used in Python as an efficient means
for transforming, filtering, or collecting data.  Due to the syntax,
you don’t want to go overboard—try to keep each list comprehension as
simple as possible.  It’s okay to break things into multiple
steps. For example, it’s not clear that you would want to spring that
last example on your unsuspecting co-workers.

That said, knowing how to quickly manipulate data is a skill that’s
incredibly useful.  There are numerous situations where you might have
to solve some kind of ecepcional problem involving data imports, exports,
extraction, and so forth.  Becoming a guru master of list
comprehensions can substantially reduce the time spent devising a
solution.  Also, don't forget about the `collections` module.


[Contenidos](../Contenidos.md) \| [Anterior (1 El módulo collections)](01_Collections.md) \| [Próximo (3 Objects)](03_Objects.md)

