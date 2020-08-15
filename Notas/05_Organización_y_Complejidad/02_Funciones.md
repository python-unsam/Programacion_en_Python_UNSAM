[Contenidos](../Contenidos.md) \| [Anterior (1 Scripting)](01_Scripts.md) \| [Próximo (3 Búsqueda binaria*)](03_BusqBinaria.md)

# 5.2 Sobre Funciones

[oski]: # (Although functions were introduced earlier, very few details were provided on how they actually work at a deeper level.  This section aims to fill in some gaps and discuss matters such as calling conventions, scoping rules, and more.
  )

Aunque ya les contanmos antes sobre funciones, les dimos pocos detalles sobre su funcionamiento a un nivel algo mas profundo. En esta sección esperamos completar algunos conceptos como convenciones de uso, alcance (*scope*) y otros temas.  

### Llamando a una función

Imaginá la siguiente función:

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

### Argumentos por omisión

Si preferís que un argumento sea opcional (*by default*), en ese caso asignale un valor en la definición de la función. Ése será el valor del argumento si llamás a la función sin especificar un valor para ese argumento.

```python
def leer_precios(nombre_archivo, debug=False):
    ...
```

En la declaración de la función podés asignar un valor a un argumento. Entonces, ese argumento será opcional al invocar a esa funcion y si lo omitís al invocar a la función va a tomar su valor asignado. A ese valor lo llamomos valor por omisión.

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

### Buenas prácticas de diseño

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

### Devolver un resultado

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

### Devolver múltiples resultados

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

### Alcance de variables

En un programa se declaran variables y se les asignan valores.
Esto ocurre dentro y fuera de funciones.

```python
x = valor # Variable Global

def foo():
    y = valor # Variable Local
```

Las variables declaradas fuera de funciones son "globales". Las variables declaradas dentro de funciones son "locales". A esto se llama *scope* o (visibilidad ó alcance) de una variable.

### Variables locales

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

### Variables globales

Desde cualquier función se puede acceder a las variables globales declaradas en ese mismo archivo.

```python
nombre = 'Dave'

def saludo():
    print('Hola', nombre)  # Usa la variable global `nombre`
```

No es trivial, sin embargo, alterar una variable global desde dentro de una función.

[oski]:# (However, functions can't modify globals:)

```python
name = 'Dave'

def spam():
  name = 'Guido'

spam()
print(name) # imprime 'Dave'
```

[oski]: # (esto es mio)

Aquí hay dos variables diferentes: `nombre` global, que vale `'Dave'`, y `nombre` local, declarada dentro de la función `spam()` que vale `'Guido'`. Cambiar una no cambia la otra: al cambiar el valor de `nombre` local, `nombre` global no cambia.

[oski]:# (
**Remember: All assignments in functions are local.**
)

**Acordate: Las asignaciones de valores a variables y las declaraciones de variables  dentro de funciones son locales**



[oski]: # (### Modifying Globals)
### Modificar el valor de una variable global

[oski]: # (If you must modify a global variable you must declare it as such.
)

Si necesitás modificar el valor de una variable global desde dentro de una función, la variable tiene que estar declarada `global`.

```python
nombre = 'Dave'

def spam():
    global nombre
    nombre = 'Guido' # Cambia el valor de la variable global
```

Si declaramos `global nombre` dentro de la función, entonces `nombre` fuera de la función `spam()` y dentro de la función `spam()` refieren a la misma variable, y al modificar una de ellas modificás la otra.

[oski]: # ( The global declaration must appear before its use and the corresponding variable must exist in the same file as the function.   Having seen this, know that it is considered poor form.  In fact, try to avoid `global` entirely if you can.  If you need a function to modify some kind of state outside of the function, it's better to use a class instead - more on this later.
)

La palabra reservada `global` tiene que aparecer antes del uso de la variable dentro de una función, y la declaración de la variable global fuera de la función debe ocurrir en el mismo archivo que ésta.

Dicho ésto, hay que decir también que ésta se considera una mala práctica. Tratá de evitar completamente el uso de `global`. Si tenés una función que depende del estado de una variable global, tu programa es menos modular: no podés reutilizar la función en otro contexto sin agregar una variable global. Si necesitás que una función modifique el estado de algo fuera de esa función, es mejor entonces usar una clase en lugar de una función - hablaremos de ésto mas adelante.       

[oski]: # (### Argument Passing)

### Pasaje de argumentos

Cuando llamás a una función, las variables argumento (o simplemente los "argumentos") son los nombres que refieren a los valores que le pasás. Estos valores no son copias de los originales. (ver sección [Sección 3.5](../03_Mas_Python/05_Objetos.md#35-objetos) ) Si le pasás tipos mutables, como listas ó diccionarios, la función *si* los puede modificar.

```python
def foo(items):
    items.append(42)    # Cambia el valor de items

a = [1, 2, 3]
foo(a)
print(a)                # [1, 2, 3, 42]
```

**Fundamental: Las funciones no reciben una *copia* de los argumentos, sino los argumentos mismos.**

### Reasignar versus modificar

Existe una sutil pero importante diferencia entre *modificar* el valor de una variable y *reasignar* una variable.

Es importante que entiendas esa diferencia.

```python
def foo(items):
    items.append(42)    # Modifica el valor de 'items'

a = [1, 2, 3]
foo(a)
print(a)                # [1, 2, 3, 42]

# Versus
def bar(items):
    items = [4,5,6]    # Cambia la variable local 'items' y
    # hace que apunte a otro objeto completamente diferente.

b = [1, 2, 3]
bar(b)
print(b)               # imprime [1, 2, 3]
```

[oski]: # (*Reminder: Variable assignment never overwrites memory. The name is merely bound to a new value.*)

*Recordá: reasignar una variable nunca sobreescribe la memoria que ocupaba. Sólo se asocia el nombre de la variable a un nuevo valor.*



## Ejercicios

Este conjunto de ejercicios te llevan a implementar un programa, que será la parte mas dificil y poderosa del curso. Hay varios pasos involucrados e implica articular muchos conceptos al mismo tiempo.

La solución que vas a desarrollar involucra unas 25 líneas de código, pero tomáte tu tiempo para asegurarte que entendés cada concepto y cada parte del código por separado y en su relación con las demás.   

[oski]:# (  
This set of ejercicios have you implement what is, perhaps, the most
powerful and difficult part of the course.  There are a lot of steps
and many concepts from past ejercicios are put together all at once.
The final solution is only about 25 lines of code, but take your time
and make sure you understand each part.
)

La parte central del programa `informe.py` resuelve la lectura de archivos de tipo CSV. Por ejemplo, la función `leer_camion()` lee un archivo que contiene los datos de un camión organizados como filas, y la función `leer_precios()` lee un archivo que contiene precios. En ambas funciones hay una variedad de acciones detallistas y minuciosas, por ejemplo, ambos abren un archivo y lo envuelven con el módulo `cvs` y ambos convierten cada uno de los campos a un tipo de datos diferente.

[oski]:# (
A central part of your `informe.py` program focuses on the reading of
CSV files.  For example, the function `leer_camion{}` reads a file
containing rows of camion data and the function `leer_precios{}`
reads a file containing rows of precio data. In both of those
functions, there are a lot of low-level "fiddly" bits and similar
features.  For example, they both open a file and wrap it with the
`csv` module and they both convert various fields into new types.
)

Si tu tarea fuera de verdad leer datos de archivos, entonces querrías limpiar este código un poco, hacerlo mas prolijo, y aplicable a un uso mas general. Ésa es nuestra intención ahora:  

Comenzá este ejercicio creando un nuevo archivo llamado `ejercicios_python/fileparse.py`. Allí vamos a trabajar.

[oski]:# (
If you were doing a lot of file parsing for real, you’d probably want
to clean some of this up and make it more general purpose.  That's
our goal.
Start this ejercicio by creating a new file called
`ejercicios_python/fileparse.py`. This is where we will be doing our work.
)

### Ejercicio 5.3: Reading CSV Files
Vamos a empezar por el problema simple de leer un archivo CSV para guardar los datos que contiene en una lista de diccionarios. En el archivo `fileparse.py` definí la siguiente función:

[oski]:# (
To start, let’s just focus on the problem of reading a CSV file into a
list of dictionaries.  In the file `fileparse.py`, define a
function that looks like this:
)
```python
# fileparse.py
import csv

def parse_csv(nombre_archivo):
    '''
    Separa un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)

        # Lee los encabezados
        headers = next(rows)
        records = []
        for row in rows:
            if not row:    # Saltea filas sin datos
                continue
            record = dict(zip(headers, row))
            records.append(record)

    return records
```

[oski]:# (
This function reads a CSV file into a list of dictionaries while
hiding the details of opening the file, wrapping it with the `csv`
module, ignoring blank lines, and so forth.
Try it out:
Ayuda: `python3 -i fileparse.py`.
)

Esta función lee un archivo CSV y arma una lista de diccionarios a partir del contenido del archivo CSV. La función aísla al programador de los múltiples pequeños pasos necesarios para abrir un archivo, "envolverlo" con el módulo `csv`, ignorar líneas vacías, y demás minucias.

(*un "wrapper" (envoltorio) en programación es una estructura que expone la interfase de un objeto, pero aísla al usuario de los detalles de funcionamiento de ese objeto.*)

Probémoslo:

Ayuda: `python3 -i fileparse.py`.


```python
>>> camion = parse_csv('Data/camion.csv')
>>> camion
[{'precio': '32.20', 'name': 'Lima', 'cajones': '100'}, {'precio': '91.10', 'name': 'Naranja', 'cajones': '50'}, {'precio': '83.44', 'name': 'Caqui', 'cajones': '150'}, {'precio': '51.23', 'name': 'Mandarina', 'cajones': '200'}, {'precio': '40.37', 'name': 'Durazno', 'cajones': '95'}, {'precio': '65.10', 'name': 'Mandarina', 'cajones': '50'}, {'precio': '70.44', 'name': 'Naranja', 'cajones': '100'}]
>>>
```

La función hace lo que queríamos, pero no podemos usar los resultados para hacer cálculos porque todos los datos recuperados son de tipo cadena (*string*).
Ya vamos a solucionar esto. Por ahora sigamos extendiendo sus funciones.

[oski]:# (
This is good except that you can’t do any kind of useful calculation
with the data because everything is represented as a string.  We’ll
fix this shortly, but let’s keep building on it.
)

### Ejercicio 5.4: Selector de Columnas
La mayoría de los casos, uno no está interesado en todos los datos que un archivo CSV contiene, sino sólo en algunas columnas.
Modifiquemos la función `parse_csv` de modo que permita elegir opcionalmente algunas columnas indicadas por el usuario, del siguiente modo:

[oski]:# (
In many cases, you’re only interested in selected columns from a CSV
file, not all of the data.  Modify the `parse_csv` function so that
it optionally allows user-specified columns to be picked out as
follows:
)

```python
>>> # Lee todos los datos
>>> camion = parse_csv('Data/camion.csv')
>>> camion
[{'precio': '32.20', 'name': 'Lima', 'cajones': '100'}, {'precio': '91.10', 'name': 'Naranja', 'cajones': '50'}, {'precio': '83.44', 'name': 'Caqui', 'cajones': '150'}, {'precio': '51.23', 'name': 'Mandarina', 'cajones': '200'}, {'precio': '40.37', 'name': 'Durazno', 'cajones': '95'}, {'precio': '65.10', 'name': 'Mandarina', 'cajones': '50'}, {'precio': '70.44', 'name': 'Naranja', 'cajones': '100'}]

>>> # Lee solo algunos datos
>>> cajones_retenidos = parse_csv('Data/camion.csv', select=['name','cajones'])
>>> cajones_retenidos
[{'name': 'Lima', 'cajones': '100'}, {'name': 'Naranja', 'cajones': '50'}, {'name': 'Caqui', 'cajones': '150'}, {'name': 'Mandarina', 'cajones': '200'}, {'name': 'Durazno', 'cajones': '95'}, {'name': 'Mandarina', 'cajones': '50'}, {'name': 'Naranja', 'cajones': '100'}]
>>>
```

Vimos un ejemplo de un selector de columnas en el [Ejercicio 3.10](../03_Mas_Python/04_Comprension_Listas.md#ejercicio-310-extraer-datos-de-una-arhcivo-csv)

[oski]:# (no se donde quedó el que se llamaba "Exercise 2.23: Extracting Data From CSV Files" en el original en ingles)

De todos modos, esta es otra forma de resolverlo:

```python
# fileparse.py
import csv

def parse_csv(nombre_archivo, selec=None):
    '''
    Parse a CSV file into a list of records
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)

        # Lee los encabezados del archivo
        encabezados = next(filas)

        # Si se indicó un selector de columnas,
        #   buscar los índices de las columnas especificadas.
        # Y achicar el conjunto de encabezados para diccionarios

        if selec:
            indices = [encabezados.index(ncolumna) for ncolumna in selec]
            encabezados = selec
        else:
            indices = []

        registros = []
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [ fila[index] for index in indices ]

            # Armar el diccionario
            registro = dict(zip(encabezados, fila))
            registros.append(registro)

    return registros
```

[oski]:# (
There are a number of tricky bits to this part. Probably the most
important one is the mapping of the column selections to row indices.
For example, suppose the input file had the following headers:
)

Esta parte no es trivial y merece una mirada de más cerca.

El paso mas importante es traducir los nombres de las columnas seleccionadas a índices. Por ejemplo, supongamos que los encabezados en el archivo de entrada fueran los siguientes:

[oski]:# (
There are a number of tricky bits to this part. Probably the most
important one is the mapping of the column selections to row indices.
For example, suppose the input file had the following headers:
)
```python
>>> encabezados = ['nombre', 'dia', 'hora', 'cajones', 'precio']
>>>
```

Y que las columnas seleccionadas fueran:

```python
>>> selec = ['nombre', 'cajones']
>>>
```

[oski]: # (To perform the proper selection, you have to map the selected column names to column indices in the file.
That’s what this step is doing:)

Para hacer la selección correctamente, tendrías que relacionar los nombres de las columnas listadas en `selec` a índices de columnas en el archivo. Eso es exactamente lo que hace este paso:

```python
>>> indices = [encabezados.index(ncolumna) for ncolumna in selec ]
>>> indices
[0, 3]
>>>
```

[oski]:# (
In other words, "name" is column 0 and "cajones" is column 3.
When you read a row of data from the file, the indices are used to filter it:
)

En otras palabras, "nombre" es la columna 0 y "cajones" es la columna 3.
Al leer una línea de datos del archivo, usás los índices para filtrarla y rescatar sólo las columnas que te interesan:

```python
>>> linea = ['Lima', '6/11/2007', '9:50am', '100', '32.20' ]
>>> linea = [ linea[indice] for indice in indices ]
>>> row
['Lima', '100']
>>>
```

### Ejercicio 5.5: Performing Type Conversion
Modificá la función `parse_csv()` de modo que permita, opcionalmente,  convertir el tipo de los datos recuperados antes de devolverlos.

```python
>>> camion = parse_csv('Data/camion.csv', types=[str, int, float])
>>> camion
[{'precio': 32.2, 'name': 'Lima', 'cajones': 100}, {'precio': 91.1, 'name': 'Naranja', 'cajones': 50}, {'precio': 83.44, 'name': 'Caqui', 'cajones': 150}, {'precio': 51.23, 'name': 'Mandarina', 'cajones': 200}, {'precio': 40.37, 'name': 'Durazno', 'cajones': 95}, {'precio': 65.1, 'name': 'Mandarina', 'cajones': 50}, {'precio': 70.44, 'name': 'Naranja', 'cajones': 100}]

>>> cajones_lote = parse_csv('Data/camion.csv', select=['name', 'cajones'], types=[str, int])
>>> cajones_lote
[{'name': 'Lima', 'cajones': 100}, {'name': 'Naranja', 'cajones': 50}, {'name': 'Caqui', 'cajones': 150}, {'name': 'Mandarina', 'cajones': 200}, {'name': 'Durazno', 'cajones': 95}, {'name': 'Mandarina', 'cajones': 50}, {'name': 'Naranja', 'cajones': 100}]
>>>
```

Ya vimos esto en el [Ejercicio 2.24](../02_Working_with_data/07_Objects). Vas a necesitar insertar la siguiente porción de código en tu implementación:

```python
...
if tipos	:
    fila = [func(val) for func, val in zip(tipos, fila) ]
...
```

### Ejercicio 5.6: Working without Headers
Muchos archivos CSV no incluyen encabezados de ningún tipo. Por ejemplo, el archivo `precios.csv` tiene este aspecto: 

```csv
"Lima",9.22
"Uva",24.85
"Ciruela",44.85
"Cereza",11.27
...
```

Modificá la función `parse_csv()` de modo que pueda trabajar con archivos de ese estilo. Vas a tener que devolver una lista de tuplas en lugar de una lista de diccionarios. Por ejemplo:  

```python
>>> precios = parse_csv('Data/precios.csv', types=[str,float], has_headers=False)
>>> precios
[('Lima', 9.22), ('Uva', 24.85), ('Ciruela', 44.85), ('Cereza', 11.27), ('C', 3.72), ('Caqui', 35.46), ('Tomate', 66.67), ('Berenjena', 28.47), ('Lechuga', 24.22), ('Durazno', 13.48), ('Remolacha', 0.75), ('Habas', 23.16), ('Frambuesa', 34.35), ('Naranja', 106.28), ('Bruselas', 15.72), ('Batata', 55.16), ('Rúcula', 36.9), ('Radicheta', 26.11), ('Repollo', 49.16), ('Cebolla', 58.99), ('Cebollín', 57.1), ('Puerro', 27.58), ('Mandarina', 20.89), ('Ajo', 15.19), ('Rabanito', 51.94), ('T', 24.79), ('Espinaca', 52.61), ('Acelga', 29.26), ('Zanahoria', 49.74), ('Papa', 69.35)]
>>>
```

Para obtener este comportamiento, vas a tener que modificar tu código de modo que la primer línea de datos no sea interpretada como un encabezado. Además, ya no tenés nombres de columnas que puedas usar como claves en un diccionario, así que vas a tener que devolver otra estructura de datos en lugar de una lista de diccionarios.


### Ejercicio 5.7: Picking a different column delimitier
Aunque los archivos en formato CSV son muy comunes(\*), también es posible que encuentres archivos que usen distintos separadores de columnas, tales como un espacio o un tabulador. Por ejemplo, el archivo `Data/camion.dat` tiene este aspecto: 
(\*) recordar que CSV="comma separated values" ó valores separados por *comas*.

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

La función `csv.reader()` permite especificar el separador de columnas a elección, como se muestra: 

```python
rows = csv.reader(f, delimiter=' ')
```

Modificá tu función `parse_csv()` de modo que también admita otros separadores que no sean `,` (coma).

Veamos:

```python
>>> camion = parse_csv('Data/camion.dat', types=[str, int, float], delimiter=' ')
>>> camion
[{'precio': '32.20', 'name': 'Lima', 'cajones': '100'}, {'precio': '91.10', 'name': 'Naranja', 'cajones': '50'}, {'precio': '83.44', 'name': 'Caqui', 'cajones': '150'}, {'precio': '51.23', 'name': 'Mandarina', 'cajones': '200'}, {'precio': '40.37', 'name': 'Durazno', 'cajones': '95'}, {'precio': '65.10', 'name': 'Mandarina', 'cajones': '50'}, {'precio': '70.44', 'name': 'Naranja', 'cajones': '100'}]
>>>
```

### Comentario

Llegaste lejos. Hasta este punto creaste una biblioteca de funciones que es genuinamente útil. La podés usar para parsear archivos CSV de formato arbitrario, eligiendo las columnas relevantes y cambiando el tipo de datos devuelto, todo esto sin tener que preocuparte mucho por el manejo de archivos o entender cómo funciona el módulo `csv`.  



[Contenidos](../Contenidos.md) \| [Anterior (1 Scripting)](01_Scripts.md) \| [Próximo (3 Búsqueda binaria*)](03_BusqBinaria.md)

