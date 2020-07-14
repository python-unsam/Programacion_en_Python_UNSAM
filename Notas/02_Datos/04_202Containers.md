[Contenidos](../Contenidos.md) \| [Anterior (3 Tipos y estructuras de datos)](03_201Datatypes.md) \| [Próximo (5 Formatting)](05_203Formatting.md)

# 2.4 Contenedores

En esta sección trataremos listas, diccionarios y conjuntos.

### Panorama

Los programas suelen trabajar con muchos objetos.

* Un camión con cajones de fruta
* Una tabla de precios de cajones de fruta

En Python hay tres opciones principales para elegir.

* Listas. Datos ordenados.
* Diccionarios. Datos desordenados.
* Conjuntos. Colección desordenada de elemenos únicos.

### Listas como contenedores

Usá listas cuando el orden de los datos importe. Acordate que las listas pueden contener cualquier tipo de objeto.
Por ejemplo, una lista de tuplas

```python
camion = [
    ('Pera', 100, 490.1),
    ('Naranja', 50, 91.3),
    ('Limon', 150, 83.44)
]

camion[0]            # ('Pera', 100, 490.1)
camion[2]            # ('Limon', 150, 83.44)
```

### Construcción de una lista

Cómo armar una lista desde cero.

```python
registros = []  # Empezamos con una lista vacía

# Usamos el .append() para agregar elementos
registros.append(('Pera', 100, 490.10))
registros.append(('Naranja', 50, 91.3))
...
```

Un ejemplo de cómo cargar registros desde un archivo.

```python
registros = []  # Empezamos con una lista vacía

with open('Data/camion.csv', 'rt') as f:
    next(f) # Saltear el encabezado
    for line in f:
        row = line.split(',')
        registros.append((row[0], int(row[1]), float(row[2])))
```

### Diccionarios como contenedores

Los diccionarios son útiles si vamos a querer buscar rápidamente (por claves).
Por ejemplo, un diccionario de precios de cajones.

```python
precios = {
   'Pera': 513.25,
   'Limon': 87.22,
   'Naranja': 93.37,
   'Mandarina': 44.12
}
```

Así podemos buscar datos:

```python
>>> precios['Naranja']
93.37
>>> precios['Pera']
513.25
>>>
```

### Construcción de diccionarios

Ejemplo de armado de un diccionario desde cero.

```python
precios = {} # Empezamos con un diccionario vacío

# Agregamos elementos
precios['Pera'] = 513.25
precios['Limon'] = 87.22
precios['Naranja'] = 93.37
```

Un ejemplo de cómo armar un diccionario a partir del contenido de un archivo.

```python
precios = {}  # Empezamos con un diccionario vacío

with open('Data/precios.csv', 'rt') as f:
    for line in f:
        row = line.split(',')
        precios[row[0]] = float(row[1])
```

Nota: Si probás estos comandos en el archivo `Data/precios.csv`, vas a ver que casi anda. Pero hay una línea en blanco al final que genera un error. Vas a tener que encontrar la manera de modificar el código para resolverlo (ver Ejercicio 2.6).

### Búsquedas en un diccionario

Podés chequear si una clave existe:

```python
if key in d:
    # YES
else:
    # NO
```

Podés buscar un valor que quizás no figure en el diccionario, y dar un valor predeterminado para estos casos.

```python
nombre = d.get(key, default)
```

Un ejemplo:

```python
>>> precios.get('Naranja', 0.0)
93.37
>>> precios.get('Guayaba', 0.0)
0.0
>>>
```

### Claves compuestas

Casi cualquier valor puede usarse como clave en un diccionario de Python. Una clave debe ser de tipo inmutbale.
Por ejemplo, tuplas:

```python
feriados = {
  (1, 1) : 'Año nuevo',
  (5, 1) : 'Día del trabajador',
  (9, 13) : "Día del programador",
}
```

Luego, podemos acceder al diccionario así:

```python
>>> feriados[5, 1]
'Día del trabajador'
>>>
```

*Las listas, los conjuntos y los diccionarios no pueden ser usados como claves de diccionarios, porque son mutables.*

### Conjuntos

Un conjunto es una colección desordenada de elementos únicos.


```python
citricos = { 'Naranja','Limon','Mandarina' }
# Alternativamente podemos escribirlo así
citricos = set(['Naranja', 'Limon', 'Mandarina'])
```

Los conjuntos son útiles para evaluar pertenencia.

```python
>>> citricos
set(['Naranja', 'Limon', 'Mandarina'])
>>> 'Naranja' in citricos
True
>>> 'Manzana' in citricos
False
>>>
```

Los conjuntos también son útiles para eliminar duplicados.

```python
nombres = ['Naranja', 'Manzana', 'Pera', 'Naranja', 'Pera', 'Banana']

unique = set(nombres)
# unique = set(['Naranja', 'Manzana','Pera','Banana'])
```

Más operaciones en conjuntos:

```python
nombres.add('Limon')        # Agregar un elemento
nombres.remove('Banana')    # Eliminar un elemento

s1 | s2                 # Unión de conjuntos
s1 & s2                 # Intersección de conjuntos
s1 - s2                 # Diferencia de conjuntos
```

## Ejercicios

En estos ejercicios, vas a empezar a construir uno de los programas más grandes que usaremos en el resto del curso. Trabajá en un archivo `Work/reporte.py`.

### Ejercicio 2.12: Lista de tuplas

El archivo `Data/camion.csv` contiene una lista de cajones de un camión.  En el [Ejercicio 2.5](../02_Datos/02_107Funciones.md#ejercicio-25-transformar-un-script-en-una-función) de una sección anterior escribiste una función `costo_camion(nombre_archivo)` que leía el archivo y realizaba un cálculo.

Tu código debería verse parecido a éste:

```python
# pcamion.py

import csv

def costo_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones*precio) de un archivo'''
    total = 0.0

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            ncajones = int(row[1])
            precio = float(row[2])
            total += ncajones * precio
    return total
```

Usando este código como guía, creá un nuevo archivo `reporte.py`.  En este archivo, definí una función `leer_camion(nombre_archivo)` que abre un archivo con el contenido de un camión, lo lee y pasa la información a una lista de tuplas. Para hacerlo vas a tener que hacer algunas modificaciones menores al código de arriba.

Primero, en vez de definir `total = 0`, tenés que empezar con una variable que empieza siendo una lista vacía Por ejemplo:

```python
camion = []
```

Después, en vez de sumar el costo, tenés que pasar cada fila a una tupla igual a como lo hiciste en el último ejercicio, y agregarla a la lista. Por ejemplo:

```python
for row in rows:
    lote = (row[0], int(row[1]), float(row[2]))
    camion.append(lote)
```

Por último, la función debe devolver la lista `camion`.

Experimentá con tu función interactivamente (acordate de que primero tenés que correr el programa `reportepy` en el intérprete):

*Ayuda: Usá `-i` para ejecutar un archivo en la terminal*

```python
>>> camion = leer_camion('Data/camion.csv')
>>> camion
[('Lima', 100, 32.2), ('Naranja', 50, 91.1), ('Limon', 150, 83.44), ('Mandarina', 200, 51.23),('Durazno', 95, 40.37), ('Mandarina', 50, 65.1), ('Naranja', 100, 70.44)]
>>>
>>> camion[0]
('Lima', 100, 32.2)
>>> camion[1]
('Naranja', 50, 91.1)
>>> camion[1][1]
50
>>> total = 0.0
>>> for s in camion:
        total += s[1] * s[2]

>>> print(total)
44671.15
>>>
```

Esta lista de tuplas que creaste es muy similar a un array o matriz 2-D. Por ejemplo, podés acceder a una fila específica y columna específica usando una búsqueda como `camion[fila][columna]` donde `fila` y `columna` son números enteros.

También podés reescribir el último ciclo for usando un comando como éste:

```python
>>> total = 0.0
>>> for nombre, cajones, precio in camion:
            total += cajones*precio

>>> print(total)
44671.15
>>>
```

### Ejercicio 2.13: Lista de diccionarios

Tomá la función que escribiste en el ejercicio *Lista de tuplas* y modificala para representar cada cajón del camión con un diccionario en vez de una tupla. En este diccionario usá los campos "nombre", "cajones" y "precio" para representar las diferentes columnas del achivo input.

Experimentá con esta función nueva igual que en el ejercicio anterior.

```python
>>> camion = leer_camion('Data/camion.csv')
>>> camion
[{'nombre': 'Lima', 'cajones': 100, 'precio': 32.2}, {'nombre': 'Naranja', 'cajones': 50, 'precio': 91.1}, {'nombre': 'Limon', 'cajones': 150, 'precio': 83.44}, {'nombre': 'Mandarina', 'cajones': 200, 'precio': 51.23}, {'nombre': 'Durazno', 'cajones': 95, 'precio': 40.37}, {'nombre': 'Mandarina', 'cajones': 50, 'precio': 65.1}, {'nombre': 'Naranja', 'cajones': 100, 'precio': 70.44}]
>>> camion[0]
{'nombre': 'Lima', 'cajones': 100, 'precio': 32.2}
>>> camion[1]
{'nombre': 'Naranja', 'cajones': 50, 'precio': 91.1}
>>> camion[1]['cajones']
50
>>> total = 0.0
>>> for s in camion:
        total += s['cajones']*s['precio']

>>> print(total)
44671.15
>>>
```

Fijate que acá los distintos campos para cada entrada se acceden a través de claves en vez de números de fila y columna. Muchas veces preferimos esto porque el código resulta más fácil de leer en el futuro.

Mirando diccionarios y listas muy grandes puede ser un lío. Para limpiar el output para debugging, considerá la función `pprint`.

```python
>>> from pprint import pprint
>>> pprint(camion)
[{'nombre': 'Lima', 'precio': 32.2, 'cajones': 100},
    {'nombre': 'Naranja', 'precio': 91.1, 'cajones': 50},
    {'nombre': 'Limon', 'precio': 83.44, 'cajones': 150},
    {'nombre': 'Mandarina', 'precio': 51.23, 'cajones': 200},
    {'nombre': 'Durazno', 'precio': 40.37, 'cajones': 95},
    {'nombre': 'Mandarina', 'precio': 65.1, 'cajones': 50},
    {'nombre': 'Naranja', 'precio': 70.44, 'cajones': 100}]
>>>
```

### Ejercicio 2.14: Diccionarios como contenedores

Los diccionarios son útiles si querés buscar elementos usando índices que no sean números enteros. En la terminal de Python, juygá con un diccionario:

```python
>>> precios = { }
>>> precios['Naranja'] = 92.45
>>> precios['Mandarina'] = 45.12
>>> precios
... look at the result ...
>>> precios['Naranja']
92.45
>>> precios['Manzana']
... look at the result ...
>>> 'Manzana' in precios
False
>>>
```

El archivo `Data/precios.csv` contiene una serie de líneas con precios de cajones.
El archivo se ve así:

```csv
"Lima",9.22
"Uva",24.85
"Ciruela",44.85
"Cereza",11.27
"Frutilla",3.72
...
```

Escribí una función `leer_precios(nombre_archivo)` que a partir de un conjunto de precios como éste arme un diccionario donde las claves sean los nombres de frutas y los valores sean los precios por cajón.

Para hacerlo, empezá con un diccionario vacío y agregale valores igual que hiciste antes, pero ahora leyendo los valores del archivo.

Vamos a usar esta estructura de datos para buscar rápidamente los precios de las frutas.

Un par de consejos:
Usá el módulo `csv` igual que antes.

```python
>>> import csv
>>> f = open('Data/precios.csv', 'r')
>>> rows = csv.reader(f)
>>> for row in rows:
        print(row)


['Lima', '9.22']
['Uva', '24.85']
...
[]
>>>
```

El archivo `Data/precios.csv` puede tener líneas en blanco, esto te puede traer complicaciones.
Observá que arriba figura una lista vacía (la última), porque la última línea del archivo no tenía datos.

Puede suceder que esto haga que tu programa termine con una excepción. Usá los comandos `try` y `except` comandos para evitar el problema.
Para pensar: ¿Sería mejor prevenir estos problemas con el comando `if` en vez de `try` y `except`?

Una vezq ue hayas escrito tu función `leer_precios()`, testeala interactivamente para asegurarte de que funciona bien:

```python
>>> precios = leer_precios('Data/precios.csv')
>>> precios['Naranja']
106.28
>>> precios['Mandarina']
20.89
>>>
```

### Ejercicio 2.15: Determinando si te podés jubilar

Juntá todo este trabajo agregando algunos comandos adicionales a tu programa `reporte.py` que calcula ganancias y pérdidas. Estos comandos deberían tomar la lisa de cajones del ejercicio *Lista de diccionarios* y el diccionario de precios del ejercicio *Diccionarios como contenedores*, y calcular el valor actual del camión y la ganancia o pérdida.


[Contenidos](../Contenidos.md) \| [Anterior (3 Tipos y estructuras de datos)](03_201Datatypes.md) \| [Próximo (5 Formatting)](05_203Formatting.md)

