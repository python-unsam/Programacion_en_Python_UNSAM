[Contenidos](../Contenidos.md) \| [Anterior (1 Manejo de archivos)](01_Archivos.md) \| [Próximo (3 Tipos y estructuras de datos)](03_TiposDatos.md)

# 2.2 Funciones

A medida que tus programas se vuelven más largos y complejos, vas a necesitar organizarte. En esta sección vamos a introducir brevemente funciones y módulos de la biblioteca así como también la administración de errores y excepciones.

### Funciones a medida

Usá funciones para encapsular código que quieras reutilizar. El siguiente ejemplo muestra una definición de una función:

```python
def sumcount(n):
    '''
    Devuelve la suma de los primeros n enteros
    '''
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total
```

Para llamar a una función:

```python
a = sumcount(100)
```

Una función es una serie de instrucciones que realiza una tarea y devuelve un resultado. La palabra  `return` es necesaria para explicitar el valor de retorno de la función.

### Funciones de la biblioteca

Python trae una gran biblioteca estándar.
Los módulos de esta biblioteca se cargan usando `import`.
Por ejemplo:

```python
import math
x = math.sqrt(10)

import urllib.request
u = urllib.request.urlopen('http://www.python.org/')
data = u.read()
```

Vamos a estudiar bibliotecas y módulos en detalle más adelante.

### Errores y excepciones

Las funciones informan los errores como excepciones. Dado que una excepción interrumpe la ejecución de una función, la misma puede generar que todo el programa se detenga si no es administrada adecuadamente.

Probá por ejemplo lo siguiente en tu intérprete:

```python
>>> int('N/A')
Traceback (most recent call last):
File "<stdin>", line 1, in <módulo>
ValueError: invalid literal for int() with base 10: 'N/A'
>>>
```

Para poder entender qué pasó (debuguear), el mensaje describe cuál fue el problema, dónde ocurrió y un poco de la historia (traceback) de los llamados que terminaron en este error.

### Atrapar y administrar excepciones

Las excepciones pueden ser atrapadas y administradas.
Para atrapar una excepción, se usan los comandos `try - except`.

```python
numero_valido=False
while not numero_valido:
    try:
        a = input('Ingresá un número entero: ')
        n = int(a)
        numero_valido = True
    except ValueError:
        print('No es válido. Intentá de nuevo.')
print(f'Ingresaste {n}.')
```

Si en este ejemplo el usuario ingresa por ejemplo una letra, el comando `n = int(a)` genera una excepción de tipo `ValueError`: el comando `numero_valido = True` no se ejecuta, la excepción es atrapada por el `except ValueError` y el ciclo se repite. Probalo ingresando letras, números con decimales y números enteros. Probá también qué ocurre si querés salir sin ingresar nada generando una excepción presionando las teclas `Ctrl+C`. Leé el mensaje que describe lo ocurrido:  `Ctrl+C` genera una excepción de tipo `KeyboardInterrupt` que no es atrapada.

Si no especificamos el tipo de excepción que queremos atrapar, vamos a terminar atrapando todas la excepciones. Probá lo mismo que antes pero con este código.

```python
numero_valido=False
while not numero_valido:
    try:
        a = input('Ingresá un número entero: ')
        n = int(a)
        numero_valido = True
    except:
        print('No es válido. Intentá de nuevo.')
print(f'Ingresaste {n}.')
```

Deberías observar una diferencia: al presionar las teclas `Ctrl+C` la excepción `KeyboardInterrupt` sí es atrapada y no se termina el ciclo hasta no ingresar un número entero.

Suele ser difícil saber exactamente qué tipo de errores pueden ocurrir por adelantado. Para bien o para mal, la administración de excepciones suele ir creciendo a medida que un programa va generando errores inesperados (al mejor estilo: "Uh! Me olvidé de que podía pasar esto. Deberíamos preverlo y administrarlo adecuadamente para la próxima").

### Generar excepciones

Para generar una excepción (también diremos *levantar* una excepción, porque más cercano al término inglés "raise"), se usa el comando `raise`. Por ejemplo, si tenemos el siguiente código en el archivo `foo.py`:

```python
raise RuntimeError('¡Qué moco!')
```

Al correrlo va a detener la ejecución y permite rastrear la excepción leyendo el mensaje de error que imprime.

```bash
bash $ python3 foo.py
Traceback (most recent call last):
  File "foo.py", line 21, in <módulo>
    raise RuntimeError("¡Qué moco!")
RuntimeError: ¡Qué moco!
```

Alternativamente, esa excepción puede ser atrapada por un bloque `try-except`, pudiendo de esta forma evitar que el programa termine.

## Ejercicios

### Ejercicio 2.4: Definir una función
Probá primero definir una función simple:

```python
>>> def saludar(nombre):
        'Saluda a alguien'
        print('Hola', nombre)

>>> saludar('Guido')
Hola Guido
>>> saludar('Paula')
Hola Paula
>>>
```

Si la primera instrucción de una función es una cadena, sirve como documentación de la función. Probalo escribiendo `help(saludar)` para ver cómo la muestra.

### Ejercicio 2.5: Transformar un script en una función
Transformá el programa `costo_camion.py`  (que escribiste en el [Ejercicio 2.2](../02_Datos/01_Archivos.md#ejercicio-22-lectura-de-un-archivo-de-datos) de la sección anterior) en una función `costo_camion(nombre_archivo)`.  Esta función recibe un nombre de archivo como entrada, lee la información sobre los cajones que cargó el camión y devuelve el costo de la carga de frutas como una variable de punto flotante.

Para usar tu función, cambiá el programa de forma que se parezca a esto:

```python
def costo_camion(nombre_archivo):
    ...
    # Tu código
    ...

costo = costo_camion('Data/camion.csv')
print('Costo total:', costo)
```

Cuando ejecutás tu programa, deberías ver la misma salida impresa que antes. Una vez que lo hayas corrido, podés llamar interactivamente a la función escribiendo esto:

```bash
bash $ python3 -i costo_camion.py
```

Esto va a ejecutar el código en el programa y dejar abierto el intérprete interactivo.

```python
>>> costo_camion('Data/camion.csv')
47671.15
>>>
```

Es útil para testear y debuguear poder interactuar interactivamente con tu código.

### Ejercicio 2.6: Administración de errores
Probá correr la siguiente función ingresando tu edad real, una edad escrita con letras (como "ocho") y una edad negativa (-3):

```python
def preguntar_edad(nombre):
    edad = int(input(f'ingresá tu edad {nombre}: '))
    if edad<0:
        raise ValueError('La edad no puede ser negativa.')
    return edad
```

Ahora probá este ejemplo que atrapa la excepción generada con `raise` y continúa la ejecución con la siguiente persona.

```python
for nombre in ['Pedro','Juan','Caballero']:
    try:
        edad = preguntar_edad(nombre)
        print(f'{nombre} tiene {edad} años.')
    except ValueError:
        print(f'{nombre} no ingesó una edad válida.')
```

Vamos a usar estas ideas aplicadas al procesamiento de un archivo CSV. ¿Qué pasa si intentás usar la función `costo_camion()` con un archivo que tiene datos faltantes?

```python
>>> costo_camion('Data/missing.csv')
Traceback (most recent call last):
    File "<stdin>", line 1, in <módulo>
    File "costo_camion.py", line 11, in costo_camion
    ncajones = int(fields[1])
ValueError: invalid literal for int() with base 10: ''
>>>
```

El programa termina con un error. A esta altura tenés que tomar una decisión. Para que el programa funcione podés editar el archivo CSV de entrada de manera de corregirlo (borrando líneas o adecuando la información) o podés modificar el código para que maneje las líneas *incorrectas* de  alguna manera.

Modificá el programa `costo_camion.py` para que atrape la excepción, imprima un mensaje de aviso (warning) y continúe procesando el resto del archivo.

Vamos a profundizar en la administración  de errores en las próximas clases.

### Ejercicio 2.7: Funciones de la biblioteca
Python viene con una gran biblioteca estándar de funciones útiles. En este caso el módulo `csv` podría venirnos muy bien. Podés usarlo cada vez que tengas que leer archivos CSV. Acá va un ejemplo de cómo funciona.

```python
>>> import csv
>>> f = open('Data/camion.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> headers
['nombre', 'cajones', 'precio']
>>> for row in rows:
        print(row)

['Lima', '100', '32.20']
['Naranja', '50', '91.10']
['Caqui', '150', '83.44']
['Mandarina', '200', '51.23']
['Durazno', '95', '40.37']
['Mandarina', '50', '65.10']
['Naranja', '100', '70.44']
>>> f.close()
>>>
```

Una cosa buena que tiene el módulo `csv` es que maneja solo una gran variedad de detalles de bajo nivel como el problema de las comillas, o la separación con comas de los datos. En la salida del último ejemplo podés ver que el lector ya sacó las comillas dobles de los nombres de las frutas de la primera columna.


Modificá tu programa `costo_camion.py` para que use el módulo `csv` para leer los archivos CSV y probalo en un par de los ejemplos anteriores.

### Ejercicio 2.8: Ejecución desde la línea de comandos con parámetros

En el programa `costo_camion.py`, el nombre del archivo de entrada `'Data/camion.csv'` fue escrito en el código.

```python
# costo_camion.py
import csv

def costo_camion(nombre_archivo):
    ...
    # Tu código
    ...

cost = costo_camion('Data/camion.csv')
print('Total cost:', cost)
```

Esto está bien para ejercitar, pero en un programa real probablemente no harías eso ya que querrías una mayor flexibilidad. Una posibilidad es pasarle al programa el nombre del archivo que querés procesar como un parámetro cuando lo llamás desde la línea de comandos.

Copiá el contenido de `costo_camion.py` a un nuevo archivo llamado `camion_commandline.py` que incorpore la lectura de parámetros por línea de comando según la sugerencia del siguiente ejemplo:

```python
# camion_commandline.py
import csv
import sys

def costo_camion(nombre_archivo):
    ...
    # Tu código
    ...

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)
```

`sys.argv` es una lista que contiene los argumentos que le pasamos al script al momento de llamarlo desde la línea de comandos (si es que le pasamos alguno). Por ejemplo, desde una terminal de Unix (en Windows es similar), para correr nuestro programa y que procese el mismo archivo podríamos escribir:

```bash
bash $ python3 camion_commandline.py Data/camion.csv
Costo total: 47671.15
bash $
```

O con el archivo `missing.csv`:
```bash
bash $ python3 camion_commandline.py Data/missing.csv
...
Costo total: 30381.15
bash $
```
Si no le pasamos ningún archivo, va a mostrar el resultado para `camion.csv` porque lo indicamos con la línea `nombre_archivo = 'Data/camion.csv'`.

Guardá el archivo `camion_commandline.py` para entregar al final de la clase.

[Contenidos](../Contenidos.md) \| [Anterior (1 Manejo de archivos)](01_Archivos.md) \| [Próximo (3 Tipos y estructuras de datos)](03_TiposDatos.md)

