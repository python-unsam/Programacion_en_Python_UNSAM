[Contenidos](../Contenidos.md) \| [Anterior (1 Entorno de desarrollo integrado)](01_IDE.md) \| [Próximo (3 Listas y búsqueda lineal)](03_IteradoresLista.md)

# 3.2 Errores

## Tres tipos de errores:

Programando nos podemos encontrar con tres tipos de errores.

Los *errores sintácticos* son los que se dan cuando escribimos incorrectamente. Por ejemplo si queremos escribir `x = (a + b) * c` pero en vez de eso escribimos `x = (a + b] * c`, el programa no va a correr.

Un segundo tipo de error lo forman los errores *en tiempo de ejecución*, que se dan cuando el programa empieza a ejecutarse pero se produce un error durante su ejecución. Por ejemplo si le pedimos al usuarie que ingrese su edad esperando un número entero e ingresa "veintiséis años", es probable que el programa dé un error. Si leemos un archivo CSV y una fila tiene datos faltantes, el programa puede dar un error. Este tipo de errores en Python generan _excepciones_ que, como veremos más adelante, pueden administrarse adecuadamente.

El tercer tipo de error es el más difícil de encontrar y de entender. Son los *errores semánticos*, que se dan cuando el programa no hace lo que está diseñado para hacer. Tienen que ver con el sentido de las instrucciones. En estos casos el programa se ejecuta pero da un resultado incorrecto o inesperado. En general, la mejor forma de encontrar estos errores es correr paso a paso el código que genera un resultado inesperado, tratando de entender dónde está la falla, usando el debugger. Veremos cómo usar el debugger la clase que viene, por ahora trabajaremos de forma un poco más primitiva.

## Debuggear a mano

Los errores (o bugs) son difíciles de rastrear y resolver. Especialmente errores que sólo aparecen bajo cierta combinación particular de condiciones que resulta en que el programa no pueda continuar o dé un resultado inesperado. Si tu programa corre, pero no da el resultado que esperás, o _se cuelga_ y no entendés porqué, tenés algunas herramientas concretas que te ayudan a buscar el origen del problema. A continuación veremos algunas metodologías específicas (aunque un poco primitivas) que permiten rastrear el origen del problema.

### ¿Qué dice un traceback?

Si te da un error, lo primero que podés hacer es intentar entender la causa del error usando como punto de partida el "traceback":

```bash
python3 blah.py
Traceback (most recent call last):
  File "blah.py", line 13, in ?
    foo()
  File "blah.py", line 10, in foo
    bar()
  File "blah.py", line 7, in bar
    spam()
  File "blah.py", line 4, in spam
    x.append(3)
AttributeError: 'int' object has no attribute 'append'
```
La última línea dice algo como que "el objeto `int` no tiene un atributo `append` "- lo cual es obvio, pero ¿cómo llegamos ahí?

La última línea es el motivo concreto del error.

Las líneas anteriores te dicen el camino que siguió el programa hasta llegar al error. En este caso: el error ocurrió en `x.append(3)` en la línea 4, dentro de la función `spam` del módulo `"blah.py"`, que fue llamado por la función `bar` en la línea 7 del mismo archivo, que fue llamada por... y así siguiendo.

Sin embargo a veces esto no proporciona suficiente información (por ejemplo, no sabemos el valor de cada parámetro usado en las llamadas).

Una posibilidad que a veces da resultado es copiar el traceback en Google. Si estás usando una biblioteca de funciones que mucha gente usa (como `numpy` ó `math`) es muy probable que alguien se haya encontrado antes con el mismo problema que vos, y alguien más le haya explicado qué lo causa, o cómo evitarlo.

### Usá el modo [REPL](https://es.wikipedia.org/wiki/REPL) de Python


Si usás Python desde la línea de comandos, podés usarlo pasándole un `-i` como parámetro antes del script a ejecutar. Cuando el intérprete de Python termine de ejecutar el script se va a quedar en modo interactivo (en lugar de volver al sistema operativo). Podés averiguar en qué estado quedó el sistema. 

```bash
python3 -i blah.py
Traceback (most recent call last):
  File "blah.py", line 13, in ?
    foo()
  File "blah.py", line 10, in foo
    bar()
  File "blah.py", line 7, in bar
    spam()
  File "blah.py", line 4, in spam
    x.append(3)
AttributeError: 'int' object has no attribute 'append'
>>>     print( repr(x) )
```

Este *parámetro* (el `-i`, que ya usamos antes) preserva el estado del intérprete al finalizar el script y te permite interrogarlo sobre el estado de las variables y obtener información que de otro modo perderías. En el ejemplo de recién interesa saber qué es `x` y cómo llegó a ese estado. Si estás usando un IDE esta posibilidad de interacción suele ocurrir naturalmente.

### Debuggear con `print`

`print()` es una forma rápida y sencilla de permitir que el programa se ejecute (casi) normalmente mientras te da información del estado de las variables. Si elegís bien las variables que mostrar, es probable que digas "¡¡Ajá!!".

*Sugerencia: es conveniente usar `repr()` para imprimir las variables*

```python
def spam(x):
    print('DEBUG:', repr(x))
    ...
```

`repr()` te muestra una representación técnicamente más precisa del valor de una variable, y no la representación *bonita* que solemos ver.

```python
>>> from decimal import Decimal
>>> x = Decimal('3.4')
# SIN `repr`
>>> print(x)
3.4
# CON `repr`
>>> print(repr(x))
Decimal('3.4')
>>>
```

### Debuggear con lápiz y papel

Muchas veces uno *asume* que el intérprete está haciendo algo. Si agarrás un lápiz y un papel y _hacés de intérprete_ anotando el estado de cada variable y siguiendo las instrucciones del programa paso a paso, es posible que entiendas que las cosas no son como creías.

Estas alternativas son útiles pero un poco primitivas. La mejor forma de debuggear un programa en Python es usar el debugger.


## Ejercicios:

En los siguientes ejercicios te proponemos que uses las técnicas que mencionamos arriba para resolver los problemas que aparecen a continuación.
Determiná los errores de los siguientes códigos y corregilos en un archivo `solucion_de_errores.py` comentando brevemente los errores. ¿Qué tipo de errores tiene cada uno?

En el archivo `solucion_de_errores.py` separá las correcciones de los distintos códigos con una línea que contenga solamente los símbolos `#%%` seguido de una o varias líneas comentadas indicando el ejercicio y el problema que tenía. Al terminar, debería verse así tu archivo:

```python
#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El error era de TAL tipo y estaba ubicado en TAL lugar.
#    Lo corregí cambiando esto por aquello.
#    A continuación va el código corregido
...
...

#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: El error era de TAL tipo y estaba ubicado en TAL lugar.
...
...

#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: El error era de TAL tipo y estaba ubicado en TAL lugar.
...
...
...
```


### Ejercicio 3.1: Semántica
¿Anda bien en todos los casos de prueba?
```python
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            return False
        i += 1

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')
```

### Ejercicio 3.2: Sintaxis
¿Anda bien en todos los casos de prueba?
```python
def tiene_a(expresion)
    n = len(expresion)
    i = 0
    while i<n
        if expresion[i] = 'a'
            return True
        i += 1
    return Falso

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')
```

### Ejercicio 3.3: Tipos
¿Anda bien en todos los casos de prueba?
```python
def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)
```

### Ejercicio 3.4: Alcances
La siguiente suma no da lo que debería:
```python
def suma(a,b):
    c = a + b

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")
```

### Ejercicio 3.5: Pisando memoria
El siguiente ejemplo usa el dataset de la clase anterior, pero no lo imprime como corresponde, ¿podés determinar por qué y explicarlo brevemente en la versión corregida?
```python
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion("Data/camion.csv")
pprint(camion)
```

_Ayuda: Primero tratá de pensarlo, pero si este último se te hace muy difícil, podés mirar un poco de la teoría relacionada con esto un par de secciones más adelante ([Sección 3.5](../03_Listas_y_Listas/05_Objetos.md#ejemplo-de-asignación))._


[Contenidos](../Contenidos.md) \| [Anterior (1 Entorno de desarrollo integrado)](01_IDE.md) \| [Próximo (3 Listas y búsqueda lineal)](03_IteradoresLista.md)

