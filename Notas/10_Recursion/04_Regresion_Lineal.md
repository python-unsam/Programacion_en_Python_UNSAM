[Contenidos](../Contenidos.md) \| [Anterior (3 Práctica de Recursión)](03_EjerciciosRec.md) \| [Próximo (5 Cierre de la clase de Recursión)](05_Cierre.md)

# 10.4 Regresión lineal

En esta sección vamos a trabajar con **regresión lineal**. No es una clase con todos los fundamentos del tema, sino un acercamiento práctico a las técnicas y sus formas de uso en Python. Para un desarrollo más profundo te recomendamos por ejemplo las notas de [Andrew Ng](http://cs229.stanford.edu/notes/cs229-notes1.pdf).

## Regresión lineal simple

Supongamos que queremos modelar la relación entre dos variables reales mediante un modelo lineal. Y que vamos a ajustar los parámetros de ese modelos a partir de ciertos valores conocidos (mediciones, digamos). Es decir que vamos a estar pensando que las variables tienen una relación lineal, `Y = a*X + b`, donde `X` es la variable *explicativa* (sus componentes se denominan *independientes* o *regresores*), e `Y` es la variable *a explicar* (también denominada *dependiente* o *regresando*).

A partir de un conjunto de datos de tipo `(x_i, y_i)`, planteamos el modelo `Y = a*X + b`.

En general el modelo no va a ser exacto, es decir, no se va a complir que `y_i = a*x_i + b` para los valores `(x_i, y_i)` (salvo que estén, justamente, todos los valores sobre una línea recta). En general, decíamos, vamos a tener que `y_i = a*x_i + b + r_i` donde, los valores `r_i`, llamados _residuos_, representan las diferencias entre los valores de la recta en cada valor de `x` que tenemos y los valores de `y` asociados.

El problema de regresión lineal consiste en elegir los parámetros `a, b` de la recta (es decir, su pendiente y ordenada al origen), de manera que la recta sea la que *mejor se adapte* a los datos disponibles.


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

- Por un lado, minimizar el error cuadrático medio puede resolverse derivando la fórumla del error. Los que sepan algo de análisis matemático, recordarán que la derivada nos permite encontrar mínimos y que la derivada de una función cudrática es una función lineal. Por lo tanto, encontrar la recta que mejor ajusta los datos se reduce a buscar el cero de una derivada que en el fondo se reduce a resolver un sistema lineal, algo que sabemos hacer muy bien y muy rápido. Si en lugar de minimar la suma de los cuadrados de los residuos planteáramos, por ejemplo, minimizar la suma de los valores absolutos de los residuos no podríamos encotrar la recta que mejor ajusta tan fácilmente.
- Otro argumento muy fuerte, de naturaleza estadística en este caso, es que si uno considera que los residuos son por ejemplo errores de medición y que tienen una distribución normal (una gaussiana), entonces puede mostrarse que la recta que da el método de los cuadrados mínimos es _la recta de máxima verosimilitud_.

Estas cosas se explican muy bien en [el apunte de Andrew Ng](http://cs229.stanford.edu/notes/cs229-notes1.pdf) que citamos antes.

### Ejemplo

Para los datos que graficamos antes, ésta es _la mejor recta_, es decir, la que minimiza la suma de los cuadrados de los residuos. Vamos a decir que esta recta es **el ajuste lineal de los datos**.

![ej0_ajuste](./ej0_ajuste.png)

¿Cómo se encuentran estos coeficientes?

#### Una opción: derivando

Como buscamos el mínimo de la expresión ![\Sigma_{i=1}^n (a*x_i + b - y_i)^2](https://render.githubusercontent.com/render/math?math=\Sigma_{i=1}^n%20(a%20\cdot%20x_i%20%2B%20b%20-%20y_i)^2)
 podemos derivar respecto de los parámetros `a, b` e igualar a cero para despejarlos. El único cero que va a tener la derivada se corresponde con un mínimo porque la recta se puede ajusta *tan mal como uno quiera*. De esta manera se obtienen las siguientes fórmulas para el ajuste:

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
r = np.random.normal(0, 25, N) #residuos simulados
y = 1.3*x + r

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
plt.title('datos y su ajuste lineal')
plt.plot(grilla_u, grilla_v, c = 'green')
plt.xlabel('x')
plt.ylabel('y')

plt.show()
```

![ejsint_ajuste](./ejsint_ajuste.png)

### Ejercicio 10.14: Alquiler y superficie
Consdieramos datos de precios (en miles de pesos) de alquiler mensual de departamentos en el barrio de Caballito, CABA, y sus superficies (en metros cuadrados). Queremos modelar el precio de alquiler a partir de la superficie para este barrio.

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

Veamos qué pasa si los datos guardan en realidad una relación cuadrática. Genermos aletoriamente variables independientes y dependientes.

```python
np.random.seed(3141) #semilla para fijar la aleatoriedad
N=50
indep_vars = np.random.uniform(size = N, low = 0, high = 10)
r = np.random.normal(size = N, loc = 0.0, scale = 8.0) # residuos
dep_vars = 2 + 3*indep_vars + 2*indep_vars**2 + r # relación cuadrática
```

Grafiquemos los datos obtenidos y, por comodidad, llamémoslos `x` e `y`.

```python
x = indep_vars
y = dep_vars
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

Vermos próximamente que podemos usar ambas `x` y `x^2` como vartiables explicativas y obtener un ajuste aún mejor de los datos.

### Scikit-Learn

La biblioteca [scikit-learn](https://scikit-learn.org/stable/) tiene herramientas muy útiles para el análisis de datos y el desarrollo de modelos de aprendizaje automático. En particular, para regresión lineal tiene el módulo *linear_model*. En el siguiente ejemplo mostramos cómo puede usarse.

Fijate que, al igual que el modelo de clustering que usamos en el Ejercicio ? de teledetección, el modelo lineal también tiene un método `fit()` que permite ajustar el modelo a los datos y otro `predict()` que permite usar el modelo ajustado con nuevos datos.

Acá rehacemos el primer ejemplo que dimos ([Sección 10.4](../10_Recursion/04_Regresion_Lineal.md#ejemplo)), usando pandas y el módulo `linear_model`.

```python
import pandas as pd
from sklearn import linear_model

x = np.array([55.0, 38, 68, 70, 53, 46, 11, 16, 20, 4]) # mismos datos x, y
y = np.array([153.0, 98, 214, 220, 167, 145, 41, 63, 65, 25])
datosxy = pd.DataFrame({'x': x, 'y': y}) # paso los datos a un dataframe

ajus = linear_model.LinearRegression() # llamo al modelo de regresión lineal
ajus.fit(datosxy[['x']], datosxy['y']) # ajusto el modelo

grilla_x = np.linspace(start = 0, stop = 70, num = 1000)
grilla_y = ajus.predict(grilla_x_df)

datosxy.plot.scatter('x','y')
plt.title('ajuste lineal usando sklearn')
plt.plot(grilla_x, grilla_y, c = 'green')
plt.show()
```

![ejsk1_ajuste](./ejsk1_ajuste.png)

Usamos el método `fit()` para ajustar el modelo y el método `predict()` para obtener los valores de `y` de la recta. Fijate que al método `fit` le pasamos el Dataframe `datosxy[['x']]` y no la serie `datosxy['x']` ya que el método está preparado para trabajar con regresiones múltiples (es decir, tenés muchos regresores).


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

ajuste_deptos = linear_model.LinearRegression()
ajuste_deptos.fit(X,data_deptos.alquiler)

errores = data_deptos.alquiler - (ajuste_deptos.predict(X))
print(errores)
print("ECM:", (errores**2).mean())
```

Usando los atributos `intercept_` y `ajuste_deptos.coef_` escribí a mano la fórmula de la regresión múltiple obtenida y respondé las siguientes preguntas respecto al modelo obtenido:
- A mayor superficie, ¿aumenta o disminuye el precio?
- A mayor antigüedad, ¿aumenta o disminuye el precio?
- ¿Cuánto vale la ordenada al origen del modelo?

### Ejercicio 10.15: Modelo cuadrático
Volvamos ahora al ejemplo cuadrático de antes. La relación entre `x` (`indep_vars`) e `y` (`dep_vars`) estaba dada por `y = 2 + 3*x + 2*x**2 + r`. Ya tratamos de ajustar regresiones simples tipo `y = a*x + b` y `y = a*x^2 + b`. Ajustemos ahora una regresión lilean múltiple, usando como regresores a `x` y a `x^2`. 

Nos gustaría no generar datos aleatorios nuevamente sino usar los anteriores, ya generados, para poder comparar (los errores cuadráticos medios de) los tres modelos.

```python
x = indep_vars
xc = x**2
y = dep_vars
```

Para preparar los datos a usar como regresores (en este caso múltiple serán `x` y `x^2`) podés usar:

```python
X = np.concatenate((x.reshape(-1,1),xc.reshape(-1,1)),axis=1)
```

Si te fijás, el array `X` tiene un shape de `(50, 2)`. Esto se corresponde a cincuenta datos con dos atributos.

* Usá un objeto `lm = linear_model.LinearRegression()` para comparar los ajustes obtenidos usando `x` como unica variable regresora, `xc` (los cuadrados) com única variable regresora o ambas en un modelo múltiple. Imprimí para cada un o de los tres modelos, el error cuadrático medio y los coeficientes (ordenada al orígen y coeficientes de los regresores) obtenidos. ¿Qué modelo ajusta mejor? ¿Cuál da coeficientes más similares a los originales?
* Graficá los datos originales y los tres ajustes en un solo gráfico indicando adecuadamente los nombres de los modelos.


### Ejercicio 10.16: Peso específico
Queremos estimar el peso específico de un metal (es decir, peso divido volumen, en unidades de g/cm³). Para esto, disponemos de barras de dicho metal, con base de 1cm² y largos diversos, y de una balanza que tiene pequeños errores de medición (desconocidos). Vamos a estimar el peso específico _R_ del metal de la siguiente manera:

Sabemos que el volumen de una barra de largo `m` es `m`cm³, por lo que su peso debería ser `R*m`. Queremos estimar `R`. Utilizando la balanza, tendremos los pesos aproximados de distintas barras, con ciertos errores de medición. Si ajustamos un modelo lineal a los datos de volumen y peso aproximado vamos a tener una buena aproximación para `R` (la pendiente de la recta).

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

 + Estimá el peso específico del metal mirando el coeficiente obtenido.

 + Graficá los datos junto con la recta del ajuste, y calculá el error cuadrático medio.

 + Guardá el código en un archivo `peso_especifico.py`.

*Cuidado:* por cómo planteamos el problema, estamos ajustando una recta con ordenada al origen igual a cero. Para esto tendrás que usar el parámetro `fit_intercept = False` en la declaración de tu modelo.


### Ejercicio 10.17: Altura y diámetro de árboles.
Queremos comparar las formas de las siguientes especies de árboles en los parques de Buenos Aires:

- Jacarandá,
- Palo borracho rosado,
- Eucalipto, y
- Ceibo.

Vamos a trabajar nuevamente con el archivo de arbolado porteño en parques que tenés en el archivo 'Data/arbolado-en-espacios-verdes.csv'.

+ Cargá los datos en un DataFrame `data_arbolado_parques`.

+ Para cada especie, seleccioná los datos correspondientes, realizá un ajuste lineal (sin ordenada al orígen) de la altura dependiendo del diámetro a la altura del pecho. Realizá un scatterplot de los datos de la especie junto con la recta de regresión lineal. 

+ Realizá un gráfico comparando los cuatro modelos obtenidos.

+ Guardá el código de este ejercicio en un archivo `ajuste_arboles.py`.


*Observación*: Como podés ver en los scatterplots, para árboles más anchos hay mayor variabilidad de alturas que para árboles angostos. Esto implica que el modelo va a ser más sensible a datos de árboles anchos que a datos de árboles angostos. Esta caraceterística se llama _heterocedasticidad_ y muchas veces es un problema para usar regresiones lineales. Por ejemplo no es posible aplicar directamente tests de hipótesis a los resultados obtenidos. 

Para explicarlo con un ejemplos: imaginá que tenemos tres pares de datos (_DAP_ y _altura_ para un árbol angosto, para un árbol mediano y para un árbol muy ancho) y supongamos que hay una relación lineal _real_ que es la que estamos buscando estimar a partir de los datos. La altura del arbol angosto va a variar unos pocos centímetros respecto a este modelo ideal mientras que la altura del árbol ancho puede variar muchos metros. Esto hace que el _residuo_ del árbol grueso respecto al modelo ideal sea mucho mayor que el residuo del árbol angosto y, por lo tanto, que su infuencia en los coeficientes estimados sea mayor también. Esto viola una de las hipótesis de la regresión lineal (la *homosedasticidad*) que dice todos los residuos tienen la *misma* distribución.

En este caso contamos con una gran cantidad de datos y podemos aplicar de todas formas la regresión en el marco de un análsis exploratorio de los datos.

### Ejercicio 10.18: Gráficos de ajuste lineal con Seaborn
 + Seleccioná los datos correspondientes a las especies: Jacarandá, Palo borracho rosado, Eucalipto y Ceibo, todas en un mismo DataFrame, usando el siguiente filtro.

 ```Python
 filtro = data_arbolado_parques['nombre_com'].isin(esp_selec)
 ```

 + Explorá el comando de seaborn `sns.regplot()`, que ajusta el modelo lineal y lo grafica sin pasar por scikit learn. El parámetro `order` te permite hacer ajustes polinomiales. El `ci` se refiere al intervalo de confianza a sombrear.

 + Para facilitar la comparación que hiciste en el ejercicio anterior, graficá todos los ajustes juntos usando:

 ```python
 g = sns.FacetGrid(datos_selec_p, col = 'nombre_com')
 g.map(sns.regplot, 'diametro', 'altura_tot')
 ```

*Observación*: Nos quedaron afuera de esta clase temas importantes como sobreajuste (_Overfitting_), partición de los datos en conjuntos de entrenamiento y evaluación, validación cruzada, presencia de datos atípicos (outliers), tests de hipótesis, selección de modelos... No era nuestra idea dar estos contenidos sino mostrar un acercamiento práctico desde Python al problema de la regresión lineal.


[Contenidos](../Contenidos.md) \| [Anterior (3 Práctica de Recursión)](03_EjerciciosRec.md) \| [Próximo (5 Cierre de la clase de Recursión)](05_Cierre.md)

