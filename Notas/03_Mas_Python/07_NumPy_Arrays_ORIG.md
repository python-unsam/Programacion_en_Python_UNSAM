[Contenidos](../Contenidos.md) \| [Anterior (6 NumPy)](07_NumPy_Arrays.md) \| [Próximo (8 El album de Figuritas+)](08_Figuritas.md)

# 3.7 NumPy

Esta es una introducción al módulo NumPy.

NumPy (**Numerical Python**) es una biblioteca de Python (una colección de módulos) de código abierto que tiene aplicaciones en casi todos los campos de las ciencias y de la ingeniería.  Es el estándar para trabajar con datos numéricos en Python. Muchos módulos como Pandas, SciPy, Matplotlib, scikit-learn, scikit-image usan NumPy.

Esta biblioteca permite trabajar cómodamente con matrices multidimensionales por medio del tipo  **ndarray**, un objeto n-dimensional homogéneo (con entradas del mismo tipo), y con métodos para operar eficientemente sobre él. NumPy puede usarse para una amplia variedad de operaciones matemáticas sombre matrices. Le agrega a Python estructuras de datos muy potentes osbre las que se puede calcular y operar matemáticamente con eficiencia y a un alto nivel.

## Instalar NumPy

Si no lo tenés instalado (primero probá imoprtarlo, es muy probable que ya lo tengas) podés instalarlo escribiendo :

```bash
conda install numpy
```

o

```bash
pip install numpy
```

## Importar  NumPy

Cuando quieras usar NumPy en Python, primero tenés que importarlo:

```python
import numpy as np
```

Acortamos `numpy` a `np` para ahorrar tiempo y mantener el código estandarizado. Todes escriben `np`.


## ¿Cuál es la diferencia entre listas y arreglos?

NumPy ofrece varias formas muy eficientes de crear vectores y manipular datos numericos en su interior. Mientras que una lista de Python puede contener diferentes tipos de datos en su interior, los elementos de un vector numpy serán todos del mismo tipo. De esta forma numpy puede asegurar una alta perforance en las operaicones matemáticas.

Además, los arreglos están pensados para tener un tamaño fijo, mientras que las listas están diseñadas para agregar y sacar elementos. Son estructuras de datos similares desde un punto de vista superficial, pero muy diferentes en cuanto a las posibilidades y perfomances que brindan. 

Las operaciones matemáticas sobre vectores de numpy son más rápidas que sobre listas. Además los vectores ocupan menos memoria que las listas análogas. Pero cambiar el tamaño de una lista es algo muy sencilo mientras que el de un vector es costoso. O mezclar diferentes tipos de datos es posible en las listas pero imposible en los vectores de NumPy.

## Arreglos n-dimensionales

Los vectores (unidimensionales) y matrices (bidimensiones) se generalizan a arreglos n-dimensionales. Esta estructura de datos es la central de la biblioteca NumPy. Un arreglo (`ndarray`) es una grilla de valores que contiene información sobre los datos crudos, cómo ubicarlos y cómo interpretarlos. Tiene una grilla de elementos que pueden ser indexados de diversas maneras. Los elementos de un arreglo son todos del mismo tipo, frecuentemente abreviado como `dtype`.

Un arreglo puede ser indexado por tuplas de enteros no negativos, por variables booleanas, por otro arreglo o por enteros. El rango (`rank`) de un arreglo es su número de dimensiones. Su forma (`shape`) es una tupla de enteros que dice su tamaño en cada dimensión.

Una forma de inicializar un arreglo de NumPy es mediante una lista de números. Esto nos da un vector (arreglo de dimensión uno). Usando listas anidadas, podemos definir arreglos de más altas dimensiones.

Por ejemplo:

```python
>>> a = np.array([1, 2, 3, 4, 5, 6])
```

o:

```python
>>> a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
```

Podemos acceder a los elementos de un arreglo usando corchetes. Acordate que los índices comienzan a contar en 0. Esto significa que si querés acceder al primer elemento, vas a acceder al elemento “0”.

```python
>>> print(a[0]) #si tiene múltiples dimensiones, esto me da una "rebanada" de una dimension menos
[1 2 3 4]
>>> print(a[2]) #  otra rebanada
array([ 9, 10, 11, 12])
>>> print(a[2][3]) #accedo al cuarto elemento del tercer vector de a
12
>>> print(a[2,3]) # o, equivalentemente, accedo al elemento en la tercera fila y cuarta columna de a
12
```


## Más información sobre arreglos


Ocasionalmente vas a ver que alguien se refiere a un arreglo como un  “ndarray” que es una forma breve de decir arreglo n-dimensional. Un arreglo n-dimensional es simplemente un arreglo con n dimensiones. Recordemos que cuando son unidimensionales los llamamos vectores y si son bidimensionales los llamamos matrices.

**¿Qué atributos tiene un arreglo?**

Un arreglo es usualmente un contenedor de tamaño fijo de elementos del mismo tipo. Su forma (shape) es una tupla de enteros no negativos que especifica el tamaño del arreglo en cada dimensión. Tiene tantas dimensiones como coordenadas en la tupla.

En NumPy, las dimensiones se llaman **axes** (ejes). Esto dignifica que si tenés una arrglo bidimensional que se ve así:

```
[[0., 0., 0.],
 [1., 1., 1.]]
```

el arreglo tendrá dos ejes. El primer eje tiene tamaño dos, el segundo tamaño tres (si, se cuentan primero filas, luego columnas).

De la misma forma que los otros objetos contenedores de Python, los elementos de un arreglo pueden ser accedidos y modificados usando índices y rebanadas.

## Crear un arreglo básico

Para crear un arreglo de NumPy podés usar la función `np.array()`.
Lo único que necesitás es pasarle una lista. Si querés, podés especificar el tipo de datos que querés que tenga. 

```python
>>> import numpy as np
>>> a = np.array([1, 2, 3])
```

Vamos a representar la creación con este gráfico:

![./np_array.png](./np_array.png)

_Ojo, estas visualizaciones son simplificaciones para representar lo que esta pasando y darte un entendimiento básico de los conceptos y mecanismos de NumPy. Los arreglos y sus operaciones tienen aspectos más complejos que los que quedan capturados en estos dibujitos._

A parte de poder crear una arreglo a partir de una secuencia de elementos, podés crear un arreglo lleno de `0`’s:

```python
>>> np.zeros(2)
array([0., 0.])
```

O uno lleno de `1`’s:

```python
>>> np.ones(2)
array([1., 1.])
```

¡O incluso uno no inicializado! La función `empty` crea un arreglo cuyo contenido inicial depende del estado de la memoria. Usar `empty` en lugar de  `zeros` (o `ones`) es la velocidad - al no inicilizar los valores no perdemos tiempo. ¡Pero asegurate de ponerle valores con sentido luego!

```python
>>> # Crea un arreglo con dos elementos
>>> np.empty(2)
array([ 3.14, 42.  ])  # puede variar
```

También podés crear vectores a partir de un rango de valores:

```python
>>> np.arange(4)
array([0, 1, 2, 3])
```

También un vector que contiene elementos equiespaciados, especificando el **primer número**, el **límite**, y el **paso**.

```python
>>> np.arange(2, 9, 2)
array([2, 4, 6, 8])
```
El límite nunca está en la lista. 

También podés usar `np.linspace()` para crear un vector especificando el **primer número**, el **último número**, y la **cantidad** de elementos:

```python
>>> np.linspace(0, 10, num=5)
array([ 0. ,  2.5,  5. ,  7.5, 10. ])
```


**Especificar el tipo de datos**

Si no lo especificá, el tipo de datos (por omisión) de los arreglos es el punto flotante (`np.float64`). Sin embargo, podés explicitar otro tipo de datos usando la palabra clave `dtype`.

```python
>>> x = np.ones(2, dtype=np.int64)
>>> x
array([1, 1])
```

En estos dos casos el 64 de los tipos de datos se refiere a la cantidad de bits, 64 bits. 

## Agregar, borrar y ordenar elementos

Ordenar un vector es sencillo usando `np.sort()`. 
Por ejemplo, si comenzás con este vector:

```python
>>> arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
```

Podés ordenar sus elementos con:

```python
>>> np.sort(arr)
array([1, 2, 3, 4, 5, 6, 7, 8])
```
Fijate que el vector `arr` quedó desordenado. `sort` simplemente devolvió una copia ordenada de los datos pero no modificó el original.

Otra operación usual es la concatenación. Si empezás con estos dos vectores:

```python
>>> a = np.array([1, 2, 3, 4])
>>> b = np.array([5, 6, 7, 8])
```

los podés concatenar usado `np.concatenate()`.

```python
>>> np.concatenate((a, b))
array([1, 2, 3, 4, 5, 6, 7, 8])
```

Un ejemplo un poco más complejo es el siguiente: Si tenés:

```python
>>> x = np.array([[1, 2], [3, 4]])
>>> y = np.array([[5, 6]])
```

Los podés concatenar usando:

```python
>>> np.concatenate((x, y), axis=0)
array([[1, 2],
 [3, 4],
 [5, 6]])
```

Para sacar elementos de un arreglo, lo más sencillo es usar los índices para seleccionar los que queremos conservar.


## Conocer el tamaño, dimensiones y forma de un arreglo


`ndarray.ndim` te dice la cantidad de ejes (o dimensiones) de arreglo.

`ndarray.shape` te va a dar una tupla de enteros que indican la cantidad de elementos en cada eje. Si tenés una matriz con 2 filas y 3 columnas de va a dar `(2, 3)`.

`ndarray.size` te dice la cantidad de elementos (cantidad de numeros) de tu arreglo. Es el producto de la tupla `shape`. En el ejemplo del renglón anterior, el `size` es 6.

Por ejemplo, si creás este arreglo de tres dimensiones:

```python
>>> array_example = np.array([[[0, 1, 2, 3],
...                            [4, 5, 6, 7]],
...
...                           [[0, 1, 2, 3],
...                            [4, 5, 6, 7]],
...
...                           [[0 ,1 ,2, 3],
...                            [4, 5, 6, 7]]])
```

Vas a tener
```python
>>> array_example.ndim # cantidad de dimensiones
3
>>> array_example.shape # cantidad de elementos en cada eje 
(3, 2, 4)
>>> array_example.size # total de elementos 3*2*4
24
```

## Cambiar la forma de un arreglo

Usando `arr.reshape()` le podés dar una nueva forma a tu arreglo sin cambiar los datos. Solo tené en cuenta que antes y después del reshape el arreglo tiene que tener la misma cantidad de elementos. Por ejemplo, si comenzás con un arreglo con 12 elementos, tendrás que asegurarte que el nuevo arreglo siga teniendo 12 elementos.

Por ejemplo:

```python
>>> a = np.arange(6)
>>> print(a)
[0 1 2 3 4 5]
```

Podés usar `reshape()` para cambiarle la forma y que en lugar de ser un vectore de 6 elementos, sea una matriz de 3 filas y dos columnas:

```python
>>> b = a.reshape(3, 2)
>>> print(b)
[[0 1]
 [2 3]
 [4 5]]
```

## Agregar un nuevo eje a un arreglo

A veces pasa que tenemos un vector con n elementos y necesitamos pensarlo como una matriz de una fila y seis columnas o de seis filas y una columna. Podés usar `np.newaxis` para agregarle dimensiones a un vector existente.

Usando `np.newaxis` una vez podés incrementar la dimensión de tu arreglo en uno. Por ejemplo podés pasar de un vector a una matriz o de una matriz a un arreglo tridimensional, etc.

Por ejemplo, si comenzás con este vector:

```python
>>> a = np.array([1, 2, 3, 4, 5, 6])
>>> a.shape
(6,)
```

Podés usar `np.newaxis` para agregarle una dimensión y convertirlo en un vector fila:

```python
>>> vec_fila = a[np.newaxis, :]
>>> vec_fila.shape
(1, 6)
```

Or, para convertirlo en un vector columna, podés unsertar un eje en la segunda  dimensión:

```python
>>> vec_col = a[:, np.newaxis]
>>> vec_col.shape
(6, 1)
```

## Índices y rebanadas

Los arreglos de NumPy los podes indexar y rebanar como hicimos con las listas.

```python
>>> data = np.array([1, 2, 3])
```


```python
>>> data[1]
2
>>> data[0:2]
array([1, 2])
>>> data[1:]
array([2, 3])
>>> data[-2:]
array([2, 3])
```

Lo podés visualizar así:

![./np_indexing.png](./np_indexing.png)

Otra operación muy útil es seleccionar los elementos que cumplen cierta condición. Por ejemplo, si comenzás con un arreglo así:

```python
>>> a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
```

Podés imprimir todos los valores menores que cinco.

```python
>>> print(a[a < 5])
[1 2 3 4]
```

También podés seleccionar, por ejemplo, aquellos elementos mayores o iguales que 5 y usar el resultado para indexar el arreglo.

```python
>>> five_up = (a >= 5)
>>> print(a[five_up])
[ 5  6  7  8  9 10 11 12]
```

Es interesante que `five_up` da un vectore de valores booleanos. `True` si satisface la condición y `False` si no la satisface.

Podés seleccionar los elementos pares:

```python
>>> divisible_by_2 = a[a%2==0]
>>> print(divisible_by_2)
[ 2  4  6  8 10 12]
```


Usando los operadores lógicos `&` y `|` podés combinar dos o más condiciones.

Ya sea para seleccionar elementos directamente:
```python
>>> c = a[(a > 2) & (a < 11)]
>>> print(c)
[ 3  4  5  6  7  8  9 10]
```

o para definir una nueva variable booleana:
```python
>>> five_up = (a > 5) | (a == 5)
>>> print(five_up)
[[False False False False]
 [ True  True  True  True]
 [ True  True  True True]]
```

Finalmente, podés suar `np.nonzero()` para obtener las coordenadas de ciertos elementos de un arreglo.

Si empezamos con este arreglo:

```python
>>> a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
```

Podés usar `np.nonzero()` para imprimir los índices de los elementos que son, digamos, menores que 5:

```python
>>> b = np.nonzero(a < 5)
>>> print(b)
(array([0, 0, 0, 0]), array([0, 1, 2, 3]))
```

En este ejemplo, la respuesta es una tupla de arreglos: uno por cada dimensión. El primer arreglo representa las filas de los elementos que satisfacen la condición y el segundo sus columnas.

Si querés generar la lista de coordenadas donde se encuetran estos elementos, podés zipear los arreglos, convertir el resultado a una lista e imprimir la lista:

```python
>>> list_of_coordinates= list(zip(b[0], b[1]))
```

Surge naturalmente la pregunta: ¿porqué tengo que convertir el objeto `zip` a una lista? Vermos en la segunda mitad de la materia más detalles sobre generadores en Python para entender exactamente lo que está pasando aquí. Simplemente digamos que al zipear `b[0]`, `b[1]` no se genera la lista realmente, sino potencialmente. Solo al solicitar sus elementos (con `list`) se generan realmente las coordenadas.

```python
>>> for coord in list_of_coordinates:
...     print(coord)
(0, 0)
(0, 1)
(0, 2)
(0, 3)
```


You can also use `np.nonzero()` to print the elements in an array that are less than 5 with:

```python
>>> print(a[b])
[1 2 3 4]
```


If the element you’re looking for doesn’t exist in the array, then the returned array of indices will be empty. For example:

```python
>>> not_there = np.nonzero(a == 42)
>>> print(not_there)
(array([], dtype=int64), array([], dtype=int64))
```




## How to create an array from existing data


You can easily use create a new array from a section of an existing array.

Let’s say you have this array:

```python
>>> a = np.array([1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
```


You can create a new array from a section of your array any time by specifying where you want to slice your array.

```python
>>> arr1 = a[3:8]
>>> arr1
array([4, 5, 6, 7, 8])
```


Here, you grabbed a section of your array from index position 3 through index position 8.

You can also stack two existing arrays, both vertically and horizontally. Let’s say you have two arrays, `a1` and `a2`:

```python
>>> a1 = np.array([[1, 1],
...                [2, 2]])
```


```python
>>> a2 = np.array([[3, 3],
...                [4, 4]])
```


You can stack them vertically with `vstack`:

```python
>>> np.vstack((a1, a2))
array([[1, 1],
 [2, 2],
 [3, 3],
 [4, 4]])
```


Or stack them horizontally with `hstack`:

```python
>>> np.hstack((a1, a2))
array([[1, 1, 3, 3],
 [2, 2, 4, 4]])
```


You can split an array into several smaller arrays using `hsplit`. You can specify either the number of equally shaped arrays to return or the columns _after_ which the division should occur.

Let’s say you have this array:

```python
>>> x = np.arange(1, 25).reshape(2, 12)
>>> x
array([[ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12],
 [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]])
```


If you wanted to split this array into three equally shaped arrays, you would run:

```python
>>> np.hsplit(x, 3)
[array([[1,  2,  3,  4],
 [13, 14, 15, 16]]), array([[ 5,  6,  7,  8],
 [17, 18, 19, 20]]), array([[ 9, 10, 11, 12],
 [21, 22, 23, 24]])]
```


If you wanted to split your array after the third and fourth column, you’d run:

```python
>>> np.hsplit(x, (3, 4))
[array([[1, 2, 3],
 [13, 14, 15]]), array([[ 4],
 [16]]), array([[ 5, 6, 7, 8, 9, 10, 11, 12],
 [17, 18, 19, 20, 21, 22, 23, 24]])]
```



You can use the `view` method to create a new array object that looks at the same data as the original array (a _shallow copy_).

Views are an important NumPy concept! NumPy functions, as well as operations like indexing and slicing, will return views whenever possible. This saves memory and is faster (no copy of the data has to be made). However it’s important to be aware of this - modifying data in a view also modifies the original array!

Let’s say you create this array:

```python
>>> a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
```


Now we create an array `b1` by slicing `a` and modify the first element of `b1`. This will modify the corresponding element in `a` as well!

```python
>>> b1 = a[0, :]
>>> b1
array([1, 2, 3, 4])
>>> b1[0] = 99
>>> b1
array([99,  2,  3,  4])
>>> a
array([[99,  2,  3,  4],
 [ 5,  6,  7,  8],
 [ 9, 10, 11, 12]])
```


Using the `copy` method will make a complete copy of the array and its data (a _deep copy_). To use this on your array, you could run:

```python
>>> b2 = a.copy()
```



## Basic array operations


Once you’ve created your arrays, you can start to work with them. Let’s say, for example, that you’ve created two arrays, one called “data” and one called “ones”

![./np_array_dataones.png](./np_array_dataones.png)

You can add the arrays together with the plus sign.

```python
>>> data = np.array([1, 2])
>>> ones = np.ones(2, dtype=int)
>>> data + ones
array([2, 3])
```


![./np_data_plus_ones.png](./np_data_plus_ones.png)

You can, of course, do more than just addition!

```python
>>> data - ones
array([0, 1])
>>> data * data
array([1, 4])
>>> data / data
array([1., 1.])
```


![./np_sub_mult_divide.png](./np_sub_mult_divide.png)

Basic operations are simple with NumPy. If you want to find the sum of the elements in an array, you’d use `sum()`. This works for 1D arrays, 2D arrays, and arrays in higher dimensions.

```python
>>> a = np.array([1, 2, 3, 4])
```


```python
>>> a.sum()
10
```


To add the rows or the columns in a 2D array, you would specify the axis.

If you start with this array:

```python
>>> b = np.array([[1, 1], [2, 2]])
```


You can sum the rows with:

```python
>>> b.sum(axis=0)
array([3, 3])
```


You can sum the columns with:

```python
>>> b.sum(axis=1)
array([2, 4])
```



## Broadcasting

There are times when you might want to carry out an operation between an array and a single number (also called _an operation between a vector and a scalar_) or between arrays of two different sizes. For example, your array (we’ll call it “data”) might contain information about distance in miles but you want to convert the information to kilometers. You can perform this operation with:

```python
>>> data = np.array([1.0, 2.0])
>>> data * 1.6
array([1.6, 3.2])
```


![./np_multiply_broadcasting.png](./np_multiply_broadcasting.png)

NumPy understands that the multiplication should happen with each cell. That concept is called **broadcasting**. Broadcasting is a mechanism that allows NumPy to perform operations on arrays of different shapes. The dimensions of your array must be compatible, for example, when the dimensions of both arrays are equal or when one of them is 1. If the dimensions are not compatible, you will get a `ValueError`.


## More useful array operations


NumPy also performs aggregation functions. In addition to `min`, `max`, and `sum`, you can easily run `mean` to get the average, `prod` to get the result of multiplying the elements together, `std` to get the standard deviation, and more.

```python
>>> data.max()
2.0
>>> data.min()
1.0
>>> data.sum()
3.0
```


![./np_aggregation.png](./np_aggregation.png)

Let’s start with this array, called “a”

```python
>>> a = np.array([[0.45053314, 0.17296777, 0.34376245, 0.5510652],
...               [0.54627315, 0.05093587, 0.40067661, 0.55645993],
...               [0.12697628, 0.82485143, 0.26590556, 0.56917101]])
```


It’s very common to want to aggregate along a row or column. By default, every NumPy aggregation function will return the aggregate of the entire array. To find the sum or the minimum of the elements in your array, run:

```python
>>> a.sum()
4.8595784
```


Or:

```python
>>> a.min()
0.05093587
```


You can specify on which axis you want the aggregation function to be computed. For example, you can find the minimum value within each column by specifying `axis=0`.

```python
>>> a.min(axis=0)
array([0.12697628, 0.05093587, 0.26590556, 0.5510652 ])
```


The four values listed above correspond to the number of columns in your array. With a four-column array, you will get four values as your result.


## Creating matrices

You can pass Python lists of lists to create a 2-D array (or “matrix”) to represent them in NumPy.

```python
>>> data = np.array([[1, 2], [3, 4]])
>>> data
array([[1, 2],
 [3, 4]])
```


![./np_create_matrix.png](./np_create_matrix.png)

Indexing and slicing operations are useful when you’re manipulating matrices:

```python
>>> data[0, 1]
2
>>> data[1:3]
array([[3, 4]])
>>> data[0:2, 0]
array([1, 3])
```


![./np_matrix_indexing.png](./np_matrix_indexing.png)

You can aggregate matrices the same way you aggregated vectors:

```python
>>> data.max()
4
>>> data.min()
1
>>> data.sum()
10
```


![./np_matrix_aggregation.png](./np_matrix_aggregation.png)

You can aggregate all the values in a matrix and you can aggregate them across columns or rows using the `axis` parameter:

```python
>>> data.max(axis=0)
array([3, 4])
>>> data.max(axis=1)
array([2, 4])
```


![./np_matrix_aggregation_row.png](./np_matrix_aggregation_row.png)

Once you’ve created your matrices, you can add and multiply them using arithmetic operators if you have two matrices that are the same size.

```python
>>> data = np.array([[1, 2], [3, 4]])
>>> ones = np.array([[1, 1], [1, 1]])
>>> data + ones
array([[2, 3],
 [4, 5]])
```


![./np_matrix_arithmetic.png](./np_matrix_arithmetic.png)

You can do these arithmetic operations on matrices of different sizes, but only if one matrix has only one column or one row. In this case, NumPy will use its broadcast rules for the operation.

```python
>>> data = np.array([[1, 2], [3, 4], [5, 6]])
>>> ones_row = np.array([[1, 1]])
>>> data + ones_row
array([[2, 3],
 [4, 5],
 [6, 7]])
```


![./np_matrix_broadcasting.png](./np_matrix_broadcasting.png)

Be aware that when NumPy prints N-dimensional arrays, the last axis is looped over the fastest while the first axis is the slowest. For instance:

```python
>>> np.ones((4, 3, 2))
array([[[1., 1.],
 [1., 1.],
 [1., 1.]],

 [[1., 1.],
 [1., 1.],
 [1., 1.]],

 [[1., 1.],
 [1., 1.],
 [1., 1.]],

 [[1., 1.],
 [1., 1.],
 [1., 1.]]])
```


There are often instances where we want NumPy to initialize the values of an array. NumPy offers functions like `ones()` and `zeros()`, and the `random.Generator` class for random number generation for that. All you need to do is pass in the number of elements you want it to generate:

```python
>>> np.ones(3)
array([1., 1., 1.])
>>> np.zeros(3)
array([0., 0., 0.])
# the simplest way to generate random numbers
>>> rng = np.random.default_rng(0)
>>> rng.random(3)
array([0.63696169, 0.26978671, 0.04097352])
```


![./np_ones_zeros_random.png](./np_ones_zeros_random.png)

You can also use `ones()`, `zeros()`, and `random()` to create a 2D array if you give them a tuple describing the dimensions of the matrix:

```python
>>> np.ones((3, 2))
array([[1., 1.],
 [1., 1.],
 [1., 1.]])
>>> np.zeros((3, 2))
array([[0., 0.],
 [0., 0.],
 [0., 0.]])
>>> rng.random((3, 2))
array([[0.01652764, 0.81327024],
 [0.91275558, 0.60663578],
 [0.72949656, 0.54362499]])  # may vary
```


![./np_ones_zeros_matrix.png](./np_ones_zeros_matrix.png)


## Generating random numbers

The use of random number generation is an important part of the configuration and evaluation of many numerical and machine learning algorithms. Whether you need to randomly initialize weights in an artificial neural network, split data into random sets, or randomly shuffle your dataset, being able to generate random numbers (actually, repeatable pseudo-random numbers) is essential.

With `Generator.integers`, you can generate random integers from low (remember that this is inclusive with NumPy) to high (exclusive). You can set `endpoint=True` to make the high number inclusive.

You can generate a 2 x 4 array of random integers between 0 and 4 with:

```python
>>> rng.integers(5, size=(2, 4))
array([[2, 1, 1, 0],
 [0, 0, 0, 4]])  # may vary
```



## How to get unique items and counts


You can find the unique elements in an array easily with `np.unique`.

For example, if you start with this array:

```python
>>> a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
```


you can use `np.unique` to print the unique values in your array:

```python
>>> unique_values = np.unique(a)
>>> print(unique_values)
[11 12 13 14 15 16 17 18 19 20]
```


To get the indices of unique values in a NumPy array (an array of first index positions of unique values in the array), just pass the `return_index` argument in `np.unique()` as well as your array.

```python
>>> unique_values, indices_list = np.unique(a, return_index=True)
>>> print(indices_list)
[ 0  2  3  4  5  6  7 12 13 14]
```


You can pass the `return_counts` argument in `np.unique()` along with your array to get the frequency count of unique values in a NumPy array.

```python
>>> unique_values, occurrence_count = np.unique(a, return_counts=True)
>>> print(occurrence_count)
[3 2 2 2 1 1 1 1 1 1]
```


This also works with 2D arrays! If you start with this array:

```python
>>> a_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [1, 2, 3, 4]])
```


You can find unique values with:

```python
>>> unique_values = np.unique(a_2d)
>>> print(unique_values)
[ 1  2  3  4  5  6  7  8  9 10 11 12]
```


If the axis argument isn’t passed, your 2D array will be flattened.

If you want to get the unique rows or columns, make sure to pass the `axis` argument. To find the unique rows, specify `axis=0` and for columns, specify `axis=1`.

```python
>>> unique_rows = np.unique(a_2d, axis=0)
>>> print(unique_rows)
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
```


To get the unique rows, index position, and occurrence count, you can use:

```python
>>> unique_rows, indices, occurrence_count = np.unique(
...      a_2d, axis=0, return_counts=True, return_index=True)
>>> print(unique_rows)
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
>>> print(indices)
[0 1 2]
>>> print(occurrence_count)
[2 1 1]
```



## Transposing and reshaping a matrix


It’s common to need to transpose your matrices. NumPy arrays have the property `T` that allows you to transpose a matrix.

![./np_transposing_reshaping.png](./np_transposing_reshaping.png)

You may also need to switch the dimensions of a matrix. This can happen when, for example, you have a model that expects a certain input shape that is different from your dataset. This is where the `reshape` method can be useful. You simply need to pass in the new dimensions that you want for the matrix.

```python
>>> data.reshape(2, 3)
array([[1, 2, 3],
 [4, 5, 6]])
>>> data.reshape(3, 2)
array([[1, 2],
 [3, 4],
 [5, 6]])
```


![./np_reshape.png](./np_reshape.png)

You can also use `.transpose` to reverse or change the axes of an array according to the values you specify.

If you start with this array:

```python
>>> arr = np.arange(6).reshape((2, 3))
>>> arr
array([[0, 1, 2],
 [3, 4, 5]])
```


You can transpose your array with `arr.transpose()`.

```python
>>> arr.transpose()
array([[0, 3],
 [1, 4],
 [2, 5]])
```



## How to reverse an array


NumPy’s `np.flip()` function allows you to flip, or reverse, the contents of an array along an axis. When using `np.flip`, specify the array you would like to reverse and the axis. If you don’t specify the axis, NumPy will reverse the contents along all of the axes of your input array.

**Reversing a 1D array**

If you begin with a 1D array like this one:

```python
>>> arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
```


You can reverse it with:

```python
>>> reversed_arr = np.flip(arr)
```


If you want to print your reversed array, you can run:

```python
>>> print('Reversed Array: ', reversed_arr)
Reversed Array:  [8 7 6 5 4 3 2 1]
```


**Reversing a 2D array**

A 2D array works much the same way.

If you start with this array:

```python
>>> arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
```


You can reverse the content in all of the rows and all of the columns with:

```python
>>> reversed_arr = np.flip(arr_2d)
>>> print(reversed_arr)
[[12 11 10  9]
 [ 8  7  6  5]
 [ 4  3  2  1]]
```


You can easily reverse only the _rows_ with:

```python
>>> reversed_arr_rows = np.flip(arr_2d, axis=0)
>>> print(reversed_arr_rows)
[[ 9 10 11 12]
 [ 5  6  7  8]
 [ 1  2  3  4]]
```


Or reverse only the _columns_ with:

```python
>>> reversed_arr_columns = np.flip(arr_2d, axis=1)
>>> print(reversed_arr_columns)
[[ 4  3  2  1]
 [ 8  7  6  5]
 [12 11 10  9]]
```


You can also reverse the contents of only one column or row. For example, you can reverse the contents of the row at index position 1 (the second row):

```python
>>> arr_2d[1] = np.flip(arr_2d[1])
>>> print(arr_2d)
[[ 1  2  3  4]
 [ 8  7  6  5]
 [ 9 10 11 12]]
```


You can also reverse the column at index position 1 (the second column):

```python
>>> arr_2d[:,1] = np.flip(arr_2d[:,1])
>>> print(arr_2d)
[[ 1 10  3  4]
 [ 8  7  6  5]
 [ 9  2 11 12]]
```



## Reshaping and flattening multidimensional arrays


There are two popular ways to flatten an array: `.flatten()` and `.ravel()`. The primary difference between the two is that the new array created using `ravel()` is actually a reference to the parent array (i.e., a “view”). This means that any changes to the new array will affect the parent array as well. Since `ravel` does not create a copy, it’s memory efficient.

If you start with this array:

```python
>>> x = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
```


You can use `flatten` to flatten your array into a 1D array.

```python
>>> x.flatten()
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12])
```


When you use `flatten`, changes to your new array won’t change the parent array.

For example:

```python
>>> a1 = x.flatten()
>>> a1[0] = 99
>>> print(x)  # Original array
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
>>> print(a1)  # New array
[99  2  3  4  5  6  7  8  9 10 11 12]
```


But when you use `ravel`, the changes you make to the new array will affect the parent array.

For example:

```python
>>> a2 = x.ravel()
>>> a2[0] = 98
>>> print(x)  # Original array
[[98  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
>>> print(a2)  # New array
[98  2  3  4  5  6  7  8  9 10 11 12]
```




## Working with mathematical formulas

The ease of implementing mathematical formulas that work on arrays is one of the things that make NumPy so widely used in the scientific Python community.

For example, this is the mean square error formula (a central formula used in supervised machine learning models that deal with regression):

![./np_MSE_formula.png](./np_MSE_formula.png)

Implementing this formula is simple and straightforward in NumPy:

![./np_MSE_implementation.png](./np_MSE_implementation.png)

What makes this work so well is that `predictions` and `labels` can contain one or a thousand values. They only need to be the same size.

You can visualize it this way:

![./np_mse_viz1.png](./np_mse_viz1.png)

In this example, both the predictions and labels vectors contain three values, meaning `n` has a value of three. After we carry out subtractions the values in the vector are squared. Then NumPy sums the values, and your result is the error value for that prediction and a score for the quality of the model.

![./np_mse_viz2.png](./np_mse_viz2.png) ![./np_MSE_explanation2.png](./np_MSE_explanation2.png)

## How to save and load NumPy objects

You will, at some point, want to save your arrays to disk and load them back without having to re-run the code. Fortunately, there are several ways to save and load objects with NumPy. The ndarray objects can be saved to and loaded from the disk files with `loadtxt` and `savetxt` functions that handle normal text files, `load` and `save` functions that handle NumPy binary files with a **.npy** file extension, and a `savez` function that handles NumPy files with a **.npz** file extension.

The **.npy** and **.npz** files store data, shape, dtype, and other information required to reconstruct the ndarray in a way that allows the array to be correctly retrieved, even when the file is on another machine with different architecture.

If you want to store a single ndarray object, store it as a .npy file using `np.save`. If you want to store more than one ndarray object in a single file, save it as a .npz file using `np.savez`. You can also save several arrays into a single file in compressed npz format with `savez_compressed`.

It’s easy to save and load and array with `np.save()`. Just make sure to specify the array you want to save and a file name. For example, if you create this array:

```python
>>> a = np.array([1, 2, 3, 4, 5, 6])
```


You can save it as “filename.npy” with:

```python
>>> np.save('filename', a)
```


You can use `np.load()` to reconstruct your array.

```python
>>> b = np.load('filename.npy')
```


If you want to check your array, you can run::

```python
>>> print(b)
[1 2 3 4 5 6]
```


You can save a NumPy array as a plain text file like a **.csv** or **.txt** file with `np.savetxt`.

For example, if you create this array:

```python
>>> csv_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
```


You can easily save it as a .csv file with the name “new_file.csv” like this:

```python
>>> np.savetxt('new_file.csv', csv_arr)
```


You can quickly and easily load your saved text file using `loadtxt()`:

```python
>>> np.loadtxt('new_file.csv')
array([1., 2., 3., 4., 5., 6., 7., 8.])
```


The `savetxt()` and `loadtxt()` functions accept additional optional parameters such as header, footer, and delimiter. While text files can be easier for sharing, .npy and .npz files are smaller and faster to read. If you need more sophisticated handling of your text file (for example, if you need to work with lines that contain missing values), you will want to use the `genfromtxt` function.

With `savetxt`, you can specify headers, footers, comments, and more.




[Contenidos](../Contenidos.md) \| [Anterior (6 NumPy)](07_NumPy_Arrays.md) \| [Próximo (8 El album de Figuritas+)](08_Figuritas.md)

