[Contenidos](../Contenidos.md) \| [Anterior (1 Intro a la Recursión)](01_Recursion.md)

# 11.2 Recursión

## Ejercicios


### Ejercicio 11.2: 
Escribir una función recursiva que calcule recursivamente el n-ésimo número
triangular (es decir, el número *1 + 2 + 3 + ... + n*).

### Ejercicio 11.3: 
Escribir una función recursiva que reciba un número positivo, n, y devuelva
la cantidad de dígitos que tiene.


### Ejercicio 11.4: 
Escribir una función recursiva que reciba 2 enteros, *n* y *b*, y devuelva
`True` si *n* es potencia de *b*.

Ejemplos:
```
es_potencia(8, 2) -> True
es_potencia(64, 4) -> True
es_potencia(70, 10) -> False
```



### Ejercicio 11.5: 
Escribir una funcion recursiva que reciba como parámetros dos cadenas *a* y
*b*, y devuelva una lista con las posiciones en donde se encuentra *b*
dentro de *a*.

Ejemplo:
```
posiciones_de("Un tete a tete con Tete", "te") -> [3, 5, 10, 12, 21]
```



### Ejercicio 11.6: 
Escribir dos funciones mutualmente recursivas ``par(n)` e `impar(n)` que
determinen la paridad del numero natural dado, usando solo que:

* 1 es impar.
* Un número mayor que uno es impar (resp. par) si su antecesor es par (resp. impar).


### Ejercicio 11.7: 
Escribir una funcion recursiva que encuentre el mayor elemento de una lista. (sin usar `max()`).


### Ejercicio 11.8: 
Escribir una función recursiva para replicar los elementos de una lista
una cantidad n de veces. Por ejemplo:
```
replicar([1, 3, 3, 7], 2) -> ([1, 1, 3, 3, 3, 3, 7, 7])
```

_Sugerencia: hacé la recursión el el largo de la lista._

### Ejercicio 11.9: 
El [triángulo de Pascal](https://es.wikipedia.org/wiki/Tri%C3%A1ngulo_de_Pascal) es un arreglo triangular de números que se define de la siguiente manera: Las filas se enumeran desde *n = 0*, de arriba hacia
abajo. Los valores de cada fila se enumeran desde *k = 0* (de izquierda a
derecha). Los valores que se encuentran en los bordes del triángulo son
1. Cualquier otro valor se calcula sumando los dos valores contiguos de
la fila de arriba.

![Pascal animado](./PascalTriangleAnimated2.gif)

Escribir la función recursiva `pascal(n, k)` que calcula el valor que se
encuentra en la fila `n` y la columna `k`. 

Ejemplo:
```python
>>> pascal(5, 2)
10
```



### Ejercicio 11.10: 
Escribir una función recursiva que reciba un conjunto de caracteres únicos,
y un número *k*, e imprima todas las posibles cadenas de longitud *k* formadas
con los caracteres dados (permitiendo caracteres repetidos).

Ejemplo: 

```python
>>> combinaciones(['a', 'b', 'c'], 2)
aa ab ac ba bb bc ca cb cc
```


### Ejercicio 11.11: 
Escribir una función recursiva que implemente la búsqueda binaria de un elemento *e* en una lista ordenada *L*. Para esto complete el siguiente código:

```python
def busqueda(L, e):
    '''Pre: L es una lista con los elementos en orden ascendente.
    Post: Devuelve True si e esta en L y False si no'''

    def busqueda_binaria(L, e, low, high):
        #Funcion recursiv a que va achicando high - low
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        #AQUI COMPLETAR

    if len(L) == 0:
        return False
    else:
        return busqueda_binaria(L, e, 0, len(L) - 1)
```

_Observación_: La función `busqueda()` **envuelve** a la función `busqueda_binaria()`. Es un **wrapper** (envoltorio).

### Ejercicio 11.12: 
La implementación recursiva inmediata del cálculo del número de Fibonacci
(F(n) = F(n-1) + F_(n-2), F(0) = 0, F(1)= 1) es ineficiente porque muchas de las ramas calculan reiteradamente los mismos valores.

Escribir una función `fibonacci(n)` que calcule el *n*-ésimo número
de Fibonacci de forma recursiva pero que utilice un diccionario para almacenar
los valores ya computados y no computarlos más de una vez.

_Observación_: Será necesario implementar una función *wrapper* (es decir, una función que envuelva a otra) como en el ejercicio anterior para cumplir con la firma de la función pedida.




[Contenidos](../Contenidos.md) \| [Anterior (1 Intro a la Recursión)](01_Recursion.md)

