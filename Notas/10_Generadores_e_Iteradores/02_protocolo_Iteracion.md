# 10.2 El protocolo de iteración

En esta sección vemos lo que realmente sucede en Python durante una proceso de iteración. Esta sección tiene un [video](https://youtu.be/WyNiWuCnrhc) introductorio.

### Iteraciones por doquier

Podemos iterar sobre una gran diversidad de objetos.

```python
a = 'hola a todes'
for c in a: # Iterar sobre las letras en a
    ...

b = {'nombre': 'Elsa', 'password':'foo'}
for k in b: # Iterar sobre las claves de diccionario
    ...

c = [1, 2, 3, 4]
for i in c: # Iterar sobre los items en una lista o tupla
    ...

f = open('foo.txt')
for x in f: # Iterar sobre las líneas de un archivo ASCII
    ...
```

Podemos iterar sobre todos estos objetos porque cumplen con un *protocolo* que permite, justamente, iterar. Veamos algo sobre este protocolo:

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

### Ejercicio 10.1: Iteradores, un ejemplo
Construí la siguiente lista:

```python
a = [1, 9, 4, 25, 16]
```

Y ahora iterá sobre esa lista *a mano*: Llamá al método `__iter__()` para obtener un objeto iterador y llama al método  `__next__()` para obtener sucesivamente cada uno de los elementos.

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
>>> f = open('../Data/camion.csv')
>>> f.__iter__()    # Notar que esto apunta al método...
                    # ...que accede al archivo mismo.
<_io.TextIOWrapper name='../Data/camion.csv' mode='r' encoding='UTF-8'>
>>> next(f)
'nombre,cajones,precio\n'
>>> next(f)
'Lima,100,32.20\n'
>>> next(f)
'Naranja,50,91.10\n'
>>>
```

Llamá a `next(f)` hasta que llegues al final del archivo, y fijate qué sucede.

### Ejercicio 10.2: Iteración sobre objetos
Como decíamos, cuando definas tus propios objetos, es posible que quieras que se pueda iterar sobre ellos (especialmente si estos objetos son "envoltorios" (wrappers) para listas u otros iterables). Hagamos esto: en un nuevo archivo llamado `camion.py`, definí la siguiente clase:

```python
# camion.py

class Camion:

    def __init__(self, lotes):
        self.lotes = lotes

    def precio_total(self):
        return sum([l.costo() for l in self.lotes])

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total
```

La intención es crear un envoltorio para una lista, y de paso agregarle algunos métodos, como la propiedad de calcular el costo total del camión. Copiá los archivos `fileparse.py`, `formato_tabla.py`, `informe_final.py` y `lote.py` a la carpeta de ejercicios de la clase actual. Ahora, modificá la función `leer_camion()` en `informe_final.py` de modo que cree una instancia de `Camion`, como se muestra:


```python
# informe_final.py
...

from camion import Camion
...

def leer_camion(filename):
    '''
    Lee un archivo con el contenido de un camión
    y lo devuelve como un objeto Camion.
    '''
    with open(filename) as file:
        camiondicts = fileparse.parse_csv(file,
                                        select = ['nombre', 'cajones', 'precio'],
                                        types = [str, int, float])

    camion = [Lote(d['nombre'], d['cajones'], d['precio']) for d in camiondicts]
    return Camion(camion)
...
```

Ahora intentá correr el programa `informe_final.py`. No hay forma. `informe_final.py` intenta iterar sobre las instancias de `Camion` pero éstas no son iterables y el programa no funciona.

```python
>>> import informe_final
>>> informe_final.informe_camion('../Data/camion.csv', '../Data/precios.csv')
... muere ...
```

La forma de arreglar este programa roto es modificar la clase `Camion` y hacerla iterable.

```python
class Camion:

    def __init__(self, lotes):
        self.lotes = lotes

    def __iter__(self):
        return self.lotes.__iter__()

    def precio_total(self):
        return sum([l.costo() for l in self.lotes])

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for lote in self.lotes:
            cantidad_total[lote.nombre] += lote.cajones
        return cantidad_total
```

Después de haber hecho este cambio, tu `informe_final.py` debería estar funcionando de nuevo. Guardá esta versión de `informe_final.py` para entregar al final de la clase (en el próximo ejercicio te pediremos también `camion.py`).

Y ya que estás, copiá el programa `costo_camion.py` a la carpeta de ejercicios de la clase actual y cambialo para que use objetos que sean instancias de la clase `Camion`, por ejemplo así:

```python
# costo_camion.py

import informe_final

def costo_camion(filename):
    '''
    Computa el precio total (cantidad * precio) de un archivo camion
    '''
    camion = informe_final.leer_camion(filename)
    return camion.precio_total()
...
```

Testealo, testealo, y testealo para asegurarte que funciona:

```python
>>> import costo_camion
>>> costo_camion.costo_camion('../Data/camion.csv')
47671.15
>>>
```

### Ejercicio 10.3: Un iterador adecuado
Cuando hagas clases que sean recipientes o contenedores de estructuras de datos vas a necesitar que hagan algo más que simplemente iterar. Probá modificar la clase `Camion` de modo que tenga algunos de los "métodos mágicos" que mencionamos en la [Sección 9.4](../09_Clases_y_Objetos/04_Métodos_Especiales.md#métodos-especiales-para-convertir-a-strings). Aquí hay algunos:

```python
class Camion:
    def __init__(self, lotes):
        self.lotes = lotes

    def __iter__(self):
        return self.lotes.__iter__()

    def __contains__(self, nombre):
        return any([lote.nombre == nombre for lote in self.lotes])

    def precio_total(self):
        return sum([l.costo() for l in self.lotes])

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total
```

Ahora probá esta nueva estructura:

```python
>>> import informe_final
>>> camion = informe_final.leer_camion('../Data/camion.csv')
>>> 'Naranja' in camion
True
>>> 'Manzana' in camion
False
>>>
```

Agregá más métodos especiales (`__len__` y `__getitem__`) para que tu clase se comporte de la siguiente manera:


```python
>>> import informe_final
>>> camion = informe_final.leer_camion('../Data/camion.csv')
>>> len(camion)
7
>>> camion[0]
Lote('Lima', 100, 32.2)
>>> camion[1]
Lote('Naranja', 50, 91.1)
>>> camion[0:3]
[Lote('Lima', 100, 32.2),
 Lote('Naranja', 50, 91.1),
 Lote('Caqui', 150, 103.44)]
```

Por último, agregale a la clase camión métodos `__repr__` y `__str__` para que muestre los camiones de esta manera. Es probable que debas modificar también la clase Lote de `lote.py` para lograrlo.


```python
>>> import informe_final
>>> camion = informe_final.leer_camion('../Data/camion.csv')
>>> camion
Camion([Lote('Lima', 100, 32.2), Lote('Naranja', 50, 91.1), Lote('Caqui', 150, 103.44), Lote('Mandarina', 200, 51.23), Lote('Durazno', 95, 40.37), Lote('Mandarina', 50, 65.1), Lote('Naranja', 100, 70.44)])
>>> print(camion)
Camion con 7 lotes:
Lote de 100 cajones de 'Lima', pagados a $32.2 cada uno.
Lote de 50 cajones de 'Naranja', pagados a $91.1 cada uno.
Lote de 150 cajones de 'Caqui', pagados a $103.44 cada uno.
Lote de 200 cajones de 'Mandarina', pagados a $51.23 cada uno.
Lote de 95 cajones de 'Durazno', pagados a $40.37 cada uno.
Lote de 50 cajones de 'Mandarina', pagados a $65.1 cada uno.
Lote de 100 cajones de 'Naranja', pagados a $70.44 cada uno.
```

Guardá tu versión de `camion.py` con estos cambios para entregar y para la revisión de pares.

**Un comentario importante sobre todo esto:**
Se considera *de buen estilo Python* al código que comparte ciertas normas de interacción con el resto del mundo Python. Este concepto aplicado a objetos contenedores significa que éstos cumplen con las buenas costumbres de ser iterables, indexables y que admiten otras operaciones que naturalmente se espera *a priori* que vayan a cumplir, justamente por el simple hecho de ser objetos contenedores.


