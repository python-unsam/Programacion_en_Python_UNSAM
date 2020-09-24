[Contenidos](../Contenidos.md) \| [Anterior (1 [Contents](../Contents.md) \| [Previous (5.2 Encapsulation)](../05_Object_model/02_Classes_encapsulation.md) \| [Next (6.2 Customizing Iteration)](02_Customizing_iteration.md))](02_protocolo_Iteracion.md) \| [Próximo (3 [Contents](../Contents.md) \| [Previous (6.2 Customizing Iteration)](02_Customizing_iteration.md) \| [Next (6.4 Generator Expressions)](04_More_generators.md))](04_Producers_consumers.md)

# 9.2 [Contents](../Contents.md) \| [Previous (6.1 Iteration Protocol)](01_Iteration_protocol.md) \| [Next (6.3 Producer/Consumer)](03_Producers_consumers.md)

# 6.2 Iteración a medida

Acá vemos como usar una función generadora para obtener el iterador que necesites.

### Un problema
Suppose you wanted to create your own custom iteration pattern.

Suponé que querés crear su secuencia particular de iteración, una cuenta regresiva, por decir algo.

For example, a countdown.

```python
>>> for x in regresiva(10):
...   print(x, end=' ')
...
10 9 8 7 6 5 4 3 2 1
>>>
```
Existe una forma fácil de hacer esto.
There is an easy way to do this.

### Generadores

Un generador es una función que define un patrón de iteración.
A generator is a function that defines iteration.

```python
def regresiva(n):
    while n > 0:
        yield n
        n -= 1
```
*Nota: "yield" se traduce como "rendir" ó "entregar"
Por ejemplo:
For example:

```python
>>> for x in regresiva(10):
...   print(x, end=' ')
...
10 9 8 7 6 5 4 3 2 1
>>>
```

Un generador es *cualquier* función que usa el commando `yield`.
A generator is any function that uses the `yield` statement.

El comportamiento de los generadores es algo diferente al del resto de las funciones.

The behavior of generators is different than a normal function.

Al llamar a un generador creás un objeto generador, pero su función no se ejecuta de inmediato. 

Calling a generator function creates a generator object. It does not
immediately execute the function.

```python
def regresiva(n):
    # Agreguemos este print para ver qué pasa...
    print('Cuenta regresiva desde', n)
    while n > 0:
        yield n
        n -= 1
```

```python
>>> x = regresiva(10)
# No se ejecuta ningún PRINT !
>>> x
# sin embargo x es un objeto generador
<generator object at 0x58490>
>>>
```
La función sólo se ejecuta ante un llamado al método `__next__()`

The function only executes on `__next__()` call.

```python
>>> x = regresiva(10)
>>> x
<generator object at 0x58490>
>>> x.__next__()
Cuenta regresiva desde 10
10
>>>
```
Lo que hace `yield` es notable: produce un valor, y luego suspende la ejecución de la función. La ejecución continúa al volver a llamar a `__next__()`.

`yield` produces a value, but suspends the function execution.
The function resumes on next call to `__next__()`.

```python
>>> x.__next__()
9
>>> x.__next__()
8
```
Cuando finalmente se llega al final de la función, la iteración da un error. 

When the generator finally returns, the iteration raises an error.

```python
>>> x.__next__()
1
>>> x.__next__()
Traceback (most recent call last):
File "<stdin>", line 1, in ? StopIteration
>>>
```

*Observación: Una función generadora implementa el mismo protocolo de bajo nivel que los  `for` usan sobre listas, tuplas, diccionarios, tuplas, archivos, etc.*

A generator function implements the same low-level
 protocol that the for statements uses on lists, tuples, dicts, files,
 etc.*

## Exercises

### Ejercicio 9.4: A Simple Generatorlabel_ej{un_generador_simple}

Si te encontrás con la necesidad de obtener una iteración particular, siempre pensá en funciones generadoras. Son fáciles de escribir: hacé una función que implemente la lógica de iteración deseada y use `yield` para entregar valores.

If you ever find yourself wanting to customize iteration, you should
always think generator functions.  They're easy to write---make
a function that carries out the desired iteration logic and use `yield`
to emit values.

Por ejemplo, probá este generador que busca un archivo y entrega las líneas que incluyen cierto substring.

For example, try this generator that searches a file for lines containing
a matching substring:

```python
>>> def filematch(filename, substr):
        with open(filename, 'r') as f:
            for line in f:
                if substr in line:
                    yield line

>>> for line in open('Data/portfolio.csv'):
        print(line, end='')

nombre,cajones,precio
"Lima",100,32.20
"Naranja",50,91.10
"Limon",150,83.44
"Mandarina",200,51.23
"Durazno",95,40.37
"Mandarina",50,65.10
"Naranja",100,70.44
>>> for line in filematch('Data/portfolio.csv', 'Naranja'):
        print(line, end='')

"Naranja",50,91.10
"Naranja",100,70.44
>>>
```

Esta idea es muy interesante: podés armar una función con código que procesa tus datos y recorrerla con un ciclo for.

El próximo ejemplo es de un caso aún mas especial.

This is kind of interesting--the idea that you can hide a bunch of
custom processing in a function and use it to feed a for-loop.
The next example looks at a more unusual case.

### Ejercicio 9.5: Monitoreo de datos en tiempo real.ing a streaming data source

Un generador puede ser una forma interesante de vigilar datos a medida que son producidos. En esta sección vamos a probar esa idea. Para empezar, hacé lo siguiente.

Generators can be an interesting way to monitor real-time data sources
such as log files or stock market feeds.  In this part, we'll
explore this idea.  To start, follow the next instructions carefully.

El programa `Data/stocksim.py` es un generador de datos. Al ejecutarlo, el programa escribe datos en un archivo llamado `Data/stocklog.csv` contínuamente hasta que es detenido. Corre durante varias horas y una vez que inicies su ejecución podés dejarlo correr y olvidarte de él. Abrí una consola del sistema operativo nueva y ejecutá el programa. Si estás en Windows, dale un doble click al ícono de `stocksim.py`, desde unix:

The program `Data/stocksim.py` is a program that
simulates stock market data.  As output, the program constantly writes
real-time data to a file `Data/stocklog.csv`.  In a
separate command window go into the `Data/` directory and run this program:

```bash
bash % python3 stocksim.py
```

Después, olvidate de él. Dejálo ahí, corriendo.

Usando otra consola, mirá el contenido de `Data/stocklog.csv`. Vas a ver que cada tanto se grega una nueva línea al archivo. 


If you are on Windows, just locate the `stocksim.py` program and
double-click on it to run it.  Now, forget about this program (just
let it run).  Using another window, look at the file
`Data/stocklog.csv` being written by the simulator. You should see
new lines of text being added to the file every few seconds. Again,
just let this program run in the background---it will run for several
hours (you shouldn't need to worry about it).

Once the above program is running, let's write a little program to
open the file, seek to the end, and watch for new output.  Create a
file `follow.py` and put this code in it:

Ahora que el programa generador de datos está en ejecución, escribamos un programa que abra el archivo, vaya al final, y espere nuevos datos. Para esto creá un programa llamado `vigilante.py` que contenga el siguiente código.


```python
# vigilante.py
import os
import time

f = open('Data/stocklog.csv')
f.seek(0, os.SEEK_END)   # Mover el índice 0 posiciones desde el EOF

while True:
    line = f.readline()
    if line == '':
        time.sleep(0.1)   # Esperar un rato y volver a probar
        continue
    fields = line.split(',')
    name = fields[0].strip('"')
    price = float(fields[1])
    change = float(fields[4])
    if change < 0:
        print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
```

*Nota: EOF = End Of File (fin de archivo)*

Cuando ejecutes el programa vas a ver un indicador de precios en tiempo real. 

If you run the program, you'll see a real-time stock ticker.  

Observación: La forma en que usamos el método `readline()` en este ejemplo es un poco rara, no es la forma en que se suele usar (detro de un ciclo `for` para recorrer el contenido de un archivo). En este caso la estamos usando para mirar constantemente el fin de archivo para obtener los últimos datos que se hayan agregado (`readline()` devuelve ó bien el último dato o bien una cadena vacía) 

Note: The use of the `readline()` method in this example is
somewhat unusual in that it is not the usual way of reading lines from
a file (normally you would just use a `for`-loop).  However, in
this case, we are using it to repeatedly probe the end of the file to
see if more data has been added (`readline()` will either
return new data or an empty string).

### Ejercicio 9.6: Uso de un generador para producir datos
Si analizás un poco el código en el ejercicio [Ejercicio 9.5](../09_Generadores_e_Iteradores/03_iteracion_a_medida.md#ejercicio-95-monitoreo-de-datos-en-tiempo-real) vas a notar que la primera parte del programa "produce" datos (los obtiene del archivo) y la segunda los procesa y los imprime. Una característica importante de las funciones generadoras es que podés mover todo el código a una función reutilizable.


If you look at the code in Exercise 6.5, the first part of the code is producing
lines of data whereas the statements at the end of the `while` loop are consuming
the data.  A major feature of generator functions is that you can move all
of the data production code into a reusable function.

Modify the code in Exercise 6.5  so that the file-reading is performed by
a generator function `follow(filename)`.   Make it so the following code
works:

Modificá el código del [Ejercicio 9.5](../09_Generadores_e_Iteradores/03_iteracion_a_medida.md#ejercicio-95-monitoreo-de-datos-en-tiempo-real) de modo que la lectura del archivo sea resuelta por una función generadora `seguir()` a la que se le pase un nombre de archivo como parámetro. Hacelo de modo que el siguiente código funcione:

```python
>>> for line in follow('Data/stocklog.csv'):
          print(line, end='')

... Acá deberías ver las líneas impresas ...
```

Modify the stock ticker code so that it looks like this:

```python
if __name__ == '__main__':
    for line in follow('Data/stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if change < 0:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
```

### Ejercicio 9.7: Watching your portfolio
Modificá el programa `follow.py` para que sólo informe las líneas que tienen precios de fruta incluída en un camión, e ignore el resto de los productos. Por ejemplo: 

Modify the `follow.py` program so that it watches the stream of stock
data and prints a ticker showing information for only those stocks
in a portfolio.  For example:

```python
if __name__ == '__main__':
    import report

    portfolio = report.read_portfolio('Data/portfolio.csv')

    for line in follow('Data/stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
```

Observación: para que esto funcione, tu clase `Portfolio` tiene que haber implementado el operador `in`.

Note: For this to work, your `Portfolio` class must support the `in`
operator.  See [Exercise 6.3](01_Iteration_protocol) and make sure you
implement the `__contains__()` operator.

### Discusión

Hay que mencionar que acaba de suceder algo muy potente: Moviste tu patrón de iteración (el que toma las últimas líneas de un archivo) y lo pusiste en su propia función. La función `follow()` ahora es una función de uso amplio, que podés usar en cualquier programa. Por ejemplo la podrias usar para mirar historial (logs) en un servidor ó de un debugger, o de otras fuentes contínuas de datos.

No está bueno ?


Something very powerful just happened here.  You moved an interesting iteration pattern
(reading lines at the end of a file) into its own little function.   The `follow()` function
is now this completely general purpose utility that you can use in any program.  For
example, you could use it to watch server logs, debugging logs, and other similar data sources.
That's kind of cool.

[Contents](../Contents.md) \| [Previous (6.1 Iteration Protocol)](01_Iteration_protocol.md) \| [Next (6.3 Producer/Consumer)](03_Producers_consumers.md)

[Contenidos](../Contenidos.md) \| [Anterior (1 [Contents](../Contents.md) \| [Previous (5.2 Encapsulation)](../05_Object_model/02_Classes_encapsulation.md) \| [Next (6.2 Customizing Iteration)](02_Customizing_iteration.md))](02_protocolo_Iteracion.md) \| [Próximo (3 [Contents](../Contents.md) \| [Previous (6.2 Customizing Iteration)](02_Customizing_iteration.md) \| [Next (6.4 Generator Expressions)](04_More_generators.md))](04_Producers_consumers.md)

