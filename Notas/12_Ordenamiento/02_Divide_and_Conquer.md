[Contenidos](../Contenidos.md) \| [Anterior (1 Ordenamientos sencillos de listas)](01_Ordenamiento_sencillo.md)

# 12.2 Ordenamiento mergesort

Los métodos de ordenamiento vistos en la unidad anterior eran métodos
iterativos cuyo tiempo estaba relacionado con `N^2`.

En esta unidad veremos dos métodos de ordenamiento basados
en un planteo recursivo del problema, que nos permitirán obtener el
mismo resultado de forma más eficiente.

## Ordenamiento por mezcla, o *Merge sort* 

*Merge sort* se basa en la siguiente idea:

* Si la lista es pequeña (vacía o de tamaño 1) ya está ordenada y
no hay nada que hacer. De lo contrario hacer lo siguiente:
* Dividir la lista al medio, formando dos sublistas de (aproximadamente) el
mismo tamaño cada una.
* Ordenar cada una de esas dos sublistas (usando
este mismo método).
* Una vez que se ordenaron ambas sublistas, intercalarlas de manera ordenada.

Por ejemplo, si la lista original es `[6, 7, -1, 0, 5, 2, 3, 8]`
deberemos ordenar recursivamente `[6, 7, -1, 0]` y
`[5, 2, 3, 8]` con lo cual obtendremos `[-1, 0, 6, 7]` y
`[2, 3, 5, 8]`.  Si intercalamos ordenadamente las dos listas
ordenadas obtenemos la solución buscada:
`[-1, 0, 2, 3, 5, 6, 7, 8]`.

Diseñamos la función `merge_sort(lista)`:

* Si lista es pequeña (vacía o de tamaño 1) ya está ordenada y
no hay nada que hacer. Se devuelve lista tal cual.
* De lo contrario:
* `medio = len(lista) / 2`
* `izq = merge_sort(lista[:m])`
* `der = merge_sort(lista[m:])`
* Se devuelve `merge(izq, der)`.

Falta sólo diseñar la función `merge`: dadas dos listas ordenadas
debe obtener una nueva lista que resulte de intercalar a ambas de manera
ordenada:

* Utilizaremos dos índices, `i` y `j`, para recorrer
cada una de las dos listas.
* Utilizaremos una tercera lista, `resultado`, donde
almacenaremos el resultado.

* Mientras `i` sea menor que el largo de `lista1` y
`j` menor que el largo de `lista2`, significa que hay
elementos para comparar en ambas listas.

* Si el menor es el de `lista1`:
* Agregar el elemento `i` de `lista1` al final del
resultado.
* Avanzar el índice `i`.
* de lo contrario:
* Agregar el elemento `j` de `lista2` al final del
resultado.
* Avanzar el índice `j`.


* Una vez que una de las dos listas se termina, simplemente hay que
agregar todo lo que queda en la otra al final del resultado.

El código resultante del diseño de ambas funciones puede verse a continuación:

```python
import random

def al_azar (N):
    return random.sample(range(0, N), N)


def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        return lista
    medio = len(lista) // 2
    izq = merge_sort(lista[:medio])
    der = merge_sort(lista[medio:])
    return merge(izq, der)

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""

    i, j = 0, 0
    resultado = []

    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado

l=al_azar(30)
print(l)
print(merge_sort(l))
```

_El método que hemos usado para resolver este problema se llama *divide y reinarás*, y se aplica en las situaciones en las que vale el siguiente principio_:

Para obtener una solución es posible partir el problema en varios subproblemas
de tamaño menor, resolver cada uno de esos subproblemas por separado aplicando
la misma técnica (en nuestro caso ordenar por mezcla cada una de las dos
sublistas), y finalmente juntar estas soluciones parciales en una solución
completa del problema mayor (en nuestro caso la intercalación ordenada de las
dos sublistas ordenadas).

Como siempre sucede con las soluciones recursivas, debemos encontrar un caso
base en el cual no se aplica la llamada recursiva (en nuestro caso la base
sería el paso 1: Si la lista es pequeña (vacía o de tamaño 1) ya está ordenada
y no hay nada que hacer). Además debemos asegurar que siempre se alcanza el
caso base, y en nuestro caso aseguramos eso porque las lista original se divide
siempre en mitades cuando su longitud es mayor que 1.

### ¿Cuánto cuesta el *Merge sort*?

Sea `N` la longitud de la lista. Observamos lo siguiente:

* Para intercalar dos listas de longitud `N/2` hace falta recorrer
ambas listas que en total tienen `N` elementos, por lo que es proporcional
a `N`. Llamemos `a \cdot N` a ese tiempo.

* Si llamamos `T(N)` al tiempo que tarda el algoritmo en ordenar
una lista de longitud `N`, vemos que `T(N) = 2 * T(N/2) + a * N`.

* Además, cuando la lista es pequeña, la operación es de tiempo
constante: `T(1) = T(0) = b`.
\end{itemize*

Para simplificar la cuenta vamos a suponer que `N = 2^k`.


```
T(N) = T(2^k) = 2 * T(2^(k-1)) + a * 2^k 
              = 2 * ( 2 * T(2^(k-2)) + a * 2^(k-1)) + a * 2^k
              = 2^2 * T(2^(k-2)) + a * 2^k +a * 2^k
              .
              .
              .
              = 2^i * T(2^(k-i))+ i * a * 2^k
              .
              .
              .
              = 2^k * T(1) + k * a * 2^k
              = b * 2^k  + k * a * 2^k
```

Pero si `N = 2^k` entonces `k=\log_2N`, y por lo tanto hemos demostrado
que:

`T(N) = b * N + a * N * log2(N).`

Como lo que nos interesa es aproximar el valor, diremos (despreciando el
término de menor orden) que

`` T(N) \sim N * \log_2 N ``

Hemos mostrado entonces
un algoritmo que se porta mucho mejor que los que vimos en la unidad
pasada (ya que `\log_2 N` es un número mucho más pequeño que `N`).

Si analizamos el espacio que consume, vemos que a cada paso la función `merge`
genera una nueva lista cuya longitud es la suma de los tamaños de las dos
listas, por lo que `merge_sort` duplica el espacio consumido.

## Resumen?

* Los ordenamientos de selección e inserción, presentados en la unidad
anterior son ordenamientos sencillos pero costosos en cantidad de
intercambios o de comparaciones.  Sin embargo, es posible conseguir
ordenamientos con mejor orden utilizando algoritmos recursivos.

* El algoritmo *Merge Sort* consiste en dividir la lista a ordenar
hasta que tenga 1 ó 0 elementos y luego combinar la lista de forma ordenada.
De esta manera se logra un tiempo proporcional a `N * log N`.  Tiene como
desventaja que siempre utiliza el doble de la memoria requerida por la lista a
ordenar.

## Ejercicios:

### Ejercicio 12.2: 
Mostrar los pasos del ordenamiento de la lista: `[6, 0, 3, 2, 5, 7, 4, 1]` con los métodos de inserción y con merge sort. ¿Cuáles son las principales diferencias entre los métodos? ¿Cuál usarías en qué casos?

### Ejercicio 12.3: 
Ordená la lista `[6, 0, 3, 2, 5, 7, 4, 1]` usando el método merge sort. Dibujá el árbol de recursión explicando las llamadas que se hacen en cada paso, y el orden en el que se realizan.

### Ejercicio 12.4: Escribí una función `merge_sort_3` que funcione igual que el merge sort pero
en lugar de dividir los valores en dos partes iguales, los divida en tres. Debrás escribir la función `merge(lista_1, lista_2, lista_3)`. ¿Cómo te parece que se va a comportar este método con respecto al merge sort original?

### Ejercicio 12.5: 
Rehace el último ejercicio de la sección anterior incorporando el mergesort a la comparación y al gráfico. Describí con tus palabras qué observas.



[Contenidos](../Contenidos.md) \| [Anterior (1 Ordenamientos sencillos de listas)](01_Ordenamiento_sencillo.md)

