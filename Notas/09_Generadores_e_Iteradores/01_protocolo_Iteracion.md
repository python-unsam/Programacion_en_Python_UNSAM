[Contenidos](../Contenidos.md) \| [Próximo (2 Iteración a medida)](02_iteracion_a_medida.md)

# 9.1 El protocolo de iteración

En esta sección vemos lo que realmente sucede en Python durante una proceso de iteración.

### Iteraciones por doquier

Podemos iterar sobre una gran diversidad de objetos.

```python
a = 'hola a todes'
for c in a: # Iterar las letras en a 
    ...

b = { 'nombre': 'Elsa', 'password':'foo'}
for k in b: # Iterar para cada clave de diccionario
    ...

c = [1,2,3,4]
for i in c: # Iterar sobre los items en una lista ó tupla
    ...

f = open('foo.txt')
for x in f: # Iterar sobre las líneas de un archivo ASCII
    ...
```

Podemos iterar sobre todos estos objetos porque cumplen con un *protocolo* que permite, justamente, iterar.  Veamos algo sobre este protocolo:

### El protocolo de iteración

Analicemos la instrucción `for`.

```python
for x in obj:
    # instrucciones
```

¿Cómo funciona realmente ésto? Mediante un protocolo de iteración que puede resumirse así:

```python
_iter = obj.__iter__()        # Buscar el objeto iterador
while True:
    try:
        x = _iter.__next__()  # Dame el siguiente item
    except StopIteration:     # No hay más items
        break
    # instrucciones ...
```

Todo objeto compatible con un ciclo `for` implementa, a bajo nivel, este protocolo de iteración.

Un ejemplo: Iteración manual sobre una lista.

```python
>>> x = [1,2,3]
>>> it = x.__iter__()
>>> it
<listiterator object at 0x590b0>
>>> it.__next__()
1
>>> it.__next__()
2
>>> it.__next__()
3
>>> it.__next__()
Traceback (most recent call last):
File "<stdin>", line 1, in ? StopIteration
>>>
```
Fijate que al agotar los elementos, el *traceback* acusa una excepción de tipo *StopIteration*. Fijate también que en la tercera línea, al preguntar por `it`, python responde <es un objeto de tipo listiterator (iterador de listas) alojado en 590b0 hexadecimal> .

### Iterable

Es necesario que entiendas los mecanismos de iteradores si querés permitir iteración sobre objetos que vos definas, es decir, hacerlos *iterables*. El siguiente ejemplo construye un contenedor iterable, simplemente basado en una lista:

```python
class Camion:
    def __init__(self):
        self.lotes = []

    def __iter__(self):
        return self.lotes.__iter__()
    ...

camion = Camion()
for c in camion:
    ...
```

## Ejercicios

### Ejercicio 9.1: Iteradores, un ejemplo
Construí la siguiente lista:

```python
a = [1,9,4,25,16]
```

Y ahora iterá sobre esa lista *a mano*: Llamá al método `__iter__()` para obtener un objeto iterador y llama al método  `__next__()`  para obtener sucesivamente cada uno de los elementos.

```python
>>> i = a.__iter__()
>>> i
<listiterator object at 0x64c10>
>>> i.__next__()
1
>>> i.__next__()
9
>>> i.__next__()
4
>>> i.__next__()
25
>>> i.__next__()
16
>>> i.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
```

La función nativa de Python `next()` es un "atajo" al método `__next__()` de un iterador. Probá usarlo a mano sobre un archivo:

```python
>>> f = open('Data/camion.csv')
>>> f.__iter__()    # Notar que esto apunta al método...
                    # ...que accede al archivo mismo.
<_io.TextIOWrapper name='Data/portfolio.csv' mode='r' encoding='UTF-8'>
>>> next(f)
'nombre,cajones,precio\n'
>>> next(f)
'Lima,100,32.20\n'
>>> next(f)
'Naranja,50,91.10\n'
>>>
```

Llamá a `next(f)` hasta que llegues al final del archivo, y fijate qué sucede.

### Ejercicio 9.2: Iteración sobre objetos
Como decíamos en la sección [Sección 9.1](../09_Generadores_e_Iteradores/01_protocolo_Iteracion.md#iterable), cuando definas tus propios objetos, es posible que quieras que se pueda iterar sobre ellos (especialmente si estos objetos son "envoltorios" (wrappers) para listas u otros iterables). Hagamos esto: en un nuevo archivo llamado `camion.py`, definí la siguiente clase:

```python
# camion.py

class Camion:

    def __init__(self, lotes):
        self._lotes = lotes

    def precio_total(self):
        return sum([l.costo() for l in self._lotes])

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self._lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total
```

La intención es crear un envoltorio para una lista, y de paso agregarle algunos métodos, como la propiedad de calcular el costo total del camión. Vamos a usar lo que hiciste en el [Ejercicio 8.1](../08_Clases_y_Objetos/01_Clases.md#ejercicio-81-objetos-como-estructura-de-datos). Modificá la función `leer_camion()` en `informe.py` de modo que cree una instancia de `Camion`, como se muestra:


```python
# informe.py
...

import fileparse
from lote import Lote
from camion import Camion

def leer_camion(filename):
    '''
    Lee un archivo con el contenido de un camión 
    y lo devuelve como un objeto Camion.
    '''
    with open(filename) as file:
        camiondicts = fileparse.parse_csv(file,
                                        select=['nombre','cajones','precio'],
                                        types=[str,int,float])

    camion = [ Lote(d['nombre'], d['cajones'], d['precio']) for d in camiondicts ]
    return Camion(camion)
...
```

Ahora intentá correr el programa `informe.py`. No hay forma. `informe.py` intenta iterar sobre las instancias de `Camion` pero éstas no son iterables y el programa no funciona.

```python
>>> import informe
>>> informe.informe_camion('Data/camion.csv', 'Data/precios.csv')
... muere ...
```

La forma de arreglar este programa roto es modificar la clase `Camion` y hacerla iterable.

```python
class Camion:

    def __init__(self, lotes):
        self._lotes = lotes

    def __iter__(self):
        return self._lotes.__iter__()

    def precio_total(self):
        return sum([l.costo() for l in self._lotes])

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for lote in self._lotes:
            cantidad_total[lote.nombre] += lote.cajones
        return cantidad_total
```

Después de haber hecho este cambio, tu `informe.py` debería estar funcionando de nuevo. Guardá esta versión de `informe.py` para entregar al final de la clase (en el próximo ejercicio te pediremos también `camion.py`).

Y ya que estás, cambiá el programa `costo_camion.py` para que use objetos que sean instancias de la clase  `Camion`, por ejemplo así:

```python
# costo_camion.py

import informe

def costo_camion(filename):
    '''
    Computa el precio total (cantidad * precio) de un archivo camion
    '''
    camion = informe.leer_camion(filename)
    return camion.precio_total()
...
```

Testealo, testealo, y testealo para asegurarte que funciona:

```python
>>> import costo_camion
>>> costo_camion.costo_camion('Data/camion.csv')
47671.15
>>>
```

### Ejercicio 9.3: Un iterador adecuado
Cuando hagas clases que sean recipientes ó contenedores de estructuras de datos vas a necesitar que hagan algo más que simplemente iterar. Probá modificar la clase `Camion` de modo que tenga algunos de los "métodos mágicos" que mencionamos en la [Sección 8.3](../08_Clases_y_Objetos/03_Métodos_Especiales.md#métodos-especiales-para-convertir-a-strings). Aquí hay algunos:

```python
class Camion:
    def __init__(self, lotes):
        self._lotes = lotes

    def __iter__(self):
        return self._lotes.__iter__()

    def __len__(self):
        return len(self._lotes)

    def __getitem__(self, index):
        return self._lotes[index]

    def __contains__(self, nombre):
        return any([lote.nombre == nombre for lote in self._lotes])

    def precio_total(self):
        return sum([l.costo() for l in self._lotes])

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self._lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total
```

Por último, probemos esta nueva estructura:

```python
>>> import informe
>>> camion = informe.leer_camion('Data/camion.csv')
>>> len(camion)
7
>>> camion[0]
Lote('Lima', 100, 32.2)
>>> camion[1]
Lote('Naranja', 50, 91.1)
>>> camion[0:3]
[Lote('Lima', 100, 32.2), Lote('Naranja', 50, 91.1), Lote('Caqui', 150, 83.44)]
>>> 'Naranja' in camion
True
>>> 'Manzana' in camion
False
>>>
```

Guardá tu versión de `camion.py` con estos cambios para entregar y para la revisión de pares.

**Un comentario importante sobre todo esto:** 
Se considera *de buen estilo Python* al código que comparte ciertas normas de interacción con el resto del mundo Python. Este concepto aplicado a objetos contenedores significa que estos cumplen con las buenas costumbres de ser iterables, indexables y que admiten otras operaciones que naturalmente se esperan *a priori* que vayan a cumplir, justamente por el simple hecho de ser objetos contenedores.


[Contenidos](../Contenidos.md) \| [Próximo (2 Iteración a medida)](02_iteracion_a_medida.md)

