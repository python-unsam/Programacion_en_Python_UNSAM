[Contenidos](../Contenidos.md) \| [Próximo (2 List Comprehensions)](02_206List_comprehension.md)

# 3.1 collections module

The `collections` module provides a number of useful objects for data handling.
This part briefly introduces some of these features.

### Example: Counting Things

Let's say you want to tabulate the total cajones of each cajon.

```python
camion = [
    ('Pera', 100, 490.1),
    ('Naranja', 50, 91.1),
    ('Caqui', 150, 83.44),
    ('Naranja', 100, 45.23),
    ('Pera', 75, 572.45),
    ('Lima', 50, 23.15)
]
```

There are two `Naranja` entries and two `Pera` entries in this list. The cajones need to be combined together somehow.

### Counters

Solution: Use a `Counter`.

```python
from collections import Counter
total_cajones = Counter()
for name, cajones, precio in camion:
    total_cajones[name] += cajones

total_cajones['Naranja']     # 150
```

### Example: One-Many Mappings

Problem: You want to map a key to multiple values.

```python
camion = [
    ('Pera', 100, 490.1),
    ('Naranja', 50, 91.1),
    ('Caqui', 150, 83.44),
    ('Naranja', 100, 45.23),
    ('Pera', 75, 572.45),
    ('Lima', 50, 23.15)
]
```

Like in the previous example, the key `Naranja` should have two different tuples instead.

Solution: Use a `defaultdict`.

```python
from collections import defaultdict
holdings = defaultdict(list)
for name, cajones, precio in camion:
    holdings[name].append((cajones, precio))
holdings['Naranja'] # [ (50, 91.1), (100, 45.23) ]
```

The `defaultdict` ensures that every time you access a key you get a default value.

### Example: Keeping a History

Problem: We want a history of the last N things.
Solution: Use a `deque`.

```python
from collections import deque

history = deque(maxlen=N)
with open(nombre_archivo) as f:
    for line in f:
        history.append(line)
        ...
```

## Ejercicios

The `collections` module might be one of the most useful biblioteca
modules for dealing with special purpose kinds of data handling
problems such as tabulating and indexing.

In this ejercicio, we’ll look at a few simple examples.  Start by
running your `reporte.py` program so that you have the camion of
cajones loaded in the interactive mode.

```bash
bash % python3 -i reporte.py
```

### Ejercicio 3.1: Tabulating with Counters
Suppose you wanted to tabulate the total number of cajones of each cajon.
This is easy using `Counter` objects. Try it:

```python
>>> camion = leer_camion('Data/camion.csv')
>>> from collections import Counter
>>> holdings = Counter()
>>> for s in camion:
        holdings[s['name']] += s['cajones']

>>> holdings
Counter({'Mandarina': 250, 'Naranja': 150, 'Caqui': 150, 'Lima': 100, 'Durazno': 95})
>>>
```

Carefully observe how the multiple entries for `Mandarina` and `Naranja` in `camion` get combined into a single entry here.

You can use a Counter just like a dictionary to retrieve individual values:

```python
>>> holdings['Naranja']
150
>>> holdings['Mandarina']
250
>>>
```

If you want to rank the values, do this:

```python
>>> # Get three most held cajones
>>> holdings.most_common(3)
[('Mandarina', 250), ('Naranja', 150), ('Caqui', 150)]
>>>
```

Let’s grab another camion of cajones and make a new Counter:

```python
>>> camion2 = leer_camion('Data/camion2.csv')
>>> holdings2 = Counter()
>>> for s in camion2:
          holdings2[s['name']] += s['cajones']

>>> holdings2
Counter({'Frambuesa': 250, 'Durazno': 125, 'Lima': 50, 'Mandarina': 25})
>>>
```

Finally, let’s combine all of the holdings doing one simple operation:

```python
>>> holdings
Counter({'Mandarina': 250, 'Naranja': 150, 'Caqui': 150, 'Lima': 100, 'Durazno': 95})
>>> holdings2
Counter({'Frambuesa': 250, 'Durazno': 125, 'Lima': 50, 'Mandarina': 25})
>>> combined = holdings + holdings2
>>> combined
Counter({'Mandarina': 275, 'Frambuesa': 250, 'Durazno': 220, 'Lima': 150, 'Naranja': 150, 'Caqui': 150})
>>>
```

This is only a small taste of what counters provide. However, if you
ever find yourself needing to tabulate values, you should consider
using one.

### Commentary: collections module

The `collections` module is one of the most useful biblioteca modules
in all of Python.  In fact, we could do an extended tutorial on just
that.  However, doing so now would also be a distraction.  For now,
put `collections` on your list of bedtime reading for later.


[Contenidos](../Contenidos.md) \| [Próximo (2 List Comprehensions)](02_206List_comprehension.md)

