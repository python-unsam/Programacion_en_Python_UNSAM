[Contenidos](../Contenidos.md) \| [Anterior (2 Funciones)](02_Funciones.md) \| [Próximo (4 Búsqueda binaria)](04_BusqBinaria.md)

# 5.3 Módulos

En esta sección vamos a introducir conceptos que nos permiten crear módulos y trabajar con programas cuyas partes están repartidas en múltiples archivos. 

### Módulos y la instrucción `import`

Todos los archivos con código Python son módulos.

```python
# foo.py
def grok(a):
    ...
def spam(b):
    ...
```
El comando `import` carga un módulo y lo *ejecuta*. 

```python
# programa.py
import foo

a = foo.grok(2)
b = foo.spam('Hola')
...
```

### Namespaces

Se puede decir que un módulo es una colección de valores asignados a nombres. A ésto se lo llama un *namespace* (espacio de nombres). Es el contexto en el cual esos nombres existen: todas las variables globales y las funciones definidas en un módulo *pertenecen* a ese módulo. Una vez importado, el nombre del módulo se usa como un prefijo al nombrar esas variables y funciones. Por eso se llama un namespace.


```python
import foo

a = foo.grok(2)
b = foo.spam('Hello')
...
```

El nombre del módulo es el nombre del archivo que lo contiene.

### Definiciones globales

El espacio de nombres contiene todo aquello definido con visibilidad *global*.
Supongamos dos módulos diferentes que definen cada uno una variable `x`:


```python
# foo.py
x = 42
def grok(a):
    ...
```

```python
# bar.py
x = 37
def spam(a):
    ...
```

Entonces hay dos definiciones de `x` y cada una refiere a una variable diferente. Una de ellas es `foo.x` y la otra es `bar.x`. De este modo, diferentes módulos tienen la libertad de definir variables con el mismo nombre sin que existan ambigüedades ni conflictos.

**Los módulos están aislados uno de otro.**

### Módulos como entornos
Los módulos crean un entorno que contiene a todo el código definido ahí.

```python
# foo.py
x = 42

def grok(a):
    print(x)
```

Incluso las variables *globales* son visibles sólo dentro del módulo en que fueron definidas (el mismo archivo).
Cada módulo es un pequeño universo.

### Ejecución de módulos

Cuando importás un módulo se ejecutan *todas* las instrucciones en ese módulo, una tras otra, hasta llegar al final del archivo. 
El *namespace* del módulo está poblado por todas las funciones y variables globales cuya definición siga vigente al terminar de ejecutar el módulo. 
Si existen comandos que se ejecutan en el *namespace* global del módulo y hacen tareas como crear archivos, imprimir mensajes, etc., se van a ejecutar al importar el módulo.

### El comando `import as` 

En el momento de importar un módulo, podés cambiar el nombre que le asignás dentro del contexto en que lo importás. 

```python
import math as m
def rectangular(r, theta):
    x = r * m.cos(theta)
    y = r * m.sin(theta)
    return x, y
```

Funciona del mismo modo que un `import` común salvo que, para quien lo importa, el nombre del módulo cambia.

### `from` módulo `import` nombre

Este comando toma ciertos nombres selectos de un módulo, y los hace accesibles localmente.

```python
from math import sin, cos

def rectangular(r, theta):
    x = r * cos(theta)
    y = r * sin(theta)
    return x, y
```

Esta forma de importar te permite usar partes de un módulo sin necesidad de especificar la pertenencia a un módulo como prefijo. Es útil para nombres (funciones o variables) que se usan mucho.

Si usás `from math import *` vas a importar *todas* las funciones y constantes del módulo `math` como si estuvieran definidas localmente. No es coveniente hacer esto ya que se pierden las ventajas que da trabajar con namespaces.

### Notas sobre `import` 

Estas distintas formas de usar `import` *no modifican* el funcionamiento de un módulo.

```python
import math
# vs
import math as m
# vs
from math import cos, sin
...
```
Más específicamente, `import` siempre ejecuta el módulo completo, y los módulos siguen siendo pequeños entornos aislados.
El comando `import módulo as` sólo cambia el nombre local del módulo.
El comando `from math import cos, sin`, aunque sólo hace accesibles las funciones `sin` y `cos`, de todos modos carga todo el módulo y lo ejecuta. La única diferencia es que copia los nombres de las funciones `sin` y `cos` al namespace local.


### Carga de módulos

Cada módulo es cargado y ejecutado sólo *una* vez.

*Observación: Repetir la instrucción `import` sólo devuelve una referencia al módulo ya cargado.*

La variable `sys.modules` es un diccionario de los módulos cargados. 

```python
>>> import sys
>>> sys.modules.keys()
['copy_reg', '__main__', 'site', '__builtin__', 'encodings', 'encodings.encodings', 'posixpath', ...]
>>>
```
**Precaución:**
Si cambiás el código de un módulo y lo volvés a cargar sucede algo que suele causar confusión hasta que lo entendés: 
Dado que existe la lista de módulos cargados `sys.modules`, un pedido de cargar un módulo por segunda vez siempre devolverá el módulo ya cargado, aún si el módulo fue modificado, si se trata de una versión nueva de ese módulo y si el archivo en disco ha sido modificado. Es posible usar `reload(módulo)` pero sólo en ciertos casos. El método que asegura que el módulo se vuelva a cargar es cerrar y volver a abrir el intérprete de Python. 


## Ejercicios

Para estos ejercicios que involucran módulos, es de suma importancia que te asegures de que estás ejecutando Python en el directorio adecuado.

### Ejercicio 5.7: Importar módulos
En el [Ejercicio 5.3](../05_Organización_y_Complejidad/02_Funciones.md#ejercicio-53-parsear-un-archivo-csv) creamos una función llamada `parse_csv()` para parsear el contenido de archivos de datos en formato CSV. Ahora vamos a ver cómo usar esa función en otros programas. 

Empezá por asegurarte que el directorio de trabajo es `ejercicios_python/` y que en el mismo tengas tus ejercicios anteriores (como `hipoteca.py` y el archivo `fileparse.py` con la función `parse_csv()` que armaste antes). Los vamos a importar.

Con el directorio de trabajo adecuado (puede que tengas que reiniciar tu intérprete para que tome efecto un cambio), intentá importar los programas que escribiste antes. Con sólo importarlos deberías ver su salida exactamente como cuando los terminaste de escribir.

Repetimos: al importar un módulo ejecutás su código.

```python
>>> import rebotes
... mirá la salida ...
>>> import hipoteca
... mirá la salida ...
>>> import informe
... mirá la salida ...
>>>
```

Si nada de esto funciona, es probable que estés ejecutando Python desde la carpeta equivocada.

Ahora probá importar tu módulo `fileparse` y pedile `help`.

```python
>>> import fileparse
>>> help(fileparse)
... mirá la salida ...
>>> dir(fileparse)
... mirá la salida ...
>>>
```

Intentá usar el módulo para leer datos de un archivo:

```python
>>> camion = fileparse.parse_csv('Data/camion.csv',select=['nombre','cajones','precio'], types=[str,int,float])
>>> camion
... mirá la salida ...
>>> lista_precios = fileparse.parse_csv('Data/precios.csv',types=[str,float], has_headers=False)
>>> lista_precios
... mirá la salida ...
>>> precios = dict(lista_precios)
>>> precios
... fijate la salida ...
>>> precios['Naranja']
106.11
>>>
```

Importá sólo la función para evitar escribir el nombre del módulo:

```python
>>> from fileparse import parse_csv
>>> camion = parse_csv('Data/camion.csv', select=['nombre','cajones','precio'], types=[str,int,float])
>>> camion
... fijate la salida ...
>>>
```

### Ejercicio 5.8: Usemos tu módulo
En el [Ejercicio 5.1](../05_Organización_y_Complejidad/01_Scripts.md#ejercicio-51-estructurar-un-programa-como-una-colección-de-funciones)
escribiste un programa `informe_funciones.py` que produce un informe como éste:

```
    Nombre    Cajones     Precio     Cambio
---------- ---------- ---------- ----------
      Lima        100     $32.20       8.02
   Naranja         50     $91.10      15.18
     Caqui        150    $103.44       2.02
 Mandarina        200     $51.23      29.66
   Durazno         95     $40.37      33.11
 Mandarina         50     $65.10      15.79
   Naranja        100     $70.44      35.84
```

Retomá ese programa (si lo perdiste, te dejamos una versión para que la leas y la puedas usar) y modificalo de modo que todo el procesamiento de archivos de entrada de datos se haga usando funciones del módulo `fileparse`. Para lograr éso, importá `fileparse` como un módulo y cambiá las funciones `leer_camion()` y `leer_precios()` para que usen la función `parse_csv()` .

Guiate por el ejemplo interactivo que dimos un poco más arriba.
Al final, deberías obtener exactamente el mismo resultado que al principio.

### Ejercicio 5.9: Un poco más allá
En [Ejercicio 2.5](../02_Datos/02_Funciones.md#ejercicio-25-transformar-un-script-en-una-función) escribiste el programa `costo_camion.py` que lee, mediante una función llamada `costo_camion()` los datos de un camión y calcula su costo.

```python
>>> import costo_camion
>>> costo_camion.costo_camion('Data/camion.csv')
47671.15
>>>
```

Modificá el archivo `costo_camion.py` para que use la función `informe.leer_camion()` del programa `informe_funciones.py`.

### Comentario

Al terminar este ejercicio tenés tres programas.
`fileparse.py` contiene una función para parsear datos de archivos CSV en general, `parse_csv()`. Por otra parte, `informe_funciones.py` que produce un bello informe, y que contiene las funciones `leer_camion()` y `leer_precios()`. Finalmente, `costo_camion.py` calcula el costo de un camión, pero usando la función `leer_camion()` que fue escrita para el programa que genera el informe.


[Contenidos](../Contenidos.md) \| [Anterior (2 Funciones)](02_Funciones.md) \| [Próximo (4 Búsqueda binaria)](04_BusqBinaria.md)

