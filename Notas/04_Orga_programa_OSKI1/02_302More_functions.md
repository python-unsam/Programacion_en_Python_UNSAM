[Contenidos](../Contenidos.md) \| [Anterior (1 Scripting)](01_301Script.md) \| [Próximo (3 Chequeo de errores)](03_303Error_checking.md)

# 4.2 Sobre Funciones

[oski]: # (Although functions were introduced earlier, very few details were provided on how they actually work at a deeper level.  This section aims to fill in some gaps and discuss matters such as calling conventions, scoping rules, and more.
  )

Aunque ya les contanmos antes sobre funciones, les dimos pocos detalles sobre su funcionamiento a un nivel algo mas profundo. En esta sección esperamos completar algunos conceptos como convenciones de uso, alcance (*scope*) y otros temas.  

### Llamando a una Función

Imagine la siguiente función:

```python
def leer_precios(nombre_archivo, debug):
    ...
```

Podés llamar a la función pasando los argumentos por orden:
```
precios = leer_precios('precios.csv', True)
```

O podés llamarla usando palabras clave (*keywords*):

```python
precios = leer_precios(nombre_archivo='precios.csv', debug=True)
```

### Argumentos por Omisión

Si preferís que un argumento sea opcional (*by default*), en ese caso asignale un valor en la definición de la función. Ése será el valor del argumento si llamás a la función sin especificar un valor para ese argumento.

```python
def leer_precios(nombre_archivo, debug=False):
    ...
```

Si asignas un valor para un argumento en la declaración de la función, el argumento será opcional al invocar a esa funcion. Se puede omitir el argumento en la invocación y éste tomará su valor por omisión.

```python
d = leer_precios('precios.csv')
e = leer_precios('precios.dat', True)
```

*Nota: Todos los argumentos con valores por omisión deben aparecer al final de la lista de argumentos (primero se declaran todos los argumentos no-opcionales)*

### Si un argumento es opcional, dale un nombre.

Comparemos estos dos estilos de invocar funciones:

```python
cortar_datos(data, False, True) # ?????

cortar_datos(data, ignore_errores=True)
cortar_datos(data, debug=True)
cortar_datos(data, debug=True, ignore_errores=True)
```

In most cases, keyword arguments improve code clarity--especially for arguments that
serve as flags or which are related to optional features.

En la mayoría de los casos los argumentos con nombre hacen al código más claro, mas fácil de entender, especialmete para argumentos que son signos que deciden funciones opcionales.

### Buenas Prácticas de Diseño

Compará estas dos formas de declarar una misma función. Para comprender cómo usar la primera, tendríamos que explorar dentro de la función y saber que significan sus parámetros. Usá siempre nombres cortos para los argumentos, pero con significado.

```python
def leer_precios(f, d=False):
    ...

def leer_precios(nombre_archivo, debug=False):
    ...
```

Quien use la función podría elegir llamarla con argmuentos nombrados.

```python
d = leer_precios('precios.csv', debug=True)
```

Las herramientas de desarrollo para Python crean automáticamente documentación sobre los argumentos de las funciones, usar nombres con significado hace más útil esta documentación.

### Devolver Resultados

El comando `return` termina la función y devuelve un valor.

```python
def cuadrado(x):
    return x * x
```

Si no se define un resultado, o si falta el comando return, la función devuelve la constante `None`.   

```python
def bar(x):
    instrucciones
    return

a = bar(4)          # a = None

# O TAMBIEN...
def foo(x):
    instrucciones   # No hay `return`

b = foo(4)          # b = None
```

### Devolver Múltiples Resultados

Las funciones sólo pueden devolver una cosa. Si necesitás devolver más de un valor, podés armar una tupla con ellos y devolver la tupla.

```python
def divide(a,b):
    c = a // b      # Cociente
    r = a % b       # Resto
    return c, r     # Devolver una tupla con c y r
```

Ejemplo:

```python
x, y = divide(37,5) # x = 7, y = 2

x = divide(37, 5)   # x = (7, 2)
```

### Alcance de Variables

En un programa se declaran variables y se les asignan valores.
Esto ocurre dentro y fuera de funciones.

```python
x = valor # Variable Global

def foo():
    y = valor # Variable Local
```

Las variables declaradas fuera de funciones son "globales". Las variables declaradas dentro de funciones son "locales".

### Variables Locales

Las variables locales, declaradas dentro de funciones, son privadas.

[oski]:# (Variables assigned inside functions are private.)

```python
def leer_camion(nombre_archivo):
    camion = []
    for line in open(nombre_archivo):
        campos = line.split(',')
        s = (campos[0], int(campos[1]), float(campos[2]))
        camion.append(s)
    return camion
```
[oski]:# (
In this example, `nombre_archivo`, `camion`, `line`, `fields` and `s` are local variables.
Those variables are not retained or accessible after the function call.
)

En este ejemplo, `nombre_archivo`, `camion`, `line`, `campos` y `s` son variables locales.

```python
>>> cajones = leer_camion('camion.csv')
>>> campos
Traceback (most recent call last):
File "<stdin>", line 1, in ?
NameError: name 'campos' is not defined
>>>
```
*El error significa: Error de Nombre: el nombre 'campos' no está definido.*

No hay conflicto entre variables locales y variables declaradas en otras partes (funciones o globales).

[oski]:# (Locals also can't conflict with variables found elsewhere.)

### Variables Globales

Desde cualquier función se puede acceder a las variables globales declaradas en ese mismo archivo.

```python
nombre = 'Dave'

def saludo():
    print('Hola', nombre)  # Usa la variable global `nombre`
```

No es posible, sin embargo, alterar una variable global desde dentro de una función.

[oski]:# (However, functions can't modify globals:)

```python
name = 'Dave'

def spam():
  name = 'Guido'

spam()
print(name) # prints 'Dave'
```
[oski]:# (esto es mío)

Aquí hay dos variables diferentes: 'nombre' global, que vale 'Dave', y 'nombre' local, declarada dentro de `spam()` que vale 'Guido'. Por lo tanto cambiar una no cambia la otra.

**Remember: All assignments in functions are local.**

**Acordate: Las declaraciones dentro de funciones son locales**

[oski]:# (hasta acá llegué 2020-07-15)

### Modifying Globals

If you must modify a global variable you must declare it as such.

```python
name = 'Dave'

def spam():
    global name
    name = 'Guido' # Changes the global name above
```

The global declaration must appear before its use and the corresponding
variable must exist in the same file as the function.   Having seen this,
know that it is considered poor form.  In fact, try to avoid `global` entirely
if you can.  If you need a function to modify some kind of state outside
of the function, it's better to use a class instead (more on this later).

### Argument Passing

When you call a function, the argument variables are names that refer
to the passed values. These values are NOT copies (see [section
2.7](../02_Working_with_data/07_Objects)). If mutable data types are
passed (e.g. lists, dicts), they can be modified *in-place*.

```python
def foo(items):
    items.append(42)    # Modifies the input object

a = [1, 2, 3]
foo(a)
print(a)                # [1, 2, 3, 42]
```

**Key point: Functions don't receive a copy of the input arguments.**

### Reassignment vs Modifying

Make sure you understand the subtle difference between modifying a
value and reassigning a variable name.

```python
def foo(items):
    items.append(42)    # Modifies the input object

a = [1, 2, 3]
foo(a)
print(a)                # [1, 2, 3, 42]

# VS
def bar(items):
    items = [4,5,6]    # Changes local `items` variable to point to a different object

b = [1, 2, 3]
bar(b)
print(b)                # [1, 2, 3]
```

*Reminder: Variable assignment never overwrites memory. The name is merely bound to a new value.*

## Ejercicios

This set of ejercicios have you implement what is, perhaps, the most
powerful and difficult part of the course.  There are a lot of steps
and many concepts from past ejercicios are put together all at once.
The final solution is only about 25 lines of code, but take your time
and make sure you understand each part.

A central part of your `reporte.py` program focuses on the reading of
CSV files.  For example, the function `leer_camion()` reads a file
containing rows of camion data and the function `leer_precios()`
reads a file containing rows of precio data. In both of those
functions, there are a lot of low-level "fiddly" bits and similar
features.  For example, they both open a file and wrap it with the
`csv` module and they both convert various fields into new types.

If you were doing a lot of file parsing for real, you’d probably want
to clean some of this up and make it more general purpose.  That's
our goal.

Start this ejercicio by creating a new file called
`Work/fileparse.py`. This is where we will be doing our work.

### Ejercicio 4.3: Reading CSV Files
To start, let’s just focus on the problem of reading a CSV file into a
list of dictionaries.  In the file `fileparse.py`, define a
function that looks like this:

```python
# fileparse.py
import csv

def parse_csv(nombre_archivo):
    '''
    Parse a CSV file into a list of records
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)
        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            record = dict(zip(headers, row))
            records.append(record)

    return records
```

This function reads a CSV file into a list of dictionaries while
hiding the details of opening the file, wrapping it with the `csv`
module, ignoring blank lines, and so forth.

Try it out:

Ayuda: `python3 -i fileparse.py`.

```python
>>> camion = parse_csv('Data/camion.csv')
>>> camion
[{'precio': '32.20', 'name': 'Lima', 'cajones': '100'}, {'precio': '91.10', 'name': 'Naranja', 'cajones': '50'}, {'precio': '83.44', 'name': 'Caqui', 'cajones': '150'}, {'precio': '51.23', 'name': 'Mandarina', 'cajones': '200'}, {'precio': '40.37', 'name': 'Durazno', 'cajones': '95'}, {'precio': '65.10', 'name': 'Mandarina', 'cajones': '50'}, {'precio': '70.44', 'name': 'Naranja', 'cajones': '100'}]
>>>
```

This is good except that you can’t do any kind of useful calculation
with the data because everything is represented as a string.  We’ll
fix this shortly, but let’s keep building on it.

### Ejercicio 4.4: Building a Column Selector
In many cases, you’re only interested in selected columns from a CSV
file, not all of the data.  Modify the `parse_csv()` function so that
it optionally allows user-specified columns to be picked out as
follows:

```python
>>> # Read all of the data
>>> camion = parse_csv('Data/camion.csv')
>>> camion
[{'precio': '32.20', 'name': 'Lima', 'cajones': '100'}, {'precio': '91.10', 'name': 'Naranja', 'cajones': '50'}, {'precio': '83.44', 'name': 'Caqui', 'cajones': '150'}, {'precio': '51.23', 'name': 'Mandarina', 'cajones': '200'}, {'precio': '40.37', 'name': 'Durazno', 'cajones': '95'}, {'precio': '65.10', 'name': 'Mandarina', 'cajones': '50'}, {'precio': '70.44', 'name': 'Naranja', 'cajones': '100'}]

>>> # Read only some of the data
>>> cajones_held = parse_csv('Data/camion.csv', select=['name','cajones'])
>>> cajones_held
[{'name': 'Lima', 'cajones': '100'}, {'name': 'Naranja', 'cajones': '50'}, {'name': 'Caqui', 'cajones': '150'}, {'name': 'Mandarina', 'cajones': '200'}, {'name': 'Durazno', 'cajones': '95'}, {'name': 'Mandarina', 'cajones': '50'}, {'name': 'Naranja', 'cajones': '100'}]
>>>
```

An example of a column selector was given in [Ejercicio 2.23](../02_Working_with_data/06_List_comprehension).
However, here’s one way to do it:

```python
# fileparse.py
import csv

def parse_csv(nombre_archivo, select=None):
    '''
    Parse a CSV file into a list of records
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [headers.index(ncolumna) for ncolumna in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            # Filter the row if specific columns were selected
            if indices:
                row = [ row[index] for index in indices ]

            # Make a dictionary
            record = dict(zip(headers, row))
            records.append(record)

    return records
```

There are a number of tricky bits to this part. Probably the most
important one is the mapping of the column selections to row indices.
For example, suppose the input file had the following headers:

```python
>>> headers = ['name', 'date', 'time', 'cajones', 'precio']
>>>
```

Now, suppose the selected columns were as follows:

```python
>>> select = ['name', 'cajones']
>>>
```

To perform the proper selection, you have to map the selected column names to column indices in the file.
That’s what this step is doing:

```python
>>> indices = [headers.index(ncolumna) for ncolumna in select ]
>>> indices
[0, 3]
>>>
```

In other words, "name" is column 0 and "cajones" is column 3.
When you read a row of data from the file, the indices are used to filter it:

```python
>>> row = ['Lima', '6/11/2007', '9:50am', '100', '32.20' ]
>>> row = [ row[index] for index in indices ]
>>> row
['Lima', '100']
>>>
```

### Ejercicio 4.5: Performing Type Conversion
Modify the `parse_csv()` function so that it optionally allows
type-conversions to be applied to the returned data.  For example:

```python
>>> camion = parse_csv('Data/camion.csv', types=[str, int, float])
>>> camion
[{'precio': 32.2, 'name': 'Lima', 'cajones': 100}, {'precio': 91.1, 'name': 'Naranja', 'cajones': 50}, {'precio': 83.44, 'name': 'Caqui', 'cajones': 150}, {'precio': 51.23, 'name': 'Mandarina', 'cajones': 200}, {'precio': 40.37, 'name': 'Durazno', 'cajones': 95}, {'precio': 65.1, 'name': 'Mandarina', 'cajones': 50}, {'precio': 70.44, 'name': 'Naranja', 'cajones': 100}]

>>> cajones_held = parse_csv('Data/camion.csv', select=['name', 'cajones'], types=[str, int])
>>> cajones_held
[{'name': 'Lima', 'cajones': 100}, {'name': 'Naranja', 'cajones': 50}, {'name': 'Caqui', 'cajones': 150}, {'name': 'Mandarina', 'cajones': 200}, {'name': 'Durazno', 'cajones': 95}, {'name': 'Mandarina', 'cajones': 50}, {'name': 'Naranja', 'cajones': 100}]
>>>
```

You already explored this in [Ejercicio 2.24](../02_Working_with_data/07_Objects).
You'll need to insert the following fragment of code into your solution:

```python
...
if types:
    row = [func(val) for func, val in zip(types, row) ]
...
```

### Ejercicio 4.6: Working without Headers
Some CSV files don’t include any header information.
For example, the file `precios.csv` looks like this:

```csv
"Lima",9.22
"Uva",24.85
"Ciruela",44.85
"Cereza",11.27
...
```

Modify the `parse_csv()` function so that it can work with such files
by creating a list of tuples instead.  For example:

```python
>>> precios = parse_csv('Data/precios.csv', types=[str,float], has_headers=False)
>>> precios
[('Lima', 9.22), ('Uva', 24.85), ('Ciruela', 44.85), ('Cereza', 11.27), ('C', 3.72), ('Caqui', 35.46), ('Tomate', 66.67), ('Berenjena', 28.47), ('Lechuga', 24.22), ('Durazno', 13.48), ('Remolacha', 0.75), ('Habas', 23.16), ('Frambuesa', 34.35), ('Naranja', 106.28), ('Bruselas', 15.72), ('Batata', 55.16), ('Rúcula', 36.9), ('Radicheta', 26.11), ('Repollo', 49.16), ('Cebolla', 58.99), ('Cebollín', 57.1), ('Puerro', 27.58), ('Mandarina', 20.89), ('Ajo', 15.19), ('Rabanito', 51.94), ('T', 24.79), ('Espinaca', 52.61), ('Acelga', 29.26), ('Zanahoria', 49.74), ('Papa', 69.35)]
>>>
```

To make this change, you’ll need to modify the code so that the first
line of data isn’t interpreted as a header line.  Also, you’ll need to
make sure you don’t create dictionaries as there are no longer any
column names to use for keys.

### Ejercicio 4.7: Picking a different column delimitier
Although CSV files are pretty common, it’s also possible that you
could encounter a file that uses a different column separator such as
a tab or space.  For example, the file `Data/camion.dat` looks like
this:

```csv
name cajones precio
"Lima" 100 32.20
"Naranja" 50 91.10
"Caqui" 150 83.44
"Mandarina" 200 51.23
"Durazno" 95 40.37
"Mandarina" 50 65.10
"Naranja" 100 70.44
```

The `csv.reader()` function allows a different column delimiter to be given as follows:

```python
rows = csv.reader(f, delimiter=' ')
```

Modify your `parse_csv()` function so that it also allows the
delimiter to be changed.

For example:

```python
>>> camion = parse_csv('Data/camion.dat', types=[str, int, float], delimiter=' ')
>>> camion
[{'precio': '32.20', 'name': 'Lima', 'cajones': '100'}, {'precio': '91.10', 'name': 'Naranja', 'cajones': '50'}, {'precio': '83.44', 'name': 'Caqui', 'cajones': '150'}, {'precio': '51.23', 'name': 'Mandarina', 'cajones': '200'}, {'precio': '40.37', 'name': 'Durazno', 'cajones': '95'}, {'precio': '65.10', 'name': 'Mandarina', 'cajones': '50'}, {'precio': '70.44', 'name': 'Naranja', 'cajones': '100'}]
>>>
```

### Commentary

If you’ve made it this far, you’ve created a nice biblioteca function
that’s genuinely useful.  You can use it to parse arbitrary CSV files,
select out columns of interest, perform type conversions, without
having to worry too much about the inner workings of files or the
`csv` module.


[Contenidos](../Contenidos.md) \| [Anterior (1 Scripting)](01_301Script.md) \| [Próximo (3 Chequeo de errores)](03_303Error_checking.md)

