[Contenidos](../Contenidos.md) \| [Anterior (1 Ordenamientos sencillos de listas)](01_Ordenamiento_sencillo.md) \| [Próximo (3 Cierre de la clase de Ordenamiento)](03_Cierre.md)

# 11.2 Divide y reinarás

El problema del ordenamiento es un problema fundamental y hay [muchísimos algoritmos que lo resuelven](https://www.youtube.com/watch?v=kPRA0W1kECg). Los métodos de ordenamiento vistos en la sección anterior eran métodos
iterativos cuyo tiempo de ejecución era cuadrático.

Veremos ahora el **merge sort** que es un algoritmo un poco más complejo conceptualmente pero menos complejo computacionalmente. El algoritmo está basado en una idea muy fecunda en el diseño de algoritmos eficientes que se denomina **divide y reinarás** (ó _divide and conquer_ en inglés). 

Divide y reinarás es un paradigma de diseño de algoritmos recursivos que trabaja partiendo (dividiendo) el problema original en subproblemas del mismo tipo pero más sencillos de resolver. Las soluciones de estos subproblemas luego se combinan para obtner una solución del problema original. 

La correctitud de los algoritmos de este tipo suele probarse utilizando la inducción matemática y el cálculo de su complejidad involucra la resolución de ecuaciones de recurrencia cuyos detalles escapan el alcance de este curso.

## El algoritmo *merge sort* (u odenamiento por mezcla)

![con colores](https://img.devrant.com/devrant/rant/r_950434_EjPWY.gif)

El *merge sort* se basa en la siguiente idea:

* Si la lista es pequeña (vacía o de tamaño 1) ya está ordenada y
no hay nada que hacer. De lo contrario hacer lo siguiente:
* Dividir la lista al medio, formando dos sublistas de (aproximadamente) el
mismo tamaño cada una.
* Ordenar cada una de esas dos sublistas (usando
este mismo método).
* Una vez que se ordenaron ambas sublistas, intercalarlas (mergearlas)  de manera ordenada.

Por ejemplo, si la lista original es `[6, 7, -1, 0, 5, 2, 3, 8]`
deberemos ordenar recursivamente `[6, 7, -1, 0]` y
`[5, 2, 3, 8]` con lo cual obtendremos `[-1, 0, 6, 7]` y
`[2, 3, 5, 8]`.  Si intercalamos ordenadamente las dos listas
ordenadas obtenemos la solución buscada:
`[-1, 0, 2, 3, 5, 6, 7, 8]`.

Veamos otro ejemplo con un gif animado:

![mergesort](./Merge-sort-example-300px.gif)

Diseñemos la función `merge_sort(lista)`:

* Si lista es pequeña (vacía o de tamaño 1) ya está ordenada y
no hay nada que hacer. Se devuelve lista original.
* De lo contrario:
  * `medio = len(lista) // 2`
  * `izq = merge_sort(lista[:medio])`
  * `der = merge_sort(lista[medio:])`
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
  * Agregar el elemento `lista1[i]` al final de la lista `resultado`.
  * Incrementar el índice `i`.
* de lo contrario:
  * Agregar el elemento `lista2[j]` al final de la lista `resultado`.
  * Incrementar el índice `j`.


* Una vez que una de las dos listas se termina, simplemente hay que
agregar todo lo que queda en la otra al final de la lista `resultado`.

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

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado

l=al_azar(30)
print(l)
print(merge_sort(l))
```

El método **divide y reinarás** que hemos usado para resolver el problema de ordenar una lista puede aplicarse también en otras situaciones. Hace falta que sea posible resolver el problema partiéndolo en varios subproblemas de tamaño menor, resolver cada uno de esos subproblemas por separado aplicando
la misma técnica (en nuestro caso ordenar por mezcla cada una de las dos
sublistas), y finalmente juntar estas soluciones parciales en una solución
completa del problema mayor (en nuestro caso la intercalación ordenada de las
dos sublistas ordenadas).

Como siempre sucede con las soluciones recursivas, debemos encontrar un caso
base en el cual no se aplica la llamada recursiva (en nuestro caso: si la lista tiene largo cero o uno, ya está ordenada y no hay nada que hacer). Además debemos asegurar que siempre se alcanza el caso base, y en nuestro caso aseguramos eso porque, si no estamos en el caso base, la lista se divide en mitades decrementando su longitud.

El método **divide y reinarás** es fecundo y ha dado lugar a algoritmos muy eficientes para tareas muy discímiles como multiplicar matrices, calcular la transformada de Fourier o realizar análisis sintácticos (parsear).

### ¿Cuánto cuesta el *Merge sort*?

Supongamos que tenemos que ordenar una lista de l longitud  `N` . Observamos lo siguiente:

* Para intercalar dos listas de longitud `N/2` hace falta recorrer
ambas listas que en total tienen `N` elementos. La cantidad de operaciones resulta proporcional a `N`. Llamemos `a * N` a ese tiempo.

* Si llamamos `T(N)` al tiempo que tarda el algoritmo en ordenar
una lista de longitud `N`, vemos que `T(N) = 2 * T(N/2) + a * N`.

* Además, cuando la lista es pequeña, la operación es de tiempo
constante: `T(1) = T(0) = b`.

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

Pero si `N = 2^k` entonces `k = log2(N)`, y por lo tanto hemos demostrado
que:

`T(N) = b * N + a * N * log2(N).`

Como lo que nos interesa es aproximar el valor, diremos (despreciando el
término de menor orden) que

` T(N) ~ N * log2(N) `

Dado que `log2(N)` es un número mucho más pequeño que `N`, hemos mostrado entonces que el merge sort se porta mucho mejor (es decir, es más eficiente) que los tres métodos de ordenamiento que discutimos en la sección anterior (que eran cuadráticos).

Si analizamos el espacio que consume, vemos que a cada paso la función `merge`
genera una nueva lista cuya longitud es la suma de los tamaños de las dos
listas, por lo que `merge_sort` usa el doble de espacio que la lista de entrada.

## Resumen

* Los métodos de ordenamiento de selección, inserción y burbujeo presentados en la sección anterior son métodos conceptualmente sencillos pero costosos en cantidad de operaciones (intercambios y/o comparaciones).  Sin embargo, es posible conseguir métodos más eficientes usando algoritmos recursivos.

* El algoritmo *merge sort* consiste en dividir la lista a ordenar
hasta que tenga 1 ó 0 elementos y luego combinar la lista de forma ordenada.
De esta manera se logra un tiempo proporcional a `N * log2(N)`.

## Ejercicios:

### Ejercicio 11.5: 
Mostrar los pasos del ordenamiento de la lista: `[6, 0, 3, 2, 5, 7, 4, 1]` con los métodos de inserción y con merge sort. ¿Cuáles son las principales diferencias entre los métodos? ¿Cuál usarías en qué casos?

### Ejercicio 11.6: 
Ordená la lista `[6, 0, 3, 2, 5, 7, 4, 1]` usando el método merge sort. Dibujá el árbol de recursión explicando las llamadas que se hacen en cada paso, y el orden en el que se realizan.

### Ejercicio 11.7: 
Rehace el último ejercicio de la sección anterior ([Ejercicio 11.4](../11_Ordenamiento/01_Ordenamiento_sencillo.md#ejercicio-114)) incorporando el mergesort a la comparación y al gráfico. Describí con tus palabras qué observas.

### Ejercicio 11.8: 
Escribí una función `merge3sort` que funcione igual que el merge sort pero
en lugar de dividir la lista de entrada en dos partes, la divida en tres partes. Debrás escribir la función `merge3(lista1, lista2, lista3)`. ¿Cómo te parece que se va a comportar este método con respecto al merge sort original?



[Contenidos](../Contenidos.md) \| [Anterior (1 Ordenamientos sencillos de listas)](01_Ordenamiento_sencillo.md) \| [Próximo (3 Cierre de la clase de Ordenamiento)](03_Cierre.md)

