[Contenidos](../Contenidos.md) \| [Anterior (2 Herencia)](02_Herencia.md) \| [Próximo (4 Objetos, pilas y colas)](04_Pilas_Colas.md)

# 8.3 Métodos especiales

Podemos modificar muchos comportamientos de Python definiendo lo que se conoce como "métodos especiales". Acá vamos a ver cómo usar estos métodos y a discutir brevemente otras herramientas relacionadas.

### Introducción

Una clase puede tener definidos métodos especiales. Estos métodos tienen un significado particular para el intérprete de Python. Sus nombres empiezan y terminan en `__` (doble guión bajo). Por ejemplo `__init__`.

```python
class Lote(object):
    def __init__(self):
        ...
    def __repr__(self):
        ...
```

Hay decenas de métodos especiales pero sólo vamos a tratar algunos ejemplos específicos acá. 

### Métodos especiales para convertir a strings


Los objetos tienen dos representaciones de tipo cadena.

```python
>>> from datetime import date
>>> d = date(2020, 12, 21)
>>> print(d)
2020-12-21
>>> d
datetime.date(2020, 12, 21)
>>>
```

La función `str()` se usa para crear una representación agradable de ver:

```python
>>> str(d)
'2020-12-21'
>>>
```

Pero para crear una representación más informativa para programadores, se usa la función `repr()`. 

```python
>>> repr(d)
'datetime.date(2020, 12, 21)'
>>>
```

Las funciones `str()` y `repr()` llaman a métodos especiales de la clase para generar la cadena de caracteres que se va a mostrar. 

```python
class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Con `str()`
    def __str__(self):
        return f'{self.year}-{self.month}-{self.day}'

    # Con `repr()`
    def __repr__(self):
        return f'Date({self.year},{self.month},{self.day})'
```
*Nota: Hay una convención para `__repr__()` que indica que debe devolver un string que, cuando sea pasado a `eval()` vuelva a crear el objeto subayacente. Analizá el ejemplo de `datetime.date(2020, 12, 21)`. Si no es posible crear un string que haga eso, la convención es generar una representación que sea fácil de interpretar para una persona.*

```python
class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    # Used with `repr()`
    def __repr__(self):
        return f'Punto({self.x}, {self.y})'
```


### Métodos matemáticos especiales

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

Así, al definir un método `__add__(b)` en la clase `Punto`, por ejemplo, nos permitirá sumar dos instancias de esta clase usando el operador `+`.

```python
class Punto():
    ...
    ...
    def __add__(self, b):
      return Punto(self.x + b.x, self.y + b.y)
```

Como en el siguiente ejemplo:

```python
>>> a = Punto(1,2)  
>>> b = Punto(3,4)  
>>> repr(a + b)
'Punto(4, 6)'
```


### Métodos especiales para acceder a elementos

Los siguientes métodos se usan para implementar contenedores:

```python
len(x)      x.__len__()
x[a]        x.__getitem__(a)
x[a] = v    x.__setitem__(a,v)
del x[a]    x.__delitem__(a)
```

Los podés implementar en tus clases.

```python
class Secuencia:
    def __len__(self):
        ...
    def __getitem__(self,a):
        ...
    def __setitem__(self,a,v):
        ...
    def __delitem__(self,a):
        ...
```

### Invocar métodos

El proceso de invocar un método puede dividirse en dos partes:

1. Búsqueda: Se usa el operator `.`
2. Llamado: Se usan `()`

```python
>>> m = Lote('Pera', 100, 490.10)
>>> c = m.costo  # Búsqueda
>>> c
<bound method Lote.costo of <Lote object at 0x590d0>>
>>> c()          # Llamado
49010.0
>>>
```
*Nota*: la respuesta al pedido de representación de `c` es algo así como 
<Método Lote.costo asociado al <objeto Lote en 0x590d0>>*

### Métodos ligados

Un método que aún no ha sido llamado por el operador de llamado a funciones `()` se conoce como *método ligado* y opera dentro de la instancia en la que fue originado.

```python
>>> m = Lote('Pera', 100, 490.10) 
>>> m
<Lote object at 0x590d0>
>>> c = m.costo
>>> c
<bound method Lote.costo of <Lote object at 0x590d0>>
>>> c()
49010.0
>>>
```

Estos métodos ligados pueden ser el origen de errores por desprolijidad, que no son nada obvios. Por ejemplo:

```python
>>> m = Lote('Pera', 100, 490.10)
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
f.close   # EPA! No hicimos nada. `f` sigue abierto.
```

En ambos casos, el error está causado por omitir los paréntesis en el (intento de) llamado a la función. En estos casos debería haber sido: `m.costo()` o `f.close()`. Sin los paréntesis, no estamos llamando a la función sino refiriéndonos al método.

### Acceso a atributos

Existe una forma alternativa de acceder, manipular, y administrar los atributos de un objeto.

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

*Nota*: si `getattr()` no encuentra el atributo buscado (`x` en este ejemplo), devuelve el argumento opcional *arg* (`None` en este caso)

```python
x = getattr(obj, 'x', None)
```



## Ejercicios

### Ejercicio 8.9: Mejor salida para objetos
Modificá el objeto `Lote` que definiste en `lote.py` (del [Ejercicio 8.1](../08_Clases_y_Objetos/01_Clases.md#ejercicio-81-objetos-como-estructura-de-datos)) de modo que el método `__repr__()` genere una salida más agradable. Por ejemplo queremos un comportamiento como éste: 

```python
>>> peras = Lote('Pera', 100, 490.1)
>>> peras
Lote('Pera', 100, 490.1)
>>>
```

Fijate lo que ocurre cuando leés un camión de frutas y mirás la salida resultante después de hacer estos cambios. Un ejemplo:

```python
>>> import informe
>>> camion = informe.leer_camion('Data/camion.csv')
>>> camion
... fijate cuál es la salida ...
>>>
```

Guardá el archivo `lote.py` para entregar.

### Ejercicio 8.10: Ejemplo de getattr()
`getattr()` es un mecanismo alternativo de leer atributos. Puede usarse para escribir código sumamente versátil. Probá este ejemplo, para empezar: 

```python
>>> import lote
>>> c = lote.Lote('Peras', 100, 490.1)
>>> columnas = ['nombre', 'cajones']
>>> for colname in columnas:
        print(colname, '=', getattr(c, colname))

nombre = Peras
cajones = 100
>>>
```

Queremos que observes algo interesante: los datos de salida están completamente especificados por los nombres de los atributos listados en la variable `columnas`. Estamos usando el contenido de una variable ('nombre' y 'cajones') como nombres de otras variables, o de atributos de un objeto. No es usual. 

Si te dan ganas, en el archivo `formato_tabla.py` usá esta idea pero extendela, y creá una función `imprimir_tabla()` que imprima una tabla mostrando, de una lista de objetos de tipo arbitrario, una lista de atributos especificados por le usuarie.

Tal como antes hicimos con la función `imprimir_informe()` del [Ejercicio 5.1](../05_Organización_y_Complejidad/01_Scripts.md#ejercicio-51-estructurar-un-programa-como-una-colección-de-funciones) `imprimir_tabla()` también debería aceptar cualquier instancia de la clase `FormatoTabla` para definir el formato de la salida. La idea es que funcione más o menos así:

```python
>>> import informe
>>> camion = informe.leer_camion('Data/camion.csv')
>>> from formato_tabla import crear_formateador, imprimir_tabla
>>> formateador = crear_formateador('txt')
>>> imprimir_tabla(camion, ['nombre','cajones'], formateador)
    nombre    cajones 
---------- ---------- 
      Lima        100 
   Naranja         50 
     Caqui        150 
 Mandarina        200 
   Durazno         95 
 Mandarina         50 
   Naranja        100 

>>> imprimir_tabla(camion, ['nombre','cajones','precio'], formateador)
    nombre    cajones     precio 
---------- ---------- ---------- 
      Lima        100       32.2 
   Naranja         50       91.1 
     Caqui        150     103.44 
 Mandarina        200      51.23 
   Durazno         95      40.37 
 Mandarina         50       65.1 
   Naranja        100      70.44
>>>
```


[Contenidos](../Contenidos.md) \| [Anterior (2 Herencia)](02_Herencia.md) \| [Próximo (4 Objetos, pilas y colas)](04_Pilas_Colas.md)

