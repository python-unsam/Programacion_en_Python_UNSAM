[Contenidos](../Contenidos.md) \| [Anterior (2 Comprensión de listas)](02_List_comprehension.md) \| [Próximo (4 Numpy)](04_Numpy.md)

# 3.3 Objects


En esta sección introducimos algunos conceptos sobre el modelo de objeto interno de Python y discutimos algunos temas relacionados con el manejo de memoria, copias de variable y chequeo de tipos.

### Asignaciones

Muchas operaciones en Python están relacionas a *asignar* o *guardar* valores.

```python
a = valor         # Asignación a una variable
s[n] = valor      # Asignación a una lista
s.append(valor)   # Agregar a una list
d['key'] = valor  # Agregar a una diccionario
```

*Ojo: las operaciones de asignación **nunca hacen una copia** del valor asignado.*
Las asignaciones son simplemente copias de la referencias (o copias del puntero, si preferís).

### Ejemplo de asignación

Considerá este fragemnto de código.

```python
a = [1,2,3]
b = a
c = [a,b]
```

Un gráfico de las operaciones de memoria suyacentes. En este ejemplo, hay solo un objeto lista `[1,2,3]`, pero hay cuatro referencias a él.

![Referencias](referencias.png)

Esto significa que al modificar un valor modificamos *todas* las referencias.

```python
>>> a.append(999)
>>> a
[1,2,3,999]
>>> b
[1,2,3,999]
>>> c
[[1,2,3,999], [1,2,3,999]]
>>>
```

Observá cómo un cambio en la lista original desencadena cambios en todas las demás variables (ouch!). Esto es porque no se hizo ninguna copia. Todos son punteros a la misma cosa.

### Reasignar valores

La reasignación de valores *nunca* sobreescribe la memoria ocupada por un valor anterior.

```python
a = [1,2,3]
b = a
a = [4,5,6]

print(a)      # [4, 5, 6]
print(b)      # [1, 2, 3]    Mantiene el valor original
```

Acordate: **Las variables son nombre, no ubicaciones en la memoria.**

### Peligros

Si no te explican esto, tarde o temprano te trae problemas. Un típico ejemplo es cuando cambiás un dato pensando que es una copia privada y, sin querer, esto corrompe los datos en otra parte del programa.

*Comentario: Esta es una de las razones por las que los tipos de datos primitivos (int,  float, string) son immutable (de sólo lectura).*

### Identidad y referencias

Podés usar el operador `is` (es) para verificar si dos valores corresponden al mismo objeto.

```python
>>> a = [1,2,3]
>>> b = a
>>> a is b
True
>>>
```

`is` compara la identidad del objeto (un entero).  esta identidad tambien la podés obtener usando `id()`.

```python
>>> id(a)
3588944
>>> id(b)
3588944
>>>
```

Observación: Para ver si dos valores son iguales, es mejor usar el `==`. El comportamiento de `is` puede dar resultados inesperados:

```python
>>> a = [1,2,3]
>>> b = a
>>> c = [1,2,3]
>>> a is b
True
>>> a is c
False
>>> a == c
True
>>>
```

### Copias playas

Las listas y diccionarios tienen metodos para hacer copias (no meras referencias, copias, duplicados):

```python
>>> a = [2,3,[100,101],4]
>>> b = list(a) # Hacer una copia
>>> a is b
False
```

Ahora `b` es una nueva lista. 

```python
>>> a.append(5)
>>> a
[2, 3, [100, 101], 4, 5]
>>> b
[2, 3, [100, 101], 4]
```

A pesar de esto, los elementos de `a` y de `b` siguen siendo compartidos.

```python
>>> a[2].append(102)
>>> b[2]
[100,101,102]
>>>
>>> a[2] is b[2]
True
>>>
```

En este ejemplo, la lista interna `[100, 101, 102]` es compartida por ambas variables. La copia que hicimos con el comando `b = list(a)` es un *copia playa* (shallow copy, playa significa *poco profunda*).
Mirá este gráfico.

![Shallow copy](shallow.png)

La lista interna está siendo compartida aún.

### Deep copies

A veces vas a necesitar hacer una copia de un objeto así como de todos los objetos que contenga. Llamamaos a esto una *copia pofunda* (deep copy) Podés usar el módulo `copy` para esto:

```python
>>> a = [2,3,[100,101],4]
>>> import copy
>>> b = copy.deepcopy(a)
>>> a[2].append(102)
>>> b[2]
[100,101]
>>> a[2] is b[2]
False
>>>
```

### Nombre, vlaores y tipos

Los nombres de variables no tienen un tipo asociado. Solo son nombres. Pero los valores sí tiene un tipo subyacente.

```python
>>> a = 42
>>> b = 'Hello World'
>>> type(a)
<type 'int'>
>>> type(b)
<type 'str'>
```

`type()` te dice el tipo del valor. Se usa como una función que transofrma un valor en un tipo.

### Chequeo de tipos

Podés verificar si un objeto es una instancia de cierto tipo.

```python
if isinstance(a, list):
    print('a is a list')
```

O incluso si su tipo está entre varios tipos.

```python
if isinstance(a, (list,tuple)):
    print('a is a list or tuple')
```

*Cuidado: Demasiado chequeo de tipos puede resultar en un código excesivamente complejo. Típicamente lo usás para evitar errores comunes cometidos por otros usuarios de tu código.*

### Todo es un objeto

Números, cadenas, listas, funciones, excepciones, clases, instancias, etc. son todes objetos. Esto significa que todos los objetos que pueden ser nombrados pueden ser pasados como datos, ubicados en contenedors, etc. sin restricciones. No hay objetos especiales en Python. Todos los objetos viajan en primera clase.

Un ejemplo simple:

```python
>>> import math
>>> items = [abs, math, ValueError ]
>>> items
[<built-in function abs>,
  <module 'math' (builtin)>,
  <type 'exceptions.ValueError'>]
>>> items[0](-45)
45
>>> items[1].sqrt(2)
1.4142135623730951
>>> try:
        x = int('not a number')
    except items[2]:
        print('Failed!')
Failed!
>>>
```

Acá, `items` es una lista que tiene una función, un módulo y una
excepción. Si, es un ejemplo raro. Pero es un ejemplo al fin. Podés usar los elementos de la lista en lugar de los nombres originales:

```python
items[0](-45)       # abs
items[1].sqrt(2)    # math
except items[2]:    # ValueError
```

Con un gran poder viene siempre una gran responsabilidad. Que puedas no significa que debas hacer este tipo de cosas.

## Ejercicios

In this set of ejercicios, we look at some of the power that comes from first-class
objects.

### Ejercicio 3.7: First-class Data
In the file `Data/camion.csv`, we read data organized as columns that look like this:

```csv
name,cajones,precio
"Lima",100,32.20
"Naranja",50,91.10
...
```

In previous code, we used the `csv` module to read the file, but still
had to perform manual type conversions. For example:

```python
for row in rows:
    name   = row[0]
    cajones = int(row[1])
    precio  = float(row[2])
```

This kind of conversion can also be performed in a more clever manner
using some list basic operations.

Make a Python list that contains the names of the conversion functions
you would use to convert each column into the appropriate type:

```python
>>> types = [str, int, float]
>>>
```

The reason you can even create this list is that everything in Python
is *first-class*.  So, if you want to have a list of functions, that’s
fine.  The items in the list you created are functions for converting
a value `x` into a given type (e.g., `str(x)`, `int(x)`, `float(x)`).

Now, read a row of data from the above file:

```python
>>> import csv
>>> f = open('Data/camion.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> row = next(rows)
>>> row
['Lima', '100', '32.20']
>>>
```

As noted, this row isn’t enough to do calculations because the types
are wrong. For example:

```python
>>> row[1] * row[2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
>>>
```

However, maybe the data can be paired up with the types you specified
in `types`. For example:

```python
>>> types[1]
<type 'int'>
>>> row[1]
'100'
>>>
```

Try converting one of the values:

```python
>>> types[1](row[1])     # Same as int(row[1])
100
>>>
```

Try converting a different value:

```python
>>> types[2](row[2])     # Same as float(row[2])
32.2
>>>
```

Try the calculation with converted values:

```python
>>> types[1](row[1])*types[2](row[2])
3220.0000000000005
>>>
```

Zip the column types with the fields and look at the result:

```python
>>> r = list(zip(types, row))
>>> r
[(<type 'str'>, 'Lima'), (<type 'int'>, '100'), (<type 'float'>,'32.20')]
>>>
```

You will notice that this has paired a type conversion with a
value. For example, `int` is paired with the value `'100'`.

The zipped list is useful if you want to perform conversions on all of
the values, one after the other. Try this:

```python
>>> converted = []
>>> for func, val in zip(types, row):
          converted.append(func(val))
...
>>> converted
['Lima', 100, 32.2]
>>> converted[1] * converted[2]
3220.0000000000005
>>>
```

Make sure you understand what’s happening in the above code.  In the
loop, the `func` variable is one of the type conversion functions
(e.g., `str`, `int`, etc.) and the `val` variable is one of the values
like `'Lima'`, `'100'`.  The expression `func(val)` is converting a
value (kind of like a type cast).

The above code can be compressed into a single list comprehension.

```python
>>> converted = [func(val) for func, val in zip(types, row)]
>>> converted
['Lima', 100, 32.2]
>>>
```

### Ejercicio 3.8: Making dictionaries
Remember how the `dict()` function can easily make a dictionary if you
have a sequence of key names and values?  Let’s make a dictionary from
the column headers:

```python
>>> headers
['name', 'cajones', 'precio']
>>> converted
['Lima', 100, 32.2]
>>> dict(zip(headers, converted))
{'precio': 32.2, 'name': 'Lima', 'cajones': 100}
>>>
```

Of course, if you’re up on your list-comprehension fu, you can do the
whole conversion in a single step using a dict-comprehension:

```python
>>> { name: func(val) for name, func, val in zip(headers, types, row) }
{'precio': 32.2, 'name': 'Lima', 'cajones': 100}
>>>
```

### Ejercicio 3.9: The Big Picture
Using the techniques in this ejercicio, you could write statements that
easily convert fields from just about any column-oriented datafile
into a Python dictionary.

Just to illustrate, suppose you read data from a different datafile like this:

```python
>>> f = open('Data/dowcajones.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> row = next(rows)
>>> headers
['name', 'precio', 'date', 'time', 'change', 'open', 'high', 'low', 'volume']
>>> row
['Lima', '39.48', '6/11/2007', '9:36am', '-0.18', '39.67', '39.69', '39.45', '181800']
>>>
```

Let’s convert the fields using a similar trick:

```python
>>> types = [str, float, str, str, float, float, float, float, int]
>>> converted = [func(val) for func, val in zip(types, row)]
>>> record = dict(zip(headers, converted))
>>> record
{'volume': 181800, 'name': 'Lima', 'precio': 39.48, 'high': 39.69,
'low': 39.45, 'time': '9:36am', 'date': '6/11/2007', 'open': 39.67,
'change': -0.18}
>>> record['name']
'Lima'
>>> record['precio']
39.48
>>>
```

Bonus: How would you modify this example to additionally parse the
`date` entry into a tuple such as `(6, 11, 2007)`?

Spend some time to ponder what you’ve done in this ejercicio. We’ll
revisit these ideas a little later.


[Contenidos](../Contenidos.md) \| [Anterior (2 Comprensión de listas)](02_List_comprehension.md) \| [Próximo (4 Numpy)](04_Numpy.md)

