[Contenidos](../Contenidos.md) \| [Anterior (3 Listas y búsqueda lineal)](03_IteradoresLista.md) \| [Próximo (5 Objetos)](05_Objetos.md)

# 3.4 Comprensión de listas

Una tarea que realizamos una y otra vez es procesar los elementos de una lista. En esta sección introducimos la definición de listas por compresión que es una herramienta potente para hacer exactamente eso.

### Crear listas nuevas

La comprensión de listas crea un una nueva lista aplicando una operación a cada elemento de una secuencia.

```python
>>> a = [1, 2, 3, 4, 5]
>>> b = [2*x for x in a]
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

La sintaxis general es : `[<expresión> for <variable> in <secuencia>]`.

### Filtros

La comprensión de listas se puede usar para filtrar.

```python
>>> a = [1, -5, 4, 2, -2, 10]
>>> b = [2*x for x in a if x > 0]
>>> b
[2, 8, 4, 20]
>>>
```

### Casos de uso

La comprensión de listas es enormemente útil. Por ejemplo, podés recolectar los valores de un campo específico de un diccionario:

```python
frutas = [s['nombre'] for s in camion]
```

O podés hacer consultas (*queries*) como si las secuencias fueran bases de datos.

```python
a = [s for s in camion if s['precio'] > 100 and s['cajones'] > 50 ]
```

También podés combinar la comprensión de listas con reducciones de secuencias:

```python
costo = sum([s['cajones']*s['precio'] for s in camion])
```

### Sintaxis general

```code
[<expresión> for <variable> in <secuencia> if <condición>]
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

a = { x^2 | x ∈ s, x > 0 }        # Matemática
```

La mayoría de los programadores no suelen pensar en el costado matemático de esta herramienta. Podemos verla simplemente como una abreviación copada para definir listas.

## Ejercicios

Corré tu programa `informe.py` de forma de tener los datos sobre cajones cargados en tu intérprete en modo interactivo. 

Luego, tratá de escribir los comandos adecuados para realizar las operaciones descriptas abajo. Estas operaciones son reducciones, transformaciones y consultas sobre la carga del camión.

### Ejercicio 3.10: Comprensión de listas
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

### Ejercicio 3.11: Reducción de secuencias
Calculá el costo total de la carga del camión en un solo comando.

```python
>>> camion = leer_camion('Data/camion.csv')
>>> costo = sum([ s['cajones'] * s['precio'] for s in camion ])
>>> costo
47671.15
>>>
```

Luego, leyendo la variable `precios`, calculá también el valor en el mercado de la carga del camión usando una sola línea de código.

```python
>>> precios = leer_precios('Data/precios.csv')
>>> valor = sum([ s['cajones'] * precios[s['nombre']] for s in camion ])
>>> valor
62986.1
>>>
```

Ambos son ejemplos de aplicación-reducción. La comprensión de listas está aplicando una operación a lo largo de la lista. 

```python
>>> [ s['cajones'] * s['precio'] for s in camion ]
[3220.0000000000005, 4555.0, 15516.0, 10246.0, 3835.1499999999996, 3254.9999999999995, 7044.0]
>>>
```
La función `sum()` luego realiza una reducción del resultado

```python
>>> sum(_)
47671.15
>>>
```

Con este conocimiento algunos ya empiezan su startup de big-data.

### Ejercicio 3.12: Consultas de datos
Probá los siguientes ejemplos de consultas (queries) de datos.

Primero, generá una lista con la info de todas las frutas que tienen más de 100 cajones en el camión.

```python
>>> mas100 = [ s for s in camion if s['cajones'] > 100 ]
>>> mas100
[{'cajones': 150, 'nombre': 'Caqui', 'precio': 103.44},
 {'cajones': 200, 'nombre': 'Mandarina', 'precio': 51.23}]
>>>
```

Ahora, una con la info sobre cajones de Mandarina y Naranja.

```python
>>> myn = [ s for s in camion if s['nombre'] in {'Mandarina','Naranja'} ]
>>> myn
[{'cajones': 50, 'nombre': 'Naranja', 'precio': 91.1},
 {'cajones': 200, 'nombre': 'Mandarina', 'precio': 51.23},
 {'cajones': 50, 'nombre': 'Mandarina', 'precio': 65.1},
 {'cajones': 100, 'nombre': 'Naranja', 'precio': 70.44}]
>>>
```

O una con la info de las frutas que costaron más de $10000.

```python
>>> costo10k = [ s for s in camion if s['cajones'] * s['precio'] > 10000 ]
>>> costo10k
[{'cajones': 150, 'nombre': 'Caqui', 'precio': 103.44},
 {'cajones': 200, 'nombre': 'Mandarina', 'precio': 51.23}]
 >>>
```

Esta forma de escribir resulta análoga a las consultas a una base de datos con 
SQL.

### Ejercicio 3.13: Extracción de datos
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
{'Caqui', 'Durazno', 'Lima', 'Mandarina', 'Naranja'}
>>>
```

Si especificás pares `clave:valor`, podés construir un diccionario. Por ejemplo, si queremos un diccionario con el total de cada fruta en el camión podemos comenzar con

```python
>>> stock = { nombre: 0 for nombre in nombres }
>>> stock
{'Caqui': 0, 'Durazno': 0, 'Lima': 0, 'Mandarina': 0, 'Naranja': 0}
>>>
```
que es una comprensión de diccionario. Y seguir sumando los cajones:

```python
>>> for s in camion:
        stock[s['nombre']] += s['cajones']

>>> stock
{'Caqui': 150, 'Durazno': 95, 'Lima': 100, 'Mandarina': 250, 'Naranja': 150}
>>>
```

Otro ejemplo útil podría ser generar un diccionario de precios de venta de aquellos productos que están efectivamente cargados en el camión:

```python
>>> camion_precios = { nombre: precios[nombre] for nombre in nombres }
>>> camion_precios
{'Caqui': 105.46, 'Durazno': 73.48, 'Lima': 40.22, 'Mandarina': 80.89, 'Naranja': 106.28}
 >>>
```


### Ejercicio 3.14: Extraer datos de una arhcivo CSV
Saber usar combinaciones de comprensión de listas, diccionarios y conjuntos resulta útil para procesar datos en diferentes contextos. Aunque puede volverse medio críptico si no estás habituade. Acá te mostramos un ejemplo de cómo extraer columnas seleccionadas de un archivo CSV que tiene esas características. No es dificil cuando lo entendés, pero está muy concentrado todo.

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
>>> record = { ncolumna: row[index] for ncolumna, index in zip(select, indices) }   # comprensión de diccionario
>>> record
{'precio': '32.20', 'nombre': 'Lima', 'cajones': '100'}
>>>
```

No es trivial este comando. El comando es sintácticamente muy compacto, pero es conceptualmente (un poco) complejo. Cuando te sientas cómode con esta lectura de una línea del archivo (si no pasa, tranca, podemos seguir sin esto), leé el resto:

```python
>>> camion = [ { ncolumna: row[index] for ncolumna, index in zip(select, indices) } for row in rows ]
>>> camion
[{'cajones': '50', 'nombre': 'Naranja', 'precio': '91.1'},
 {'cajones': '150', 'nombre': 'Caqui', 'precio': '103.44'},
 {'cajones': '200', 'nombre': 'Mandarina', 'precio': '51.23'},
 {'cajones': '95', 'nombre': 'Durazno', 'precio': '40.37'},
 {'cajones': '50', 'nombre': 'Mandarina', 'precio': '65.1'},
 {'cajones': '100', 'nombre': 'Naranja', 'precio': '70.44'}]
>>>
```

¡Por las barbas de mi abuelo! Acabamos de reducir casi toda la función `leer_camion()` a un solo comando.

### Comentario

La comprensión de listas se usa frecuentemente Python. Es una forma eficiente de transformar, filtrar o juntar datos. Tiene una sintaxis potente pero tratá de no pasarte con su uso: mantené cada comando tan simple como sea posible. Está perfecto descomponer un solo comando complejo en muchos pasos. Concretamente: compartir el último ejemplo con personas desprevenidas puede no ser lo ideal.  

Dicho esto, saber manipular datos rápidamente es una habilidad increíblemente útil. Hay numerosas situaciones donde puede que tengas que resolver algún tipo de problema excepcional (en el sentido de raro o único) para importar, extraer o exportar datos. La comprensión de listas te puede ahorrar muchísimo tiempo en esas tareas.

[Contenidos](../Contenidos.md) \| [Anterior (3 Listas y búsqueda lineal)](03_IteradoresLista.md) \| [Próximo (5 Objetos)](05_Objetos.md)

