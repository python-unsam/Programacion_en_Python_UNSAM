[Contenidos](../Contenidos.md) \| [Próximo (2 Manejo de archivos y carpetas)](02_Archivos_y_Directorios.md)

# 7.1 Manejo de fechas y horas


## El módulo datetime

A continuación introducimos el módulo `datetime` que permite trabajar con fechas y horas. Este módulo define un nuevo tipo de objeto: `datetime` (sí, con el mismo nombre del módulo), que permite representar un instante temporal (fecha y hora). También  define objetos de tipo `date`  para representar sólo una fecha y de tipo `time` para guardar y trabajar con horarios. Finalmente, en esta breve introducción al módulo `datetime` mencionamos el tipo `timedelta` que se usa para representar diferencias entre instantes de tiempos, es decir, duraciones y trabajar con ellas.

### Ejemplo: Obtener fecha y hora actuales

```python
>>> import datetime

>>> fecha_hora = datetime.datetime.now()
>>> print(fecha_hora)
2020-09-24 10:03:18.636670
```

Lo que hicimos fue importar el módulo **datetime** y usar el método `now()` de la clase `datetime` del módulo (con el mismo nombre) para crear el objeto `fecha_hora` que va a contener la fecha y la hora actuales.


### Ejemplo: Obtener fecha actual

Análogamente, podemos obtener solo la fecha:

```python
>>> fecha = datetime.date.today()
>>> print(fecha)
2020-09-24
```

Acá usamos el método `today()` de la clase `date` para obtener la fecha actual.

**¿Qué hay dentro del módulo datetime?**

En Python podemos usar la función `dir()` para obtener una lista de todos los atributos de un módulo.

```python
>>> print(dir(datetime))
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__',
 '__loader__', '__name__', '__package__', '__spec__', '_divide_and_round',
 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo']
```


Nos vamos a concentrar en lo más usado de `datetime`:

* date
* time
* datetime
* timedelta


## La clase datetime.date

Podés generar objetos de tipo fecha con la clase `date`. Un objeto de esta clase representa una fecha (año, mes, día).


### Ejemplo: Un objeto para representar una fecha

```python
>>> d = datetime.date(2019, 4, 13)
>>> print(d)
2019-04-13
```

El comando `date()` de este ejemplo construye un objeto de tipo `date`. Este _constructor_ toma tres argumentos: año, mes y día.

La variable `d` es un objeto de tipo `date` (es decir, representa una fecha).

También podríamos importar directamente la clase `date` del módulo `datetime`:

```python
>>> from datetime import date
>>>
>>> d = date(2019, 4, 13)
>>> print(d)
2019-04-13
```

### Ejemplo: Obtener la fecha a partir de un timestamp

En los sistemas operativos derivados de Unix (Mac OS X, Linux, etc.) se toma como medida de tiempo el número de segundos transcurridos desde el primero de enero de 1970 a las 0 horas UTC hasta el momento a representar. Se lo conoce como Unix timestamp. Podés convertir un timestamp a fecha usando el método `fromtimestamp()`.


```python
>>> from datetime import date
>>>
>>> timestamp = date.fromtimestamp(1326244364)
>>> print('Fecha =', timestamp)
Fecha = 2012-01-10
```

Esto es importante porque las fechas de modificación de los archivos usan timestamps por ejemplo.

### Ejemplo: Obtener el año, el mes y el día por separado.

Así podés obtener el año, el mes, el día y el día de la semana:

```python
from datetime import date

hoy = date.today()

print('Año actual:', hoy.year)
print('Mes actual:', hoy.month)
print('Día actual:', hoy.day)
print('Día de la semana:', hoy.weekday()) # va de 0 a 6 empezando en lunes
```

## La clase datetime.time

Un objeto de la clase `time` representa la hora local (de como este configurada tu computadora). No nos vamos a meter en esta clase con los [husos horarios](https://es.wikipedia.org/wiki/Huso_horario) (conocido también como timezones), pero si vas a usar datos provistos por otres, es importante que sepas si está expresado en tu hora local, en la hora local de otro lugar o en [UTC](https://es.wikipedia.org/wiki/Tiempo_universal_coordinado).

### Ejemplo: Representar la hora con un objeto `time`

La clase  `time` se usa para representar horarios. A continuación damos algunos ejemplos de constructores de esta clase (un constructor es una forma de construir un objeto de una clase dada, una forma de inicializarlo, digamos).

```python
>>> from datetime import time
>>>
>>> a = time()       # time(hour = 0, minute = 0, second = 0)
>>> print('a =', a)
a = 00:00:00

>>> b = time(11, 34, 56)
>>> print('b =', b)
b = 11:34:56

>>> c = time(hour = 11, minute = 34, second = 56)
>>> print('c =', c)
c = 11:34:56

>>> d = time(11, 34, 56, 234566)  # time(hour, minute, second, microsecond)
>>> print('d =', d)
d = 11:34:56.234566
```


### Ejemplo: Obtener horas, minutos, segundos y micro-segundos

Una vez que creaste un objeto `time`, podés extraer sus atributos así:

```python
from datetime import time

a = time(11, 34, 56)

print('hour =', a.hour)
print('minute =', a.minute)
print('second =', a.second)
print('microsecond =', a.microsecond)
```

Como no le pasaste ningún valor para el argumento `microsecond`, éste va a tomar el valor predeterminado, que es `0`.

## La clase datetime.datetime

Como ya mencionamos, el módulo `datetime` tiene una clase con su mismo nombre que permite almacenar información de fecha y hora en un solo objeto.

### Ejemplo: Objeto datetime

```python
>>> from datetime import datetime

>>> # datetime(year, month, day)
>>> a = datetime(2020, 4, 21)
>>> print(a)
2020-04-21 00:00:00

>>> # datetime(year, month, day, hour, minute, second, microsecond)
>>> b = datetime(2021, 4, 21, 6, 53, 31, 342260)
>>> print(b)
2021-04-21 06:53:31.342260
```

Los primeros tres argumentos, `year`, `month` y `day` del constructor `datetime()` son obligatorios. Los otros tienen a 0 como valor por omisión.

### Ejemplo: Obtener año, mes, día, hora, minutos, timestamp de un datetime

El siguiente código genera un objeto `datetime` con valores pasados por parámetro y luego imprime la información.

En particular, muestra cómo convertir una fecha a timestamp. En general los timestamps son enteros y no tienen en cuenta las décimas de segundos.

```python
from datetime import datetime

a = datetime(2021, 4, 21, 6, 53, 31, 342260)
print('año =', a.year)
print('mes =', a.month)
print('día =', a.day)
print('hora =', a.hour)
print('minuto =', a.minute)
print('timestamp =', a.timestamp())
```

## La clase datetime.timedelta

Un objeto `timedelta` representa una duración, es decir, la diferencia entre dos instantes de tiempo.

### Ejemplo: Diferencia entre fechas y horarios

```python
>>> from datetime import datetime, date

>>> t1 = date(year = 2021, month = 4, day = 21)
>>> t2 = date(year = 2020, month = 8, day = 23)
>>> t3 = t1 - t2
>>> print(t3)
241 days, 0:00:00

>>> t4 = datetime(year = 2020, month = 7, day = 12, hour = 7, minute = 9, second = 33)
>>> t5 = datetime(year = 2021, month = 6, day = 10, hour = 5, minute = 55, second = 13)
>>> t6 = t4 - t5
>>> print(t6)
-333 days, 1:14:20

>>> print('tipo de t3 =', type(t3))
tipo de t3 = <class 'datetime.timedelta'>

>>> print('tipo de t6 =', type(t6))
tipo de t6 = <class 'datetime.timedelta'>
```

Observá que `t3` y `t6` son de tipo `<class 'datetime.timedelta'>`.


### Ejemplo: Diferencia entre objetos timedelta

```python
>>> from datetime import timedelta

>>> t1 = timedelta(weeks = 1, days = 2, hours = 1, seconds = 33)
>>> t2 = timedelta(days = 6, hours = 11, minutes = 4, seconds = 54)
>>> t3 = t1 - t2

>>> print('t3 =', t3)
2 days, 13:55:39
```

`t3` también es de tipo `<class 'datetime.timedelta'>`.


### Ejemplo: Imprimir objetos timedelta negativos

```python
>>> from datetime import timedelta

>>> t1 = timedelta(seconds = 21)
>>> t2 = timedelta(seconds = 55)
>>> t3 = t1 - t2

>>> print(t3)
-1 day, 23:59:26

>>> print(abs(t3))
0:00:34
```


### Ejemplo: Duración en segundos

Podés obtener el tiempo medido en segundos usando el método `total_seconds()`.

```python
>>> from datetime import timedelta

>>> t = timedelta(days = 1, hours = 2, seconds = 30, microseconds = 100000)
>>> print('segundos totales =', t.total_seconds())
segundos totales = 93630.1
```

También podés sumar fechas y horarios usando el operador `+`. También podés multiplicar o dividir un objeto `timedelta` por números enteros o floats.


## Formato para fechas y horas

Hay diversas formas de representar el tiempo, que varían según el lugar, la organización, etc. Por ejemplo, en Argentina solemos usar `dd/mm/yyyy`, mientras que en las culturas anglosajonas  es más común usar `mm/dd/yyyy`.

En Python tenemos los métodos `strftime()` y `strptime()` para manejar esto.


### Python strftime() - convertir un objeto datetime a string

El método `strftime()` está definido en las clases `date`, `datetime` y `time`. Este método crea una cadena con formato a partir estos objetos.


### Ejemplo: Formato de fecha usando strftime()

```python
>>> from datetime import datetime

>>> now = datetime.now()

>>> t = now.strftime('%H:%M:%S')
>>> print('hora:', t)
hora: 14:40:06

>>> s1 = now.strftime('%m/%d/%Y, %H:%M:%S')
>>> # en formato mm/dd/YY H:M:S
>>> print('s1:', s1)
s1: 09/24/2020, 14:40:06


>>> s2 = now.strftime('%d/%m/%Y, %H:%M:%S')
>>> # en formato dd/mm/YY H:M:S
>>> print('s2:', s2)
s2: 24/09/2020, 14:40:06

```


Acá, `%Y`, `%m`, `%d`, `%H` etc. son códigos de formato. El método `strftime()`toma uno o más códigos de formato y devuelve la cadena con formato basado en esos códigos.

En el programa de arriba, `t`, `s1` y `s2` son cadenas. Y los códigos de formato son:

* `%Y` - año [0001,..., 2018, 2019,..., 9999]
* `%m` - mes [01, 02, ..., 11, 12]
* `%d` - día [01, 02, ..., 30, 31]
* `%H` - hora [00, 01, ..., 22, 23
* `%M` - minuto [00, 01, ..., 58, 59]
* `%S` - segundo [00, 01, ..., 58, 59]


Para aprender más sobre `strftime()` visitá [la documentación](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior).


### Python strptime() - convertir una cadena a un objeto datetime

El método `strptime()` crea un objeto `datetime` a partir de una cadena.


### Ejemplo: strptime()

```python
>>> from datetime import datetime

>>> cadena_con_fecha= '21 September, 2021'
>>> print('date_string =', cadena_con_fecha)
date_string = 21 September, 2021

>>> date_object = datetime.strptime(cadena_con_fecha, '%d %B, %Y')
>>> print('date_object =', date_object)
date_object = 2021-09-21 00:00:00
```

El método `strptime()` toma dos argumentos:

* una cadena que representa una fecha y hora
* un código de formato correspondiente al primer argumento

Los códigos de formato `%d`, `%B`, `%Y` significan  `day`, `month` (full name) y `year` respectivamente.

Visitá [la documentación](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior) para más detalles.

## Ejercicios:

### Ejercicio 7.1: Segundos vividos
Escribí una función a la que le pasás tu fecha de nacimiento como cadena en formato 'dd/mm/AAAA' (día, mes, año con 2, 2 y 4 dígitos, separados con barras normales) y te devuelve la cantidad de segundos que viviste (asumiendo que naciste a las 00:00hs de tu fecha de nacimiento).

Guardá este código en el archivo `vida.py`.

### Ejercicio 7.2: Cuánto falta
Un conocido canal Argentino tiene por costumbre anunciar la cantidad de días que faltan para la próxima primavera.

![Figura](./cronica.jpg)


Escribí un programa que asista a los técnicos del canal indicándoles, al correr el programa el número que deben poner en la placa.

### Ejercicio 7.3: Fecha de reincorporación
Si tenés una licencia por xaternidad que empieza el 26 de septiembre de 2020 y dura 200 días, ¿qué día te reincorporás al trabajo?

### Ejercicio 7.4: Días hábiles
Escribí una función `dias_habiles(inicio, fin, feriados)` que calcule los días hábiles entre dos fechas dadas. La función debe tener como argumentos el día inicial, el día final, y una lista con las fechas correspondientes a los feriados que haya en ese lapso, y debe devolver una lista con las fechas de días hábiles del período, incluyendo la fecha inicial y la fecha final indicadas. Las fechas de entrada y salida deben manejarse en formato de texto.

Consideramos día hábil a un día que no es feriado ni sábado ni domingo.

Probala entre hoy y el 10 de octubre, sabiendo que no hay feriados en el medio.
Probala entre hoy y fin de año considerando los siguientes feriados de Argentina:

`feriados = ['12/10/2020', '23/11/2020', '7/12/2020', '8/12/2020', '25/12/2020']`



[Contenidos](../Contenidos.md) \| [Próximo (2 Manejo de archivos y carpetas)](02_Archivos_y_Directorios.md)

