[Contenidos](../Contenidos.md) \| [Próximo (2 Debuguear programas+)](02_debugger-oski.md)

# 6.1 Control de errores

Aunque ya hablamos de *excepciones*, en esta sección hablaremos de administración de excepciones y control de errores con mayor detalle.

[oski]:# (### How programs fail)
### Formas en que los programas fallan

Python no hace ningún control ni validación sobre los tipos de los argumentos que las funciones reciben ni los valores de estos argumentos. Las funciones trabajarán sobre todo dato que sea compatible con las instrucciones dentro de la función. 

```python
def add(x, y):
    return x + y

add(3, 4)               # 7
add('Hello', 'World')   # 'HelloWorld'
add('3', '4')           # '34'
```

Si existen errores en una función, serán evidentes durante la ejecución de la función (en forma de una excepción).

```python
def add(x, y):
    return x + y

>>> add(3, '4')
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for +:
'int' and 'str'
>>>
```
Python acusa los errores en el idioma en que fué programado: inglés. El error acusado aquí puede entenderse como:
Recapitulando (llamada mas reciente al final)
...
Error de tipo (de datos): tipo de operando no admitido para +: 'int' y 'str'
Es decir: la función intentó aplicar el operador + (suma) a dos operandos de tipo entero y cadena y no pudo hacerlo, levantando una excepción. 

Se hace un fuerte énfasis en *probar* el código para verificar que funcione (hablaremos de ello mas adelante)

### Excepciones

Las excepciones se usan para señalar errores. 
Si necesitás levantar una excepción, usá la instrucción `raise` . 

```python
if nombre not in autorizados:
    raise RuntimeError(f'{nombre} no autorizado')
```

Para "atrapar" una excepción, usá `try-except`. 

```python
try:
    authenticate(nusuario)
except RuntimeError as e:
    print(e)
```

### Administración de excepciones

Una excepción se propagará hasta el primer `except` que coincida con ella.

```python
def grok():
    ...
    raise RuntimeError('Whoa!')   # Levanta una excepción aquí

def spam():
    grok()                        # Esta llamada resultará en una excepción

def bar():
    try:
       spam()
    except RuntimeError as e:     # Aquí atrapamos la excepción
        ...

def foo():
    try:
         bar()
    except RuntimeError as e:     # Por lo tanto la excepción no llega aquí
        ...

foo()
```

[oski]: # (To handle the exception, put statements in the `except` block. You can add any statements you want to handle the error.)

Para administrar la excepción, usá instrucciones en la porción `except`. Cualquier instrucción en este segmento hará que la excepción no se propague más. Es pertinente realizar acciones relacionadas con la excepción en particular. 

```python
def grok(): ...
    raise RuntimeError('Whoa!')

def bar():
    try:
      grok()
    except RuntimeError as e:   # Excepción atrapada
        statements              # Ejecute estos comandos
        statements
        ...

bar()
```

Una vez administrada, la ejecución continúa en la primera instrucción a continuación del `try-except`.

```python
def grok(): ...
    raise RuntimeError('Whoa!')

def bar():
    try:
      grok()
    except RuntimeError as e:   # Excepción atrapada
        statements
        statements
        ...
    statements                  # La ejecución del programa 
    statements                  # continúa aquí
    ...

bar()
```

### Excepciones integradas

Hay mas de una veintena de tipos de excepciones ya integradas en Python. Normalmente, el nombre de la excepción indica qué anduvo mal. (i.e. se levanta un  `ValueError` si el valor suministrado no es adecuado). La siguiente no es una lista completa. Vas a encontrar más en la [documentación del lenguaje](https://docs.python.org/3/library/exceptions.html#bltin-exceptions).

[oski]: # (
There are about two-dozen built-in exceptions.  Usually the name of
the exception is indicative of what's wrong {e.g., a `ValueError` is
raised because you supplied a bad value}. This is not an
exhaustive list. Check the documentation for more.
)

```python
ArithmeticError
AssertionError
EnvironmentError
EOFError
ImportError
IndexError
KeyboardInterrupt
KeyError
MemoryError
NameError
ReferenceError
RuntimeError
SyntaxError
SystemError
TypeError
ValueError
```

### Valores asociados a excepciones

Usualmente las excepciones llevan valores asociados, proveyendo mas información sobre la causa detallada del error. Este valor puede ser una cadena (*string*) o una tupla de valores diversos, por ejemplo un código de error y un texto explicando ese código). 

```python
raise RuntimeError('Nombre de usuario no valido')
```

La instancia de la variable suministrada a `except` lleva este valor asociado. 

[oski]: # (no me gusta como queda. Confuso. El original tambien confuso. En los ejemplos no se muestra como usar este valor asociado.  Igual sigo.
This value is part of the exception instance that's placed in the variable supplied to `except`.)

```python
try:
    ...
except RuntimeError as e:   # `e` contiene la excecpcion lanzada
    ...
```

`e` es una instancia del mismo tipo que la excepción, aunque si lo imprimís suele tener aspecto de una cadena de caracteres.

```python
except RuntimeError as e:
    print('Failed : Reason', e)
```

### Podés atrapar múltiples excepciones

Es posible atrapar diferentes tipos de excepciones en la misma porción de código, si incluís varios `except` en tu `try:`.

```python
try:
  ...
except LookupError as e:
  ...
except RuntimeError as e:
  ...
except IOError as e:
  ...
except KeyboardInterrupt as e:
  ...
```

Como alternativa, si las vas a procesar a todas de la misma manera, las podés agrupar:

```python
try:
  ...
except (IOError,LookupError,RuntimeError) as e:
  ...
```

### Todas las excepciones

Para atrapar todas y cualquier excepción, se usa `Exception` así: 

```python
try:
    ...
except Exception:       # PELIGRO. (ver abajo)
    print('An error occurred')
```

En general es mala idea "administrar" las excepciones de este modo, porque no te dá ninguna pista de porqué falló el programa.

### Así NO se atrapan excepciones. 

Así es como NO debe hacerse la administración de excepciones.

```python
try:
    hacer_algo()
except Exception:
    print('Hubo un error.')
```

Esto atrapa todos los errores posibles, y puede resultar imposible hacer debugging cuando el código falla por algún motivo que no esperabas (p.ej. falta algún módulo de Python, etc.)

### Así es un poco mejor.

Si va a atrapar todas las excepciones, aquí hay un modo algo mas decente:

```python
try:
    hacer_algo()
except Exception as e:
    print('Hubo un error. Porque...', e)
```

`Exception` incluye toda excepción posible, de modo que no sabés cuál atrapaste.
Al menos esto informa el motivo específico del error. Siempre es bueno tener alguna forma de ver o informar errores cuando atrapás todas las excepciones posibles. 

Sin embargo, por lo general es mejor atrapar errores específicos, y sólo aquéllos que podés administrar. Errores que no administres, déjalos correr (tal vez alguna otra porción de código los atrape y administre correctamente)

### Re-lanzar una excepción

Si necesitás hacer algo en respuesta a una excepción pero no querés atraparla, podés usar `raise` para volver a lanzar la misma excepción.

```python
try:
    hacer_algo()
except Exception as e:
    print('Hubo un error. Porque...', e)
    raise
```

Esto te permite, por ejemplo, llevar un registro de las excepciones (*log*) sin administrarla, y re-lanzarla para administrarla adecuadamente mas tarde.

### Buenas prácticas al administrar excepciones

No atrapes excepciones. Dejalas caer ruidosamente.
Si es importante, alguien se va a encargar del problema. Sólo atrapá excepciones si *sos ese "alguien"*. Es decir: sólo atrapá aquéllos errores que podés administrar elegantemente y permitir que el programa siga ejecutando.   

### La instrucción `finally`.

`finally` especifica que esa porción de código debe ejecutarse sin importar si una excepción fué atrapada o no.

```python
lock = Lock()
...
lock.acquire()
try:
    ...
finally:
    lock.release()  # esto SIEMPRE se ejecuta. Haya o no haya excepciones.
```

Una estructura como ésa resulta en un manejo seguro de los recursos disponibles (seguros, archivos, hardware, etc.)

### La instrucción `with`.

En Python moderno los bloques `try-finally` se reemplazan con `with`.

```python
lock = Lock()
with lock:
    # obtengo el seguro (lock)
    ...
# libero el seguro (lock)
```

Un ejemplo más común: 

```python
with open(nombre_archivo) as f:
    # Usar el archivo
    ...
# Archivo cerrado
```

`with` define un *contexto* dentro del cual se usa un recurso.  Fuera de ese contexto, los recursos son liberados. `with` sólo funciona sobre ciertos objetos que fueron específicamente programados para poder usarlo.

## Ejercicios

### Ejercicio 6.1: Raising exceptions
La función `parse_csv()` que escribiste en la sección anterior admite seleccionar algunas columnas por el usuario, pero éso sólo funciona si el archivo de entrada tiene encabezados.

Modifcá tu código para que lance una excepción en caso que ambos parámetros `select` y `has_headers=False` sean pasados juntos. Y que resulte: 

```python
>>> parse_csv('Data/precios.csv', select=['name','precio'], has_headers=False)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "fileparse.py", line 9, in parse_csv
    raise RuntimeError("select argument requires column headers")
RuntimeError: select argument requires column headers
>>>
```

(nota: el mensaje de error puede entenderse aproximadamente como 
"RuntimeError: para seleccionar argumentos necesito encabezados")

Ahora que agregaste este control, te estarás preguntando si no deberías comprobar otras cosas también en tu función. Por ejemplo, ¿deberías comprobar que `nombre_archivo` sea una cadena, que `tipos` sea una lista y otras cosas de ese estilo ? 

Como regla general, es mejor no controlar esas cosas, y dejar que el programa dé un error ante entradas inválidas. El mensaje de error va a darte una idea del origen del problema y te va ayudar a solucionarlo.

El motivo principal para agregar controles de calidad sobre los argumentos de entrada es evitar que tu programa sea ejecutado en condiciones que no tienen sentido (pedirle que haga algo que requiere encabezados y simultáneamente decirle que no existen encabezados) lo cual implicaria un error en el código que ha llamado y pretende usar a tu función. La idea general es estar protegido contra situaciones que "no deberían suceder" pero podrían. 

[oski]:# (
Having added this one check, you might ask if you should be performing
other kinds of sanity checks in the function.  For example, should you
check that the nombre_archivo is a string, that types is a list, or anything
of that nature?
As a general rule, it’s usually best to skip such tests and to just
let the program fail on bad inputs.  The traceback message will point
at the source of the problem and can assist in debugging.
The main reason for adding the above check is to avoid running the code
in a non-sensical mode {e.g., using a feature that requires column
headers, but simultaneously specifying that there are no headers}.
This indicates a programming error on the part of the calling code.
Checking for cases that "aren't supposed to happen" is often a good idea.
)

### Ejercicio 6.2: Catching exceptions
La función `parse_csv()` que escribiste está destinada a procesar un archivo completo. Pero en una situacion real, es posible que los archivos CSV de entrada estén "rotos", ausentes, o su contenido no conforme con el formato esperado. Probá esto:  

```python
>>> camion = parse_csv('Data/missing.csv', types=[str, int, float])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "fileparse.py", line 36, in parse_csv
    row = [func(val) for func, val in zip(types, row)]
ValueError: invalid literal for int() with base 10: ''
>>>
```

Modificá la función `parse_csv()` de modo que atrape todas las excepciones de tipo `ValueError` generadas durante el armado de los registros a devolver, e imprima un mensaje de advertencia para las filas que no pudieron ser convertidas.
Este mensaje deberá incluír el número de fila que causó el fallo y el motivo por el cual falló la conversión. Para probar tu nueva función, intentá procesar `Data/missing.csv`. Veamos:  

[oski]: # (
Modify the `parse_csv` function to catch all `ValueError` exceptions
generated during record creation and print a warning message for rows
that can’t be converted.
The message should include the row number and information about the
reason why it failed.  To test your function, try reading the file
`Data/missing.csv` above.  For example:
)

```python
>>> camion = parse_csv('Data/missing.csv', types=[str, int, float])
Row 4: Couldn't convert ['Mandarina', '', '51.23']
Row 4: Reason invalid literal for int() with base 10: ''
Row 7: Couldn't convert ['Naranja', '', '70.44']
Row 7: Reason invalid literal for int() with base 10: ''
>>>
>>> camion
[{'precio': 32.2, 'name': 'Lima', 'cajones': 100}, {'precio': 91.1, 'name': 'Naranja', 'cajones': 50}, {'precio': 83.44, 'name': 'Caqui', 'cajones': 150}, {'precio': 40.37, 'name': 'Durazno', 'cajones': 95}, {'precio': 65.1, 'name': 'Mandarina', 'cajones': 50}]
>>>
```

### Ejercicio 6.3: Silencing Errors
Modificá `parse_csv()` de modo que el usuario pueda silenciar los informes de errores de separación (*parsing*). Por ejemplo:

```python
>>> camion = parse_csv('Data/missing.csv', types=[str,int,float], silence_errors=True)
>>> camion
[{'precio': 32.2, 'name': 'Lima', 'cajones': 100}, {'precio': 91.1, 'name': 'Naranja', 'cajones': 50}, {'precio': 83.44, 'name': 'Caqui', 'cajones': 150}, {'precio': 40.37, 'name': 'Durazno', 'cajones': 95}, {'precio': 65.1, 'name': 'Mandarina', 'cajones': 50}]
>>>
```

[oski]: # (
Error handling is one of the most difficult things to get right in
most programs.  As a general rule, you shouldn’t silently ignore
errors.  Instead, it’s better to informe problems and to give the user
an option to the silence the error message if they choose to do so.
)

### Comentarios

Lograr un buen manejo o administración de errores es una de las partes mas difíciles en la mayoría de los programas. Estás intentando preveer imprevistos. Como regla general, no ignores los errores. Es mejor informar los problemas y ofrecer al usuario la opción de no informarlos más. Un buen diálogo entre el código y el usuario  facilita el debugging y el buen uso del programa. 


[Contenidos](../Contenidos.md) \| [Próximo (2 Debuguear programas+)](02_debugger-oski.md)

