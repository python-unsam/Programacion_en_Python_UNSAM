[Contenidos](../Contenidos.md) \| [Anterior (4 Herencia***)](04_Herencia.md) \| [Próximo (6 Ejercicio de objetos)](06_Ejs_OOP.md)

# 8.5 Métodos especiales

Podemos modificar muchos comportamientos de Python definiendo lo que se conoce como "métodos mágicos". Aquí vamos a ver como usarlos, además de discutir brevemente otras herramientas, como *acceso dinámco de atributos* y *métodos asociados*.

### Introducción

Una clase puede definir métodos especiales. Estos métodos tienen un significado particular para el intérprete de Python. Sus nombres empiezan y terminan en `__` (doble guión bajo). Por ejemplo `__init__`.

```python
class Stock(object):
    def __init__(self):
        ...
    def __repr__(self):
        ...
```

Hay decenas de métodos especiales pero sólo vamos a tratar algunos ejemplos específicos acá. 

### Special methods for String Conversions
Métodos especiales para convertir Strings

Los objetos tienen dos representaciones de tipo cadena (string)

```python
>>> from datetime import date
>>> d = date(2012, 12, 21)
>>> print(d)
2012-12-21
>>> d
datetime.date(2012, 12, 21)
>>>
```

La función `str()` se usa para crear una representación agradable de ver:

```python
>>> str(d)
'2012-12-21'
>>>
```

Pero para crear una representación mas agradable para programadores, se usa la función `repr()`. 

```python
>>> repr(d)
'datetime.date(2012, 12, 21)'
>>>
```

Las funciones `str()` y `repr()` usan un par de métodos especiales de la clase datetime.date() para generar la cadena de caracteres que se va a mostrar. 

```python
class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Used with `str()`
    def __str__(self):
        return f'{self.year}-{self.month}-{self.day}'

    # Used with `repr()`
    def __repr__(self):
        return f'Date({self.year},{self.month},{self.day})'
```
*Nota: La convención para `__repr__()` es devolver un string que, cuando sea pasado a `eval()` vuelva a crear el objeto subayacente. Analizá el ejemplo de `datetime.date(2012, 12, 21)`.  Si no es posible crear un string que haga éso, la convención es generar una representación que sea fácil de leer para un humano.*


### Special Methods for Mathematics
Métodos especiales para operaciones matemáticas.

Las operaciones matemáticas sobre los objetos involucran llamados a los siguientes métodos.

```python
a + b       a.__add__(b)
a - b       a.__sub__(b)
a * b       a.__mul__(b)
a / b       a.__truediv__(b)
a // b      a.__floordiv__(b)
a % b       a.__mod__(b)
a << b      a.__lshift__(b)
a >> b      a.__rshift__(b)
a & b       a.__and__(b)
a | b       a.__or__(b)
a ^ b       a.__xor__(b)
a ** b      a.__pow__(b)
-a          a.__neg__()
~a          a.__invert__()
abs(a)      a.__abs__()
```

### Special Methods for Item Access
Métodos especiales para acceder a elementos.

Los siguientes métodos se usan para implementar containers (contenedores / recipientes):

```python
len(x)      x.__len__()
x[a]        x.__getitem__(a)
x[a] = v    x.__setitem__(a,v)
del x[a]    x.__delitem__(a)
```

Los podés implementar en tus clases.

```python
class Sequence:
    def __len__(self):
        ...
    def __getitem__(self,a):
        ...
    def __setitem__(self,a,v):
        ...
    def __delitem__(self,a):
        ...
```

### Method Invocation
Invocar métodos.

El proceso de invocar un método puede dividirse en dos partes:

1. Busqueda: Se usa el operator `.`
2. Llamado : Se usan `()`

```python
>>> m = Mercado('Pera',100,490.10)
>>> c = m.costo  # Búsqueda
>>> c
<bound method Mercado.costo of <Mercado object at 0x590d0>>
>>> c()         # Llamado
49010.0
>>>
```
*Nota: la respuesta al pedido de representación de `c` es algo así como 
<Método Mercado.costo asociado al <objeto Mercado en 0x590d0>>*

### Bound Methods
Métodos asociados.

Un método que aún no ha sido llamado por el operador de llamado a funciones `()` se conoce como *método asociado* y opera dentro de la instancia en la que fué originado.

```python
>>> m = Mercado('Pera', 100, 490.10) 
>>> m
<Mercado object at 0x590d0>
>>> c = m.cost
>>> c
<bound method Mercado.costo of <Mercado object at 0x590d0>>
>>> c()
49010.0
>>>
```

Estos métodos asociados pueden ser el origen de errores por desprolijidad, que no son nada obvios. Por ejemplo:

```python
>>> m = Mercado('Pera', 100, 490.10)
>>> print('Costo : %0.2f' % m.costo)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: float argument required
>>>
```

O una fuente de comportamiento extraño que es difícil de debuggear.

```python
f = open(filename, 'w')
...
f.close   # EPA !! No hicimos nada. `f` sigue abierto.
```

En ambos casos, el error está causado por omitir los paréntesis en el (intento de) llamado a la función. Por ejemplo, `m.costo()` o `f.close()`. Sin los paréntesis, no estamos llamando a la función sino buscando al objeto.

### Attribute Access
Acceso a atributos.

Existe una forma alternativa de acceder, manipular, y administrar las propiedades (o atributos) de un objeto.

```python
getattr(obj, 'name')          # Equivale a obj.name
setattr(obj, 'name', value)   # Equivale a obj.name = value
delattr(obj, 'name')          # Equivale a del obj.name
hasattr(obj, 'name')          # Mira si la propiedad existe
```

Ejemplo:

```python
if hasattr(obj, 'x'):
    x = getattr(obj, 'x'):
else:
    x = None
```

*Nota: si `getattr()` no encuentra el atributo buscado (`x` en este ejemplo), devuelve el argumento opcional *arg* (`None` en este caso)

```python
x = getattr(obj, 'x', None)
```

## Ejercicios

### Ejercicio 8.9: Better output for printing objects

```python
>>> peras = Cajon('Pera', 100, 490.1)
>>> peras
Cajon('Pera', 100, 490.1)
>>>
```

Fijate lo que ocurre cuando lees un camión de frutas y mirás la salida resultante después de hacer estos cambios. Un ejemplo:

```python
>>> import informe
>>> camion = report.read_camion('Data/camion.csv')
>>> camion
... fijate cual es la salida ...
>>>
```

### Ejercicio 8.10: An example of using getattr()`getattr()` es un mecanismo alternativo de leer atributos. Puede usarse para escribir código sumamente versátil. Probá este ejemplo, para empezar: 

```python
>>> import cajones
>>> c = cajon.Cajones('Peras', 100, 490.1)
>>> columnas = ['nombre', 'cantidad']
>>> for colname in columnas:
        print(colname, '=', getattr(c, colname))

nombre = Peras
cantidad = 100
>>>
```

Queremos que notes algo interesante: los datos de salida están completamente especificados por los nombres de los atributos listados en la variable `columnas`. No fué necesario hacer ninguna conversión ni preguntar nada al usuario para usar el nombre de un dato como nombre de una variable.  



```python
>>> import informe
>>> portfolio = informe.leer_camion('Data/camion.csv')
>>> from formatotabla import crear_formato, imprimir_tabla
>>> formato = crear_formato('txt')
>>> imprimir_tabla(camion, ['name','shares'], formato)
    Nombre   Cantidad
---------- ----------
      Lima        100
   Naranja         50
     Caqui        150
 Mandarina        200
   Durazno         95
 Mandarina         50
   Naranja        100

>>> imprimir_tabla(camion, ['nombre','cantidad','precio'], formato)
    Nombre   Cantidad     Precio
---------- ---------- ----------
      Lima        100       32.2
   Naranja         50       91.1
     Caqui        150      83.44
 Mandarina        200      51.23
   Durazno         95      40.37
 Mandarina         50       65.1
   Naranja        100      70.44
>>>
```


[Contenidos](../Contenidos.md) \| [Anterior (4 Herencia***)](04_Herencia.md) \| [Próximo (6 Ejercicio de objetos)](06_Ejs_OOP.md)

