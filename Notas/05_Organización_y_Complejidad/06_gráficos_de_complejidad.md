[Contenidos](../Contenidos.md) \| [Anterior (5 Complejidad de algoritmos)](05_Complejidad.md) \| [Próximo (7 Cierre de la quinta clase)](07_Cierre.md)

# 5.6 Gráficos de complejidad

## Grḉafico que comparan la complejidad de algoritmos

La siguiente función realiza una búsqueda secuencial de un elemento en una lkista. Devuelve la posición del elemento si lo encuentra y -1 si no lo encuentra.

```python
def busqueda_secuencial(lista,e):
    '''Si e está en la lista devuelve el índice de su primer aparición, 
    de lo contrario devuelve -1.
    '''
    pos = -1
    for i,z in enumerate(lista):
        if z == e:
            pos = i
            break
    return pos
```

Esta modificación de la función cuenta (y devuelve) adeḿas cuántas comparaciones (`z==e`) hace la función. Observá que devuelve un par de datos. 

```python
def busqueda_secuencial_(lista,e):
    '''Si e está en la lista devuelve el índice de su primer aparición, 
    de lo contrario devuelve -1.
    '''
    comps = 0 #inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 #sumo la comparación que estoy por hacer
        if z == e:
            pos = i
            break
    return pos, comps

```

Si querés acceder a la posición podés usar `busqueda_secuencial_(lista,e)_[0]` y para acceder a la cantidad de comparaciones que hizo `busqueda_secuencial_(lista,e)_[1]`.

### Ejercicio 5.16: Contar comparaciones en la búsqueda binaria.



- Introducir gráficos de lineas con Matplotlib básico para comparar algoritmos
- Contar comparaciones
- Ver 2do parcial 2020C1

### Ejercicio 5.17: Búsqueda binaria vs. búsqueda secuencial


1. Escribí una función `generar_lista(N)` que dado un `N <= 1000` genere una lista ordenada con `N` números diferentes entre 1 y 1000. Puede usar el método `sort()`` para ordenar.
2. Escribí una función `contar_promedio_comparaciones(N,k)` que dado un `N<=1000` y `k` entero, genere una lista ordenada como en el punto anterior y repita `k` veces lo siguiente: genere un nuevo elemento `1< e<1000` al azar y lo busque con ambos métodos de búsqueda y devuelva el promedio de las compraciones que realizó cada uno para las `k` búsquedas realizadas.
3. Por último, usá la función `contar_promedio_comparaciones(N,k)` con `k=25` fijo y `N` entre 1 y 250. Almacená en dos listas de longitud 250 los promedios de comparaciones que realiza cada uno de los métodos al buscar `e` en listas de longitudes desde 1 hasta 250. Graficá los resultados y explicá con tus palabras lo que observás.

Este ejercicio guardalo en `plot_bbin_vs_bsec.py`.


[Contenidos](../Contenidos.md) \| [Anterior (5 Complejidad de algoritmos)](05_Complejidad.md) \| [Próximo (7 Cierre de la quinta clase)](07_Cierre.md)

