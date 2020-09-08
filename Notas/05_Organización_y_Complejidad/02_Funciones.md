[Contenidos](../Contenidos.md) \| [Anterior (1 Scripting)](01_Scripts.md) \| [Próximo (3 Módulos)](03_Modulos.md)

# 5.2 Funciones

Aunque ya hablamos sobre funciones, dimos pocos detalles sobre su funcionamiento a un nivel algo más profundo. En esta sección esperamos completar algunos conceptos como convenciones de uso, alcance (*scope*) y otros temas.  

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

Si preferís que un argumento sea opcional (que tenga un valor _por omisión_ o  *by default*), en ese caso asignale un valor en la definición de la función. Ése será el valor del argumento si llamás a la función sin especificar un valor para ese argumento.

```python
def leer_precios(nombre_archivo, debug=False):
    ...
```

En la declaración de la función podés asignar un valor a un argumento. Entonces, ese argumento será opcional al invocar a esa funcion y si lo omitís al invocar a la función va a tomar su valor asignado. A ese valor lo llamamos valor por omisión.

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

En la mayoría de los casos los argumentos con nombre hacen al código más claro, más fácil de entender, especialmente si estos argumentos son booleanos, que determinan opciones si-no.

### Buenas prácticas de diseño

Compará estas dos formas de declarar una misma función. Para comprender cómo usar la primera, tendríamos que explorar dentro de la función y saber que significan sus parámetros. Usá siempre nombres cortos para los argumentos, pero con significado.

```python
def leer_precios(f, d=False):
    ...

def leer_precios(nombre_archivo, debug=False):
    ...
```

Quien use la función podría elegir llamarla con argumentos nombrados.

```python
d = leer_precios('precios.csv', debug=True)
```

Hay herramientas que crean automáticamente documentación sobre el uso de las funciones y sus argumentos. Si los nombres tienen significado, la documentación resulta más clara.

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
def dividir(a,b):
    c = a // b      # Cociente
    r = a % b       # Resto
    return c, r     # Devolver una tupla con c y r
```

Ejemplo:

```python
x, y = dividir(37,5) # x = 7, y = 2

x = dividir(37, 5)   # x = (7, 2)
```

### Alcance de variables

En un programa se declaran variables y se les asignan valores.
Esto ocurre dentro y fuera de funciones.

```python
x = valor # Variable Global

def foo():
    y = valor # Variable Local
```

Las variables declaradas fuera de funciones son "globales". Las variables declaradas dentro de funciones son "locales". A esto se llama el alcance (*scope*) de una variable.

### Variables locales

Las variables locales, declaradas dentro de funciones, son privadas.

```python
def leer_camion(nombre_archivo):
    camion = []
    for linea in open(nombre_archivo):
        campos = line.split(',')
        s = (campos[0], int(campos[1]), float(campos[2]))
        camion.append(s)
    return camion
```

En este ejemplo, `nombre_archivo`, `camion`, `linea`, `campos` y `s` son variables locales.

```python
>>> cajones = leer_camion('camion.csv')
>>> campos
Traceback (most recent call last):
File "<stdin>", line 1, in ?
NameError: name 'campos' is not defined
>>>
```
El error significa: *Error de Nombre: el nombre 'campos' no está definido.*

No hay conflicto entre variables locales y variables declaradas en otras partes (funciones o globales).

### Variables globales

Desde cualquier función se puede acceder a las variables globales declaradas en ese mismo archivo.

```python
nombre = 'Dave'

def saludo():
    print('Hola', nombre)  # Usa la variable global `nombre`
```

Las funciones, sin embargo, no alteran normalmente el valor de una variable global.

```python
nombre = 'Dave'

def spam():
  nombre = 'Guido'

spam()
print(nombre) # imprime 'Dave'
```

Aquí hay dos variables diferentes: `nombre` global, que vale `'Dave'`, y `nombre` local, declarada dentro de la función `spam()` que vale `'Guido'`. Cambiar una no cambia la otra: al cambiar el valor de `nombre` local, `nombre` global no cambia.

**Acordate: Las asignaciones de valores a variables y las declaraciones de variables  dentro de funciones son locales.**

### Modificar el valor de una variable global

Si necesitás modificar el valor de una variable global desde dentro de una función, la variable tiene que estar declarada como `global` dentro de la misma función.

```python
nombre = 'Dave'

def spam():
    global nombre
    nombre = 'Guido' # Cambia el valor de la variable global
```

Si declaramos `global nombre` dentro de la función, entonces `nombre` fuera de la función `spam()` y dentro de la función `spam()` refieren a la misma variable, y al modificar una de ellas modificás la otra.

La declaración de globalidad de la variable (con la palabra reservada `global`) tiene que aparecer antes del uso de la variable dentro de una función, y la declaración de la variable global fuera de la función debe ocurrir en el mismo archivo que ésta.

Dicho esto, hay que decir también que usar variables globales se considera una mala práctica. Tratá de evitar completamente el uso de `global`. Si tenés una función que depende del estado de una variable global, tu programa es menos modular: no podés reutilizar la función en otro contexto sin agregar una variable global. Si necesitás que una función modifique el estado de algo fuera de esa función, es mejor entonces usar una clase en lugar de una función. Hablaremos de ésto más adelante, en la segunda mitad de la materia.

### Pasaje de argumentos

Cuando llamás a una función, los argumentos son los nombres que refieren a los valores que le pasás. Estos valores no son copias de los originales (ver [Sección 3.5](../03_Listas_y_Listas/05_Objetos.md#35-objetos)). Si le pasás tipos mutables, como listas o diccionarios, la función *sí* los puede modificar.

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

Es importante que entiendas esta diferencia.

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

*Recordá: reasignar una variable nunca sobreescribe la memoria que ocupaba. Sólo se asocia el nombre de la variable a un nuevo valor.*

## Ejercicios

Este conjunto de ejercicios te llevan a implementar un programa medianamente complejo. Es no trivial. Hay varios pasos involucrados e implica articular muchos conceptos al mismo tiempo.

La solución que vas a desarrollar involucra sólo unas 25 líneas de código, pero tomate tu tiempo para asegurarte de que entendés cada concepto y cada parte del código por separado.

La parte central del programa `informe_funciones.py` resuelve la lectura de archivos de tipo CSV. Por ejemplo, la función `leer_camion()` lee un archivo que contiene los datos de un camión organizados como filas, y la función `leer_precios()` lee un archivo que contiene precios. En ambas funciones hay una variedad de acciones detallistas y minuciosas, por ejemplo, ambos abren un archivo y lo envuelven con el módulo `csv` y ambos convierten cada uno de los campos a un tipo de datos diferente.

Si tu tarea fuera de verdad leer datos de archivos, entonces querrías limpiar este código un poco, hacerlo más prolijo, y aplicable a un uso más general. Ésa es nuestra intención ahora:

Comenzá este ejercicio creando un nuevo archivo llamado `ejercicios_python/fileparse.py`. Ahí vamos a trabajar.

_Nota:_ En inglés *to parse* significa analizar gramaticalmente (por ejemplo una frase), separándola en sus partes constitutivas. Es un término muy usado en ciencias de la computación que no tiene una traducción compacta al castellano. Mucha gente usa el anglicismo *parsear* para referirse a esta actividad.

### Ejercicio 5.3: Parsear un archivo CSV
Vamos a empezar por el problema simple de leer un archivo CSV para guardar los datos que contiene en una lista de diccionarios. En el archivo `fileparse.py` definí la siguiente función:

```python
# fileparse.py
import csv

def parse_csv(nombre_archivo):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)

        # Lee los encabezados
        headers = next(rows)
        registros = []
        for row in rows:
            if not row:    # Saltea filas sin datos
                continue
            registro = dict(zip(headers, row))
            registros.append(registro)

    return registros
```

Esta función lee un archivo CSV y arma una lista de diccionarios a partir del contenido del archivo CSV. La función aísla al programador de los múltiples pequeños pasos necesarios para abrir un archivo, "envolverlo" con el módulo `csv`, ignorar líneas vacías, y demás minucias.

(*un "wrapper" (envoltorio) en programación es una estructura que expone la interfase de un objeto, pero aísla al usuario de los detalles de funcionamiento de ese objeto.*)

Probémoslo en tu IDE o con `python3 -i fileparse.py`.


```python
>>> camion = parse_csv('Data/camion.csv')
>>> camion
[{'nombre': 'Lima', 'cajones': '100', 'precio': '32.2'}, {'nombre': 'Naranja', 'cajones': '50', 'precio': '91.1'}, {'nombre': 'Caqui', 'cajones': '150', 'precio': '103.44'}, {'nombre': 'Mandarina', 'cajones': '200', 'precio': '51.23'}, {'nombre': 'Durazno', 'cajones': '95', 'precio': '40.37'}, {'nombre': 'Mandarina', 'cajones': '50', 'precio': '65.1'}, {'nombre': 'Naranja', 'cajones': '100', 'precio': '70.44'}]
>>>
```

La función hace lo que queríamos, pero no podemos usar los resultados para hacer cálculos porque todos los datos recuperados son de tipo cadena (*string*). Ya vamos a solucionar esto. Por ahora sigamos extendiendo sus funciones.

### Ejercicio 5.4: Selector de Columnas
La mayoría de los casos, uno no está interesado en todos los datos que contiene el archivo CSV, sino sólo en algunas columnas.
Modifiquemos la función `parse_csv` de modo que permita al usuario elegir (opcionalmente) algunas columnas del siguiente modo:

```python
>>> # Lee todos los datos
>>> camion = parse_csv('Data/camion.csv')
>>> camion
[{'nombre': 'Lima', 'cajones': '100', 'precio': '32.2'}, {'nombre': 'Naranja', 'cajones': '50', 'precio': '91.1'}, {'nombre': 'Caqui', 'cajones': '150', 'precio': '103.44'}, {'nombre': 'Mandarina', 'cajones': '200', 'precio': '51.23'}, {'nombre': 'Durazno', 'cajones': '95', 'precio': '40.37'}, {'nombre': 'Mandarina', 'cajones': '50', 'precio': '65.1'}, {'nombre': 'Naranja', 'cajones': '100', 'precio': '70.44'}]

>>> # Lee solo algunos datos
>>> cajones_retenidos = parse_csv('Data/camion.csv', select=['nombre','cajones'])
>>> cajones_retenidos
[{'nombre': 'Lima', 'cajones': '100'}, {'nombre': 'Naranja', 'cajones': '50'}, {'nombre': 'Caqui', 'cajones': '150'}, {'nombre': 'Mandarina', 'cajones': '200'}, {'nombre': 'Durazno', 'cajones': '95'}, {'nombre': 'Mandarina', 'cajones': '50'}, {'nombre': 'Naranja', 'cajones': '100'}]
>>>
```

Vimos un ejemplo de un selector de columnas en el [Ejercicio 3.14](../03_Listas_y_Listas/04_Comprension_Listas.md#ejercicio-314-extraer-datos-de-una-arhcivo-csv).
De todos modos, ésta es otra forma de resolverlo:

```python
# fileparse.py
import csv

def parse_csv(nombre_archivo, select = None):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)

        # Lee los encabezados del archivo
        encabezados = next(filas)

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []

        registros = []
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]

            # Armar el diccionario
            registro = dict(zip(encabezados, fila))
            registros.append(registro)

    return registros
```

Esta parte es un toque técnica y merece una mirada de más cerca. El paso más delicado es traducir los nombres de las columnas seleccionadas a índices. Por ejemplo, supongamos que los encabezados en el archivo de entrada fueran los siguientes:

```python
>>> encabezados = ['nombre', 'dia', 'hora', 'cajones', 'precio']
>>>
```

Y que las columnas seleccionadas fueran:

```python
>>> select = ['nombre', 'cajones']
>>>
```

Para hacer la selección correctamente, tenés que conventir los nombres de las columnas listadas en `select` a índices (posiciones) de columnas en el archivo. Esto es exactamente lo que hace este paso:

```python
>>> indices = [encabezados.index(nombre_columna) for nombre_columna in select ]
>>> indices
[0, 3]
>>>
```


En otras palabras, "nombre" es la columna 0 y "cajones" es la columna 3.
Al leer una línea de datos del archivo, usás los índices para filtrarla y rescatar sólo las columnas que te interesan:

```python
>>> linea = ['Lima', '6/11/2007', '9:50am', '100', '32.20' ]
>>> linea = [ linea[indice] for indice in indices ]
>>> linea
['Lima', '100']
>>>
```

### Ejercicio 5.5: Conversión de tipo
Modificá la función `parse_csv()` de modo que permita, opcionalmente,  convertir el tipo de los datos recuperados antes de devolverlos.

```python
>>> camion = parse_csv('Data/camion.csv', types=[str, int, float])
>>> camion
[{'nombre': 'Lima', 'cajones': 100, 'precio': 32.2}, {'nombre': 'Naranja', 'cajones': 50, 'precio': 91.1}, {'nombre': 'Caqui', 'cajones': 150, 'precio': 103.44}, {'nombre': 'Mandarina', 'cajones': 200, 'precio': 51.23}, {'nombre': 'Durazno', 'cajones': 95, 'precio': 40.37}, {'nombre': 'Mandarina', 'cajones': 50, 'precio': 65.1}, {'nombre': 'Naranja', 'cajones': 100, 'precio': 70.44}]

>>> cajones_lote = parse_csv('Data/camion.csv', select=['nombre', 'cajones'], types=[str, int])
>>> cajones_lote
[{'nombre': 'Lima', 'cajones': 100}, {'nombre': 'Naranja', 'cajones': 50}, {'nombre': 'Caqui', 'cajones': 150}, {'nombre': 'Mandarina', 'cajones': 200}, {'nombre': 'Durazno', 'cajones': 95}, {'nombre': 'Mandarina', 'cajones': 50}, {'nombre': 'Naranja', 'cajones': 100}]
>>>
```

Ya vimos esto en el [Ejercicio 3.15](../03_Listas_y_Listas/05_Objetos.md#ejercicio-315-datos-de-primera-clase). Vas a necesitar insertar la siguiente porción de código en tu implementación:

```python
...
if types:
    fila = [func(val) for func, val in zip(types, fila) ]
...
```
### Ejercicio 5.6: Trabajando sin encabezados
Algunos archivos CSV no tiene información de los encabezados.
Por ejemplo, el archivo `precios.csv` se ve así:

```csv
Lima,40.22
Uva,24.85
Ciruela,44.85
Cereza,11.27
...
```

Modificá la función `parse_csv()` de forma que (opcionalmente) pueda trabajar con este tipo de archivos, creando tuplas en lugar de diccionarios cuando no haya encabezados. Por ejemplo:

```python
>>> precios = parse_csv('Data/precios.csv', types=[str,float], has_headers=False)
>>> precios
[(Lima,40.22), (Uva,24.85), (Ciruela,44.85), (Cereza,11.27), (Frutilla,53.72), (Caqui,105.46), (Tomate,66.67), (Berenjena,28.47), (Lechuga,24.22), (Durazno,73.48), (Remolacha,20.75), (Habas,23.16), (Frambuesa,34.35), (Naranja,106.28), (Bruselas,15.72), (Batata,55.16), (Rúcula,36.9), (Radicheta,26.11), (Repollo,49.16), (Cebolla,58.99), (Cebollín,57.1), (Puerro,27.58), (Mandarina,80.89), (Ajo,15.19), (Rabanito,51.94), (Zapallo,24.79), (Espinaca,52.61), (Acelga,29.26), (Zanahoria,49.74), (Papa,69.35)]
>>>
```

Para hacer este cambio, vas a tener que modificar el código de forma que, si le pasás el parámetro `has_headers = False`, la primera línea de datos no sea interpretada como encabezado. Además, en ese caso, vas a tener que asegurarte de no crear diccionarios, dado que no tenés más los nombres de las columnas para usar en el encabezado. Vale aclarar que este parámetro debe tener como valor por omisión `True`, con lo que la función sigue funcionando igual que antes si no se especifica `has_headers = False`.

Si bien no es difícil, este es un cambio muy grande en esta función. Un camino posible es poner un `if has_headers` al principio y resolver cada caso por separado. Otro camino es poner condicionales en cada paso donde sea necesario operar de manera diferente.

Incorporá todos estos cambios en el archivo `fileparse.py`.

### Comentario
Llegaste lejos. Hasta este punto creaste una biblioteca de funciones que es genuinamente útil. La podés usar para parsear archivos CSV de formato arbitrario, eligiendo las columnas relevantes y cambiando el tipo de datos devuelto, todo esto sin tener que preocuparte mucho por el manejo de archivos o entender cómo funciona el módulo `csv`.  



[Contenidos](../Contenidos.md) \| [Anterior (1 Scripting)](01_Scripts.md) \| [Próximo (3 Módulos)](03_Modulos.md)

