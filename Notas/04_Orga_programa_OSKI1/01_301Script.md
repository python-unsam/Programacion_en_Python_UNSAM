[Contenidos](../Contenidos.md) \| [Próximo (2 Sobre Funciones)](02_302More_functions.md)

# 4.1 Scripting

[oski]: # (Esto es un comentario que no se vé en el render MarkDown.)

[oski]: # (
  In this part we look more closely at the practice of writing Python scripts.
)
En esta sección vemos mas de cerca el proceso de crear scripts en Python

### Qué es un Script?

Un *script* es un programa que ejecuta una serie de comandos y termina. *Programa* en el sentido clásico de la palabra: una secuencia de eventos.

```python
# programa.py

comando1
comando2
comando3
...
```

Hasta aquí mayormente hemos escrito scripts.

### Un Problema


Cuando hayas escrito un script útil, éste va a comenzar a crecer en funciones y opciones. Vas a querer aplicarlo a otros problemas. Con el tiempo puede convertirse en un programa escencial, pero si no lo cuidás puede convertirse en un lío enorme y embrollado. Veamos como lo organizamos.


### Definir Nombres

Los nombres deben definirse antes de usarse.

```python
def cuadrado (x):
    return x*x

a = 42
b = a + 2     # Requiere que 'a' haya sido definido antes.

z = cuadrado (b) # Requiere que 'cuadrado' y 'b' estén definidos.
```

**El orden importa.**
Casi siempre definimos las variables y las funciones al comienzo.

### Definición de Funciones

Al definir una funcion podemos agrupar el código relevante a una misma *tarea* en el mismo lugar.

```python
def leer_precios(nombre_archivo):
    precios = {}
    with open(nombre_archivo) as f:
        f_csv = csv.reader(f)
        for linea in f_csv:
            precios[linea[0]] = float(linea[1])
    return precios
```
Una función simplifica las operaciones repetitivas.

```python
preciosviejos = leer_precios('preciosviejos.csv')
preciosnuevos = leer_precios('preciosnuevos.csv')
```

### Qué es una Función ?

Una función es una secuencia de comandos, con un nombre.

```python
def nombrefunc(args):
  comando
  comando
  ...
  return result
```

*Cualquier* Comando de Python puede usarse dentro de una función.

```python
def foo():
    import math
    print(math.sqrt(2))
    help(math)
```

No existen comandos *especiales* en Python (lo cual es muy fácil de recordar).

### Definición de Funciones

En Python podemos *definir* funciones en cualquier orden.

```python
def foo(x):
    bar(x)

def bar(x):
    comandos

# OR
def bar(x):
    comandos

def foo(x):
    bar(x)
```

El único requisito es que la función esté definida al momento de ser *usada* (o llamada) durante la ejecución de un programa.

```python
foo(3)        # foo tiene que haber sido definida antes
```

Probablemente sea mas común, por cuestiones de estilo, definir funciones desde abajo hacia arriba ("*bottom-up*")  

### El Estilo *Bottom-up*

Se trata a la funciones como ladrillos. Los ladrillos simples ó mas pequeños se definen primero, y luego se usan para armar funciones mas complejas.

```python
# miprograma.py
def foo(x):
    ...

def bar(x):
    ...
    foo(x)          # Definida antes
    ...

def spam(x):
    ...
    bar(x)          # Definida antes
    ...

spam(42)            # El código que *usa* la función está al final
```

Las funciones complejas se basan en funciones mas simples, definidas antes; aunque esto es sólo una cuestión de estilo en Python. Lo único que realmente importa en ése programa es que la llamada a `spam(42)` esté después que la declaración de las funciones que éste invoca.

### Diseño de Funciones

Lo ideal es que una función sea una *caja negra*. Una función debería operar únicamente sobre los parámetros provistos, evitar variables globales y efectos secundarios no esperados. Lo importante es *Diseño Modular* y *Predecibilidad*.

[oski]:# (Esto hay que ampliarlo, explicar predecibilidad y modularidad)

### Doc-Strings

Es buena costumbre incluír documentación en forma de doc-strings. Un doc-string ó "texto de documentación" es texto ubicado en la línea inmediata después del nombre de la función. Proveen información a `help()`, IDEs y otras herramientas de programación y documentación.     

```python
def leer_precios(nombre_archivo):
    '''
    Lee precios de un archivo de datos CSV como nombre,precio
    '''
    precios = {}
    with open(nombre_archivo) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            precios[linea[0]] = float(linea[1])
    return precios
```

Es bueno que un doc-string sea una frase corta, de una línea, indicando qué hace la función. Si se necesita mas información incluí un ejemplo corto de uso y una descripción de los argumentos.

### Notas de Tipo de Datos

También podés agregar, en la definición de funciones, notas sobre el tipo de datos de los parámetros y de la función.

```python
def leer_precios(nombre_archivo: str) -> dict:
    '''
    Lee precios de un archivo de datos CSV como nombre,precio
    Devuelve un diccionario {nombre:precio, ...}
    '''
    precios = {}
    with open(nombre_archivo) as f:
        f_csv = csv.reader(f)
        for linea in f_csv:
            precios[linea[0]] = float(linea[1])
    return precios
```
Estas notas no modifican al programa y son puramente informativas. Aún así pueden ser usadas por IDEs, comprobadores de código, y otras herramientas.

[oski]: #()
Aunque `-> dict` indica al programador que la función devuelve un diccionario, es útil anotar en el doc-string la estructura del diccionario devuelto.  

## Ejercicios

[oski]: # (In section 2, you wrote a program called  `reporte.py` that printed out a report showing the performance of a cajon camion. This program consisted of some functions. For example:)

En la sección 2, escribiste un programa llamado `reporte.py` que imprime un informe mostrando ...  
El programa está hecho con algunas funciones, por ejemplo:

```python
# reporte.py
import csv

def leer_camion(nombre_archivo):
    '''
    Read a cajon camion file into a list of dictionaries with keys
    name, cajones, and precio.
    '''
    camion = []
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            cajon = {
                'name' : record['name'],
                'cajones' : int(record['cajones']),
                'precio' : float(record['precio'])
            }
            camion.append(cajon)
    return camion
...
```

[oski]: # (However, there were also portions of the program that just performed a series of scripted calculations.  This code appeared near the end of the program. For example:)

Sin embargo había también partes del programa que ejecutaban una serie de cálculos en forma de script. Este código estaba casi al final del programa. Por ejemplo:

```python
...

# Output the report

headers = ('Name', 'Cajons', 'Price', 'Change')
print('%10s %10s %10s %10s'  % headers)
print(('-' * 10 + ' ') * len(headers))
for row in report:
    print('%10s %10d %10.2f %10.2f' % row)
...
```
[oski]:# (In this ejercicio, we’re going take this program and organize it a little more strongly around the use of functions.)

En este ejercicio vamos a tomar este programa y organizarlo mejor usando el concepto de funciones.

### Ejercicio 4.1: Estructurar un programa como una colección de funciones
Modificá tu programa `reporte.py` de modo que todas las operaciones principales, incluyendo cálculos e impresión, sean llevados a cabo por una colección de funciones. Más específicamente:

* Creá una función `print_report(report)` que imprima el informe.
* Cambiá la última parte del programa de modo que consista sólo en una serie de llamados a funciones, sin ningún cómputo.


### Ejercicio 4.2: Crear una función de alto nivel para la ejecución del programa.
[oski]:# ( Take the last part of your program and package it into a single function reporte_camion { camion_nombre_archivo, precios_nombre_archivo }.
Have the function work so that the following function call creates the report as before: )

Empaquetá la última parte de tu programa en una única función `reporte_camion(camion_nombre_archivo, precios_nombre_archivo)`.

Hacé que el siguiente llamado resulte en la creación de un informe, como antes:

```python
reporte_camion('Data/camion.csv', 'Data/precios.csv')
```

En su versión final tu programa será una serie de definiciones de funciones seguidos por un único llamado a la funcion `reporte_camion()` (la cual ejecuta todos los pasos que constituyen tu programa).

Cuando tu programa es una única función, es muy simple ejecutarlo con diferentes entradas. Por ejemplo, después de ejecutar tu programa probá estos comandos en modo interactivo:

```python
>>> reporte_camion('Data/camion2.csv', 'Data/precios.csv')
... mirá el resultado ...

>>> files = ['Data/camion.csv', 'Data/camion2.csv']
>>> for name in files:
        print(f'{name:-^43s}')
        reporte_camion(name, 'Data/precios.csv')
        print()

... mirá el resultado ...
>>>
```

### Comentarios

[oski]:# (
Python makes it very easy to write relatively unstructured scripting code where you just have a file with a sequence of comandos in it. In the big picture, it's almost always better to utilize functions whenever you can.  At some point, that script is going to grow and you'll wish you had a bit more organization.  Also, a little known fact is that Python
runs a bit faster if you use functions.
)

En Python es muy fácil escribir código en forma de un script relativamente poco estructurado, en el que tenés un archivo que contiene una secuencia de comandos. En perspectiva, casi siempre es mejor usar funciones siempre que puedas. En algún momento ese script va a crecer, y vas a desear haber sido un poco más organizado. Además Python ejecuta algo más rápido si usás funciones.


[Contenidos](../Contenidos.md) \| [Próximo (2 Sobre Funciones)](02_302More_functions.md)

