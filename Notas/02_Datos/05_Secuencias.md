[Contenidos](../Contenidos.md) \| [Anterior (4 Contenedores)](04_Contenedores.md) \| [Próximo (6 Contadores del módulo _collections_)](06_Contadores.md)

# 2.5 Secuencias

### Tipo de secuencias

Python tiene tres tipos de datos que son *secuencias*.

* String: `'Hello'`. Una cadena es una secuencia de caracteres.
* Lista: `[1, 4, 5]`.
* Tupla: `('Pera', 100, 490.1)`.

Todas las secuencias tienen un orden, indexado por enteros, y tienen una longitud.

```python
a = 'Hello'               # String o cadena
b = [1, 4, 5]             # Lista
c = ('Pera', 100, 490.1)  # Tupla

# Orden indexado
a[0]                      # 'H'
b[-1]                     # 5
c[1]                      # 100

# Longitud de secuencias
len(a)                    # 5
len(b)                    # 3
len(c)                    # 3
```

Las secuencias pueden ser replicadas: `s * n`.

```python
>>> a = 'Hello'
>>> a * 3
'HelloHelloHello'
>>> b = [1, 2, 3]
>>> b * 2
[1, 2, 3, 1, 2, 3]
>>>
```

Las secuencias del mismo tipo también pueden ser concatenadas: `s + t`.

```python
>>> a = (1, 2, 3)
>>> b = (4, 5)
>>> a + b
(1, 2, 3, 4, 5)
>>>
>>> c = [1, 5]
>>> a + c
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate tuple (not "list") to tuple
```

### Rebanadas (slicing)

Sacar una rebanada es tomar una subsecuencia de una secuencia.
La sintaxis es `s[comienzo:fin]`, donde `comienzo` y `fin` son los índices de la subsecuencia que querés.

```python
a = [0,1,2,3,4,5,6,7,8]

a[2:5]    # [2,3,4]
a[-5:]    # [4,5,6,7,8]
a[:3]     # [0,1,2]
```

* Los índices `comienzo` y `fin` deben ser enteros.
* Las rebanadas *no* incluyen el valor final. Es como los intervalos semi-abiertos en matemática.
* Si los índices son omitidos toman sus valores por defecto: el principio o el final de la lista.

### Reasigación de rebanadas

En listas, una rebanada puede ser reasignada o eliminada.

```python
# Reasignación
a = [0,1,2,3,4,5,6,7,8]
a[2:4] = [10,11,12]       # [0,1,10,11,12,4,5,6,7,8]
```

*Observación: La rebanada reasignada no tiene que tener necesariamente la misma longitud.*

```python
# Eliminación
a = [0,1,2,3,4,5,6,7,8]
del a[2:4]                # [0,1,4,5,6,7,8]
```

### Reducciones de secuencias

Hay algunas operaciones usuales que reducen una secuencia a un solo valor.

```python
>>> s = [1, 2, 3, 4]
>>> sum(s)
10
>>> min(s)
1
>>> max(s)
4
>>> t = ['Hello', 'World']
>>> max(t)
'World'
>>>
```

### Iterar sobre una secuencia

Los ciclos `for` iteran sobre los elementos de una secuencia.

```python
>>> s = [1, 4, 9, 16]
>>> for i in s:
...     print(i)
...
1
4
9
16
>>>
```

En cada iteración del ciclo obtenés un nuevo elemento para trabajar. La variable iteradora va a tomar este nuevo valor. En el siguiente ejemplo la variable iteradora es `x`:

```python
for x in s:         # `x` es una variable iteradora
    ...instrucciones
```

En cada iteración, el valor previo de la variable (si hubo alguno) es sobreescrito. Luego de terminar el ciclo, la variable retiene su último valor.

### El comando break

Podés usar el comando `break` para romper un ciclo antes de tiempo.

```python
for name in namelist:
    if name == 'Juana':
        break
    ...
    ...
instrucciones
```

Cuando el comando  `break` se ejecuta, sale del ciclo y se mueve a las siguientes `instrucciones`.  El comando `break` sólo se aplica al ciclo más interno. Si un ciclo está anidado en otro ciclo, el comando no va a romper el ciclo externo.

### El comando continue

Para saltear un elemento y moverse al siguiente, usá el comando `continue`.

```python
for line in lines:
    if line == '\n':    # Salteo las líneas en blanco
        continue
    # Más instrucciones
    ...
```

Ésta es útil cuando el elemento actual no es de interés o es necesario ignorarlo en el procesamiento.

### Ciclos sobre enteros

Para iterar sobre un rango de números enteros, usá `range()`.

```python
for i in range(100):
    # i = 0,1,...,99
```

La sintaxis es `range([comienzo,] fin [,paso])` (lo que figura entre corchetes es opcional).

```python
for i in range(100):
    # i = 0,1,...,99
    ...codigo
for j in range(10,20):
    # j = 10,11,..., 19
    ...codigo
for k in range(10,50,2):
    # k = 10,12,...,48
    # Observá que va de a dos.
    ...codigo
```

* El valor final nunca es incluido. Es como con las rebanadas.
* `comienzo` es opcional. Por defecto es `0`.
* `paso` es opcional. Por defecto es `1`.
* `range()` calcula los valores a medida que los necesita. No guarda realmente en memoria el rango completo de números.

### La función enumerate()

La función `enumerate` agrega un contador extra a una iteración.

```python
nombres = ['Edmundo', 'Juana', 'Rosita']
for i, nombre in enumerate(nombres):
    # i = 0, nombre = 'Edmundo'
    # i = 1, nombre = 'Juana'
    # i = 2, nombre = 'Rosita'
```

La forma general es `enumerate(secuencia [, start = 0])`. `start` es opcional.
Un buen ejemplo de cuándo usar `enumerate()` es para llevar la cuenta del número de línea mientras estás leyendo un archivo:

```python
with open(nombre_archivo) as f:
    for nlinea, line in enumerate(f, start=1):
        ...
```

Al fin de cuentas, `enumerate` es sólo una forma abreviada y simpática de escribir:

```python
i = 0
for x in s:
    instrucciones
    i += 1
```

Al usar `enumerate` tenemos que tipear menos y el programa funciona un toque más rápido.

### Tuplas y ciclos for

Podés iterar con múltiples variables de iteración.

```python
points = [
  (1, 4),(10, 40),(23, 14),(5, 6),(7, 8)
]
for x, y in points:
    #   x = 1, y = 4
    #   x = 10, y = 40
    #   x = 23, y = 14
    #   ...
```

Cuando usás múltiples variables, cada tupla es *desempaquetada* en un conjunto de variables de iteración. El número de variables debe coincidir con la cantidad de elementos de cada tupla.

### La función zip()

La función `zip` toma múltiples secuencias y las combina en un iterador.

```python
columnas = ['nombre', 'cajones', 'precio']
valores = ['Pera', 100, 490.1 ]
pares = zip(columnas, valores)
# ('nombre','Pera'), ('cajones',100), ('precio',490.1)
```

Para obtener el resultado debés iterar. Podés usar múltiples variables para desempaquetar las tuplas como mostramos antes.

```python
for columna, valor in pares:
    ...
```

Un uso frecuente de `zip` es para crear pares clave/valor y construir diccionarios.

```python
d = dict(zip(columnas, valores))
```

## Ejercicios

### Ejercicio 2.16: Contar
Probá algunos ejemplos elementales de conteo:

```python
>>> for n in range(10):            # Contar 0 ... 9
        print(n, end=' ')

0 1 2 3 4 5 6 7 8 9
>>> for n in range(10,0,-1):       # Contar 10 ... 1
        print(n, end=' ')

10 9 8 7 6 5 4 3 2 1
>>> for n in range(0,10,2):        # Contar 0, 2, ... 8
        print(n, end=' ')

0 2 4 6 8
>>>
```

### Ejercicio 2.17: Más operaciones con secuencias
Interactivamente experimentá con algunas operaciones de reducción de secuencias.

```python
>>> data = [4, 9, 1, 25, 16, 100, 49]
>>> min(data)
1
>>> max(data)
100
>>> sum(data)
204
>>>
```

Probá iterar sobre los datos.

```python
>>> for x in data:
        print(x)

4
9
...
>>> for n, x in enumerate(data):
        print(n, x)

0 4
1 9
2 1
...
>>>
```

A veces los comandos for, len(), y range() son combinados para recorrer listas:

```python
>>> for n in range(len(data)):
        print(data[n])

4
9
1
...
>>>
```

Sin embargo, Python tiene mejores alternativas para esto. Te recomendamos familiarizarte con ellas y usarlas: por su simpleza producen código más legible y reducen la posibilidad de un bug en el código. Simplemente usa un ciclo `for` normal si querés iterar sobre los elementos de la variable `data`.  Y usá `enumerate()` si necesitás tener el índice por algún motivo.

### Ejercicio 2.18: Un ejemplo práctico de enumerate()
Recordá que el archivo  `Data/missing.csv` contiene datos sobre los cajones de un camión, pero tiene algunas filas que faltan. Usando `enumerate()`,
modificá tu programa `costo_camion.py` de forma que imprima un aviso (warning) cada vez que encuentre una fila incorrecta.

```python
>>> cost = costo_camion('Data/missing.csv')
Fila 4: No pude interpretar: ['Mandarina', '', '51.23']
Fila 7: No pude interpretar: ['Naranja', '', '70.44']
>>>
```

Para hacer esto, vas a tener que cambiar algunas partes de tu código.

```python
...
for n_fila, fila in enumerate(filas, start=1):
    try:
        ...
    except ValueError:
        print(f'Fila {n_fila}: No pude interpretar: {fila}')
```

### Ejercicio 2.19: La función zip()
En el archivo `Data/camion.csv`, la primera línea tiene los encabezados de las columnas. En los códigos anteriores la descartamos.

```python
>>> f = open('Data/camion.csv')
>>> filas = csv.reader(f)
>>> encabezados = next(filas)
>>> encabezados
['nombre', 'cajones', 'precio']
>>>
```

Pero, ¿no puede ser útil conocer los encabezados? Es acá donde la función `zip()` entra en acción. Primero tratá de aparear los encabezados con una fila de datos:

```python
>>> fila = next(filas)
>>> fila
['Lima', '100', '32.20']
>>> list(zip(encabezados, fila))
[ ('nombre', 'Lima'), ('cajones', '100'), ('precio', '32.20') ]
>>>
```

Fijate cómo `zip()` apareó los encabezados de las columnas con los valores de la columna.
Usamos `list()` arriba para devolver el resultado en una lista de forma que lo puedas ver. Normalmente, `zip()` crea un iterador que debe ser consumido en un ciclo for.

Este apareamiento es un paso intermedio para construir un diccionario. Probá lo siguiente:

```python
>>> record = dict(zip(encabezados, fila))
>>> record
{'precio': '32.20', 'nombre': 'Lima', 'cajones': '100'}
>>>
```

Esta transformación es un truco sumamente útil cuando tenés que procesar muchos archivos de datos. Por ejemplo, suponé que querés hacer que el programa `costo_camion.py` trabaje con diferentes archivos de entrada, pero que no le importe la posición exacta de la columna que tiene la cantidad de cajones o el precio. Es decir, que entienda que la columna tiene el precio por su encabezado y no por su posición dentro del archivo.

Modificá la función  `costo_camion()` en el archivo `costo_camion.py` para que se vea así:

```python
# costo_camion.py

def costo_camion(nombre_archivo):
    ...
        for n_fila, fila in enumerate(filas, start=1):
            record = dict(zip(encabezados, fila))
            try:
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                costo_total += ncajones * precio
            # Esto atrapa errores en los int() y float() de arriba.
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
        ...
```

Ahora, probá tu función con un archivo completamente diferente `Data/fecha_camion.csv` que se ve así:

```csv
nombre,fecha,hora,cajones,precio
"Lima","6/11/2007","9:50am",100,32.20
"Naranja","5/13/2007","4:20pm",50,91.10
"Caqui","9/23/2006","1:30pm",150,83.44
"Mandarina","5/17/2007","10:30am",200,51.23
"Durazno","2/1/2006","10:45am",95,40.37
"Mandarina","10/31/2006","12:05pm",50,65.10
"Naranja","7/9/2006","3:15pm",100,70.44
```

```python
>>> costo_camion('Data/fecha_camion.csv')
47671.15
>>>
```

Si lo hiciste bien, vas a descubrir que tu programa aún funciona a pesar de que le pasaste un archivo con un formato de columnas completamente diferente al de antes. ¡Y eso está muy bueno!

El cambio que hicimos acá es sutil, pero importante. En lugar de tener *hardcodeado* un formato fijo, la nueva versión de la función `costo_camion()` puede sacar la información de interés de cualquier archivo CSV. En la medida en que el archivo tenga las columnas requeridas, el código va a funcionar.

Modificá el programa `informe.py` que escribiste antes (ver [Ejercicio 2.15](../02_Datos/04_Contenedores.md#ejercicio-215-balances)) para que use esta técnica para elegir las columnas a partir de sus encabezados.

Probá correr el programa `informe.py` sobre el archivo  `Data/fecha_camion.csv`
y fijate si da la misma salida que antes.

### Ejercicio 2.20: Invertir un diccionario
Un diccionario es una función que mapea claves en valores. Por ejemplo, un diccionario de precios de cajones de frutas.

```python
>>> precios = {
        'Pera' : 490.1,
        'Lima' : 23.45,
        'Naranja' : 91.1,
        'Mandarina' : 34.23
    }
>>>
```

Si usás el método `items()`, obtenés pares `(clave,valor)`:

```python
>>> precios.items()
dict_items([('Pera', 490.1), ('Lima', 23.45), ('Naranja', 91.1), ('Mandarina', 34.23)])
>>>
```

Sin embargo, si lo que querés son pares `(valor, clave)`, ¿cómo lo hacés?
*Ayuda: usá `zip()`.*

```python
>>> lista_precios = list(zip(precios.values(),precios.keys()))
>>> lista_precios
[(490.1, 'Pera'), (23.45, 'Lima'), (91.1, 'Naranja'), (34.23, 'Mandarina')]
>>>
```

¿Por qué haría algo así? Por un lado porque te permite realizar cierto tipo de procesamiento de datos sobre la información del diccionario.

```python
>>> min(lista_precios)
(23.45, 'Lima')
>>> max(lista_precios)
(490.1, 'Pera')
>>> sorted(lista_precios)
[(23.45, 'Lima'), (34.23, 'Mandarina'), (91.1, 'Naranja'), (490.1, 'Pera')]
>>>
```

Esto también ilustra un atributo importante de las tuplas. Cuando son usadas en una comparación, las tuplas son comparadas elemento-a-elemento comenzando con el primero. Es similar a la lógica subyacente al orden lexicográfico o alfabético en las cadenas.

La función `zip()` se usa frecuentemente en este tipo de situaciones donde necesitás aparear datos provenientes de diferentes lugares. Por ejemplo, para aparear los nombres de las columnas con los valores para hacer un diccionario de valores con nombres.

Observá que `zip()` no está limitada a pares. Podés usarla con cualquier número de listas de entrada:

```python
>>> a = [1, 2, 3, 4]
>>> b = ['w', 'x', 'y', 'z']
>>> c = [0.2, 0.4, 0.6, 0.8]
>>> list(zip(a, b, c))
[(1, 'w', 0.2), (2, 'x', 0.4), (3, 'y', 0.6), (4, 'z', 0.8))]
>>>
```

También, tené en cuenta que `zip()` se detiene cuando la más corta de las entradas se agota.

```python
>>> a = [1, 2, 3, 4, 5, 6]
>>> b = ['x', 'y', 'z']
>>> list(zip(a,b))
[(1, 'x'), (2, 'y'), (3, 'z')]
>>>
```


[Contenidos](../Contenidos.md) \| [Anterior (4 Contenedores)](04_Contenedores.md) \| [Próximo (6 Contadores del módulo _collections_)](06_Contadores.md)

