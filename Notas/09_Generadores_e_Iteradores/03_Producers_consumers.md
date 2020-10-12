[Contenidos](../Contenidos.md) \| [Anterior (2 Iteración a medida)](02_iteracion_a_medida.md) \| [Próximo (4 Más sobre generadores)](04_Mas_generadores.md)

# 9.3 Productores, consumidores y cañerías.

Los generadores son una herramienta muy útil para configurar pipelines (cañerías). Este concepto requiere una breve *aclaración*: Un pipeline tradicional en computación consta de una serie de programas y archivos asociados que constituyen una estructura de procesamiento de datos, donde cada programa se ejecuta independientemente de los demás, pero juntos resultan en un flujo conveniente de datos a través de los archivos asociados desde un "productor" (una cámara, un sensor, un lector de código de barras) hasta un "consumidor" (un graficador, un interruptor eléctrico, un log de una página web). Construiste un pequeño pipeline en la sección anterior, usando `vigilante.py`.  

En esta sección hablaremos de cómo implementar estas estructuras de productores y consumidores de datos con generadores en Python.

### Sistemas productor-consumidor

El concepto de generadores está íntimamente asociado a problemas de tipo productor-consumidor en sus varias formas. Fijate esta estructura, que es típica de muchos programas:

```python
# Productor
def vigilar(f):
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
>>> lines = vigilar('Data/mercadolog.csv')
>>> naranjas = filematch(lines, 'Naranja')
>>> for line in naranjas:
        print(line)

... esperá que aparezca la salida ...
```

Puede pasar que tarde unos segundos en darte una salida, pero vas a ver información sobre naranjas tan pronto como sean añadidas al archivo por el primer generador.

### Ejercicio 9.9: Un pipeline más en serio
Llevemos esta idea un poco más lejos. Probemos esto:

```python
>>> from vigilante import vigilar
>>> import csv
>>> lineas = vigilar('Data/mercadolog.csv')
>>> filas = csv.reader(lineas)
>>> for fila in filas:
        print(fila)

...   
['Rabanito', ' 249.37', ' 357']
['Batata', ' 15.75', ' 1040']
['Rabanito', ' 211.31', ' 324']
['Zuccini', ' 83.12', ' 612']
...
```

¡Interesante!  La salida de la función `vigilar()` fué usada como entrada a la función `csv.reader()` (que habíamos usado para leer un archivo del disco) y el resultado es una secuencia de filas "parseadas", separadas por las comas. 

### Ejercicio 9.10: Un pipeline más largo
Veamos si podemos construír un pipeline más largo basado en la misma idea.

Creá un archivo nuevo llamado `ticker.py`, te lo vamos a pedir al final de la clase.
Comenzá creando una función que lea un archivo CSV como hiciste antes:

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
    rows = elegir_columnas(rows, [0, 2])
    return rows
```

Ejecútalo de nuevo, Sam. 
La salida ahora debería estar restringida a esto: 

```
['Brócoli', ' 388']
['Ajo', ' 120']
['Caqui', ' 108']
['Mandarina', ' 1170']
...
```

Escribí funciones generadoras que conviertan el tipo de datos a diccionarios:

```python
# ticker.py
...

def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, float])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows
...
```

Correlo de nuevo. Ahora la salida debería ser una serie de diccionarios:

```
{'nombre': 'Frutilla', 'precio': 276.81, 'volumen': 249.0}
{'nombre': 'Morrón', 'precio': 2988.42, 'volumen': 702.0}
{'nombre': 'Morrón', 'precio': 3108.63, 'volumen': 498.0}
{'nombre': 'Naranja', 'precio': 11.5, 'volumen': 870.0}
...
```

### Ejercicio 9.11: Filtremos los datos
Para seguir agregando procesamiento a nuestro pipeline, escribí un filtro de datos:

```python
# ticker.py
...

def filtrar_datos(filas, nombres):
    for fila in filas:
        if fila['nombre'] in nombres:
            yield fila
```

Esto se usa para dejar pasar únicamente aquéllos lotes incluídos en el camión. Probalo.

```python

import informe
camion = informe.leer_camion('Data/camion.csv')
filas = parsear_datos(vigilar('Data/mercadolog.csv'))
filas = filtrar_datos (filas, camion)
for fila in filas:
    print(fila)

```

### Ejercicio 9.12: El pipeline ensamblado
En el programa `ticker.py` (esta versión te vamos a pedir que la entregues) escribí una función `ticker(camion_file, log_file, fmt)` que cree un indicador en tiempo real para un camión, archivo log, y formato de tabla de salida particulares. Fijate:

```python
>>> from ticker import ticker
>>> ticker('Data/camion.csv', 'Data/mercadolog.csv', 'txt')
    Nombre     Precio    Volumen
---------- ---------- ----------
     Caqui     796.73         96
 Mandarina      12.12       1120
      Lima    2659.37        222
   Naranja      11.70       1040
   Durazno     281.76        704        
...

>>> ticker('Data/camion.csv', 'Data/mercadolog.csv', 'csv')
Nombre,Precio,Volumen
Mandarina,14.19,1140
Naranja,9.37,1150
Durazno,280.56,872
Lima,2624.94,232

...
```

### Discusión

¿Qué aprendimos hoy? Si creás varias funciones generadoras y las ponés "en serie" (una recibe los datos de la anterior) podés crear pipelines que controlen el flujo de datos: los procesen, modifiquen o filtren entre el primer generador y el último consumidor. Además viste lo fácil que es cambiar el comportamiento del programa cuando tenés interfases bien definidas. Por supuesto, podés empaquetar un conjunto de etapas de procesamiento en una función sola, si tiene sentido hacerlo.



[Contenidos](../Contenidos.md) \| [Anterior (2 Iteración a medida)](02_iteracion_a_medida.md) \| [Próximo (4 Más sobre generadores)](04_Mas_generadores.md)

