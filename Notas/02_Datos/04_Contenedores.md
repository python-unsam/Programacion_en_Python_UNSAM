[Contenidos](../Contenidos.md) \| [Anterior (3 Tipos y estructuras de datos)](03_TiposDatos.md) \| [Próximo (5 Secuencias)](05_Secuencias.md)

# 2.4 Contenedores

En esta sección trataremos listas, diccionarios y conjuntos.

### Panorama

Los programas suelen trabajar con muchos objetos.

* Un camión con cajones de fruta
* Una tabla de precios de cajones de fruta

En Python hay tres opciones principales para elegir.

* Listas. Datos ordenados.
* Diccionarios. Datos desordenados.
* Conjuntos. Colección desordenada de elementos únicos.

### Listas como contenedores

Usá listas cuando el orden de los datos importe. Acordate de que las listas pueden contener cualquier tipo de objeto.
Por ejemplo, una lista de tuplas.

```python
camion = [
    ('Pera', 100, 490.1),
    ('Naranja', 50, 91.3),
    ('Limon', 150, 83.44)
]

camion[0]            # ('Pera', 100, 490.1)
camion[2]            # ('Limon', 150, 83.44)
```

#### Construcción de una lista

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

Nota: Si probás estos comandos en el archivo `Data/precios.csv`, vas a ver que casi anda. Pero hay una línea en blanco al final que genera un error. Usando lo que ya vimos, en el [Ejercicio 2.14](../02_Datos/04_Contenedores.md#ejercicio-214-diccionarios-como-contenedores) vas a tener que modificar el código para resolver el problema.

### Búsquedas en un diccionario

Podés verificar si una clave existe:

```python
if key in d:
    # YES
else:
    # NO
```

### Claves compuestas

Casi cualquier valor puede usarse como clave en un diccionario de Python. La principal restricción es que una clave debe ser de tipo inmutable.
Por ejemplo, tuplas:

```python
feriados = {
  (1, 1) : 'Año nuevo',
  (1, 5) : 'Día del trabajador',
  (13, 9) : "Día del programador",
}
```

Luego, podemos acceder al diccionario así:

```python
>>> feriados[(1, 5)]
'Día del trabajador'
>>>
```

*Las listas, los conjuntos y los diccionarios no pueden ser usados como claves de diccionarios, porque son mutables.*

### Conjuntos

Un conjunto es una colección de elementos únicos sin orden y sin repetición.


```python
citricos = { 'Naranja','Limon','Mandarina' }
# Alternativamente podemos escribirlo así:
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

unicos = set(nombres)
# unicos = set(['Naranja', 'Manzana', 'Pera', 'Naranja', 'Pera', 'Banana'])
```

Más operaciones en conjuntos:

```python
citricos.add('Banana')        # Agregar un elemento
citricos.remove('Limon')    # Eliminar un elemento

s1 | s2                 # Unión de conjuntos s1 y s2
s1 & s2                 # Intersección de conjuntos
s1 - s2                 # Diferencia de conjuntos
```

## Ejercicios

En estos ejercicios, vas a empezar a construir un programa más largo. Trabajá en el archivo `ejercicios_python/informe.py`.

### Ejercicio 2.12: Lista de tuplas
El archivo `Data/camion.csv` contiene la lista de cajones cargados en un camión.  En el [Ejercicio 2.5](../02_Datos/02_Funciones.md#ejercicio-25-transformar-un-script-en-una-función) de la sección anterior escribiste una función `costo_camion(nombre_archivo)` que leía el archivo y realizaba un cálculo.

La función debería verse parecida a ésta:

```python
# fragmento de costo_camion.py
import csv
...

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

...
```

Usando este código como guía, creá un nuevo archivo `informe.py`. En este archivo, definí una función `leer_camion(nombre_archivo)` que abre un archivo con el contenido de un camión, lo lee y devuelve la información como una lista de tuplas. Para hacerlo vas a tener que hacer algunas modificaciones menores al código de arriba.

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

Experimentá con tu función interactivamente (acordate de que primero tenés que correr el programa `informe.py` en el intérprete):

*Ayuda: Usá `-i` para ejecutar un archivo en la terminal y quedar en el intérprete*

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
47671.15
>>>
```

Esta lista de tuplas que creaste es muy similar a un array o matriz bidimensional. Por ejemplo, podés acceder a una fila específica y columna específica usando una búsqueda como `camion[fila][columna]` donde `fila` y `columna` son números enteros.

También podés reescribir el último ciclo for usando un comando como éste:

```python
>>> total = 0.0
>>> for nombre, cajones, precio in camion:
            total += cajones*precio

>>> print(total)
47671.15
>>>
```

*Observación: la instrucción `+=` es una abreviación. Poner `a += b` es equivalente a poner `a = a + b`*

### Ejercicio 2.13: Lista de diccionarios
Tomá la función que escribiste en el ejercicio anterior y modificala para representar cada cajón del camión con un diccionario en vez de una tupla. En este diccionario usá los campos "nombre", "cajones" y "precio" para representar las diferentes columnas del archivo de entrada.

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
47671.15
>>>
```

Fijate que acá los distintos campos para cada entrada se acceden a través de claves en vez de la posición en la lista. Muchas veces preferimos esto porque el código resulta más fácil de leer. Tanto para otres como para nosotres en el futuro.

Mirar diccionarios y listas muy grandes puede ser un lío. Para limpiar el output para debuguear, probá la función `pprint` (Pretty-print) que le da un formato más sencillo de interpretar.

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
Los diccionarios son útiles si querés buscar elementos usando índices que no sean números enteros. En la terminal de Python, jugá con un diccionario:

```python
>>> precios = {}
>>> precios['Naranja'] = 92.45
>>> precios['Mandarina'] = 45.12
>>> precios
... mirá el resultado ...
>>> precios['Naranja']
92.45
>>> precios['Manzana']
... mirá el resultado ...
>>> 'Manzana' in precios
False
>>>
```

El archivo `Data/precios.csv` contiene una serie de líneas con precios de venta de cajones en el mercado al que va el camión. El archivo se ve así:

```csv
"Lima",9.22
"Uva",24.85
"Ciruela",44.85
"Cereza",11.27
"Frutilla",3.72
...
```

Escribí una función `leer_precios(nombre_archivo)` que a partir de un conjunto de precios como éste arme un diccionario donde las claves sean los nombres de frutas y verduras, y los valores sean los precios por cajón.

Para hacerlo, empezá con un diccionario vacío y andá agregándole valores igual que como hiciste antes, pero ahora esos valores los vas leyendo del archivo.

Vamos a usar esta estructura de datos para buscar rápidamente los precios de las frutas y verduras.

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

Puede suceder que esto haga que tu programa termine con una excepción. Usá los comandos `try` y `except` para evitar el problema.
Para pensar: ¿Sería mejor prevenir estos problemas con el comando `if` en vez de `try` y `except`?

Una vez que hayas escrito tu función `leer_precios()`, testeala interactivamente para asegurarte de que funciona bien:

```python
>>> precios = leer_precios('Data/precios.csv')
>>> precios['Naranja']
106.28
>>> precios['Mandarina']
80.89
>>>
```

### Ejercicio 2.15: Balances
Supongamos que los precios en `camion.csv` son los precios pagados al productor de frutas mientras que los precios en `precios.csv` son los precios de venta en el lugar de descarga del camión.

Ahora vamos calcular el balance del negocio: juntá todo el trabajo que hiciste recién en tu programa `informe.py` (usando las funciones `leer_camion()` y `leer_precios()`) y completa el programa para que con los precios del camión ([Ejercicio 2.13](../02_Datos/04_Contenedores.md#ejercicio-213-lista-de-diccionarios)) y los de venta en el negocio ([Ejercicio 2.14](../02_Datos/04_Contenedores.md#ejercicio-214-diccionarios-como-contenedores)) calcule lo que costó el camión, lo que se recaudo con la venta, y la diferencia. ¿Hubo ganancia o pérdida? El programa debe imprimir por pantalla un balance con estos datos.


[Contenidos](../Contenidos.md) \| [Anterior (3 Tipos y estructuras de datos)](03_TiposDatos.md) \| [Próximo (5 Secuencias)](05_Secuencias.md)

