[Contenidos](../Contenidos.md) \| [Anterior (2 Divide y reinarás)](02_Divide_and_Conquer.md) \| [Próximo (4 Cierre de la clase de Ordenamiento)](04_Cierre.md)

# 11.3 # Algoritmos de clasificación supervisada

En esta sección veremos un algoritmo de clasificación. Un problema de clasificación es un problema en el que tenemos algunas clases fijas (en nuestro ejemplo serán tres tipos de flores) y algunos atributos (medidas de los pétalos y sépalos, en nuestro ejemplo) a partir de los cuales queremos _inferir_ la clase. Típicamente el algoritmo de clasificación se _entrena_ con alguna parte de los datos para que _aprenda_ y luego se _evalúa_ cuán bien aprendió con el resto de los datos. Para esto hace falta tener un conjunto de datos _etiquetados_ (es decir, con la clase bien definida). Luego, si funciona bien, el algoritmo podrá usarse para etiquetar nuevos datos de los que no se conoce la clase.


En esta sección nos concentraremos en el entrenamiento y la evaluación de los algoritmo.

Trabajaremos con la librería sklearn de python que está diseñada para realizar tareas de aprendizaje automático. La misma trae algunos conjuntos de datos de ejemplo. Trabajaremos con el clásico ejemplo de **Clasificación de Especies de flores Iris** según medidas del pétalo y el sépalo.

![sepal_petal](./iris_petal_sepal.png)


```python
from sklearn.datasets import load_iris
iris_dataset = load_iris()
```

Este dataset trae una serie de datos medidos de los pétalos y sépalos de 150 flores Iris y su clasificación en tres especies (setosa, versicolor y virginica). La idea es usar algunos de los datos de flores para entrenar un algoritmo y si podemos decir la especie de las otras flores usando solo sus medidas.

El dataset es un diccionario con diferentes datos. Esencialmente en "data" tiene un array con las medidas de ancho y largo de petalo y sepalo (atribuos, o "features" en inglés) de 150 flores  y en "target" tiene un numero (0, 1 o 2) que representa la especie de estas flores. Veamos un poco la estructura de estos datos:


```python
iris_dataset

    {'data': array([[5.1, 3.5, 1.4, 0.2],
            [4.9, 3. , 1.4, 0.2],
            [4.7, 3.2, 1.3, 0.2],
            ...
            [6.7, 3. , 5.2, 2.3],
            [6.3, 2.5, 5. , 1.9],
            [6.5, 3. , 5.2, 2. ],
            [6.2, 3.4, 5.4, 2.3],
            [5.9, 3. , 5.1, 1.8]]),
     'target': array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
            2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
            2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]),
     'target_names': array(['setosa', 'versicolor', 'virginica'], dtype='<U10'),
     'DESCR': '.. _iris_dataset:\n\nIris plants dataset\n--------------------\n\n**Data Set Characteristics:**\n\n    :Number of Instances: 150 (50 in each of three classes)\n    :Number of Attributes: 4 numeric, predictive attributes and the class\n    :Attribute Information:\n        - sepal length in cm\n        - sepal width in cm\n        - petal length in cm\n        - petal width in cm\n        - class:\n                - Iris-Setosa\n                - Iris-Versicolour\n                - Iris-Virginica\n                \n    :Summary Statistics:\n\n    ============== ==== ==== ======= ===== ====================\n                    Min  Max   Mean    SD   Class Correlation\n    ============== ==== ==== ======= ===== ====================\n    sepal length:   4.3  7.9   5.84   0.83    0.7826\n    sepal width:    2.0  4.4   3.05   0.43   -0.4194\n    petal length:   1.0  6.9   3.76   1.76    0.9490  (high!)\n    petal width:    0.1  2.5   1.20   0.76    0.9565  (high!)\n    ============== ==== ==== ======= ===== ====================\n\n    :Missing Attribute Values: None\n    :Class Distribution: 33.3% for each of 3 classes.\n    :Creator: R.A. Fisher\n    :Donor: Michael Marshall (MARSHALL%PLU@io.arc.nasa.gov)\n    :Date: July, 1988\n\nThe famous Iris database, first used by Sir R.A. Fisher. The dataset is taken\nfrom Fisher\'s paper. Note that it\'s the same as in R, but not as in the UCI\nMachine Learning Repository, which has two wrong data points.\n\nThis is perhaps the best known database to be found in the\npattern recognition literature.  Fisher\'s paper is a classic in the field and\nis referenced frequently to this day.  (See Duda & Hart, for example.)  The\ndata set contains 3 classes of 50 instances each, where each class refers to a\ntype of iris plant.  One class is linearly separable from the other 2; the\nlatter are NOT linearly separable from each other.\n\n.. topic:: References\n\n   - Fisher, R.A. "The use of multiple measurements in taxonomic problems"\n     Annual Eugenics, 7, Part II, 179-188 (1936); also in "Contributions to\n     Mathematical Statistics" (John Wiley, NY, 1950).\n   - Duda, R.O., & Hart, P.E. (1973) Pattern Classification and Scene Analysis.\n     (Q327.D83) John Wiley & Sons.  ISBN 0-471-22361-1.  See page 218.\n   - Dasarathy, B.V. (1980) "Nosing Around the Neighborhood: A New System\n     Structure and Classification Rule for Recognition in Partially Exposed\n     Environments".  IEEE Transactions on Pattern Analysis and Machine\n     Intelligence, Vol. PAMI-2, No. 1, 67-71.\n   - Gates, G.W. (1972) "The Reduced Nearest Neighbor Rule".  IEEE Transactions\n     on Information Theory, May 1972, 431-433.\n   - See also: 1988 MLC Proceedings, 54-64.  Cheeseman et al"s AUTOCLASS II\n     conceptual clustering system finds 3 classes in the data.\n   - Many, many more ...',
     'feature_names': ['sepal length (cm)',
      'sepal width (cm)',
      'petal length (cm)',
      'petal width (cm)'],
     'filename': '/home/rgrimson/.local/lib/python3.6/site-packages/sklearn/datasets/data/iris.csv'}




```python
print("Claves del diccionario iris_dataset:\n", iris_dataset.keys())
```

    Claves del diccionario iris_dataset:
     dict_keys(['data', 'target', 'target_names', 'DESCR', 'feature_names', 'filename'])



```python
print(iris_dataset['DESCR'][:193] + "\n...")
```

    .. _iris_dataset:
    
    Iris plants dataset
    --------------------
    
    **Data Set Characteristics:**
    
        :Number of Instances: 150 (50 in each of three classes)
        :Number of Attributes: 4 numeric, pre
    ...



```python
print("Target names:", iris_dataset['target_names'])
```

    Target names: ['setosa' 'versicolor' 'virginica']



```python
print("Feature names:\n", iris_dataset['feature_names'])
```

    Feature names:
     ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']



```python
print("Type of data:", type(iris_dataset['data']))
```

    Type of data: <class 'numpy.ndarray'>



```python
print("Shape of data:", iris_dataset['data'].shape)
```

    Shape of data: (150, 4)



```python
print("First five rows of data:\n", iris_dataset['data'][:5])
```

    First five rows of data:
     [[5.1 3.5 1.4 0.2]
     [4.9 3.  1.4 0.2]
     [4.7 3.2 1.3 0.2]
     [4.6 3.1 1.5 0.2]
     [5.  3.6 1.4 0.2]]



```python
print("Type of target:", type(iris_dataset['target']))
```

    Type of target: <class 'numpy.ndarray'>



```python
print("Shape of target:", iris_dataset['target'].shape)
```

    Shape of target: (150,)



```python
print("Target:\n", iris_dataset['target'])
```

    Target:
     [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
     0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
     1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2
     2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
     2 2]


### Como dijimos antes, vamos a entrenar un algoritmo y luego a evaluar su capacidad de clasificar. Para evitar sesgos tenemos que partir al conjunto de datos en dos:

- una parte de los datos (training) será de entrenamiento del algoritmo
- y otra parte (testing) será usada para la evaluación.

La librería sklearn trae funciones que hacen esta separación (split) de forma aleatoria, como se ve a continuación (en este caso fijamos una semilla con random_state=0, luego lo sacaremos). Obviamente separamos tanto los atributos (features) como su clase (target). En este caso usaremos 75% para entrenar y 25% de los tados para evaluar.



```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=0)
```


```python
print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)
```

    X_train shape: (112, 4)
    y_train shape: (112,)



```python
print("X_test shape:", X_test.shape)
print("y_test shape:", y_test.shape)
```

    X_test shape: (38, 4)
    y_test shape: (38,)


#### Hagamos unos gráficos para ver los datos y entender las correlaciones entre los atributos, usando un color diferente para cada especie de flor.


```python
#import mglearn
# create dataframe from data in X_train
# label the columns using the strings in iris_dataset.feature_names
iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
# create a scatter matrix from the dataframe, color by y_train
pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15),
                           marker='o', hist_kwds={'bins': 20}, s=60,
                           alpha=.8)
```




    array([[<matplotlib.axes._subplots.AxesSubplot object at 0x7f5a337d7630>,
            <matplotlib.axes._subplots.AxesSubplot object at 0x7f5a3378b8d0>,
            <matplotlib.axes._subplots.AxesSubplot object at 0x7f5a3373eb38>,
            <matplotlib.axes._subplots.AxesSubplot object at 0x7f5a336f1da0>],
           [<matplotlib.axes._subplots.AxesSubplot object at 0x7f5a336a7fd0>,
            <matplotlib.axes._subplots.AxesSubplot object at 0x7f5a336662b0>,
            <matplotlib.axes._subplots.AxesSubplot object at 0x7f5a3361a518>,
            <matplotlib.axes._subplots.AxesSubplot object at 0x7f5a3364d748>],
           [<matplotlib.axes._subplots.AxesSubplot object at 0x7f5a3364d7b8>,
            <matplotlib.axes._subplots.AxesSubplot object at 0x7f5a335b5c50>,
            <matplotlib.axes._subplots.AxesSubplot object at 0x7f5a3356aeb8>,
            <matplotlib.axes._subplots.AxesSubplot object at 0x7f5a3352b160>],
           [<matplotlib.axes._subplots.AxesSubplot object at 0x7f5a334e03c8>,
            <matplotlib.axes._subplots.AxesSubplot object at 0x7f5a33513630>,
            <matplotlib.axes._subplots.AxesSubplot object at 0x7f5a334c6898>,
            <matplotlib.axes._subplots.AxesSubplot object at 0x7f5a3347cb00>]],
          dtype=object)




![png](./output_27_1.png)


#### Ahora si, vamos a construir nuestro primer modelo. Usaremos un algoritmo sencillo que se llama de "vecinos más cercanos" (K-nearest neighborsk en inglés, ver https://es.wikipedia.org/wiki/K_vecinos_m%C3%A1s_pr%C3%B3ximos). Lo entrenaremos con algunos datos (training) y al consultarle por un nuevo dato (de los de testing) lo que hará el algoritmo es buscar al dato de entrenamiento más cercano en el espacio de atributos y asignarle al nuevo dato la especie de esa flor. En otras palabras: cuando le preguntemos por la especie de una flor nueva va a contestarnos con la especie de la flor "mas cercana" en el especio de atributos (ancho y largos de pétalo y cépalo).


#### De esta forma el espacio de atributos queda dividido en regiones a las que se les asignará cada especie. En el siguiente gráfico puede verse una partición de un espacio de dos atributos y tres clases considerando 1 vecino más cercano y entrenado con los datos del gráfico:

![areas_knn](./images/Map1NN.png)

#### A un nuevo punto en este plano el clasificador así entrenado le asignará la clase correspondiente al color de fondo, que coincide con la clase del vecino más cercano.

Creamos una instancia de la clase KNeighborsClassifier


```python
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
```

Y la entrenamos con los datos de entrenamiento


```python
knn.fit(X_train, y_train)
```




    KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
                         metric_params=None, n_jobs=None, n_neighbors=1, p=2,
                         weights='uniform')



#### Listo, tenemos el clasificador entrenado, lo podemos usar para predecir la clase de una nueva flor a partir de sus cuatro medidas:


```python
X_new = np.array([[5, 2.9, 1, 0.2]])
print("X_new.shape:", X_new.shape)
```

    X_new.shape: (1, 4)


#### Plotiemos este nuevo punto en rojo y su relación a los datos de entrenamiento en dos de los atributos.


```python

plt.scatter(X_train[:,1],X_train[:,3],c=y_train)#,label=iris_dataset['target_names'][y_train])
plt.scatter(X_new[:,1],X_new[:,3],c='red')#,label=['nuevo'])

```




    <matplotlib.collections.PathCollection at 0x7f5a32e9a860>




![png](./output_36_1.png)


#### Aca se ve que el punto rojo esta cerca de la clase "setosa". Utilicemos ahora el algoritmo knn entrenado para que nos prediga la clase del punto X_new



```python
prediction = knn.predict(X_new)
print("Predicción:", prediction)
print("Nombre de la Especie Predicha:",
       iris_dataset['target_names'][prediction])
```

    Predicción: [0]
    Nombre de la Especie Predicha: ['setosa']


#### Evaluación del modelo.
Finalmente usaremos el 25% de los datos que nos guardamos para evaluar cuán bien funciona nuestro clasificador.


```python
y_pred = knn.predict(X_test)
print("Predicciones para el cjto de Test:\n", y_pred)
print("Etiquetas originales de este cjto:\n", y_test)
```

    Predicciones para el cjto de Test:
     [2 1 0 2 0 2 0 1 1 1 2 1 1 1 1 0 1 1 0 0 2 1 0 0 2 0 0 1 1 0 2 1 0 2 2 1 0
     2]
    Etiquetas originales de este cjto:
     [2 1 0 2 0 2 0 1 1 1 2 1 1 1 1 0 1 1 0 0 2 1 0 0 2 0 0 1 1 0 2 1 0 2 2 1 0
     1]


Se ve que coinciden todos salvo el último. Podemos medir el éxito calculando la fracción de clasificaciones bien hechas (calculamos el promedio de "1 si está bien, 0 si está mal"):



```python
print(y_pred == y_test)
print("Test set score: {:.2f}".format(np.mean(y_pred == y_test)))
```

    [ True  True  True  True  True  True  True  True  True  True  True  True
      True  True  True  True  True  True  True  True  True  True  True  True
      True  True  True  True  True  True  True  True  True  True  True  True
      True False]
    Test set score: 0.97


O usando la función "score" que ya viene en el clasificador:


```python
print("Test set score: {:.2f}".format(knn.score(X_test, y_test)))
```

    Test set score: 0.97


### Pasando en limpio todo, lo que hicimos fue:

    1) Separar los datos en dos conjuntos: test y train.
    2) definir un clasificador knn y entrenarlo con los datos de training.
    3) evaluar el clasificador con los datos de testing.


```python
X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'])

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

print("Test set score: {:.2f}".format(knn.score(X_test, y_test)))
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-1-55fec5067341> in <module>
    ----> 1 X_train, X_test, y_train, y_test = train_test_split(
          2     iris_dataset['data'], iris_dataset['target'])
          3 
          4 knn = KNeighborsClassifier(n_neighbors=1)
          5 knn.fit(X_train, y_train)


    NameError: name 'train_test_split' is not defined


Observar que en este último fragmento de código el split en test y train es aleatorio, y va a dar resultados (scores) diferentes cada vez que lo corramos

## Ejercicio 1:
####    Lea sobre los clasificadores basados en arboles de decisión en https://es.wikipedia.org/wiki/Aprendizaje_basado_en_%C3%A1rboles_de_decisi%C3%B3n y luego use el objeto clasificador "clf" (definido a continuación) como se usó "knn" en el ejemplo anterior (es decir, entrene el clasificador sobre el conjunto train y evalúelo sobre el conjunto test). Tanto knn como clf son clasificadores y heredan los métodos "fit", "predict" y "score" de forma que su uso es casi idéntico.


```python
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
```

## Ejercicio 2:
####    Esta comparación de dos clasificadores puede resultar injusta ya que está basada en UNA partición del conjunto de datos es test y train que podría darle ventaja a uno u otro clasificador. 
    
    Para evitar esto, repita 100 veces lo siguiente y calcule el promedio de los scores:
        a) Partición del conjunto original en test y train aleatoriamente (sin fijar la semilla).
        b) Entrenamiento de ambos modelos (knn y clf) con el conjunto train resultante.
        c) Evaluación de ambos clasifcadores (score) con el conjunto test resultante.
        
  #### Imprima el promedio de los scores obtenidos.


[Contenidos](../Contenidos.md) \| [Anterior (2 Divide y reinarás)](02_Divide_and_Conquer.md) \| [Próximo (4 Cierre de la clase de Ordenamiento)](04_Cierre.md)

