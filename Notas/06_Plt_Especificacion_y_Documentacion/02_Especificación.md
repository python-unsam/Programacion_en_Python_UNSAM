[Contenidos](../Contenidos.md) \| [Anterior (1 Control de errores)](01_Excepciones.md) \| [Próximo (3 Documentación y estilo**)](03_Documentar_y_Estilo.md)

# 6.2 Especificación, Documentación y contratos+

En esta unidad se le dará cierta formalización a algunos temas que habían sido
presentados informalmente, como por ejemplo la documentación de las funciones.

Se formalizarán las condiciones que debe cumplir un algoritmo al comenzar, en
su transcurso, y al terminar, y algunas técnicas para tener en cuenta estas
condiciones.

También se verá una forma de modelar el espacio donde *viven* las
variables.

## Documentación

Comenzamos formalizando un poco más acerca de la documentación, cuál es su
objetivo y las distintas formas de documentar.

###  Comentarios vs documentación

En Python tenemos dos convenciones diferentes para documentar nuestro código:
la *documentación* propiamente dicha (lo que ponemos entre `'` o
`'''` al principio de cada función o módulo), y los *comentarios*
(`#`).  En la mayoría de los lenguajes de programación hay convenciones
similares. ¿Por qué tenemos dos formas diferentes de documentar?

La *documentación* tiene como objetivo explicar *qué* hace el código.
La documentación está dirigida a cualquier persona que desee utilizar la
función o módulo, para que pueda entender cómo usarla sin necesidad de leer el
código fuente.  Esto es útil incluso cuando quien implementó la función es la
misma persona que la va a utilizar, ya que permite separar responsabilidades.

Los *comentarios* tienen como objetivo explicar *cómo* funciona el
código, y *por qué* se decidió implementarlo de esa manera. Los comentarios
están dirigidos a quien esté leyendo el código fuente.

Podemos ver la diferencia entre la documentación y los comentarios en la
función `elegir_codigo` de nuestra implementacion del juego Mastermind:

```python
def elegir_codigo():
    '''Devuelve un codigo de 4 digitos elegido al azar'''
    digitos = ('0','1','2','3','4','5','6','7','8','9')
    codigo = "
    for i in range(4):
        candidato = random.choice(digitos)
        # Debemos asegurarnos de no repetir digitos
        while candidato in codigo:
            candidato = random.choice(digitos)
        codigo = codigo + candidato
    return codigo
```

### ¿Por qué documentamos?

Seamos sinceros: nadie quiere escribir documentación. ¿Para qué repetir con
palabras lo que ya está estipulado en el código? La documentación es algo que
muy a menudo se deja *para después*, y cuando llega el tan angustioso
momento de escribirla, lo que se termina haciendo es escribir lo más
escueto posible que pueda pasar como "documentación".

Incluso es muy frecuente que durante el desarrollo de un proyecto el código
evolucione con el tiempo, pero que nos olvidemos de actualizar la documentación
para reflejar los cambios. En este caso no solamente tenemos documentación de
mala calidad, ¡sino que además es incorrecta`

Pese a todo esto, la realidad sigue siendo que una buena documentación es
componente esencial de cualquier proyecto exitoso. Esto en parte se debe a que
el código fuente transmite en detalle las operaciones individuales que componen
un algoritmo o programa, pero no suele transmitir en forma transparente cosas
como la *intención* del programa, el *diseño* de alto nivel, las
*razones* por las que se decidió utilizar un algoritmo u otro, etc.

### Código autodocumentado

En teoría, si nuestro código pudiera transmitir en forma eficiente todos esos
conceptos, la documentación sería menos necesaria. De hecho, existe una técnica de
programación llamada *código autodocumentado*, en la que la idea principal
es elegir los nombres de funciones y variables de forma tal que la
documentación sea innecesaria.

Tomemos como ejemplo el siguiente código:

```python
a = 9.81
b = 5
c = 0.5 * a * b**2
```

Leyendo esas tres líneas de código podemos razonar cuál será el valor final de
las variables `a`, `b` y `c`, pero no hay nada que nos indique qué representan
esas variables, o cuál es la intención del código. Una opción para mejorarlo sería
utilizar comentarios para aclarar la intención:

```python
a = 9.81   # Valor de la constante G (aceleración gravitacional), en m/s²
b = 5      # Tiempo en segundos
c = 0.5 * a * b**2  # Desplazamiento (en metros)
```

Otra opción, según la técnica de código autodocumentado, es simplemente asignar
nombres descriptivos a las variables:

```python
aceleracion_gravitacional = 9.81
tiempo_segundos = 5
desplazamiento_metros = 0.5 * aceleracion_gravitacional * tiempo_segundos ** 2
```

De esta manera logramos que no sea necesario ningún comentario ni documentación
adicional, ya que la intención del código es mucho más descriptiva.

La técnica de código autodocumentado presenta varias limitaciones. Entre ellas:


- Elegir buenos nombres es una tarea difícil, que requiere tener en cuenta cosas como: qué tan descriptivo es el nombre (cuanto más, mejor), la longitud del identificador (cuanto más corto mejor), el alcance del identificador (cuánto más grande, más descriptivo debe ser el nombre), y convenciones (`i` para índices, `c` para caracteres, etc).
- La documentación de todas formas termina siendo necesaria, ya que por muy bien que elijamos los nombres, muchas veces la única forma de explicar la intención del código y todos sus detalles es en lenguaje coloquial.
- En ciertos contextos sigue siendo deseable, o imprescindible, que quien quiera utilizar nuestra función o módulo pueda entender su funcionamiento sin necesidad de leer el código fuente.



### Un error común: la sobredocumentación

Si bien la ausencia de documentación suele ser perjudicial, el otro extremo
también lo es: la *sobredocumentación*. Después de todo, en la vida
diaria no necesitamos carteles que nos recuerden cosas como "esta es la
puerta", "este es el picaporte" y "empujar hacia abajo para abrir". De
la misma manera, podríamos decir que el siguiente código peca de ser sobredocumentado:

```python
def buscar_elemento(lista_de_numeros, numero):
    '''Esta función devuelve el índice (contando desde 0) en el que se
       encuentra el número `numero` en la lista `lista_de_numeros`.
       Si el elemento no está en la lista devuelve -1.
    '''
    # Recorremos todos los índices de la lista, desde 0 (inclusive) hasta N
    # (no inclusive)
    for indice in range(len(lista_de_numeros)):
        # Si el elemento en la posicion `indice` es el buscado
        if lista_de_numeros[indice] == numero:
            # Devolvemos el índice en el que está el elemento
            return indice
    # No lo encontramos, devolvemos -1
    return -1
```

Algunas cosas que podemos mejorar:

- En la firma de la función los nombres `buscar_elemento`, `lista_de_numeros` y `numero` se pueden simplificar a `buscar`, `secuencia` y `elemento`. Cambiamos `lista_de_numeros` por `secuencia`, ya que la función puede recibir secuencias de cualquier tipo, con elementos de cualquier tipo, y no hay ninguna razón para limitar a que sea una lista de números.
- Las variable interna `indice` también se puede simplificar: por convención podemos usar `i`.
- "Esta función" es redundante: cuando alguien lea la documentación ya va    a saber que se trata de una función.
- "contando desde 0" es redundante: en Python siempre contamos desde 0.
- Los comentarios son excesivos: la función es suficientemente simple y cualquier persona que sepa programación básica podrá entender el algoritmo.
- Podemos usar `enumerate`!

Corrigiendo todos estos detalles resulta:

```python
def buscar(lista, elemento):
    '''Devuelve el índice en el que se encuentra el `elemento` en la `lista`,
       o -1 si no está.
    '''
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1
```

## Contratos

Cuando hablamos de **contratos** o *programación por
contratos*, nos referimos a la necesidad de estipular tanto lo que necesita
como lo que devuelve nuestro código. El contrato de una función suele ser
incluido en su documentación.

Algunos ejemplos de cosas que deben ser estipuladas como parte del contrato
son: cómo deben ser los parámetros recibidos, cómo va a ser lo que se devuelve,
y si la función provoca algún efecto secundario (como por ejemplo modificar
alguno de los parámetros recibidos o imprimir algo en la consola).

Algunas de estas condiciones deben estar dadas antes de ejecutar el código o
función; a estas condiciones las llamamos *precondiciones*. Si se cumplen
las precondiciones, habrá un conjunto de condiciones sobre el estado en que
quedan las variables y el o los valores de retorno una vez finalizada la
ejecución, que llamamos *postcondiciones*.

### Precondiciones

Las precondiciones de una función son las condiciones que deben cumplirse antes
de ejecutarla, para que se comporte correctamente: cómo deben ser los
parámetros que recibe, cómo debe ser el estado global, etc.

Por ejemplo, en una función que divide dos números, las precondiciones son que los parámetros
son números, y que el divisor es distinto de 0.

Si estipulamos las precondiciones como parte de la documentación, en el cuerpo
de la función podremos asumir que son ciertas, y no será necesario escribir
código para lidiar con los casos en los que no se cumplen.

### Postcondiciones

Las postcodiciones son las condiciones que se cumplirán una vez finalizada la
ejecución de la función (asumiendo que se cumplen las precondiciones): cómo
será el valor de retorno, si los parámetros recibidos o variables globales son
alteradas, si se imprimen cosas, si se modifican archivos, etc.

En el ejemplo anterior, la función división, dadas las precondiciones
puede asegurar que devolverá un número correspondiente al cociente solicitado.

### Aseveraciones

Tanto las precondiciones como las postcondiciones son *aseveraciones*
(en inglés *assertions*). Es decir, afirmaciones realizadas en un momento particular de la ejecución sobre el estado computacional. Si una tal aseveración llegara a ser falsa, se levanta un excepción que deberá ser (o no) administrada adecuadamente.

En algunos casos puede ser útil incorporar estas afirmaciones desde el código, y para ello podemos utilizar la instrucción `assert`. Esta instrucción
recibe una condición a verificar (o sea, una expresión booleana).
Si la condición es `True`, la instrucción no hace nada; en caso contrario se
produce un error.

```python
>>> assert True
>>> assert False
(^Traceback (most recent call last):
  File '<stdin>', line 1, in <module>
AssertionError^)
```

Opcionalmente, la instrucción `assert` puede recibir
un mensaje de error que mostrará en caso que la condición no se cumpla.

```python
>>> n = 0
>>> assert n `= 0, 'El divisor no puede ser 0'
(^Traceback (most recent call last):
  File '<stdin>', line 1, in <module>
AssertionError: El divisor no puede ser 0^)
```

**Atencion:**
Es importante tener en cuenta que `assert` está pensado para ser
usado en la etapa de desarrollo. Un programa terminado nunca debería dejar
de funcionar por este tipo de errores.

### Ejemplos

Usando los ejemplos anteriores, la función `division` nos
quedaría de la siguiente forma:

```python
def division(dividendo, divisor):
    '''Cálculo de la división

    Pre: Recibe dos números, divisor debe ser distinto de 0.
    Post: Devuelve un número real, con el cociente de ambos.
    '''
    assert divisor `= 0, 'El divisor no puede ser 0'
    return dividendo / divisor
```

Otro ejemplo, tal vez más interesante, puede ser una función que implemente
una sumatoria *sum_i=inicial^final f(i)*.  En este caso hay que
analizar cuáles van a ser los parámetros que recibirá la función, y las
precondiciones que estos parámetros deberán cumplir.

La función `sumatoria` a escribir necesita de un valor inicial, un valor
final, y una función a la cual llamar en cada paso. Es decir que recibe
tres parámetros.

```python
def sumatoria(inicial, final, f):
```

Tanto `inicial` como `final` deben ser números enteros,
y dependiendo de la implementación a realizar o de la especificación
previa, puede ser necesario que `final` deba ser mayor o igual a
`inicial`.

Con respecto a `f`, se trata de una función que será llamada con
un parámetro en cada paso y se requiere poder sumar el resultado, por lo
que debe ser una función que reciba un número y devuelva un número.

La declaración de la función queda, entonces, de la siguiente manera.

```python
def sumatoria(inicial, final, f):
    '''Calcula la sumatoria desde i=inicial hasta final de f(i)

    Pre: inicial y final son números enteros, f es una función que
         recibe un entero y devuelve un número.
    Post: Se devuelve el valor de la sumatoria de aplicar f a cada
          número comprendido entre inicial y final.
    '''
```

### Ejercicio 6.4: 
Realizar la implementación correspondiente a la función `sumatoria`.

En definitiva, la estipulación de pre y postcondiciones dentro de la
documentación de las funciones es una forma de especificar claramente el
comportamiento del código.  Las pre y postcondiciones son, en efecto, un
*contrato* entre el código invocante y el invocado.

##  Invariantes de ciclo

Los invariantes se refieren a estados o situaciones que no cambian dentro
de un contexto o porción de código.  Hay invariantes de ciclo, que son los
que veremos a continuación, e invariantes de estado, que se verán más
adelante.

El invariante de ciclo permite conocer cómo llegar desde las precondiciones
hasta las postcondiciones, cuando la implementación se compone de un ciclo.
El invariante de ciclo es, entonces, una
aseveración que debe ser verdadera al comienzo de cada iteración.

Por ejemplo, si el problema es ir desde el punto A al punto B, las
precondiciones dicen que estamos parados en A y las postcondiciones que
estamos parados en B, un invariante podría ser "estamos en algún punto entre
A y B, en el punto más cercano a B que estuvimos hasta ahora.

Más específicamente, si analizamos el ciclo para buscar el máximo en una lista
desordenada, la precondición es que la lista contiene elementos que son
comparables y la postcondición es que se devuelve el elemento máximo de la
lista.

```python
def maximo(lista):
    'Devuelve el elemento máximo de la lista o None si está vacía.'
    if not lista:
        return None
    max_elem = lista[0]
    for elemento in lista:
        if elemento > max_elem:
            max_elem = elemento
    return max_elem
```

En este caso, el invariante del ciclo es que `max_elem` contiene el
valor máximo de la porción de lista analizada.

Los invariantes son de gran importancia al momento de demostrar que un
algoritmo funciona, pero aún cuando no hagamos una demostración formal es muy
útil tener los invariantes a la vista, ya que de esta forma es más fácil
entender cómo funciona un algoritmo y encontrar posibles errores.

Los invariantes, además, son útiles a la hora de determinar las condiciones
iniciales de un algoritmo, ya que también deben cumplirse para ese caso.  Por
ejemplo, consideremos el algoritmo para obtener la potencia `n` de
un número.

```python
def potencia(b, n):
    'Devuelve la potencia n del número b, con n entero mayor que 0.'
    p = 1
    for i in range(n):
        p *= b
    return p
```

En este caso, el invariante del ciclo es que la variable `p`
contiene el valor de la potencia correspondiente a esa iteración. Teniendo en
cuenta esta condición, es fácil ver que `p` debe comenzar el ciclo
con un valor de 1, ya que ese es el valor correspondiente a $p^0$.

De la misma manera, si la operación que se quiere realizar es sumar todos los
elementos de una lista, el invariante será que una variable `suma`
contenga la suma de todos los elementos ya recorridos, por lo que es claro que
este invariante debe ser 0 cuando aún no se haya recorrido ningún elemento.

```python
def suma(lista):
    'Devuelve la suma de todos los elementos de la lista.'
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma
```



### Parámetros mutables e inmutables

Las funciones reciben parámetros que pueden ser mutables o inmutables.

Si dentro del cuerpo de la función se modifica uno de estos parámetros para
que *referencie* a otro valor, este cambio no se verá reflejado fuera de la
función.  Si, en cambio, se modifica el *contenido* de alguno de los
parámetros mutables, este cambio *sí* se verá reflejado fuera de la
función.

A continuación un ejemplo en el cual se asigna la variable recibida, a un
nuevo valor.  Esa asignación sólo tiene efecto dentro de la función.

```python
>>> def no_cambia_lista(lista):
...     lista = [0, 1, 2, 3]
...     print('Dentro de la funcion lista =', lista)
...
>>> lista = [10, 20, 30, 40]
>>> no_cambia_lista(lista)
Dentro de la funcion lista = [0, 1, 2, 3]
>>> lista
[10, 20, 30, 40]
```

A continuación un ejemplo en el cual se modifica la variable recibida. En este
caso, los cambios realizados tienen efecto tanto dentro como fuera de la
función.

```python
>>> def cambia_lista(lista):
...     for i in range(len(lista)):
...         lista[i] = lista[i] ** 3
...
>>> lista = [1, 2, 3, 4]
>>> cambia_lista(lista)
>>> lista
[1, 8, 27, 64]
```

**Atención:** Por omisión se espera que una función que recibe parámetros mutables no los modifique, ya que si se los modifica se podría perder información valiosa.

En el caso en que por una decisión de diseño o especificación se modifiquen
los parámetros mutables recibidos, esto debe estar claramente documentado
como parte de las postcondiciones.


## Resumen

- La **documentación** tiene como objetivo explicar *qué* hace el código,
    y está dirigida a quien desee utilizar la función o módulo.
- Los **comentarios** tienen como objetivo explicar *cómo* funciona el
    código y *por qué* se decidió implementarlo de esa manera, y están dirigidos a
    quien esté leyendo el código fuente.
- El **contrato** de una función especifica qué condiciones se deben
    cumplir para que la función pueda ser invocada (**precondiciones**),
    y qué condiciones se garantiza que serán válidas cuando la función termine
    su ejecución (**postcondiciones**).
- Los **invariantes de ciclo** son las condiciones que deben
cumplirse al comienzo de cada iteración de un ciclo.
- En el caso en que estas **aseveraciones** no sean verdaderas, se
deberá a un error en el diseño o utilización del código.
- Si una función modifica un valor mutable que recibe por parámetro, eso
    debe estar explícitamente aclarado en su documentación.


## Ejercicios

### Ejercicio 6.5: Analizar cada una de las siguientes funciones.
¿Cuál es el contrato de la función? ¿Cómo sería su documentación?
¿Es necesario agregar comentarios?
¿Se puede simplificar el código y/o mejorar su legibilidad?
¿Hay algún invariante de ciclo?

```python
def Abs(i):
    if i >= 0:
        return i
    else:
        return -i
```

```python
def emails(diccionario):
    for k, v in diccionario.items():
        print(f'El e-mail de {k} es {v}')
```

```python
def emails2(diccionario):
    buenos = {*
    for k, v in diccionario.items():
        if '@' in v:
            buenos[k] = v
    return buenos
```

```pythondef emails3(nombres, direcciones):
    for nom in range(len(nombres)):
        if direcciones[nom] == None:
            nombre, apellido = ' '.split(nombres[nom].lower())
            direcciones[nom] = nombre[0] + apellido + '@ejemplo.com'
```



[Contenidos](../Contenidos.md) \| [Anterior (1 Control de errores)](01_Excepciones.md) \| [Próximo (3 Documentación y estilo**)](03_Documentar_y_Estilo.md)

