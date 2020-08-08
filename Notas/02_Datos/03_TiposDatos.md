[Contenidos](../Contenidos.md) \| [Anterior (2 Funciones)](02_Funciones.md) \| [Próximo (4 Contenedores)](04_Contenedores.md)

# 2.3 Tipos y estructuras de datos

Esta sección introduce dos estructuras de datos elementales: las tuplas y los diccionarios.

### Tipos de datos primitivos

Python tiene pocos tipos primitivos de datos.

* Números enteros
* Números de punto flotante
* Cadenas de texto

Algo ya sabemos sobre estos tipos de datos por el capítulo anterior.

### Tipo None

```python
email_address = None
```

`None` suele utilizarse como un comodín para reservar el lugar para un valor opcional o faltante. En los condicionales, evalúa como `False`.

```python
if email_address:
    send_email(email_address, msg)
```

### Estructuras de datos

Los programas reales tienen datos más complejos que los que podemos almacenar en los tipos primitivos. Por ejemplo, información sobre un pedido de frutas:

```code
100 cajones de Manzanas a $490.10 cada uno
```

Podemos ver esto como un "objeto" con tres partes:

* Nombre del símbolo ("Manzanas", una cadena)
* Número o cantidad (100, un entero)
* Precio (490.10 un flotante)

### Tuplas

Una tupla es una colección con valores agrupados juntos.

Ejemplo:

```python
s = ('Manzanas', 100, 490.1)
```

Las tuplas suelen usarse para representar registros o estructuras *simples*.
Típicamente, una tupla representa un solo *objeto* con múltiples partes. Una analogía posible es la siguiente: *Una tupla es como una fila de una base de datos*.

Los contenidos de una tupla están ordenados (como en una lista).

```python
s = ('Manzana', 100, 490.1)
nombre = s[0]                   # 'Manzana'
cantidad = s[1]                 # 100
precio= s[2]                    # 490.1
```

El contenido de las tuplas no puede ser modificado.

```python
>>> s[1] = 75
TypeError: object does not support item assignment
```

Podés, sin embargo, hacer una nueva tupla basada en el contenido de otra, que no es lo mismo que modificar el contenido.

```python
s = (s[0], 75, s[2])
```

#### Empaquetar tuplas

Las tuplas suelen usarse para empaquetar información relacionada en una sola *entidad*.

```python
s = ('Manzanas', 100, 490.1)
```

Una tupla puede ser pasada de un lugar a otro de un programa como un solo objeto.

#### Desempaquetar tuplas

Para usar una tupla en otro lado, debemos desempaquetar su contenido en diferentes variables.

```python
fruta, cajones, precio = s
print('Costo:', cajones * precio)
```

El número de variables a la izquierda debe ser consistente con la estructura de la tupla.

```python
nombre, cajones = s     # ERROR
Traceback (most recent call last):
...
ValueError: too many values to unpack
```

### Tuplas vs. Listas

Las tuplas parecieran ser listas de solo-lectura. Sin embargo, las tuplas suelen usarse para un solo ítem que consiste de múltiples partes mientras que las listas suelen usarse para una colección de diferentes elementos, típicamente del mismo tipo.

```python
record = ('Manzanas', 100, 490.1)                # Una tupla representando un registro dentro de un pedido de frutas

symbols = [ 'Manzanas', 'Peras', 'Mandarinas' ]  # Una lista representando tres frutas diferentes.
```

### Diccionarios

Un diccionario es una función que manda *claves* en *valores*. Las claves sirven como índices para acceder a los valores.

```python
s = {
    'fruta': 'Manzana',
    'cajones': 100,
    'precio': 490.1
}
```

#### Operaciones usuales

Para obtener el valor almacenado en un diccionario usamos las claves.

```python
>>> print(s['fruta'], s['cajones'])
Manzanas 100
>>> s['precio']
490.10
>>>
```

Para agregar o modificar valores, simplemente asignamos usando la clave.

```python
>>> s['cajones'] = 75
>>> s['fecha'] = '6/8/2020'
>>>
```

para borrar un valor, usamos el comando `del`.

```python
>>> del s['fecha']
>>>
```

#### ¿Por qué diccionarios?

Los diccionarios son útiles cuando hay *muchos* valores diferentes y esos valores pueden ser modificados o manipulados. Dado que el acceso a los elementos se hace por *clave*, no es necesario recordar una posición para cierto dato, lo que muchas veces cumple un objetivo fundamental: hacer que el código sea más legible (y con esto menos propenso a errores).

```python
s['precio'] # diccionario
# vs
s[2] # lista
```

## Ejercicios

Anteriormente escribiste un programa que leía el archivo
`Data/camion.csv` usando el módulo `csv` para leer el archivo fila por fila.

```python
>>> import csv
>>> f = open('Data/camion.csv')
>>> filas = csv.reader(f)
>>> next(filas)
['nombre', 'cajones', 'precio']
>>> fila = next(filas)
>>> fila
['Lima', '100', '32.20']
>>>
```

A veces, además de leerlo, queremos hacer otras cosas con el archivo CSV, como por ejemplo usar los datos que contiene para hacer un cálculo. Lamentablemente una fila de datos en crudo no es suficiente para operar aritméticamente. Vamos a querer interpretar los elementos de la fila de datos de alguna manera particular, convirtiéndolos a otro tipo de datos que resulte más adecuado para trabajar. Es frecuente además de convertir los elementos de las filas, transformar las filas enteras en tuplas o diccionarios.

### Ejercicio 2.9: Tuplas
En el intérprete interactivo, creá la siguiente tupla que representa la fila de antes, pero con las columnas numéricas pasadas a formatos adecuados:

```python
>>> t = (fila[0], int(fila[1]), float(fila[2]))
>>> t
('Lima', 100, 32.2)
>>>
```

A partir de esta tupla, ahora podés calcular el costo total multiplicando cajones por precio:

```python
>>> cost = t[1] * t[2]
>>> cost
3220.0000000000005
>>>
```

¿Qué pasó? ¿Qué hace ese 5 al final?

Este error no es un problema de Python, sino de la forma en la que la máquina representa los números de punto flotante. Así como en base 10 no podemos escribir un tercio de manera exacta, en base 2 escribir un quinto requiere infinitos dígitos. Al usar una representación finita (una cantidad acotada de dígitos) la máquina redondea los números. La aritmética de punto flotante no es exacta.

Esto pasa en todos los lenguajes de programación que usan punto flotante, pero en muchos casos estos pequeños errores quedan ocultos al imprimir. Por ejemplo:

```python
>>> print(f'{cost:0.2f}')
3220.00
>>>
```

Las tuplas son de sólo lectura. Verificalo tratando de cambiar el número de cajones a 75.

```python
>>> t[1] = 75
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>>
```

Aunque no podés cambiar al tupla, sí podés reemplazar la tupla por una nueva.

```python
>>> t = (t[0], 75, t[2])
>>> t
('Lima', 75, 32.2)
>>>
```

Siempre que reasignes una variable como recién lo hiciste con `t`, el valor anterior de la variable se pierde. Aunque la asignación de arriba pueda parecer como que estás modificando la tupla, en realidad estás creando una nueva tupla y tirando la vieja.

Las tuplas muchas veces se usan para empaquetar y desempaquetar valores dentro de variables. Probá esto:

```python
>>> nombre, cajones, precio = t
>>> nombre
'Lima'
>>> cajones
75
>>> precio
32.2
>>>
```

Tomá las variables de arriba y empaquetalas en una tupla.

```python
>>> t = (nombre, 2*cajones, precio)
>>> t
('Lima', 150, 32.2)
>>>
```

### Ejercicio 2.10: Diccionarios como estructuras de datos
Una alternativa a la tupla es un diccionario.

```python
>>> d = {
        'nombre' : fila[0],
        'cajones' : int(fila[1]),
        'precio'  : float(fila[2])
    }
>>> d
{'nombre': 'Lima', 'cajones': 100, 'precio': 32.2 }
>>>
```

Calculá el costo total de este lote:

```python
>>> cost = d['cajones'] * d['precio']
>>> cost
3220.0000000000005
>>>
```

Compará este ejemplo con el mismo cálculo hecho con tuplas más arriba. Cambiá el número de cajones a 75.

```python
>>> d['cajones'] = 75
>>> d
{'nombre': 'Lima', 'cajones': 75, 'precio': 32.2 }
>>>
```

A diferencia de las tuplas, los diccionarios se pueden modificar libremente. Agregá algunos atributos:

```python
>>> d['fecha'] = (14, 8, 2020)
>>> d['cuenta'] = 12345
>>> d
{'nombre': 'Lima', 'cajones': 75, 'precio':32.2, 'fecha': (14, 8, 2020), 'cuenta': 12345}
>>>
```

### Ejercicio 2.11: Más operaciones con diccionarios
Si usás el comando `for` para iterar sobre el diccionario, obtenés las claves:

```python
>>> for k in d:
        print('k =', k)

k = nombre
k = cajones
k = precio
k = fecha
k = cuenta
>>>
```

Probá esta variante:

```python
>>> for k in d:
        print(k, '=', d[k])

nombre = 'Lima'
cajones = 75
precio = 32.2
fecha = (14, 8, 2020)
cuenta = 12345
>>>
```

Una manera más elegante de trabajar con claves y valores simultáneamente es usar el método `items()`. Esto te devuelve una lista de tuplas de la forma `(clave,valor)` sobre la que podés iterar.

```python
>>> items = d.items()
>>> items
dict_items([('nombre', 'Lima'), ('cajones', 75), ('precio', 32.2), ('fecha', (14, 8, 2020))])
>>> for k, v in d.items():
        print(k, '=', v)

nombre = Lima
cajones = 75
precio = 32.2
fecha = (14, 8, 2020)
>>>
```

Si pasás un diccionario a una lista, obtenés sus claves.

```python
>>> list(d)
['nombre', 'cajones', 'precio', 'fecha', 'cuenta']
>>>
```

También podés obtener todas las claves del diccionario usando el método `keys()`:

```python
>>> claves = d.keys()
>>> claves
dict_keys(['nombre', 'cajones', 'precio', 'fecha', 'cuenta'])
>>>
```

Si tenés tuplas como en `items` podés crear un diccionario usando la función `dict()`. Probá esto:

```python
>>> nuevos_items = [('nombre', 'Manzanas'), ('cajones', 100), ('precio', 490.1), ('fecha', (13, 8, 2020))]
>>> nuevos_items
[('nombre', 'Manzanas'), ('cajones', 100), ('precio', 490.1), ('fecha', (13, 8, 2020))]
>>> d = dict(nuevos_items)
>>> d
{'nombre': 'Manzanas', 'cajones': 100, 'precio': 490.1, 'fecha': (13, 8, 2020)}
```


[Contenidos](../Contenidos.md) \| [Anterior (2 Funciones)](02_Funciones.md) \| [Próximo (4 Contenedores)](04_Contenedores.md)

