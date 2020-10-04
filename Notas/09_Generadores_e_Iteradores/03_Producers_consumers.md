[Contenidos](../Contenidos.md) \| [Anterior (2 Iteración a medida)](02_iteracion_a_medida.md) \| [Próximo (4 Más sobre generadores)](04_Mas_generadores.md)

# 9.3 Productores, consumidores, cañerías.

Los generadores son una herramienta muy útil para configurar "cañerías".
Este concepto requiere una breve *aclaración*: Una cañería tradicional en computación ("pipeline" en inglés) consta de una serie de programas y archivos asociados que constituyen una estructura de procesamiento de datos, donde cada programa ejecuta independientemente de los demás, pero juntos resultan en un flujo conveniente de datos a través de los archivos asociados desde un "productor" (una cámara, un sensor, un lector de código de barras) hasta un "consumidor" (un graficador, un interruptor eléctrico, un de una página web). Construíste un pequeño pipeline en la sección anterior, usando `vigilante.py`.  

En esta sección hablaremos de cómo implementar estas estructuras de productores y consumidores de datos con generadores en Python.

### Sistemas productor-consumidor

El concepto de generadores está íntimamente asociado a problemas de tipo productor-consumidor en sus varias formas. Fijate esta estructura, que es típica de muchos programas:

```python
# Productor
def vigilante(f):
    ...
    while True:
        ...
        yield linea        # Produce/obtiene valores para "linea"
        ...

# Consumidor
for linea in vigilar(f):    # Consume líneas del `yield`
    ...
```

Los `yield` generan los datos que los `for` consumen.

### Pipelines con generadores

Podés usar esta característica de los generadores para construír *pipelines* que procesen tus datos, un concepto que es muy usado en Unix (pipes) pero en Windows se usa menos.

*productor* &rarr; *procesamiento* &rarr; *procesamiento* &rarr; *consumidor*

Los *pipelines* de procesamiento de datos tienen un productor al comienzo, una cadena de etapas de procesamiento y un consumidor al final.

**productor** &rarr; *procesamiento* &rarr; *procesamiento* &rarr; *consumidor*

```python
def productor():
    ...
    yield item
    ...
```

El productor es en general un generador, aunque tambien podría ser una lista o cualquier otra secuencia iterable.

El `yield` alimenta al pipeline de datos.

*productor* &rarr; *procesamiento* &rarr; *procesamiento* &rarr; **consumidor**

```python
def consumidor(s):
    for item in s:
        ...
```

El consumidor es un ciclo `for`. Obtiene los elementos `item` y los usa para algo.

*productor* &rarr; **procesamiento** &rarr; **procesamiento** &rarr; *consumidor*

```python
def procesamiento(s):
    for item in s:
        ...
        yield itemnuevo
        ...
```

Las etapas intermedias de procesamiento simultáneamente consumen y producen datos, pueden alterar el flujo de datos, eliminar o modificar datos según su función.

*productor* &rarr; *procesamiento* &rarr; *procesamiento* &rarr; *consumidor*

```python
def productor():
    ...
    yield item          # yield devuelve un item que será recibido por `procesamiento`
    ...

def procesamiento(s):
    for item in s:      # item viene del `productor`
        ...
        yield newitem   # este yield devuelve un nuevo item
        ...

def consumidor(s):
    for item in s:      # item viene de `procesamiento`
        ...
```

Vamos a construír un pipeline con la siguiente arquitectura:

```python
a = productor()
b = procesamiento(a)
c = consumidor(b)
```

Como te darás cuenta, los datos van pasando de una función a la siguiente.

## Ejercicios

Para este ejercicio, necesitás que el programa `sim_mercado.py` aún esté corriendo. Vas a usar la función `vigilar()` que escribiste en el [Ejercicio 9.7](../09_Generadores_e_Iteradores/02_iteracion_a_medida.md#ejercicio-97-cambios-de-precio-de-un-camión)

### Ejercicio 9.8: Configuremos un pipeline simple
Escribí la siguiente función y veamos como funciona un pipeline.

```python
>>> def filematch(lines, substr):
        for line in lines:
            if substr in line:
                yield line

>>>
```

Esta función es casi idéntica al primer ejemplo de generador en el ejercicio anterior, salvo que ya no abre un archivo sino que opera directamente de una secuencia de líneas que recibe como argumento. Ahora probá lo siguiente:

```python
>>> lines = vigilar('Data/stocklog.csv')
>>> naranjas = filematch(lines, 'Naranja')
>>> for line in naranjas:
        print(line)

... esperá que aparezca la salida ...
```

Puede pasar que tarde unos segundos en darte una salida, pero vas a ver información sobre narajas tan pronto como sean añadidas al archivo por el primer generador.

### Ejercicio 9.9: Un pipeline más en serio
Llevemos esta idea un poco más lejos. Probemos esto:

```python
>>> from vigilante import vigilar
>>> import csv
>>> lineas = vigilar('Data/mercadolog.csv')
>>> filas = csv.reader(lineas)
>>> for fila in filas:
        print(fila)

['BA', '98.35', '6/11/2007', '09:41.07', '0.16', '98.25', '98.35', '98.31', '158148']
['AA', '39.63', '6/11/2007', '09:41.07', '-0.03', '39.67', '39.63', '39.31', '270224']
['XOM', '82.45', '6/11/2007', '09:41.07', '-0.23', '82.68', '82.64', '82.41', '748062']
['PG', '62.95', '6/11/2007', '09:41.08', '-0.12', '62.80', '62.97', '62.61', '454327']
...
```

Interesante !  La salida de la función `vigilar()` fué usada como entrada a la función `csv.reader()` (que habíamos usado para leer un archivo del disco) y el resultado es una secuencia de filas "parseadas" en las comas. 

### Ejercicio 9.10: Un pipeline más largo
Veamos si podemos construír un pipeline más largo basado en la misma idea.
Comenzá creando una función que lea un archivo CSV como hiciste antes en `ticker.py` :

```python
# ticker.py

from vigilante import vigilar
import csv

def parsear_datos(lines):
    rows = csv.reader(lines)
    return rows

if __name__ == '__main__':
    lines = vigilar('Data/mercadolog.csv')
    rows = parsear_datos(lines)
    for row in rows:
        print(row)
```

Escribí una función nueva que elija algunas columnas específicas:

```python
# ticker.py
...
def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]
...
def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 4])
    return rows
```

Ejecútalo de nuevo, Sam. 
La salida ahora debería estar restringida a esto: 

```
['BA', '98.35', '0.16']
['AA', '39.63', '-0.03']
['XOM', '82.45','-0.23']
['PG', '62.95', '-0.12']
...
```

Escribí funciones generadoras que conviertan el tipo de datos a diccionarios:

```python
# ticker.py
...

def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))
...
def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows
...
```

Correlo de nuevo. Ahora la salida debería ser una serie de diccionarios:

```
{ 'name':'BA', 'price':98.35, 'change':0.16 }
{ 'name':'AA', 'price':39.63, 'change':-0.03 }
{ 'name':'XOM', 'price':82.45, 'change': -0.23 }
{ 'name':'PG', 'price':62.95, 'change':-0.12 }
...
```

### Ejercicio 9.11: Filtremos los datos
Para seguir agregando procesamiento a nuestro pipeline, escribí un filtro de datos:

```python
# ticker.py
...

def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row
```

Esto se usa para dejar pasar únicamente aquéllos cajones incluídos en el camión.

```python
import report
portfolio = report.read_portfolio('Data/portfolio.csv')
rows = parse_stock_data(follow('Data/stocklog.csv'))
rows = filter_symbols(rows, portfolio)
for row in rows:
    print(row)
```

### Ejercicio 9.12: El pipeline ensamblado
En el programa `ticker.py` escribí una función `ticker(portfile, logfile, fmt)` que cree un indicador en tiempo real para un camión, archivo log, y formato de tabla de salida particulares. Fijate:

```python
>>> from ticker import ticker
>>> ticker('Data/portfolio.csv', 'Data/stocklog.csv', 'txt')
      Name      Price     Change
---------- ---------- ----------
        GE      37.14      -0.18
      MSFT      29.96      -0.09
       CAT      78.03      -0.49
        AA      39.34      -0.32
...

>>> ticker('Data/portfolio.csv', 'Data/stocklog.csv', 'csv')
Name,Price,Change
IBM,102.79,-0.28
CAT,78.04,-0.48
AA,39.35,-0.31
CAT,78.05,-0.47
...
```

### Discusión

¿Qué aprendimos hoy? Si creás varias funciones generadoras y las ponés "en serie" (una recibe los datos de la anterior) podés crear pipelines que controlen el flujo de datos, los procesen modifiquen o filtren entre el primer generador y el ultimo consumidor. Por supuesto, podés empaquetar un conjunto de etapas de procesamiento en una función sola, si tiene sentido hacerlo.



[Contenidos](../Contenidos.md) \| [Anterior (2 Iteración a medida)](02_iteracion_a_medida.md) \| [Próximo (4 Más sobre generadores)](04_Mas_generadores.md)

