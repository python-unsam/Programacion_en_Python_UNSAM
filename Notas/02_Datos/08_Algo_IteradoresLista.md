[Contenidos](../Contenidos.md) \| [Anterior (7 Entorno de desarrollo integrado)](07_R_IDE.md) \| [Próximo (9 Algoritmos de búsqueda)](09_Algo_BSec_BBin.md)

# 2.8 Práctica: Iteración sobre listas

En esta sección seguiremos usando Python, pero nos concentraremos en la parte algorítmica. Vas a escribir funciones sencillas (y no tanto) que realicen operaciones sobre listas.

### Ejercicio 2.26: Búsqueda del máximo
En este primer ejercicio tenés que escribir una función que busque el elemento máximo de una lista. Python tiene el comando `max` que ya hace esto, pero como práctica te propomenos que completes el siguiente código y lo guardes en un archivo `maximo.py`:

```python
def maximo(lista):
    m=lista[0] # En principio podemos decir que el máximo es el primer elemento de la lista.
    for e in lista: # Recorro la lista y voy guardando el mayor
        ...
    return m
```

### Ejercicio 2.27: Invertir una lista
Escribí una función `invertir_lista(lista)` que dada una lista devuelva otra que tenga los mismos elementos en el orden inverso. Es decir, el que era el primer elemento de la lista de entrada deberá ser el último de la lista de salida y análogamente con los demás elementos.


```python
def invertir_lista(lista):
    invertida = []
    for e in lista: # Recorro la lista
        ... #agrego el elemento e al principio de la lista invertida
    return m
```

Guardá la función en el archivo `invlista.py` y probarla con las siguientes listas:
`[1,2,3,4,5]`
`['Bogotá', 'Rosario', 'Santiago', San Fernando', 'San Miguel']`

### Ejercicio 2.28: Tablas de multiplicar
Escribí un programa `tablamult.py` que imprima de forma prolija las tablas de
multiplicar del 1 al 9 usando f-strings. Si podés, evitá usar la multiplicación, usando sólo sumas alcanza.


### Ejercicio 2.29: Propagación
Imaginate una fila con varios fósforos uno al lado del otro. Los fósforos pueden estar en tres estados: nuevos, ya gastados (carbonizado) o prendidos fuego.
Representaremos esta situación con una lista *L* con un elemento por fósforo, que en cada posición tiene un 1 (nuevo), un 0 (carbonizado) o un -1 (encendido). 
El fuego se propaga inmediatamente de un fósforo encendido a cualquier fósoforo nuevo que tenga a su lado. Los fósforos carbonizados no se encienden nuevamente.

Escribí una función llamada `propagar` que reciba un vector con 0, 1 y -1 y devuelva un vector en el que los -1 se propagaron a sus vecinos con 1. Guardalo en un archivo `propaga.py`.

Por ejemplo:
```python
>>> propagar([ 1, 1, 1, 0,-1, 1, 1, 1, 0, 1,-1, 1, 1])
[ 1, 1, 1, 0,-1,-1,-1,-1, 0,-1,-1,-1,-1]
>>> propagar([ 1, 1, 1,-1, 1, 1])
[-1,-1,-1,-1,-1,-1]
```

![Propagación](./fosforos.jpg) Propagación análoga a la del Ejercicio


[Contenidos](../Contenidos.md) \| [Anterior (7 Entorno de desarrollo integrado)](07_R_IDE.md) \| [Próximo (9 Algoritmos de búsqueda)](09_Algo_BSec_BBin.md)

