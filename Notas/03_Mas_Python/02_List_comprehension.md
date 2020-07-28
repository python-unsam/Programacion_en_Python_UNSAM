[Contenidos](../Contenidos.md) \| [Anterior (1 El módulo collections)](01_Collections.md) \| [Próximo (3 Objects)](03_Objects.md)

# 3.2 Comprensión de listas

Una tarea que realizamos una y otra vez es procesar los elementos de una lista. En esta sección introducimos la definición de listas por compresión que es una herramienta potente para hacer exactamente eso.

### Crear listas nuevas

La comprensión de listas crea un una nueva lista aplicando una operación a cada elemento de una secuencia.

```python
>>> a = [1, 2, 3, 4, 5]
>>> b = [2*x for x in a ]
>>> b
[2, 4, 6, 8, 10]
>>>
```

Otro ejemplo:

```python
>>> nombres = ['Edmundo', 'Juana']
>>> a = [nombre.lower() for nombre in nombres]
>>> a
['edmundo', 'juana']
>>>
```

La sintaxis general es : `[ <expresión> for <variable> in <secuencia> ]`.

### Filtros

La comprensión de listas se puede usar para filtrar.

```python
>>> a = [1, -5, 4, 2, -2, 10]
>>> b = [2*x for x in a if x > 0 ]
>>> b
[2, 8, 4, 20]
>>>
```

### Casos de uso

La comprensión de listas es enormemente útil. Por ejemplo, podés recolectar los valores de un campo específico de un diccionario:

```python
frutas = [s['nombre'] for s in cajones]
```

O podés hacer consultas (queries) como si las secuencias fueran bases de datos.

```python
a = [s for s in cajones if s['precio'] > 100 and s['cajones'] > 50 ]
```

También podés combinar la comprensión de listas con reducciones de secuencias:

```python
costo = sum([s['cajones']*s['precio'] for s in cajones])
```

### Sintaxis general

```code
[ <expresión> for <variable> in <secuencia> if <condición>]
```

Lo que significa

```python
resultado = []
for variable in secuencia:
    if condición:
        resultado.append(expresión)
```

### Digresión histórica

La comprensión de listas viene de la matemática (definición de conjuntos por comprensión).

```code
a = [ x * x for x in s if x > 0 ] # Python

a = { x^2 | x ∈ s, x > 0 }         # Math
```

La mayoría de los programadores no suelen pensar en el costado matemático de esta herramienta. Podemos verla simplemente como una abreviación copada para definir listas.

## Ejercicios

Corré  tu programa `informe.py` de forma de tener los datos sobre cajones cargados en tu intérprete en modo interactivo. 

Luego, tratá de escribir los comandos adecuados para realizar las operaciones descriptas abajo. Estas operaciones son reducciones, transformaciones y consultas sobre la carga del camión.

### Ejercicio 3.2: Comprensión de listas
Probá un par de comprensión de listas para familiarizarte con la sintaxis.

```python
>>> nums = [1,2,3,4]
>>> cuadrados = [ x * x for x in nums ]
>>> cuadrados
[1, 4, 9, 16]
>>> dobles = [ 2 * x for x in nums if x > 2 ]
>>> dobles
[6, 8]
>>>
```

Observá que estás creando nuevas listas con los datos adecuadamente transformados o filtrados.

### Ejercicio 3.3: Reducción de secuencias
Calculá el costo total de la carga del camión en un solo comando.

```python
>>> camion = leer_camion('Data/camion.csv')
>>> cost = sum([ s['cajones'] * s['precio'] for s in camion ])
>>> cost
44671.15
>>>
```

Luego, usando la variable `precios` calculá también el valor en el mercado de la carga del camión usando una sola línea de código.

```python
>>> value = sum([ s['cajones'] * precios[s['nombre']] for s in camion ])
>>> value
28686.1
>>>
```

Ambos son ejemplos de aplicación-reducción. La comprensión de listas está aplicando una operación a lo largo de la lista. 

```python
>>> [ s['cajones'] * s['precio'] for s in camion ]
[3220.0000000000005, 4555.0, 12516.0, 10246.0, 3835.1499999999996, 3254.9999999999995, 7044.0]
>>>
```

La función `sum()` luego realiza una reducción del resultaqdo

```python
>>> sum(_)
44671.15
>>>
```

Con este conocimiento algunos ya empiezan su startup de big-data.

### Ejercicio 3.4: Consultas de datos
Probá los siguientes ejemplos de consultas (queries) de datos.

Primero, generá una lista con la info de todas las frutas que tienen más de 100 cajones en el camión.

```python
>>> mas100 = [ s for s in camion if s['cajones'] > 100 ]
>>> mas100
[{'precio': 83.44, 'nombre': 'Caqui', 'cajones': 150}, {'precio': 51.23, 'nombre': 'Mandarina', 'cajones': 200}]
>>>
```

Ahora, una con la info sobre cajones de Mandarina y Naranja.

```python
>>> myn = [ s for s in camion if s['nombre'] in {'Mandarina','Naranja'} ]
>>> myn
[{'precio': 91.1, 'nombre': 'Naranja', 'cajones': 50}, {'precio': 51.23, 'nombre': 'Mandarina', 'cajones': 200},
  {'precio': 65.1, 'nombre': 'Mandarina', 'cajones': 50}, {'precio': 70.44, 'nombre': 'Naranja', 'cajones': 100}]
>>>
```

O una con la info de las frutas que costaron más de $10000.

```python
>>> cost10k = [ s for s in camion if s['cajones'] * s['precio'] > 10000 ]
>>> cost10k
[{'precio': 83.44, 'nombre': 'Caqui', 'cajones': 150}, {'precio': 51.23, 'nombre': 'Mandarina', 'cajones': 200}]
>>>
```

Esta forma de escribir resulta análoga a las consultas a una base de datos con 
SQL.

### Ejercicio 3.5: Extracción de datos
Usando un comprensión de listas, construí una lista de tuplas `(nombre, cajones)` que indiquen la cantidad de cajones de cada fruta tomando los datos de `camion`.

```python
>>> nombre_cajones =[ (s['nombre'], s['cajones']) for s in camion ]
>>> nombre_cajones
[('Lima', 100), ('Naranja', 50), ('Caqui', 150), ('Mandarina', 200), ('Durazno', 95), ('Mandarina', 50), ('Naranja', 100)]
>>>
```

Si cambiás los corchetes  (`[`,`]`) por llaves (`{`, `}`), obtenés algo que se conoce como comprensión de conjuntos. Vas a obtener valores únicos.

Por ejemplo, si quisieras un listado de las frutas en el camión pordías usar:

```python
>>> nombres = { s['nombre'] for s in camion }
>>> nombres
{ 'Lima', 'Durazno', 'Naranja', 'Mandarina', 'Caqui'] }
>>>
```

Si especificas pares `clave:valor`, podés construir un diccionario. Por ejemplo, si queremos un diccionario con el total de cada fruta en el camión podemos comenzar con

```python
>>> holdings = { nombre: 0 for nombre in nombres }
>>> holdings
{'Lima': 0, 'Durazno': 0, 'Naranja': 0, 'Mandarina': 0, 'Caqui': 0}
>>>
```
que es una comprensión de diccionario. Y seguir sumando los cajones:

```python
>>> for s in camion:
        holdings[s['nombre']] += s['cajones']

>>> holdings
{ 'Lima': 100, 'Durazno': 95, 'Naranja': 150, 'Mandarina':250, 'Caqui': 150 }
>>>
```

Otro ejemplo útil podría ser generar un diccionario de precios de venta de aquellos productos que están efectivamente cargados en el camión:

```python
>>> camion_precios = { nombre: precios[nombre] for nombre in nombres }
>>> camion_precios
{'Lima': 9.22, 'Durazno': 13.48, 'Naranja': 106.28, 'Mandarina': 20.89, 'Caqui': 35.46}
>>>
```

### Ejercicio 3.6: Estraer datos de una arhcivo CSVFiles
Saber usar combinaciones de comprensión de listas diccionarios y conjuntos resulta útil para procesar datos en diferentes contextos. Aunque puede volverse medio críptico si no estás habituade. 
Aquí te mostramos una ejemplo de cómo extraer columnas seleccionadas de un archivo CSV que tiene esas características. No es dificil cuando lo entendés, pero está muy concentrado todo.

Primero, leamos el encabezado (header) del archivo CSV:

```python
>>> import csv
>>> f = open('Data/fecha_camion.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> headers
['nombre', 'fecha', 'hora', 'cajones', 'precio']
>>>
```

Luego, definamos una lista que tenga las columnas que nos importan:

```python
>>> select = ['nombre', 'cajones', 'precio']
>>>
```

Ubiquemos los índices de esas columnas en el CSV:

```python
>>> indices = [ headers.index(ncolumna) for ncolumna in select ]
>>> indices
[0, 3, 4]
>>>
```

Y finalmente leamos los datos y armemos un diccionario usando comprensión de diccionarios:

```python
>>> row = next(rows)
>>> record = { ncolumna: row[index] for ncolumna, index in zip(select, indices) }   # dict-comprehension
>>> record
{'precio': '32.20', 'nombre': 'Lima', 'cajones': '100'}
>>>
```

No es trivial este comando. El comando es sintáctricamente muy compacto, pero se conceptualmente (un poco) complejo. Cuando te sientas cómode con esta lectura de una linea del archivo (si no pasa, tranca, podemos seguir sin esto), leé el resto:

```python
>>> camion = [ { ncolumna: row[index] for ncolumna, index in zip(select, indices) } for row in rows ]
>>> camion
[{'precio': '91.10', 'nombre': 'Naranja', 'cajones': '50'}, {'precio': '83.44', 'nombre': 'Caqui', 'cajones': '150'},
  {'precio': '51.23', 'nombre': 'Mandarina', 'cajones': '200'}, {'precio': '40.37', 'nombre': 'Durazno', 'cajones': '95'},
  {'precio': '65.10', 'nombre': 'Mandarina', 'cajones': '50'}, {'precio': '70.44', 'nombre': 'Naranja', 'cajones': '100'}]
>>>
```

¡Por las barbas de mi abuelo! Acabamos de reducir casi toda la función `leer_camion()` a un solo comando.

### Comentario

La comprensión de listas es comunmente usuada en Python como una forma eficiente de transformar, filtrar o recolectar datos. Debido a su sintaxis poderosa, tratá de no pasarte con su uso: mantené cada comando tan simple como sea posible. Está perfecto descomponer algo complejo en múltiples pasos. Por ejemplo, no es claro que quieras compartir el último ejemplo con otras personas desprevenidas.  

Dicho esto, saber manipular datos rápidamente es una habilidad increíblemente útil. Hay numerosas situaciones donde puede que tengas que resolver algún tipo de problema excepcional para importar, extraer o exportar datos. La comprensión de listas te puede ahorrar muchísimo tiempo en esas tareas. Y no te olvides del módulo `collections` que también puede serte útil en este contexto.

[Contenidos](../Contenidos.md) \| [Anterior (1 El módulo collections)](01_Collections.md) \| [Próximo (3 Objects)](03_Objects.md)

