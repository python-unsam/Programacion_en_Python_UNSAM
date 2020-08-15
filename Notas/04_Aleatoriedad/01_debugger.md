[Contenidos](../Contenidos.md) \| [Anterior (1 Debuggear programas+)](01_Debugger.md) \| [Próximo (3 Random)](02_Random.md)

# 4.2 Debuguear programas+

Python tiene un debiugger que te permite probar porciones de código. Esto es sencillo, especialmente en IDEs como Spyder. 

El siguiente fragmento de código puede parecer -a primera vista- que hace lo esperado. Pero si lo ejecutás vas a ver que no funciona:

```python
def invertir_lista(lista):
    '''Recibe una lista L y la develve invertida.'''
    invertida = []
    i = len(lista)
    while i > 0:    # tomo el último elemento 
        invertida.append(lista.pop(i))  #
        i = i-1
    return invertida
```

`invertir_lista` hace un par de cosas mal. Básicamente no hace lo que debe, y hace lo que no debe.

Se dice que hay un _bug_ (un error) cuando un programa no se comporta como el programador espera o hace algo inesperado. Usualmente se trata de errores semánticos, según la terminología de la [Sección 3.2](../03_Mas_Python/02_Errores3.md#tres-tipos-de-errores).

Un programa debe 
1. hacer lo que debería hacer,
2. no hacer lo que no debería hacer.

Es muy frecuente que los programas tengan bugs. Después de escribir un fragmento de código por primera vez, es conveniente _limpiarlo_ usando tests que permitan poner en evidencia esos bugs.

Diseñar un conjunto de _tests_ adecuado no es una tarea sencilla y es frecuente que queden casos especiales que causen errores inesperados.

## Testear es genial, debuggear es un horrible.

Python es un lenguaje interpretado, con tipos de datos dinámicos (una misma variable puede cambiar de tipo, de `int` a `float`, por ejemplo). No existe un compilador que te alerte sobre inconsistencias de tipos antes de ejecutar el programa. Es bueno tener buenas prácticas que minimicen estos potenciales errores pero es posible que algunos errores se filtren.

Testear consiste en ejecutar un programa o porción de código en condiciones controladas, con entradas conocidas y salidas predichas de forma de poder verificar si lo que da el algoritmos e slo que esperabas.

La ejecución de un algoritmo puede pensarse como un árbol (el árbol de ejecución del algoritmo, cada condicion da una ramificación del árbol). Según la entrada que le des, el programa va a ir por una rama o por otra. Lo ideal es testear todas las ramas posibles de ejecución y que los casos de prueba (_test cases_) incluyan todos los casos _especiales_ (casos como listas vacías, índices apuntando al primer o al último elemento, claves ausentes, etc.) comprobando en cada caso que el programa se comporte según lo esperado.  

![Partes del Spyder, un IDE para Python que facilita el debugging](./spyder-partes.png)


Los entornos de desarrollo integrado (como el Spyder) dan la posiblidad de combinar el uso de un intérprete de Python con un editor de código y suelen permitir también el uso de un debugger. Aún con herramientas como el Spyder, hacer debugging es lento y tedioso. Antes de entrar en los detalles de cómo hacerlo, veremos métodos que tratan de reducir su necesidad.   

### Verificaciones (assert)

El comando `assert` se usa para un control interno del programa. Si la expresión que queremos verificar es `False`, se levanta una excepción de tipo `AssertionError`. La sintaxis de `assert` es la siguiente.

```python
assert <expresion> [, 'Mensaje']
```

Por ejemplo

```python
assert isinstance(10, int), 'Necesito un entero (int)'
```

La idea *no es* usarlo para comprobar la validez de lo ingresado por el usuario. El propósito de usar `assert` es verificar que ciertas condiciones se cumplan. En general se lo usa mientras el programa está en desarrollo, y luego se los quita o desactiva cuando el programa funciona.  

### Programación por contratos

En llama `programación por contratos` a una forma de programar en la que le programadore  define, para cada parte del programa, el tipo y formato de datos con que llamarla y el tipo de datos que devolverá. 

Para asegurarse que los tipos de datos sean los esperados, el uso irrestricto de verificaciones puede ayudar en el diseño de software, y detecta tempranamente un error en los datos pasados a una función evitando que se propague.

Por ejemplo: podrías poner verificaciones para cada parámetro de una función.

```python
def add(x, y):
    assert isinstance(x, int), 'Necesito un entero (int)'
    assert isinstance(y, int), 'Necesito un entero (int)'
    return x + y
```

De este modo, una funcion puede verificar que todos sus argumentos sean válidos.

```python
>>> add(2, 3)
5
>>> add('2', '3')
Traceback (most recent call last):
...
AssertionError: Necesito un entero (int)
>>>
```

## Debuguear 

Los errores en tiempo de ejecución son difíciles de rastrear. Especialmente errores que sólo aparecen bajo cierta combinación particular de condiciones que resulta en que el programa no pueda continuar o de un resultado inesperado. Si tu programa corre, pero no da el resultado que esperás, o _se cuelga_ y no entendés porqué, tenés algunas herramientas concretas. A continuación veremos algunas metodologías específicas que permiten rastrear el orígen del problema.

### **¿Que dice un traceback?**

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
    line x.append(3)
AttributeError: 'int' object has no attribute 'append'
```
La última línea dice algo como que "el objeto `int` no tiene un atributo `append` "- lo cual es obvio, pero ¿cómo llegamos ahí?

La última línea es el motivo concreto del error.

Las líneas anteriores te dicen el camino que siguió el programa hasta llegar al error. En este caso: El error ocurrió en `x.append(3)` en la línea 4, dentro de la función `spam` del módulo `"blah.py"`, que fue llamado por la función `bar` en la línea 7 del mismo archivo, que fué llamada por .... y así siguiendo. 

Sin embargo a veces esto no proporciona suficiente información (por ejemplo, no sabemos el valor de cada parámetro usado en las llamadas.)

*Sugerencia: copiá el traceback en Google.* Si estás usando una biblioteca de funciones que mucha gente usa (como `numpy` ó `math`) es muy probable que alguien se haya encontrado antes con el mismo problema que vos, y sepa qué lo causa, o cómo evitarlo. 

**Usá el modo [REPL](https://es.wikipedia.org/wiki/REPL) de Python**

Si usás Python desde la línea de comandos, podés usarlo pasándoles un `-i` como parámetro antes del script a ejecutar. Cuando el intérprete de Python termine de ejecutar el script se va a quedar en modo interactivo (en lugar de volver al sistema opertaivo. Podés averiguar en qué estado quedó el sistema. 

```bash
python3 -i blah.py
Traceback (most recent call last):
  File "blah.py", line 13, in ?
    foo()
  File "blah.py", line 10, in foo
    bar()
  File "blah.py", line 7, in bar
    spam()
  File "blah.py", 4, in spam
    line x.append(3)
AttributeError: 'int' object has no attribute 'append'
>>>     print( repr(x) )
```

Este *parámetro* (el `-i`, que ya usamos antes) preserva el estado del intérprete al finalizar el script y te permite interrogarlo sobre el estado de las variables y obtener información que de otro modo perderías. En el ejemplo de recién interesa saber que es `x` y como llegó a ese estado. Si estás usando un IDE esta posiblidad de interacción suele ocurrir naturalmente.

### Debugging con `print`

`print()` es una forma rápida y sencilla de permitir que el programa se ejecute (casi) normalmente mientas te da información del estado de las variables. Si elegís bien las variables que mostrár, es probable que digas "¡¡Ajá!!".

*Sugerencia: es conveniente usar `repr()` para imprimir las variables*

```python
def spam(x):
    print('DEBUG:', repr(x))
    ...
```

`repr()` te muestra una representación técnicamente mas precisa del valor de una variable, y no la representación *bonita* que solemos ver.  

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

**Papel y lápiz**

Muchas veces uno *asume* que el intérprete está haciendo algo. Si agarrás un lápiz y un papel y _hacés de intérprete_ anotando el estado de cada variable y siguiendo las instrucciones del programa paso a paso, es posible que entiendas que las cosas no son como creías.

Estas alternativas son útiles pero un poco primitivas. La mejor forma de debuguear un programa en Python es usar el degugger.

### El debugger de Python

Podés iniciar a mano el debugger dentro de un programa en Python, no nos vamos a explayar aquí, pero es posible usarlo manualmente, sin interfaz gráfica, para seguir el funcionamiento de un programa. 

```python
def mi_funcion():
    ...
    breakpoint()      # Iniciar el debugger (Python 3.7+)
    ...
```

La función `breakpoint ()` inicia el debugger. Vas a encontrar [instrucciones detalladas](https://docs.python.org/3/library/pdb.html) sobre como usarlo. 

Aunque esto funciona es mucho mas agradable usar un IDE como Spyder para hacer debugging y ése es el método que describiremos aquí. Fijate los nombres de cada ícono: 
	Debug: 			inicia el modo debug.
	Step:  			da un paso en el programa
	Step Into: 		entra en la función referida
	Step Return: 	ejecuta hasta salir de la función
	Continue: 		retoma la ejecución normal
	Stop: 			detiene el programa.  

![Menu Debug, en Spyder](./debug1.png)

Vamos a usar el siguiente código para que veas la utilidad del debugger:

```python
def tiene_a(palabra):
	n = len(palabra)
	i = 0
	while i < n:
		if palabra[i] == 'a':
			return True
		else:
			return False
		i += 1

print (tiene_a ('palabra'))
```

Una vez que tengas el código, vamos a ejecutarlo en modo Debug:

Primero entramos al modo DEBUG:  (Ctrl+F5) El programa queda pausado antes de comenzar. Notá los cambios en la ventana interactiva.

Si damos un paso en el programa: qué va a ocurrir ? Esta pregunta siembre debe preceder a avanzar. *Es nuestra predicción, contrastada con lo que realmente sucede, lo que delata el error*.

![Menu Debug, en Spyder](./debug2.png)

Queremos ver la solapa Variable Explorer (centro, derecha). Sabemos que el programa está en ejecución pero pausado por el “Stop” rojo de la derecha. Sabemos que estamos en modo DEBUG por el prompt “ipdb” abajo.

![Menu Debug, en Spyder](./debug3.png)

Pedimos algunos Step Into (Ctrl + F11) hasta llegar a la línea 9. Vemos que todas las variable internas de la función están definidas y con sus valores asignados (arriba, derecha).

Como i=0 sabemos que es la primera iteración. Corroboramos que n=7 (“palabra” tiene 7 letras). En este punto se evalúa `if palabra[i] == 'a':`, y saltaremos a alguna de las dos ramas de ejecución según la evaluación resulte True o False.

![Menu Debug, en Spyder](./debug4.png)

La expresión resulta `False`, lo que concuerda con lo esperado porque palabra[0] es “p” lo cual es distinto de 'a'.

La próxima instrucción será RETURN !!! conlo que saldremos de la function y aún no evaluamos mas que la primera posición. Esto es lo que deseamos ?

Para no entrar dentro del `return` que es complicada pedimos un Step (Ctrl + F10 ó F12)

![Menu Debug, en Spyder](./debug5.png)

Acabamos de volver de la function. Las variables internas a la función ya no están visibles (salimos de su "scope"). El programa sigue en ejecución, (flechas).

Salir de la función después de haber analizado solo la primera letra no era lo deseado. Que pasó ? A pensar !

![Menu Debug, en Spyder](./debug6.png)

El programa terminó. Las flechas indican el STOP apagado y el prompt normal. Tenemos control del IDE y la tarea ahora es pensar porqué la función terminó antes de lo deseado.

### Comentario
Recorrer la ejecución de un programa como un simple expectador no te va a ayudar e encontrar el error. Es la incongruencia entre lo predicho y lo que realmente sucede lo que nos abre los ojos. Es una tarea que exije mucha atención, pero bien hecha delata el error en una sóla pasada.

### Ejercicio 4.2: Debugger
Ingresá el siguiente código en el IDE, tal como está. Es el mismo del principio de esta sección. 

```python
def invertir_lista(lista):
	'''Recibe una lista L, develve otra lista invertida(L).'''
    invertida = []
    i=len(lista)
    while i > 0:    # tomo el último elemento 
        invertida.append (lista.pop(i))  #
        i=i-1
    return invertida
```
Ahora usá el debugger para ver cada uno de los errores, y devolver el código corregido. Acordate: Que haga lo que debe y no haga lo que no debe.

Vas a encontrar: problemas con el índice `i` , y problemas con la manipulación de la lista `lista`, que debería quedar intacta.



[Contenidos](../Contenidos.md) \| [Anterior (1 Debuggear programas+)](01_Debugger.md) \| [Próximo (3 Random)](02_Random.md)

