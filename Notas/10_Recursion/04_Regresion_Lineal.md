[Contenidos](../Contenidos.md) \| [Anterior (3 Práctica de Recursión)](03_EjerciciosRec.md) \| [Próximo (5 Cierre de la clase de Recursión)](05_Cierre.md)

# 10.4 Regresión lineal

En esta sección vamos a trabajar con **regresión lineal**. No es una clase con todos los fundamentos del tema, sino un acercamiento práctico a las técnicas y sus formas de uso en Python. Para un desarrollo más profundo te recomendamos por ejemplo las notas de [Andrew Ng](http://cs229.stanford.edu/notes/cs229-notes1.pdf).

## Regresión lineal simple

Supongamos que queremos modelar la relación entre dos variables reales mediante un modelo lineal. Y que vamos a ajustar los parámetros de ese modelos a partir de ciertos valores conocidos (mediciones, digamos). Es decir que vamos a estar pensando que las variables tienen una relación lineal, `Y = a*X + b`, donde `X` es la variable *explicativa* (sus componentes se denominan *independientes* o *regresores*), e `Y` es la variable *a explicar* (también denominada *dependiente* o *regresando*).

A partir de un conjunto de datos de tipo `(x, y)`, planteamos el modelo `Y = a*X + b`.

En general el modelo no va a ser exacto, es decir, no se va a complir que `y_i = a*x_i + b` para los valores `(x_i, y_i)`, salvo que justamente estén sobre una línea recta.
Vamos a tener que `y_i = a*x_i + b + r_i` donde, los valores `r_i`, llamados _residuos_, representan las diferencias entre los valores de la recta en cada valor de `x` que tenemos y los valores de `y` asociados.

El problema de regresión lineal consiste en elegir los parámetros `a, b` de para la recta (es decir, su pendiente y ordenada al origen), de manera que la recta sea la que *mejor* se adapte a los datos disponibles.


```python
import numpy as np
import matplotlib.pyplot as plt

x = np.array([55.0, 38, 68, 70, 53, 46, 11, 16, 20, 4])
y = np.array([153.0, 98, 214, 220, 167, 145, 41, 63, 65, 25])
g = plt.scatter(x = x, y = y)
plt.title('scatterplot de los datos')
plt.show()

```
![ej0_scatter](./ej0_scatter.png)


¿Qué quiere decir *mejor*? Vamos a considerar el criterio de cuadrados mínimos.

### Criterio de cuadrados mínimos

Vamos a elegir como mejor recta a la que minimice los residuos. Más precisamente, vamos a elegir la recta de manera tal que la suma de los cuadrados de los residuos sea mínima.

![ej0_posiblesrectas](./ej0_posiblesrectas.png)

Analíticamente, buscamos `a, b` tales que minimicen la siguiente suma de cuadrados:

![\Sigma_{i=1}^n (a*x_i + b - y_i)^2](https://render.githubusercontent.com/render/math?math=\Sigma_{i=1}^n%20(a%20\cdot%20x_i%20%2B%20b%20-%20y_i)^2)

Recordá que vimos que calcular el promedio de estos errores en numpy es muy sencillo en la [Sección 4.3](../04_Random_Plt_Dbg/03_NumPy_Arrays.md#fórmulas-matemáticas). Usar cudrados mínimos tiene múltiples motivaciones que no podemos detallar adecuadamente acá. Solo mencionaremos dos hechos importantes relacionados con su frecuente elección:

- Por un lado, minimizar el error cuadrático medio puede resolverse derivando la fórumla del error. Los que sepan algo de análisis matemático, recordarán que la derivada nos permite encontrar mínimos y que la derivada de una función cudrática es una función lineal. Por lo tanto, encontrar la recta que mejor ajusta los datos se reduce a buscar el cero de una derivada que en el fondo se reduce a resolver un sistema lineal, algo que sabemos hacer muy bien y muy rápido.
- Otro argumento muy fuerte, de naturaleza estadística en este caso, es que si uno considera que los residuos son por ejemplo errores de medición y que tienen una distribución normal (una gaussiana), entonces puede mostrarse que la recta que da el método de los cuadrados mínimos es _la recta de máxima verosimilitud_.

Estas cosas se explican muy bien en el apunte de Andrew Ng que citamos antes.

### Ejemplo

Para los datos que graficamos antes, ésta es _la mejor recta_, es decir, la que minimiza la suma de los cuadrados de los residuos. Vamos a decir que esta recta es **el ajuste lineal de los datos**.

![ej0_ajuste](./ej0_ajuste.png)

¿Cómo se encuentran estos coeficientes?

#### Una opción: derivando

Como buscamos el mínimo de la expresión ![\Sigma_{i=1}^n (a*x_i + b - y_i)^2](https://render.githubusercontent.com/render/math?math=\Sigma_{i=1}^n%20(a%20\cdot%20x_i%20%2B%20b%20-%20y_i)^2)
 podemos derivar respecto de los parámetros `a, b` e igualar a cero para despejarlos. De esta manera se obtienen las siguientes fórmulas para el ajuste:

```python
def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b
```
### Ejemplo

Veamos un ejemplo generado con datos sintéticos. Generamos 50 datos para la variable `x`, y determinamos a la variable `y` con una relación lineal más un error normal.

```python
import numpy as np

N = 50
minx = 0
maxx = 500
x = np.random.uniform(minx, maxx, N)
e = np.random.normal(0, 25, N)
y = 1.3*x + e

g = plt.scatter(x = x, y = y)
plt.title('gráfico de dispersión de los datos')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
```
![ejsint_scatter](./ejsint_scatter.png)

Ahora ajustamos con las fórmulas que vimos antes:

```python
a, b = ajuste_lineal_simple(x, y)

grilla_x = np.linspace(start = minx, stop = maxx, num = 1000)
grilla_y = grilla_u*a + b

g = plt.scatter(x = x, y = y)
plt.title('ajuste lineal')
plt.plot(grilla_u, grilla_v, c = 'green')
plt.xlabel('x')
plt.ylabel('x')

plt.show()
```

![ejsint_ajuste](./ejsint_ajuste.png)

### Ejercicio 10.14: Alquiler y superficie
Consdieramos datos de precios (en miles de pesos) de alquiler mensual de departamentos en el barrio de Caballito, CABA, y sus superficies (en metros cuadrados). Queremos ajustar un modelo que prediga el precio de alquiler a partir de la superficie para este barrio.

 + Usando la función que definimos antes, ajustá los datos con una recta.
 + Graficá los datos junto con la resta del ajuste.

```python
superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])
```

Una forma de cuantificar cuán bien ajusta la recta es considerar el promedio de los errores cuadráticos, llamado *error cuadrático medio*.

```python
errores = alquiler - (a*superficie + b)
print(errores)
print("ECM:", (errores**2).mean())
```
 + Calculá el error cuadrático medio del ajuste que hiciste recién.


### Ejemplo

Veamos qué pasa si los datos guardan en realidad una relación cuadrática.

```python
N = 50
x = np.random.uniform(size = N, low = 0, high = 10)
y = 2 + x + 2*x**2 + np.random.normal(size = N, loc = 0.0, scale = 12.0)
plt.scatter(x,y)
plt.title('scatterplot de los datos')
plt.show()
```
![ejcuad_scatter](./ejcuad_scatter.png)

Y ajutamos un modelo lineal a estos datos.

```python
a, b = ajuste_lineal_simple(x, y)

grilla_x = np.linspace(start = 0, stop = 10, num = 1000)
grilla_y = grilla_x*a + b
g = plt.scatter(x = x , y = y)
plt.title('ajuste lineal')
plt.plot(grilla_x, grilla_y, c = 'green')
plt.show()
```

![ejcuad_ajustelineal](./ejcuad_ajustelineal.png)

Veamos cuánto vale el error cuadrático medio.

```pyhon
errores = y - (x*a + b)
print("ECM", (errores**2).mean())
```

Un modelo alternativo es usar como variable explicativa `x^2` en vez de `x`.

```python
xc = x**2
ap, bp = ajuste_lineal_simple(xc, y)
grilla_y_p = (grilla_x**2)*ap + bp
plt.scatter(x,y)
plt.plot(grilla_x, grilla_y, c = 'green')
plt.plot(grilla_x, grilla_y_p, c = 'red')
plt.title('ajuste lineal con x^2')
plt.show()
```

![ejcuad_ajusteconx2](./ejcuad_ajusteconx2.png)


Y si queremos cuantificar el error en este modelo:

```pyhon
errores = y - ((x**2)*ap + bp)
print("MSE:", (errores**2).mean())
```

### Scikit-Learn

La biblioteca [scikit-learn](https://scikit-learn.org/stable/) tiene herramientas muy útiles para el análisis de datos. En particular para regresión lineal tiene el módulo *linear_model*. En el siguiente ejemplo mostramos cómo puede usarse.

Fijate que, al igual que el modelo de clustering que usamos en el [Ejercicio 8.19](../08_Clases_y_Objetos/05_Teledeteccion.md#ejercicio-819-clasificación-automática) de teledetección, el modelo lineal también tiene un método `fit()` que permite ajustar el modelo a los datos y otro `predict()` que permite usar el modelo ajustado con nuevos datos.

Acá analizamos el primer ejemplo que hicimos, usando el módulo `linear_model`.

```python
from sklearn import linear_model
import pandas as pd

x = np.array([55.0, 38, 68, 70, 53, 46, 11, 16, 20, 4]) # mismos datos x, y
y = np.array([153.0, 98, 214, 220, 167, 145, 41, 63, 65, 25])
datosxy = pd.DataFrame({'x': x, 'y': y}) # paso los datos a un dataframe

ajus = linear_model.LinearRegression() # llamo al modelo de regresión lineal
ajus.fit(datosxy.x.to_frame(), datosxy.y) # ajusto el modelo

grilla_x = np.linspace(start = 0, stop = 70, num = 1000)
grilla_x_df = pd.DataFrame(grilla_x)
grilla_y = ajus.predict(grilla_x_df)

g = plt.scatter(x = var_x , y = var_y)
plt.title('ajuste lineal usando sklearn')
plt.plot(grilla_x, grilla_y, c = 'green')
plt.show()
```

![ejsk1_ajuste](./ejsk1_ajuste.png)

Tuvimos que aplicar el método `to_frame()` a la serie DataFrame `datosxy.x` porque al llamar a una columna de un DataFrame obtenemos una serie, pero el input del ajuste debe ser un DataFrame.

Usamos el método `predict()` para obtener los valores de `y` de la recta.

## Regresión Lineal Múltiple

La regresión lineal múltiple tiene un planteo similar, pero con más variables explicativas. El modelo es el siguiente.

`y = \b_0 + \sum_{j=1}^k \b_j x_j`

### Ejemplo

Trabajamos nuevamente con los departamentos, ahora también conociendo su antigüedad, y la tomamos como otra variable explicativa.

```python
superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])
antigüedad = [50.0, 5.0, 25.0, 70.0]

data_deptos = pd.DataFrame({'alquiler': alquiler, 'superficie': superficie, 'antigüedad': antigüedad})

X = pd.concat([data_deptos.superficie,data_deptos.antigüedad], axis = 1)
y = data_deptos.alquiler

ajuste_deptos = linear_model.LinearRegression()
ajuste_deptos.fit(X,y)

errores = data_deptos.alquiler - (ajuste_deptos.predict(X))
print(errores)
print("ECM:", (errores**2).mean())
```

### OJO
###Meter ejemplo polinomial ACA con el mismo ejemplo cuadrático, teniendo encuenta ahora ambas x y x²

### Ejercicio 10.15: Peso específico
Queremos estimar el peso específico de un metal (es decir, peso divido volumen, en unidades de g/cm³). Para esto, disponemos de barras de dicho metal, con base de 1cm² y largos diversos, y de una balanza que tiene pequeños errores de medición (desconocidos). Vamos a estimar el peso específico _R_ del metal de la siguiente manera.

Sabemos que el volumen de una barra de largo `m` es `m`cm³ por lo que su peso debería ser `R*m`. Nosotres queremos estimar `R`. Utilizando la balanza, tendremos los pesos aproximados de distintas barras, con ciertos errores de medición. Si ajustamos un modelo lineal a los datos de volumen y peso aproximado vamos a tener una buena aproximación para `R` (la pendiente de la recta).

Los datos de longitudes y pesos se encuentran en el archivo [disponible acá]('https://raw.githubusercontent.com/python-unsam/UNSAM_2020c2_Python/master/Notas/10_Recursion/longitudes_y_pesos.csv').

 + Cargá los datos directamente con el enlace usando el siguiente código.

```python
import requests
import io

enlace = 'https://raw.githubusercontent.com/python-unsam/UNSAM_2020c2_Python/master/Notas/10_Recursion/longitudes_y_pesos.csv'
r = requests.get(enlace).content
data_lyp = pd.read_csv(io.StringIO(r.decode('utf-8')))
```

 + Hacé una regresión lineal simple con `sklearn`, con variable explicativa `longitud` y variable explicada `peso`.

 + Estimá el peso específico del metal prediciendo peso de una barra de volumen 1.

 + Graficá los datos junto con la recta del ajuste, y calculá el error cuadrático medio.

 + Guardá el código en un archivo `peso_especifico.py`.


### Ejercicio 10.16: Altura y diámetro de árboles.
Queremos comparar las formas de distintas especies de árboles en los parques de Buenos Aires. Vamos a trabajar nuevamente con el archivo de arbolado porteño en parques que tenés en el archivo 'Data/arbolado-en-espacios-verdes.csv'.


 + Cargá los datos en un DataFrame `data_arbolado_parques`.

 + Seleccioná los datos correspondientes a las especies: Jacarandá, Palo Borracho Rosado, Eucaliptus y Ceibo.

 + Para cada especie seleccionada, realizá un ajuste lineal de la altura dependiendo del diámetro.

 + Graficá para cada especie el scatterplot de los datos junto con la recta de regresión lineal.

 + Guardá el código de este ejercicio en un archivo `ajuste_arboles.py`.


*Observación: Como podrás ver en los sctterplots, para árboles más anchos hay mayor variabilidad de alturas. Esto implica que el modelo va a ser más sensible a datos de árboles anchos, que a datos de árboles chicos. Esta caraceterística se llama _heterocedasticidad_ y muchas veces es un problema para realizar una regresión lineal. En este caso lo estamos aplicando igual, y no nos trae problemas porque contamos con una gran cantidad de datos.*

### Ejercicio 10.17: Gráficos de ajuste lineal con Seaborn
 + Seleccioná los datos correspondientes a las especies: Jacarandá, Palo Borracho Rosado, Eucaliptus y Ceibo, todas en un mismo DataFrame, usando el siguiente filtro.

 ```Python
 filtro = data_arbolado_parques['nombre_com'].isin(esp_selec)
 ```

 + Explorá el comando `sns.regplot()`, que grafica la regresión lineal, sin pasar por scikit learn. El parámetro `order` te permite hacer ajustes polinomiales.

 + Para facilitar la comparación que hiciste en el ejercicio anterior, graficá todos los ajustes juntos usando:

 ```python
 g = sns.FacetGrid(datos_selec_p, col = 'nombre_com')
 g.map(sns.regplot, 'diametro', 'altura_tot')
 ```

### Sobreajuste (_Overfitting_)

Cuando disponemos de muchas variables explicativas para explicar `y`, podemos armar un modelo más complejo, que en general llevará a minimizar el error. ¿Esto significa que el modelo va a ser mejor? El sobreajuste es un tema muy importante en el análisis de datos y el aprendizaje automático. Para verlo gráficamente, consideremos que en vez de ajustar linealmente con más o menos variables, consideramos polinomios de mayor o menor grado, para ajustar valores en el plano.





### _Train - Test_

### _Cross validation_

### Datos atípicos (_Outliers_)


[Contenidos](../Contenidos.md) \| [Anterior (3 Práctica de Recursión)](03_EjerciciosRec.md) \| [Próximo (5 Cierre de la clase de Recursión)](05_Cierre.md)

