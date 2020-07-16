[Contenidos](../Contenidos.md) \| [Anterior (7 Entorno de desarrollo integrado)](07_R_IDE.md) \| [Próximo (9 Algoritmos de búsqueda)](09_Algo_BSec_BBin.md)

# 2.8 Práctica: Iteración sobre listas

En esta sección, funciones, no python: algoritmos de bajo nivel sobre listas.

### Ejercicio 2.26: Búsqueda del máximo
Python tiene. Pero si lo queremos hacer...

`maximo.py`

estructura de una solución 


### Ejercicio 2.27: Invertir una lista
Escribir una función `invertir_lista(lista)` que dada una lista devuelva otra que tenga los mismos elementos en el orden inverso. Es decir, el que era el primer elemento de la lista de entrada deberá ser el último de la lista de salida y análogamente con los demás elementos.

Probarla con las siguientes listas:


`invlista.py`

### Ejercicio 2.28: Tablas de multiplicar
Escriba un programa que imprima de forma elegante las tablas de
multiplicar del 0 al 9 (sug: imprimir ’\\t’ como separador). Si puede, evite usar la multiplicación, use solo sumas.

`tablamult.py`

### Ejercicio 2.29: Propagación
Considere una fila con *n* personas una al lado de la otra. Las personas pueden estar infectadas con un virus, ser inmunes o ser suceptibles de enfermarse.
Representaremos esta situación con una lista *L* de longitud *n* que en cada posición tiene un 0 (inmune), un 1 (suceptible de enfermarse) o un -1 (tiene el virus). 
Este virus se propaga inmediatamente a toda persona suceptible de enfermarse que tenga a alguien enfermo a su lado. Las personas inmunes, no se enferman.


Escriba una función llamada `propagar` que reciba un vector con ceros, unos y menos unos y devuelva un vector en el que los menos unos se propagaron a sus vecion con uno. Guárdela en un archivo `propaga.py`.

Por ejemplo:
```python
>>> propagar([ 1, 1, 1, 0,-1, 1, 1, 1, 0, 1,-1, 1, 1])
[ 1, 1, 1, 0,-1,-1,-1,-1, 0,-1,-1,-1,-1]
>>> propagar([ 1, 1, 1,-1, 1, 1])
[-1,-1,-1,-1,-1,-1]
```

![Propagación](./fosforos.jpg) Propagación análoga a la del Ejercicio


[Contenidos](../Contenidos.md) \| [Anterior (7 Entorno de desarrollo integrado)](07_R_IDE.md) \| [Próximo (9 Algoritmos de búsqueda)](09_Algo_BSec_BBin.md)

