[Contenidos](../Contenidos.md) \| [Anterior (2 Manejo de carpetas)](02_Archivos_y_Directorios.md) \| [Próximo (4 Plots con Pandas)](07_Pandas_graficos.md)

# 7.3 Introducción a Pandas

La  biblioteca Pandas es una extensión de NumPy para manipulación y análisis de datos. En particular, ofrece estructuras de datos y operaciones para manipular tablas de datos (numéricos o de otros tipos) y series temporales. Se distribuye como software libre.

Esta es una breve introducción [Pandas](https://pandas.pydata.org/docs/getting_started/index.html). Para información más completa te recomendamos consultar [la documentación oficial](https://pandas.pydata.org/docs/user_guide/10min.html).

Esta biblioteca tiene dos tipos de datos fundamentales: las `series` que contienen secuencias de datos y los `DataFrames` que almacenan tablas de datos. 


## Lectura de datos

Pandas permite leer diversos formatos de tablas de datos directamente. Probá el siguiente código, para leer un archivo CSV:

```python
import pandas as pd

directorio = 'Data'
archivo = 'arbolado-en-espacios-verdes.csv'
fname = os.path.join(directorio,archivo)
df = pd.read_csv(fname)
```

la variable `df` es de tipo `DataFrame` y continene todos los datos del archivo csv estructurados adecuadamente.

Con `df.head()` podés ver las primeras líneas de datos. Si a `head` le pasás un número como parámetro podés seleccionar cuántas lineas querés ver. Análogamente con `df.tail(n)` verás las últimas `n` líneas de datos.

```python
>>> df.head()
        long        lat  id_arbol  ...            origen       coord_x       coord_y
0 -58.477564 -34.645015         1  ...           Exótico  98692.305719  98253.300738
1 -58.477559 -34.645047         2  ...           Exótico  98692.751564  98249.733979
2 -58.477551 -34.645091         3  ...           Exótico  98693.494639  98244.829684
3 -58.478129 -34.644567         4  ...  Nativo/Autóctono  98640.439091  98302.938142
4 -58.478121 -34.644598         5  ...  Nativo/Autóctono  98641.182166  98299.519997
```


Usando `df.columns` pandas te va a devolver un índice con los nombres de las columnas del DataFrame. Recordá que en la \ref_sec{desc_arboles} describimos la base de datos. A su vez, `df.index` te mostrará el índice. En este caso el índice no es muy interesante, simplemente tenemos las filas numeradas. Veremos otros ejemplos donde el índice puede contener información vital, como un timestamp.

```python
>>> df.columns
Index(['long', 'lat', 'id_arbol', 'altura_tot', 'diametro', 'inclinacio',
       'id_especie', 'nombre_com', 'nombre_cie', 'tipo_folla', 'espacio_ve',
       'ubicacion', 'nombre_fam', 'nombre_gen', 'origen', 'coord_x',
       'coord_y'],
      dtype='object')
>>> df.index
RangeIndex(start=0, stop=51502, step=1)
```


Otra herramienta útil para inspeccionar los datos recien levantados es `describe()`. Para ver mejor una parte, podemos seleccionar algunas columnas de interés antes de pedirle la descripción.

```python
>>> df[['altura_tot', 'diametro', 'inclinacio']].describe()
         altura_tot      diametro    inclinacio
count  51502.000000  51502.000000  51502.000000
mean      12.167100     39.395616      3.472215
std        7.640309     31.171205      7.039495
min        0.000000      1.000000      0.000000
25%        6.000000     18.000000      0.000000
50%       11.000000     32.000000      0.000000
75%       18.000000     54.000000      5.000000
max       54.000000    500.000000     90.000000
```

## Selección

Una de las operaciones primitivas más importantes es la selección de fragmentos de las tablas de datos, ya sean filas, columnas o rangos de filas y columnas.

Por ejemplo con `df['nombre_com']` veremos la columna (que es una serie) de nombres comunes de los árboles en la base. Podemos usar `set` para ver una vez cada nombre:

```python
>>> set(df['nombre_com'])
{'Abedul blanco',
 'Abedul común (Abedul de Europa o Abedul verrugoso)',
 'Abutilo',
 'Acacia',
 'Acacia blanca',
 ...
}
```

Podemos preguntar cuáles se llaman de cierta manera ('Jacarandá' en este caso), como hacíamos con los ndarrays en numpy:

```python
>>> df['nombre_com']=='Jacarandá'
0        False
1        False
2        False
```

Observá que esto generó una serie. Podemos sumar los `True` de esta serie para contar la cantidad de Jacarandás:

```python
>>> (df['nombre_com']=='Jacarandá').sum()
3255
```

Si queremos hacer lo mismo para otras especies podemos usar `value_counts()`

```python
>>> cant_ejemplares = df['nombre_com'].value_counts()
>>> df['nombre_com'].value_counts().head(10)
Eucalipto               4112
Tipa blanca             4031
Jacarandá               3255
Palo borracho rosado    3150
Casuarina               2719
Fresno americano        2166
Plátano                 1556
Ciprés                  1467
Ceibo                   1149
Pindó                   1068
Name: nombre_com, dtype: int64
```

De esta forma obtenermos, en orden decreciente, los nombres comunes y las cantidades de las especies más frecuentes en la base de datos.

### Seleccion con indexación boolena

La serie booleana  que obtuvimos con `df['nombre_com']=='Jacarandá'` puede usarse para seleccionar esas filas del DataFrame:

```python
>>> dJ = df[df['nombre_com']=='Jacarandá']
```

Análogamente, podemos seleccionar algunas columnas de interés y generar vistas (ojo, en estos casos no estamos copiando la información):

```python
>>> cols = ['altura_tot', 'diametro', 'inclinacio']
>>> dJ=dJ[cols]
>>> dJ.tail()
       altura_tot  diametro  inclinacio
51104           7        97           4
51172           8        28           8
51180           2        30           0
51207           3        10           0
51375          17        40          20

>>> dJ.describe()
        altura_tot     diametro   inclinacio
count  3255.000000  3255.000000  3255.000000
mean     10.369585    28.804301     6.549923
std       5.905744    19.166388     8.459921
min       1.000000     1.000000     0.000000
25%       6.000000    14.000000     0.000000
50%      10.000000    25.000000     4.000000
75%      15.000000    41.000000    10.000000
max      49.000000   159.000000    70.000000
```

Observá que cuando le pedimos los últimos datos de `dJ` nos mostró los últimos 5 jacarandás de la base de datos, respetando los números de índice de la tabla original.

### Scatterplots

Pandas tambien usa matplotlib para permitirnos hacer gráficos fácilmente:

```python
>>> dJ.plot.scatter(x='altura_tot', y='diametro')
>>> Index(['Eucalipto', 'Tipa blanca', 'Jacarandá', 'Palo borracho rosado',
       'Casuarina', 'Fresno americano', 'Plátano', 'Ciprés', 'Ceibo', 'Pindó',
       ...
       'Naranjo dulce', 'Peltophorum', 'Ligustrina de California',
       'Afrocarpus', 'Caranday', 'Esterculea', 'Boj cepillo', 'Sesbania',
       'Ligustrum', 'Árbol del humo'],
      dtype='object', length=337)
```

### Selección por índice y por posición

Como ya mencionamos `df` no tiene un índice interesante. Veamos en cambio la serie que generamos con `cant_ejemplares = df['nombre_com'].value_counts()` si lo tiene:

```python
>>> cant_ejemplares.index
Index(['Eucalipto', 'Tipa blanca', 'Jacarandá', 'Palo borracho rosado',
       'Casuarina', 'Fresno americano', 'Plátano', 'Ciprés', 'Ceibo', 'Pindó',
       ...
       'Naranjo dulce', 'Peltophorum', 'Ligustrina de California',
       'Afrocarpus', 'Caranday', 'Esterculea', 'Boj cepillo', 'Sesbania',
       'Ligustrum', 'Árbol del humo'],
      dtype='object', length=337)
```

`cant_ejemplares` es una serie (es como un DataFrame de una sola columna). tiene los nombres de las especies como índice y sus respectivas cantidades como dato asociado.

Podemos usar los índices para acceder a una fila de un DataFarme o una Serie como en los siguientes ejemplos:

```python
>>> df.loc[165]
long                                                   -58.4684
lat                                                    -34.6648
id_arbol                                                    166
altura_tot                                                    5
diametro                                                     10
inclinacio                                                    0
id_especie                                                   11
nombre_com                                            Jacarandá
nombre_cie                                Jacarandá mimosifolia
tipo_folla                        Árbol Latifoliado Caducifolio
espacio_ve                                        INDOAMERICANO
ubicacion     LACARRA, Av. - ESCALADA, Av. - CASTAÑARES, Av....
nombre_fam                                         Bignoniáceas
nombre_gen                                            Jacarandá
origen                                         Nativo/Autóctono
coord_x                                                 99534.3
coord_y                                                 96061.8
Name: 165, dtype: object

>>> cant_ejemplares.loc['Eucalipto']
4112
```

También podemos acceder por posición usando `iloc`.

```python
>>> dJ.iloc[0] 
altura_tot     5
diametro      10
inclinacio     0
Name: 165, dtype: int64
```

Esto nos devuelve los datos de la primera fila de `dJ` que corresponde al índice 165 (lo dice en la última línea). También podemos acceder a rebanadas (slices) usando `iloc`:

```python
>>> cant_ejemplares.iloc[0:3]
Eucalipto      4112
Tipa blanca    4031
Jacarandá      3255
Name: nombre_com, dtype: int64
```

Por otra parte, podemos seleecciona tanto filas como columnas, si separamos con comas las respectivas selecciones:

    
```python
>>> dJ.iloc[-5:,2]
51104     4
51172     8
51180     0
51207     0
51375    20
Name: inclinacio, dtype: int64
```

### Selección de una columna

Si queremos seleccionar una sola columna podemos especificarla por medio de su nombre. Recordemos que al tener una sola columna tenemos una Series en lugar de un DataFrame:

```python
>>> dJd = dJ['diametro']
>>> type(dJ)
pandas.core.frame.DataFrame
>>> type(dJd)
pandas.core.series.Series
```

## Series temporales en Pandas

Pandas tiene un gran potencial para el manejo de series temporales. Es muy sencillo crear indices con fechas y frecuencias seleccionadas:
```python
>>> pd.date_range('20200923', periods=7)
DatetimeIndex(['2020-09-23', '2020-09-24', '2020-09-25', '2020-09-26',
               '2020-09-27', '2020-09-28', '2020-09-29'],
              dtype='datetime64[ns]', freq='D')

>>> pd.date_range('20200923 14:00', periods=7)
DatetimeIndex(['2020-09-23 14:00:00', '2020-09-24 14:00:00',
               '2020-09-25 14:00:00', '2020-09-26 14:00:00',
               '2020-09-27 14:00:00', '2020-09-28 14:00:00',
               '2020-09-29 14:00:00'],
              dtype='datetime64[ns]', freq='D')

>>> pd.date_range('20200923 14:00', periods=6, freq='H')
DatetimeIndex(['2020-09-23 14:00:00', '2020-09-23 15:00:00',
               '2020-09-23 16:00:00', '2020-09-23 17:00:00',
               '2020-09-23 18:00:00', '2020-09-23 19:00:00'],
              dtype='datetime64[ns]', freq='H')

```

Luego, podés usar esos índices junto con datos para aramr series temporales o DataFrames:

```python
>>> pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20200923 14:00', periods=6, freq='H'))
2020-09-23 14:00:00    1
2020-09-23 15:00:00    2
2020-09-23 16:00:00    3
2020-09-23 17:00:00    4
2020-09-23 18:00:00    5
2020-09-23 19:00:00    6
Freq: H, dtype: int64
```

### Caminatas al azar

Volviendo al tema de las caminatas al azar, podemos hacer una caminata de dos horas dando un paso por minuto a partir del comienzo de esta clase con el siguiente comando:

```python
>>> import random

>>> idx = pd.date_range('20200923 14:00', periods=120, freq='min')
>>> s1 = pd.Series(np.random.randint(-1,2,120), index=idx)
>>> s2 = s1.cumsum()
```

Podemos ver el gráfico sencillamentes:
```python
>>> s2.plot()
```

O usar una [media móvil](https://es.wikipedia.org/wiki/Media_m%C3%B3vil) (rolling mean) para suavizar los datos:
```python
>>> w = 5 #ancho en minutos de la ventana
>>> s3 = s2.rolling(w).mean()
>>> s3.plot()
```

Podés ver ambas curvas en un mismo gráfico para ver más claramente el efecto del suavizado:
```python
>>> pd.DataFrame([s2,s3]).T.plot()
```

Fijate que los datos van pueden estar desfazados. El parámetro `center = True` del método `rolling` te permite controlar esto. Probalo. Si te fijás, vas a ver que los primeros valores no tienen datos (ya que necesitás una ventana de tamaño `w` para poder suavizar). El parámetro  `min_periods = 1` del método `rolling` te permite controlar esto. Probálo.


### Ejemplo: 12 personas caminando 8 horas:

En el siguiente ejemplo creamos un índice que contenga un elemento por minuto apartir del comienzo de la clase y durante 8 horas. Armamos también una lista de nombres.

```python
>>> horas = 8
>>> idx = pd.date_range('20200923 14:00', periods=horas*60, freq='min')
>>> nombres = ['Pedro', 'Santiago', 'Juan', 'Andrés','Bartolomé','Tiago','Isca','Tadeo','Mateo','Felipe','Simón','Tomás']
```

Luego usamos el módulo random de numpy para generar pasos para cada persona y cada minuto. Los acumulamos con `cumsum` y los acomodamos en una DataFrame, usando el índice generado antes y poniendole nombres adecuados a cada columna:

```python
>>> dacum = pd.DataFrame(np.random.randint(-1,2,[horas*60,12]).cumsum(axis=0),index=idx, columns = nombres)
>>> dacum.plot()
```

Ahora suvizamos los datos, unsando `min_periods` para no perder los datos de los extremos

```python
>>> w = 45
>>> dsuav = dacum.rolling(w, min_periods = 1).mean()
>>> nsuav = ['S_' + n for n in nombres]
>>> dsuav.columns = nacum #Cambio el nombre de las columnas
>>> dsuav.plot()
```

### Guardando datos

Guardar una Series o un DataFrame en el disco es algo ralmente sencillo. Probá el por ejemplo el efecto del comando `dsuav.to_csv('CaminataApostolica.csv')`.

## Ejercicios de Arbolado lineal

### Ejercicio 7.5: Lectura y selección
Vamos a trabajar ahora con el archivo ['arbolado-publico-lineal-2017-2018.csv'](https://data.buenosaires.gob.ar/dataset/arbolado-publico-lineal). Descargalo y guardalo en tu ditectorio 'Data/'.

Levantalo y armá un DataFrame que tenga solamente las siguiente columnas:

```python
cols_sel = ['nombre_cientifico','ancho_acera','diametro_altura_pecho','altura_arbol']
```

Imprimí las diez especies más frecuentes con sus respectivas cantidades.

Trabajaremos con las siguientes especies seleccionadas:
```python
esp_sel = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
```

Una forma de seleccionarlas es la seguiente:

```python
We = np.array([n in esp_sel    for n in dl['nombre_cientifico']])
ds = dl[We]
```

### Ejercicio 7.6: Boxplots
El siguiente comando realiza un [boxplot](https://es.wikipedia.org/wiki/Diagrama_de_caja) de los diámteros de los árboles agrupados por especie.

```python
>>> ds.boxplot('diametro_altura_pecho',by='nombre_cientifico') 
```

Realizá un gráfico similar pero de los altos en lugar de los anchos de los árboles.

### Ejercicio 7.7: Comparando especies en parques y en veredas
Al comienzo abrimos el dataset de arboles en parques. Recién trabajamos con otro dataset: el de árboles en veredas. Ahora nos preguntamos si hay diferencias notables entre los ejemplares de una misma especie que crecen en el un tipo de sitio o en otro. Queremos hacer un boxplot de los DAP (diámetro a la altura del pecho) y para las Tipas (su nombre científico es *tipuana tipu*), que crecen en ambos tipos de sitio. Para esto tendremos que mezclar datos de dos bases de datos diferentes. 

Nos vamos en meter en un lío. El GCBA usa en un dataset 'altura_tot', 'diametro' y 'nombre_cie' para las alturas, diámetros y nombres científicos de los ejemplares, y en el otro dataset usa 'altura_arbol', 'diametro_altura_pecho' y 'nombre_cientifico' para los mismos datos.

Es más, los nombres científicos varían de un dataset al otro. 'Tipuana Tipu' se transforma en 'Tipuana tipu' y 'Jacarandá mimosifolia' en 'Jacaranda mimosifolia'. Obviamente son cambios menores pero suficientes para desalentar al usuario desprevenido.

En este ejercicio te proponemos los siguientes pasos para comparar los DAPs de las tipas en ambos tipos de entornos:

1. Abrí ambos dataset y llamamos dp y dv (por parques y veredas).
2. Para cada dateset armate otro seleccionando solamente las filas correspondientes a las tipas (llamalos dTTp y dTTv, respectivamente) y las columnas correspondientes a DAPs y alturas. Llamá a estas columnas 'DAP' y 'altura' para comanzar a uniformizar.
3. Agregale a cada nuevo dataframe (dTTp y dTTv) una columna llamada 'ambiente' que en un caso valga siempre 'parque' y en el otro caso 'vereda'. 
4. Juntá ambos datasets con el comando `dTT = pd.concat([dTTl, dTTp])` en uno solo que contenga los DAPs y altos de las tipas de ambos datasets, distinguiéndolos por ambiente.
5. Creá un boxplot para los DAPs de la tipas distinguiendo los ambientes (`boxplot('DAP',by='sitio')`).
6. Repetí para alturas.
7. Armá una función a la que le pases ambos datasets originales y los respectivos nombre científicos de una misma especie en cada dataset y te devuelva un DataFrame con los DAPs y alturas de todos los ejemplares distinguiéndolos por ambiente (pasos 2,3 y 4 anteriores).
8. Usá la función anterior para seleccionar los Jacarandás ('Jacarandá mimosifolia' y 'Jacaranda mimosifolia' se llaman en uno y otro dataset) y grafića los boxplots para ver si presentan diferencias en sus DAPs y en sus alturas.


[Contenidos](../Contenidos.md) \| [Anterior (2 Manejo de carpetas)](02_Archivos_y_Directorios.md) \| [Próximo (4 Plots con Pandas)](07_Pandas_graficos.md)

