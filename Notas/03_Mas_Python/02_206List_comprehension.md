[Contenidos](../Contenidos.md) \| [Anterior (1 collections module)](01_205Collections.md) \| [Próximo (3 Objects)](03_207Objects.md)

# 3.2 List Comprehensions

A common task is processing items in a list.  This section introduces list comprehensions,
a powerful tool for doing just that.

### Creating new lists

A list comprehension creates a new list by applying an operation to
each element of a sequence.

```python
>>> a = [1, 2, 3, 4, 5]
>>> b = [2*x for x in a ]
>>> b
[2, 4, 6, 8, 10]
>>>
```

Another example:

```python
>>> names = ['Edmundo', 'Juana']
>>> a = [name.lower() for name in names]
>>> a
['elwood', 'jake']
>>>
```

The general syntax is: `[ <expression> for <nvariable> in <sequence> ]`.

### Filtering

You can also filter during the list comprehension.

```python
>>> a = [1, -5, 4, 2, -2, 10]
>>> b = [2*x for x in a if x > 0 ]
>>> b
[2, 8, 4, 20]
>>>
```

### Use cases

List comprehensions are hugely useful.  For example, you can collect values of a specific
dictionary fields:

```python
cajonnames = [s['name'] for s in cajones]
```

You can perform database-like queries on sequences.

```python
a = [s for s in cajones if s['precio'] > 100 and s['cajones'] > 50 ]
```

You can also combine a list comprehension with a sequence reduction:

```python
cost = sum([s['cajones']*s['precio'] for s in cajones])
```

### General Syntax

```code
[ <expression> for <nvariable> in <sequence> if <condition>]
```

What it means:

```python
result = []
for nvariable in sequence:
    if condition:
        result.append(expression)
```

### Historical Digression

List comprehensions come from math (set-builder notation).

```code
a = [ x * x for x in s if x > 0 ] # Python

a = { x^2 | x ∈ s, x > 0 }         # Math
```

It is also implemented in several other languages. Most
coders probably aren't thinking about their math class though. So,
it's fine to view it as a cool list shortcut.

## Ejercicios

Start by running your `reporte.py` program so that you have the
camion of cajones loaded in the interactive mode.

```bash
bash % python3 -i reporte.py
```

Now, at the Python interactive prompt, type statements to perform the
operations described below.  These operations perform various kinds of
data reductions, transforms, and queries on the camion data.

### Ejercicio 3.2: List comprehensions

Try a few simple list comprehensions just to become familiar with the syntax.

```python
>>> nums = [1,2,3,4]
>>> squares = [ x * x for x in nums ]
>>> squares
[1, 4, 9, 16]
>>> twice = [ 2 * x for x in nums if x > 2 ]
>>> twice
[6, 8]
>>>
```

Notice how the list comprehensions are creating a new list with the
data suitably transformed or filtered.

### Ejercicio 3.3: Sequence Reductions

Compute the total cost of the camion using a single Python statement.

```python
>>> camion = leer_camion('Data/camion.csv')
>>> cost = sum([ s['cajones'] * s['precio'] for s in camion ])
>>> cost
44671.15
>>>
```

After you have done that, show how you can compute the current value
of the camion using a single statement.

```python
>>> value = sum([ s['cajones'] * precios[s['name']] for s in camion ])
>>> value
28686.1
>>>
```

Both of the above operations are an example of a map-reduction. The
list comprehension is mapping an operation across the list.

```python
>>> [ s['cajones'] * s['precio'] for s in camion ]
[3220.0000000000005, 4555.0, 12516.0, 10246.0, 3835.1499999999996, 3254.9999999999995, 7044.0]
>>>
```

The `sum()` function is then performing a reduction across the result:

```python
>>> sum(_)
44671.15
>>>
```

With this knowledge, you are now ready to go launch a big-data startup company.

### Ejercicio 3.4: Data Queries

Try the following examples of various data queries.

First, a list of all camion holdings with more than 100 cajones.

```python
>>> more100 = [ s for s in camion if s['cajones'] > 100 ]
>>> more100
[{'precio': 83.44, 'name': 'Caqui', 'cajones': 150}, {'precio': 51.23, 'name': 'Mandarina', 'cajones': 200}]
>>>
```

All camion holdings for Mandarina and Naranja cajones.

```python
>>> msftibm = [ s for s in camion if s['name'] in {'Mandarina','Naranja'} ]
>>> msftibm
[{'precio': 91.1, 'name': 'Naranja', 'cajones': 50}, {'precio': 51.23, 'name': 'Mandarina', 'cajones': 200},
  {'precio': 65.1, 'name': 'Mandarina', 'cajones': 50}, {'precio': 70.44, 'name': 'Naranja', 'cajones': 100}]
>>>
```

A list of all camion holdings that cost more than $10000.

```python
>>> cost10k = [ s for s in camion if s['cajones'] * s['precio'] > 10000 ]
>>> cost10k
[{'precio': 83.44, 'name': 'Caqui', 'cajones': 150}, {'precio': 51.23, 'name': 'Mandarina', 'cajones': 200}]
>>>
```

### Ejercicio 3.5: Data Extraction

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
to solve some kind of one-off problem involving data imports, exports,
extraction, and so forth.  Becoming a guru master of list
comprehensions can substantially reduce the time spent devising a
solution.  Also, don't forget about the `collections` module.


[Contenidos](../Contenidos.md) \| [Anterior (1 collections module)](01_205Collections.md) \| [Próximo (3 Objects)](03_207Objects.md)

