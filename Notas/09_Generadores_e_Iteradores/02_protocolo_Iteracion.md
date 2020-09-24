[Contenidos](../Contenidos.md) \| [Próximo (2 [Contents](../Contents.md) \| [Previous (6.1 Iteration Protocol)](01_Iteration_protocol.md) \| [Next (6.3 Producer/Consumer)](03_Producers_consumers.md))](03_iteracion_a_medida.md)

# 9.1 [Contents](../Contents.md) \| [Previous (5.2 Encapsulation)](../05_Object_model/02_Classes_encapsulation.md) \| [Next (6.2 Customizing Iteration)](02_Customizing_iteration.md)

# 6.1 El protocolo de iteración

En esta sección vemos lo que realmente sucede durante el proceso de iteración

### Iteration Everywhere

Podemos iterar sobre una gran diversidad de objetos.

```python
a = 'hola a todes'
for c in a: # Iterar las letras en a 
    ...

b = { 'nombre': 'Rafa', 'password':'foo'}
for k in b: # Iterar para cada clave de diccionario
    ...

c = [1,2,3,4]
for i in c: # Iterar sobre los items en una lista ó tupla
    ...

f = open('foo.txt')
for x in f: # Iterar sobre las líneas de un archivo ASCII
    ...
```

Y podemos hacer éso porque existe un protocolo que todo objeto que permita iterar sobre él debe cumplir. 

### El protocolo de iteración

Tomemos la instrucción `for` para analizar

```python
for x in obj:
    # instrucciones
```

Cómo funciona realmente ésto ?

```python
_iter = obj.__iter__()        # Buscar el objeto iterador
while True:
    try:
        x = _iter.__next__()  # Dame el siguiente item
    except StopIteration:     # No hay mas items
        break
    # instrucciones ...
```

Todo objeto compatible con un ciclo `for` implementa, a bajo nivel, este protocolo de iteración.

Un ejemplo: Iteracióin manual sobre una lista.

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
Donde el *traceback* acusa una excepción de tipo *StopIteration* en la línea de comandos (stdin). Además notá que en la tercera línea, al preguntar por `it` python responde <es un objeto de tipo listiterator (iterador de listas) alojado en 590b0 hexadecimal> .

### Compatible con iteración

Es necesario entender un poco sobre los mecanismos de iteradores si querés permitir iteración sobre objetos que vos definas. Un ejemplo: construyamos un contenedor:

```python
class Camion:
    def __init__(self):
        self.lotes = []

    def __iter__(self):
        return self.lotes.__iter__()
    ...

cam = Camion()
for c in cam:
    ...
```

## Exercises
\Label_secc{Ejercicios_Iteradores}

### Ejercicio 9.1: Iteration Illustrated\Label_ej{Iteradores_demostracion}

Construí la siguiente lista:

```python
a = [1,9,4,25,16]
```

Ahora iterá sobre esa lista *a mano*: Llamá al método `__iter__()` para obtener un objeto iterador y llama al método  `__next__()`  para obtener sucesivamente cada uno de los elementos.

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

La función nativa `next()` es un "atajo" al método `__next__()` de un iterador. Probá de usarlo a mano sobre un archivo:

```python
>>> f = open('Data/portfolio.csv')
>>> f.__iter__()    # Notar que esto apunta al método...
                    # ...que accede al archivo mismo.
<_io.TextIOWrapper name='Data/portfolio.csv' mode='r' encoding='UTF-8'>
>>> next(f)
'nombre,cantidad,precio\n'
>>> next(f)
'"Lima",100,32.20\n'
>>> next(f)
'"Naranja",50,91.10\n'
>>>
```

Llamá a `next(f)` hasta que llegues al final del archivo, y fijate qué sucede.

### Ejercicio 9.2: Supporting Iteration\Label_ej{Compatible con iteración}

[oski] : # (Ojo que esto lleva el mismo nombre que una seccion mas arriba, en el original está así y lo mantuve. Espero que el compilador de Rafa no se maree)


[oski]: # (Dudo si no llamar a esto camion_iterable.py para que no se confundan con otros archivos [versiones anteriores])

```python
# camion.py

class Camion:

    def __init__(self, lotes):
        self._lotes = lotes

    @property
    def total_cost(self):
        return sum([l.costo for l in self._lotes])

    def tabulate_shares(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self._lotes:
            cantidad_total[l.nombre] += l.cantidad
        return cantidad_total
```

La intención es crear un envoltorio para una lista, y de paso agregarle algunos métodos, como (en este ejemplo) la propiedad de calcular el costo total del camión. Modificá la función leer_camion() en `informe.py` de modo que cree una instancia de `Camion`, como se muestra:


[oski]: # (from cajones import cajon ?? quiero chequear ...)
```python
# report.py
...

import fileparse
from stock import Stock
from portfolio import Portfolio

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as file:
        portdicts = fileparse.parse_csv(file,
                                        select=['name','shares','price'],
                                        types=[str,int,float])

    portfolio = [ Stock(d['name'], d['shares'], d['price']) for d in portdicts ]
    return Portfolio(portfolio)
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

    def __init__(self, holdings):
        self._lotes = _lotes

    def __iter__(self):
        return self._lotes.__iter__()

    @property
    #def precio_total(self):
    def total_cost(self):
        return sum([lote.cantidad*lote.precio for lote in self._lotes])

    def tabulate_shares(self):
        from collections import Counter
        cantidad_total = Counter()
        for lote in self._lotes:
            cantidad_total[lote.name] += lote.cantidad
        return cantidad_total
```

Después de haber hecho este cambio tu `informe.py` debería estar funcionando de nuevo. Ya que estás en éso, cambiá también el programa `costo_camion.py` para que use objetos que sean instancias de la clase  `Camion`, por ejemplo así:

```python
# costo_camion.py

import informe

def costo_camion(filename):
    '''
    Computa el precio total (cantidad * precio) de un archivo camion
    '''
    camion = informe.leer_camion(filename)
    return camion.precio_total
...
```

Testealo, testealo, y testealo para asegurarte que funciona:

```python
>>> import costo_camion
>>> costo_camion.costo_camion('Data/camion.csv')
47671.15
>>>
```

### Ejercicio 9.3: Un recipiente adecuado

```python
class Portfolio:
    def __init__(self, holdings):
        self._lotes = lotes

    def __iter__(self):
        return self._lotes.__iter__()

    def __len__(self):
        return len(self._lotes)

    def __getitem__(self, index):
        return self._lotes[index]

    def __contains__(self, name):
        return any([lote.nombre == nombre for lote in self._lotes])

    @property
    def total_cost(self):
        return sum([lote.cantidad*lote.precio for lote in self._lotes])

    def tabulate_shares(self):
        from collections import Counter
        cantidad_total = Counter()
        for lote in self._lotes:
            cantidad_total[lote.name] += lote.cantidad
        return cantidad_total
```

Por último, probemos esta nueva estructura:

```python
>>> import informe
>>> camion = informe.leer_camion('Data/camion.csv')
>>> len(camion)
7
>>> camion[0]
Cajon('Lima', 100, 32.2)
>>> camion[1]
Cajon('Naranja', 50, 91.1)
>>> camion[0:3]
[Cajon('Lima', 100, 32.2), Cajon('Naranja', 50, 91.1), Cajon('Caqui', 150, 83.44)]
>>> 'Naranja' in camion
True
>>> 'Manzana' in camion
False
>>>
```

Un comentario importante sobre todo esto: 
Se considera "Pythonico" (buen estilo Python) al código que comparte ciertas normas de interacción con el resto del mundo Python. Este concepto aplicado a objetos contenedores significa que éstos cumplen con las buenas costumbres de ser iterables, indexables (indizables ??) y que admiten otras operaciones que naturalmente se espera *a priori* que vayan a cumplir - justamente por el simple hecho de ser objetos contenedores.


[Contents](../Contents.md) \| [Previous (5.2 Encapsulation)](../05_Object_model/02_Classes_encapsulation.md) \| [Next (6.2 Customizing Iteration)](02_Customizing_iteration.md)

[Contenidos](../Contenidos.md) \| [Próximo (2 [Contents](../Contents.md) \| [Previous (6.1 Iteration Protocol)](01_Iteration_protocol.md) \| [Next (6.3 Producer/Consumer)](03_Producers_consumers.md))](03_iteracion_a_medida.md)

