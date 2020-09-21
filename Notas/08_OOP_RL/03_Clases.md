[Contenidos](../Contenidos.md) \| [Anterior (2 Optativo: Regresión Lineal**)](02_OPT_RL.md) \| [Próximo (4 Herencia)](04_Herencia.md)

# 8.3 Clases

La programación orientada a objetos requiere un pequeño pero importante cambio en la forma de pensar la programación tradicional. Dejá decantar los conceptos nuevos mientras lees esta sección.

En esta sección veremos el concepto de clase, cómo crear nuevos objetos, su utilidad, y las ventajas de esa forma de organizar los programas.

### Programación orientada a objetos (POO)

La programación orientada a objetos es una forma de organizar el código. Así como un algoritmo suele estar asociado a una estructura de datos particular, la programación orientada a objetos "empaqueta" los datos junto con los métodos usados para tratarlos. 

Cada uno de esos *objetos* consiste en 

* Datos (atributos ó propiedades de los objetos).
* Comportamiento (son métodos de los objetos: funciones, que actúan sobre las propiedades del objeto).

Ya usaste objetos durante el curso infinidad de veces. Por ejemplo, al manipular una lista.


```python
>>> nums = [1, 2, 3]
>>> nums.append(4)      # Esto es un método
>>> nums.insert(1,10)   # Otro método
>>> nums
[1, 10, 2, 3, 4]        # Estos son los datos modificados por los métodos
>>>
```

Miremos un poco más en detalle ese fragmento de código. Decimos que `nums` es una *instancia* de un la clase *list*. Cada variable de tipo lista es una instancia de esa misma clase. 

Acá usamos "instancia" con el mismo significado que "objeto": un objeto es una instancia de una clase. La clase es como el tipo, el objeto es una instancia concreta, con sus valores reales.

Los métodos (`append()` e `insert()`) se definen cuando se define la clase, pero se usan para modificar (o acceder a) los datos de un objeto concreto (`nums` en este caso).

### La instrucción `class`

Para definir un tipo nuevo de objeto, usá la instrucción `class`.

```python
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def damage(self, pts):
        self.health -= pts
```

Muy brevemente, una clase es un conjunto de funciones que operan sobre las diversas instancias de esa clase.

Puede decirse que una clase es la definición formal de las relaciones entre los datos y los métodos que los manipulan. Un objeto es una instancia particular de la clase a la cual pertenece, con datos propios pero los mismos métodos que los demás objetos de esa clase. Este concepto te va a quedar más claro cuando lo veas funcionar y lo uses.

### Instancias

Los programas manipulan instancias individuales de las clases. Cada instancia se llama *objeto*, y es en cada objeto que uno puede manipular los datos y llamar a sus métodos. 

Podés crear un objeto mediante un llamado a la clase como si fuera una función.

```python
>>> a = Player(2, 3)    # Clase Player definida antes
>>> b = Player(10, 20)
>>>
```

`a` y `b` son instancias de `Player`, definida más arriba. i.e. a y b son objetos de la clase `Player`.

*Importante: La instrucción `class` es solamente la definición de una clase, no **hace** nada por sí misma. Es como la definición de una función: es sólo una definición.*

### Datos de una instancia

Cada instancia tiene sus propios datos locales. 
Aquí pedimos ver la propiedad `x` de cada instancia:

```python
>>> a.x
2
>>> b.x
10
```

Estos datos locales se inicializan, para cada instancia, durante la ejecución del método `__init__()` de la clase.

```python
class Player:
    def __init__(self, x, y):
        # Todo dato guardado en `self` es propio de esa instancia
        self.x = x
        self.y = y
        self.health = 100
```

No hay restricciones en la cantidad o el tipo de datos almacenados en cada instancia, ni sobre el número de propiedades que ésta pueda tener.

### Métodos de una instancia.

Los métodos de una instancia son los métodos y las funciones que actúan sobre los datos almacenados en esa instancia. 

```python
class Player:
    ...
    # `mover` es un método
    def mover(self, dx, dy):
        self.x += dx
        self.y += dy
```

Siempre se recibe la instancia misma como primer argumento:
"self" significa "mismo" como en "mi mismo" ó "en sí misma". Es como decir "yo".

```python
>>> a.mover(1, 2)

# `self` refiere a `a`
# `dx` refiere a `1`
# `dy` refiere a `2`
def move(self, dx, dy):
```

Por convención siempre llamamos `self` a la instancia actual, y ésta es siempre pasada como primer argumento a todos los métodos. En realidad el nombre real de la variable no importa, pero es una convención en Python llamar al primer argumento `self`. 

Podríamos usar `mismo`, por ejemplo, en lugar de `self` y todo va a funcionar igual, pero no repeta las convenciones de la comunidad:

```python
class Player:
    ...
    # `mover` es un método
    def mover(mismo, dx, dy):
        mismo.x += dx
        mismo.y += dy
```


### Visibilidad en clases (Scoping)

Las clases no definen ni limitan (como los módulos) un entorno de visibilidad.

```python
class Player:
    ...
    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

    def izquierda(self, dist):
        mover(-dist, 0)       # NO! Refiere a la función global `mover`.
        self.mover(-dist, 0)  # Sí. Llama al método `mover` definido antes.
```

Si necesitás referite a un dato o un método de una clase tenés que hacer una referencia explícita (agregando el `self`), sino te estás refiriendo a 
otra cosa como en el ejemplo anterior.

## Ejercicios

Vamos a comenzar esta serie de ejercicios modificando código que escribiste en secciones anteriores. En particular retomaremos el código del \ref_ref{Arreglemos_las_existentes}. Si no tenés a mano una versión que funcione, podés bajarte y usar [esta](./ejs.zip).


### Ejercicio 8.1: Objetos como estructura de datos.
En las secciones 2 y 3 trabajamos con datos en forma de tuplas y diccionarios. Un cajón de frutas, por ejemplo, estaba representado por una tupla, como esta:

```python
s = ('Pera',100,490.10)
```

ó como un diccionario, de esta otra forma:

```python
s = { 'nombre'  : 'Pera',
      'cajones' : 100,
      'precio'  : 490.10
}
```

Incluso escribimos funciones para manipular datos almacenados de ese modo:

```python
def costo_camion(camion):
    return camion['cajones'] * camion['precio']
```

A medida que tu programa se hace más grande, vas a necesitar (de nuevo) organizarlo mejor.

Otra forma de representar los datos con los que estás trabajando es definir una clase. Creá un archivo llamado `cajon.py`. Definí una clase llamada `Cajon` que represente un único cajón de mercadería. Definila de modo que cada instancia de la clase `cajon` (es decir, cada objeto cajón) tenga las propiedades `nombre`, `cantidad`, y `precio`. Este es un ejemplo del comportamiento buscado:


```python
>>> import cajon
>>> a = cajon.Cajon('Pera',100,490.10)
>>> a.nombre
'Pera'
>>> a.cantidad
100
>>> a.precio
490.1
>>>
```

Vamos a crear más objetos de tipo `Cajon` para manipularlos. Por ejemplo:

```python
>>> b = cajon.Cajon('Manzana', 50, 122.34)
>>> c = cajon.Cajon('Naranja', 75, 91.75)
>>> b.cajones * b.precio
6117.0
>>> c.cajones * c.precio
6881.25
>>> cajones = [a, b, c]
>>> cajones
[<cajon.Cajon object at 0x37d0b0>, <cajon.Cajon object at 0x37d110>, <cajon.Cajon object at 0x37d050>]
>>> for c in cajones:
     print(f'{c.nombre:>10s} {c.cantidad:>10d} {c.precio:>10.2f}')

... mirá el resultado ...
>>>
```

Algo que merece mencionar específicamente es que la clase `Cajon` funciona como una "fábrica" para crear objetos que son instancias de esa clase. Vos la llamás como si fuera una función y ésta crea una nueva instancia de sí misma. Más aún, cada instancia es única y tiene sus propios datos que son independientes de las demás instancias de la misma clase.

Una instancia definida por una clase tiene cierta similitud con un diccionario, pero usa una sintaxis algo diferente. Por ejemplo, en lugar de escribir `c['nombre']` ó `c['precio']` en objetos escribís `c.nombre` ó `c.precio`


### Ejercicio 8.2: Agregá algunos métodos
Al definir una clase podés agregar funciones a los objetos que definís. Las funciones específicas de objetos se llaman *métodos* y operan sobre los datos guardados junto con (dentro de) cada instancia.

Agregá los métodos `costo()` y `vender()` a tu objeto `Cajon`. Deberían dar este comportamiento:

```python
>>> import cajon
>>> s = cajon.Cajon('Pera', 100, 490.10)
>>> s.precio()
49010.0
>>> s.cantidad
100
>>> s.vender(25)
>>> s.cantidad
75
>>> s.precio()
36757.5
>>>
```

### Ejercicio 8.3: Lista de instancias
Seguí estos pasos para crear una lista de las instancias de `Cajon` (una lista de objetos `Cajon`) a partir de una lista de diccionarios. Luego calculá el precio total de todas esas instancias.

```python
>>> import fileparse
>>> with open('Data/camion.csv') as lineas:
...     portdicts = fileparse.parse_csv(lineas, select=['name','cajones','precio'], types=[str,int,float])
...
>>> camion = [ cajon.Cajon(d['nombre'], d['cantidad'], d['precio']) for d in portdicts]
>>> camion
[<cajon.Cajon object at 0x10c9e2128>, <cajon.Cajon object at 0x10c9e2048>, <cajon.Cajon object at 0x10c9e2080>,
 <cajon.Cajon object at 0x10c9e25f8>, <cajon.Cajon object at 0x10c9e2630>, <cajon.Cajon object at 0x10ca6f748>,
 <cajon.Cajon object at 0x10ca6f7b8>]
>>> sum([c.precio() for c in camion])
47671.15
>>>
```

### Ejercicio 8.4: Usá tu clase
Modificá la función `leer_camion()` en el programa `informe.py` de modo que lea un archivo con el contenido de un camion y devuelva una lista de instancias de `Cajon` como mostramos recién en el [Ejercicio 8.3](../08_OOP_RL/03_Clases.md#ejercicio-83-lista-de-instancias).

Cuando hayas hecho éso, cambiá un poco el código en `informe.py` y en  `costo_camion.py` de modo que funcionen con objetos `Cajon` (instancias de la clase `Cajon` en lugar de diccionarios.

Ayuda: No deberían ser cambios importantes, Las referencias a diccionarios ahora tienen que hacer referencia a objetos (`c['cajones']` cambia a `c.cajones`).

Hecho ésto, deberías poder ejecutar tus funciones como antes:

```python
>>> import costo_camion
>>> costo_camion.costo_camion('Data/camion.csv')
47671.15
>>> import informe
>>> informe.informe_camion('Data/camion.csv', 'Data/precios.csv')
      Name     Cajons      Price     Change
---------- ---------- ---------- ----------
      Lima        100       9.22     -22.98
   Naranja         50     106.28      15.18
     Caqui        150      35.46     -47.98
 Mandarina        200      20.89     -30.34
   Durazno         95      13.48     -26.89
 Mandarina         50      20.89     -44.21
   Naranja        100     106.28      35.84
>>>
```


[Contenidos](../Contenidos.md) \| [Anterior (2 Optativo: Regresión Lineal**)](02_OPT_RL.md) \| [Próximo (4 Herencia)](04_Herencia.md)

