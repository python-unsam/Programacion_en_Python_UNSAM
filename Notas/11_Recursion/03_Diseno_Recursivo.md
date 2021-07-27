# 11.3 Diseño de algoritmos recursivos

Hasta el momento vimos que hay muchas funciones matemáticas que se definen
o que pueden desarrollarse de forma recursiva, pero puede aplicarse recursividad a muchos problemas que no sean explicitamente recursivos. Diseñar un algoritmo recursivo es un proceso sistematizable.

En general, en el proceso para plantear un algoritmo recursivo, necesitamos
resolver estos tres problemas:

1. **Caso base:** Necesitamos definir uno o más casos base de acuerdo a
nuestro problema. Como regla general tratamos de pensar como caso base a
las condiciones sobre las cuales es más fácil resolver nuestro problema.
Por ejemplo, si estuviéramos trabajando sobre listas o cadenas probablemente
sepamos la respuesta a nuestro problema en el caso de una secuencia vacía;
si estuviéramos trabajando sobre conjuntos de elementos probablemente la
respuesta sea evidente para los conjuntos de un solo elemento.
2. **Caso recursivo** o caso general: Este es el caso que va a efectuar
la llamada recursiva. La idea de este caso es reducir el problema a un
problema más sencillo, del cual se hará cargo la llamada recursiva, y luego
poder ensamblar la solución al problema original. Ampliaremos esto más adelante.
3. **Convergencia:** Necesitamos que la reducción que se haga en el caso
recursivo converja hacia los casos base, de modo que la recursión alguna
vez termine. Esto es, si dijimos que el caso base se resolvía cuando teníamos
una lista vacía, las operaciones del caso recursivo tienen que reducir
reiteradamente la lista hasta que la misma quede vacía.

Si podemos hacer estas tres cosas, tendremos un algoritmo recursivo para
nuestro problema.

### Un primer diseño recursivo

Supongamos que queremos programar una función `sumar(lista)` que
determine en forma recursiva la suma de una secuencia `lista` de
números.

Como caso base debemos elegir un caso sencillo de verificar. El caso más
sencillo de verificar es uno en el que ni siquiera necesitamos
computar algo: Si la lista está vacía es evidente que la suma da cero.

Nuestro caso base será algo así como:

```python
    if len(lista) == 0:
        return 0
```

Queremos diseñar un paso recursivo que realice _una reducción_ de manera que dada cualquier lista, la aplicación sucesiva de la reducción seleccionada converja al caso base. Hay muchas maneras de reducir una lista
para lograr esto; para este caso vamos a proponer una muy sencilla: sacar el primer elemento. Si cada llamada recursiva saca el primer elemento, tarde o temprano covergeremos a una lista vacía.

Nuestra llamada recursiva podría ser algo así como:

```python
sumar(lista[1:])
```

Lo más complejo ahora es pensar el caso general.

Dijimos que íbamos a retirar un elemento de la lista por vez y hacer una
llamada recursiva. Olvidémonos por un momento de la recursividad e imaginemos
que *ya* tenemos una función `sumar2` que sabe sumar los elementos de una
`lista` y que lo hace bien.  Intentemos resolver el problema inverso: si
agregamos un elemento `x` al principio de la lista (obteniendo `[x] + lista`),
¿podemos calcular la suma de la nueva lista?  ¿Podemos resolver el problema más
grande con la solución al problema más pequeño? La solución es sencilla: La
suma de la lista ampliada será `x` más la suma de la lista original (que podemos calcular como `sumar2(lista)`).

Es decir, la solución al problema este que planteamos sería así:
```python
def sumar(lista):
   """Precondición: len(lista) >= 1.
      Devuelve: La suma de los elementos en la lista."""
   return lista[0] + sumar2(lista[1:])
```

Podemos ver que si tuviéramos implementada `sumar2` entonces
`sumar` funcionaría bien. Volvamos ahora a recursividad: Si sabemos
resolver el caso general en función a la solución del caso simplificado de la
llamada recursiva, si existen casos base que corten la recursión y si además
la recursión converge hacia los casos base tenemos resuelto el problema
completo. La función que asumimos que funcionaba *es la misma* que
acabamos de implementar.

Cuando diseñamos una función recursiva tenemos que dar este *salto de fé*:
asumir que la función del paso recursivo ya funciona; nosotros lo que vamos a implementar es una función que logra concatenar el resultado del subproblema y ensamblarlo con nuestro problema mayor. Si hacemos esto bien entonces todo funciona.

Finalmente nuestra primera función recursiva quedaría:
```python
def sumar(lista):
   """Devuelve la suma de los elementos en la lista."""
   res = 0
   if len(lista) != 0:
       res = lista[0] + sumar(lista[1:])
   return res
```

### Recursión de cola

Dentro de los problemas recursivos no siempre es inmediato establecer cómo
se va a propagar la información entre las llamadas recursivas. Es decir, cómo va a interactuar la solución de el o los subproblemas en la solución del problema general.

En todos los ejemplos presentados hasta el momento la información del resultado
se propagó desde las hojas del árbol de llamadas (los casos base) hacia las
funciones invocantes (mediante la instrucción `return`). Por ejemplo, para
resolver el resultado de Fibonacci `F(5)` se utilizan únicamente los resultados
computados por `F(4)` y `F(3)`, y no se recibe ningún dato adicional de la función invocante (más allá del parámetro `n=5`).
Esto no siempre es así, en algunos problemas sí se hace necesario propagar
información "hacia abajo". Y en otros casos, si bien no es necesario,
puede tener ventajas adicionales.

Por ejemplo, podríamos reescribir la función `sumar()` de esta forma:
```python
def sumar(lista, suma = 0):
    """Devuelve la suma de los elementos en la lista."""
    res = suma
    if len(lista) != 0:
        res = sumar(lista[1:], lista[0] + suma)
    return res
```

Puede observarse que en esta implementación en vez de *esperar* a que se
resuelva el cómputo de la parte recursiva para ensamblar la solución e ir
resolviendo los cálculos parciales desde el final de la lista hacia el
principio, le *pasamos* la solución parcial a la llamada recursiva.
Finalmente el caso base devuelve la suma de los cálculos que se realizaron
de principio a final y cada llamada recursiva devuelve este resultado.

No profundizaremos más en el tema, pero la particularidad de que lo último
que se realice en el caso general sea la llamada recursiva (sin realizar
ninguna operación adicional sobre el resultado de esta llamada) se conoce como
*recursividad de cola*. La recursividad de cola es de interés porque
implica muy poco esfuerzo reescribir una versión iterativa y no recursiva
del algoritmo. Esto es inmediato: como lo último que se hace es la llamada
recursiva entonces no hace falta seguir *recordando* el contexto de la
llamada anterior cuando se hace la siguiente, entonces no es necesario utilizar
la pila de ejecución. El código anterior puede reescribirse como

```python
def sumar(lista):
    """Devuelve la suma de los elementos en la lista."""
    suma = 0
    while lista:
        lista, suma = lista[1:], lista[0] + suma
    return suma
```

tan solo reemplazando la recursión por un bucle y actualizando las
variables según los parámetros de la llamada recursiva.

### Modificación de la firma

La *firma* de una función es su nombre, más los
parámetros que recibe, más los valores que devuelve. Para invocar una función
cualquiera, es suficiente con saber cómo es su firma, y no es necesario saber
cómo es la implementación interna. Ahora bien, si cambiamos la lista
de parámetros o el tipo de dato del valor de retorno de la función, estamos
cambiando su firma, y eso nos obliga a cambiar cualquier lugar del código
que contenga alguna llamada a la función.

En el ejemplo de `sumar` implementada con recursividad de cola nos
vimos obligados a modificar la firma de la función agregando el parámetro
`suma` que no formaba parte del problema inicial. Pudimos hacerlo
elegantemente utilizando un valor por omisión (`suma=0`), pero la firma de
todos modos quedó confusa.

Hay casos en los que no podemos salvar un cambio en la firma.  Por ejemplo,
supongamos que queremos diseñar una función recursiva que calcule el promedio
de una secuencia de números.

Como ya sabemos diseñar funciones recursivas, intuimos que el caso base será
cuando la lista tenga un solo elemento y que la reduciremos sacando de a un elemento por
vez. El cuerpo de nuestra función será algo así:

```python
def promediar(lista):
    if len(lista) == 1:
        res = lista[0]
    else:
        res = promediar(lista[1:]) ???
    return res
```
Ahora bien, con esto no alcanza para resolver el problema.

Para calcular un promedio necesitamos tanto calcular la suma como contar
la cantidad de elementos. Entonces, una implementación recursiva va a estar computando dos valores cuando el resultado del problema es evidentemente uno solo. Si bien puede elaborarse una solución similar a la que ya ensayamos con `sumar` complicaría innecesariamente el código. Es preferible modificar la firma
de la función.

Implementemos el problema resolviendo primero la llamada recursiva (en una
función diferente que llamaremos `promediar_aux()`) y luego ensamblando:

```python
def promediar_aux(lista):
    suma = lista[0]
    cantidad = 1    
    if len(lista) > 1:
        suma_resto, cantidad_resto = promediar_aux(lista[1:])
        suma += suma_resto
        cantidad += cantidad_resto
    return suma, cantidad
```

Puede verse que esta función cumple con las reglas de diseño de recursividad
que describimos antes. Con lo que no cumple esta función es con la firma
natural de la función `promediar()` que queríamos diseñar, ya que `promediar_aux()` devuelve dos cosas y no una.

Esto no invalida nuestra solución, pero la misma está incompleta. Lo que
debemos hacer es implementar una función *wrapper* (envoltorio) que lo
que haga es operar como *cara visible* para le usuarie de la función que
hace realmente el trabajo. A esta función sí la vamos a llamar `promediar`, ya
que va a cumplir con la firma deseada:

```python
def promediar(lista):
    """Devuelve el promedio de los elementos de una lista de números."""

    def promediar_aux(lista):
        suma = lista[0]
        cantidad = 1    
        if len(lista) > 1:
            suma_resto, cantidad_resto = promediar_aux(lista[1:])
            suma += suma_resto
            cantidad += cantidad_resto
        return suma, cantidad

    suma, cantidad = promediar_aux(lista)
    return suma / cantidad
```

Notar que si bien la función visible `promediar` no es recursiva, sí lo
es la función `promediar_aux` que es la que realiza el trabajo, por
lo que el conjunto se considera recursivo. Observá que estamos definiendo la función `promediar_aux` **dentro** de la función `promediar` de manera que no resulte visible desde afuera (no la podés llamar desde afuera: así como hay *variables locales*, ésta es una *función local*).

Además de para adaptar la firma de la función recursiva, las funciones wrapper
se suelen utilizar para simplificar el código de las funciones recursivas. Por
ejemplo, si quisiéramos hacer validaciones de los parámetros, no
querríamos que las mismas se reiteraran en cada iteración recursiva porque
consumirían recursos innecesarios. Entonces las podemos resolver en la función
wrapper, antes de empezar la recursión.

Por ejemplo, hace un rato implementamos la potencia en forma recursiva con la restricción `n >= 0`. Pero dado que `b^n = (1/b)^(-n)` podemos aprovechar el código implementado para
resolver para cualquier `n` entero. Podríamos modificar el código de `potencia()` para incluir este caso, pero se reiteraría la comprobación en cada nivel de la recursión. Para este caso resulta más sencillo construir una función wrapper e incluir ahí todo lo que consideremos necesario.
Habiendo renombrado la función original como `_potencia`, nuestro wrapper sería:

```python
def potencia(b, n):
    """Precondición: n es entero
       Devuelve: b^n."""
    if n < 0:
        b = 1 / b
        n = -n
    return _potencia(b, n)
```

## Limitaciones

Si creamos una función sin *caso base*, obtendremos el equivalente
recursivo de un bucle infinito. 

Éste es un bucle infinito y corre para siempre.
```python
i = 0
while i < 10:
    suma = suma + i
```

El bucle recursivo infinito, sin embargo, termina agotando la memoria. Esto se debe a que cada llamada recursiva agrega un elemento a la pila de llamadas a funciones y la memoria de nuestras computadoras no es infinita.

En particular, en Python, para evitar que la memoria se termine, la pila de
ejecución de funciones tiene un límite. Es decir, que si se ejecuta un
código como el que sigue:

```python
def inutil(n):
    return inutil(n - 1)
```

Se obtendrá un resultado como el siguiente:

```python
>>> inutil(1)
  File "<stdin>", line 2, in inutil
  File "<stdin>", line 2, in inutil
  (...)
  File "<stdin>", line 2, in inutil
RecursionError: maximum recursion depth exceeded
```

El límite por omisión es de 1000 llamadas recursivas. Es posible modificar
el tamaño máximo de la pila de recursión mediante la instrucción
`sys.setrecursionlimit(n)`.  Sin embargo, si se está alcanzando
este límite suele ser una buena idea pensar si realmente el algoritmo
recursivo es el que mejor resuelve el problema.

### Sabías que
Existen algunos lenguajes *funcionales*, como Haskell, ML, o Scheme, en
los cuales la recursión es la única forma de realizar un ciclo.  Es
decir, no existen construcciones `while` ni `for`.

Estos lenguajes cuentan con optimización de recursión de cola,
una optimización para que cuando se identifique que la recursión es de cola,
no se apile el estado de la función innecesariamente, evitando el consumo adicional de memoria mencionado anteriormente.

La ejecución de todas las funciones con recursión de cola vistas en esta
unidad podría ser optimizada por el compilador o intérprete del lenguaje.

## Resumen


* A medida que se realizan llamadas a funciones, el estado de cada
función se almacena en la *pila de ejecución*.
* Esto permite que sea posible que una función se llame a sí misma,
pero que las variables dentro de la función tomen distintos valores.
* La *recursión* es el proceso en el cual una función se invoca a
sí misma.  Este proceso permite crear un nuevo tipo de ciclos.
* Siempre que se escribe una función recursiva es importante considerar
el *caso base* (el que detendrá la recursión) y el *caso
recursivo* (el que realizará la llamada recursiva).  Una función recursiva
sin caso base es equivalente a un bucle infinito.
* Una función no es mejor ni peor por ser recursiva.  En cada situación
a resolver puede ser conveniente utilizar una solución recursiva o una
iterativa.  Para elegir una o la otra será necesario analizar las
características de elegancia y eficiencia.
* Al diseñar funciones recursivas muchas veces puede ser útil
implementar una función *wrapper*, por ejemplo para adaptar
la firma de la función, validar parámetros, inicializar datos o manejar excepciones.


