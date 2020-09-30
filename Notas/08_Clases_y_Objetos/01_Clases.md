[Contenidos](../Contenidos.md) \| [Próximo (2 Herencia)](02_Herencia.md)

# 8.1 Clases

La programación orientada a objetos requiere un pequeño pero importante cambio en la forma de pensar la programación tradicional. Dejá decantar los conceptos nuevos mientras leés esta sección.

En esta sección veremos el concepto de clase, cómo crear nuevos tipos de objetos, su utilidad, y las ventajas de esa forma de organizar los programas.

### Programación orientada a objetos (POO)

La programación orientada a objetos es una forma de organizar el código. Así como un algoritmo suele estar asociado a una estructura de datos particular, la programación orientada a objetos "empaqueta" los datos junto con los métodos usados para tratarlos. 

Cada uno de esos *objetos* consiste en 

* Datos (atributos de los objetos).
* Comportamiento (métodos de los objetos: son funciones que actúan sobre los atributos del objeto).

Ya usaste objetos durante el curso infinidad de veces. Por ejemplo, al manipular una lista.

```python
>>> nums = [1, 2, 3]
>>> nums.append(4)      # Esto es un método de la lista
>>> nums.insert(1,10)   # Otro método
>>> nums
[1, 10, 2, 3, 4]        # Estos son los datos modificados por los métodos
>>>
```

Miremos un poco más en detalle este fragmento de código. Sabemos que `nums` es una variable de tipo lista. Equivalentemente, podemos decir que `nums` es una *instancia* de la clase *list*. Cada variable de tipo lista es una instancia de la misma clase.
Al hablar de 'instancia' nos referimos a un 'objeto': un objeto es una instancia de una clase.

Un objeto de tipo lista tiene atributos (datos) y métodos.
Los métodos, como `append()` o `insert()`, se definen cuando se define la clase, pero se usan para manipular los datos de un objeto concreto (`nums` en este caso).

### La instrucción `class`

Para definir un tipo nuevo de objeto, usá la instrucción `class`.

```python
class Jugador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.salud = 100

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

    def lastimar(self, pts):
        self.salud -= pts
```

Un objeto de tipo `Jugador` tiene como atributos `x`, `y` y `salud`. Sus métodos son `mover()` y `lastimar()`.

Puede decirse que una clase es la definición formal de las relaciones entre los datos y los métodos que los manipulan. Un objeto es una instancia particular de la clase a la cual pertenece, con datos propios pero los mismos métodos que los demás objetos de esa clase. Este concepto te va a quedar más claro cuando lo veas funcionar y lo uses.

### Instancias

Los programas manipulan instancias individuales de las clases. Cada instancia es un objeto, y es en cada objeto que uno puede manipular los datos y llamar a sus métodos. 

Podés crear un objeto mediante un llamado a la clase como si fuera una función.

```python
>>> a = Jugador(2, 3)    # Clase Jugador definida antes
>>> b = Jugador(10, 20)
>>>
```

`a` y `b` son instancias de `Jugador` definida más arriba. Es decir, a y b son objetos de la clase `Jugador`.

*Importante: La instrucción `class` es solamente la definición de una clase, no **hace** nada por sí misma. Es similar a la definición de una función.*

### Datos de una instancia

Cada instancia tiene sus propios datos locales. 
Acá pedimos ver el atributo `x` de cada instancia:

```python
>>> a.x
2
>>> b.x
10
```

Estos datos locales se inicializan, para cada instancia, durante la ejecución del método `__init__()` de la clase.

```python
class Jugador:
    def __init__(self, x, y):
        # Todo dato guardado en `self` es propio de esa instancia
        self.x = x
        self.y = y
        self.salud = 100
```

No hay restricciones en la cantidad o el tipo de atributos que puede tener una clase.

### Métodos de una instancia.

Los métodos de una instancia son los métodos y las funciones que actúan sobre los datos almacenados en esa instancia. 

```python
class Jugador:
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
def mover(self, dx, dy):
    ...
```

Por convención siempre llamamos `self` a la instancia actual, y ésta es siempre pasada como primer argumento a todos los métodos. En realidad el nombre real de la variable no importa, pero es una convención en Python llamar al primer argumento `self`. 

Podríamos usar `mismo`, por ejemplo, en lugar de `self` y todo va a funcionar igual, pero no respeta las convenciones de la comunidad:

```python
class Jugador:
    ...
    # `mover` es un método
    def mover(mismo, dx, dy):
        mismo.x += dx
        mismo.y += dy
```


### Visibilidad en clases (Scoping)

Las clases no definen ni limitan (como los módulos) un entorno de visibilidad.

```python
class Jugador:
    ...
    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

    def izquierda(self, dist):
        mover(-dist, 0)      # NO! Refiere a una función global `mover`.
        self.mover(-dist, 0) # Sí. Llama al método `mover` definido antes.
```

Si necesitás referirte a un dato o un método de una clase tenés que hacer una referencia explícita (agregando el `self`), sino te estás refiriendo a 
otra cosa como en el ejemplo anterior.

## Ejercicios

Vamos a comenzar esta serie de ejercicios modificando código que escribiste antes del parcial. En particular retomaremos el código del [Ejercicio 6.5](../06_Plt_Especificacion_y_Documentacion/03_Flexibilidad.md#ejercicio-65-arreglemos-las-funciones-existentes). Te dejamos [acá](./ejs.zip) una versión funcionando que podés mirar y/o usar. Tiene cosas interesantes, aunque tengas la tuya funcionando si querés pegale una mirada. 


### Ejercicio 8.1: Objetos como estructura de datos.
Durante las primeras clases trabajamos con datos en forma de tuplas y diccionarios. Un lote con cajones de frutas, por ejemplo, estaba representado por una tupla, como ésta:

```python
s = ('Pera', 100, 490.10)
```

o por un diccionario, de esta otra forma:

```python
s = { 'nombre'  : 'Pera',
      'cajones' : 100,
      'precio'  : 490.10
}
```

Incluso escribiste funciones para manipular datos almacenados de ese modo:

```python
def costo(registro):
    return registro['cajones'] * registro['precio']
```

Otra forma de representar los datos con los que estás trabajando es definir una clase. Creá un archivo llamado `lote.py` y adentro definí una clase llamada `Lote` que represente un lote de cajones de una misma fruta. Definila de modo que cada instancia de la clase `Lote` (es decir, cada objeto lote) tenga los atributos `nombre`, `cajones`, y `precio`. Éste es un ejemplo del comportamiento buscado:


```python
>>> import lote
>>> a = lote.Lote('Pera', 100, 490.10)
>>> a.nombre
'Pera'
>>> a.cajones
100
>>> a.precio
490.1
>>>
```

Vamos a crear más objetos de tipo `Lote` para manipularlos. Por ejemplo:

```python
>>> b = lote.Lote('Manzana', 50, 122.34)
>>> c = lote.Lote('Naranja', 75, 91.75)
>>> b.cajones * b.precio
6117.0
>>> c.cajones * c.precio
6881.25
>>> lotes = [a, b, c]
>>> lotes
[<lote.Lote object at 0x37d0b0>, <lote.Lote object at 0x37d110>, <lote.Lote object at 0x37d050>]
>>> for c in lotes:
     print(f'{c.nombre:>10s} {c.cajones:>10d} {c.precio:>10.2f}')

... mirá el resultado ...
>>>
```

Fijate que la clase `Lote` funciona como una "fábrica" para crear objetos que son instancias de esa clase. Vos la llamás como si fuera una función y te crea una nueva instancia de sí misma. Más aún, cada instancia es única y tiene sus propios datos que son independientes de las demás instancias de la misma clase.

Una instancia definida por una clase puede tener cierta similitud con un diccionario, pero usa una sintaxis algo diferente. Por ejemplo, en lugar de escribir `c['nombre']` ó `c['precio']` en objetos escribís `c.nombre` o `c.precio`.


### Ejercicio 8.2: Agregá algunos métodos
Al definir una clase podés agregar funciones a los objetos que definís. Las funciones específicas de objetos se llaman *métodos* y operan sobre los datos guardados en cada instancia.

Agregá los métodos `costo()` y `vender()` a tu objeto `Lote`. Deberían dar este comportamiento:

```python
>>> import lote
>>> s = lote.Lote('Pera', 100, 490.10)
>>> s.costo()
49010.0
>>> s.cajones
100
>>> s.vender(25)
>>> s.cajones
75
>>> s.costo()
36757.5
>>>
```

### Ejercicio 8.3: Lista de instancias
Seguí estos pasos para crear una lista de las instancias de `Lote` (una lista de objetos `Lote`) a partir de una lista de diccionarios. Luego calculá el precio total de todas esas instancias.

```python
>>> import fileparse
>>> with open('Data/camion.csv') as lineas:
...     camion_dicts = fileparse.parse_csv(lineas, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
...
>>> camion = [ lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
>>> camion
[<lote.Lote object at 0x10c9e2128>, <lote.Lote object at 0x10c9e2048>, <lote.Lote object at 0x10c9e2080>,
 <lote.Lote object at 0x10c9e25f8>, <lote.Lote object at 0x10c9e2630>, <lote.Lote object at 0x10ca6f748>,
 <lote.Lote object at 0x10ca6f7b8>]
>>> sum([c.costo() for c in camion])
47671.15
>>>
```

### Ejercicio 8.4: Usá tu clase
Modificá la función `leer_camion()` en el programa `informe.py` de modo que lea un archivo con el contenido de un camion y devuelva una lista de instancias de `Lote` como mostramos recién en el [Ejercicio 8.3](../08_Clases_y_Objetos/01_Clases.md#ejercicio-83-lista-de-instancias).

Cuando hayas hecho esto, cambiá un poco el código en `informe.py` y en  `costo_camion.py` de modo que funcionen con objetos `Lote` (instancias de la clase `Lote`) en lugar de diccionarios.

Ayuda: No deberían ser cambios importantes. Las referencias a diccionarios ahora tienen que hacer referencia a objetos (`c['cajones']` cambia a `c.cajones`).

Hecho esto, deberías poder ejecutar tus funciones como antes:

```python
>>> import costo_camion
>>> costo_camion.costo_camion('Data/camion.csv')
47671.15
>>> import informe
>>> informe.informe_camion('Data/camion.csv', 'Data/precios.csv')
   Nombre    Cajones     Precio     Cambio
 ---------- ---------- ---------- ----------
      Lima        100      $32.2       8.02
   Naranja         50      $91.1      15.18
     Caqui        150    $103.44       2.02
 Mandarina        200     $51.23      29.66
   Durazno         95     $40.37      33.11
 Mandarina         50      $65.1      15.79
   Naranja        100     $70.44      35.84
```


[Contenidos](../Contenidos.md) \| [Próximo (2 Herencia)](02_Herencia.md)

