[Contenidos](../Contenidos.md) \| [Próximo (2 Manejo de carpetas)](02_Archivos_y_Directorios.md)

# 7.1 Manejo de fechas y horas

## El módulo datetime

A continuación introducimos el módulo `datetime` que permite manipular adecuadamente fechas y horas. Este módulo tiene definida una clase `datetime` (sí, la clase tiene el mismo nombre que el módulo), que permite almacenar un instante temporal (fecha y hora). También tiene definida la clase `date` que  almacena sólo una fecha. Análogamente tiene la clase `time` que sólo almacena una hora. Finalmente, en esta breve introducción al módulo `datetime` mencionaremos la clase `timedelta` que permite almacenar y manipular deltas de tiempo, es decir, duraciones.

**intercalarle un par de ejercicios**

### Ejemplo: Obtener fecha y hora actuales

```python
import datetime

fecha_hora = datetime.datetime.now()
print(fecha_hora)
```

Cuando corras este código, vas a obtener algo así:

```
2020-09-24 10:03:18.636670
```

Lo que hicimos fue importar el módulo **datetime** con la instrucción `import datetime`. Luego utilizamos la clase `datetime` del módulo, y usamos el métido `now()` para crear el objeto `fecha_hora` con la fecha y la hora actuales.


### Ejemplo: Obtener fecha actual

```python
import datetime

fecha = datetime.date.today()
print(fecha)
```

Cuando corras este código, vas a obtener algo así:


```
2020-09-24
```

Acá usamos el método `today()` de la clase `date` para obtener la fecha actual.

**Qué hay dentro de datetime?**

Podemos usar la función `dir()` para obtener una lista de todos los atributos del módulo.

```python
import datetime

print(dir(datetime))
```

Si lo hacés, vas a obtener algo así:

```
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_divide_and_round', 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo']
```


Las clases más usadas del módulo datetime son:

* date
* time
* datetime
* timedelta

## La clase datetime.date

Podés generar objetos de tipo fecha con la clase `date`. Un objeto de esta clase representa una fecha (año, mes, día).


### Ejemplo: Un objeto para representar una fecha

```python
import datetime

d = datetime.date(2019, 4, 13)
print(d)
```

Si corrés el código, vas a obtener:

```
2019-04-13
```

El comando `date()` de este ejemplo es un constructor de la clase `date`. Este constructor toma tres argumentos, año, mes y día.

La variable `d` es un objeto fecha.

Podríamos importar directamente la clase `date` del módulo `datetime`:

```python
from datetime import date

d = date(2019, 4, 13)
print(d)
```


### Ejemplo: Obtener la fecha a partir de un timestamp

También podemos crear objetos `date` desde un timestamp. Un timestamp de Unix es el número de segundos transcurridos desde el primero de enero de 1970 a las 0 horas UTC hasta un determinado momento. Podés convertir un timestamp a fecha usando el método `fromtimestamp()`.


```python
from datetime import date

timestamp = date.fromtimestamp(1326244364)
print('Fecha =', timestamp)
```

Si corrés este código, vas a obtener:

```
Fecha = 2012-01-11
```


### Ejemplo: Imprimir el año, el mes y el día por separado.

Así podés obtener el año, el mes, el día y el día de la semana:

```python
from datetime import date

hoy = date.today()

print('Año actual:', hoy.year)
print('Mes actual:', hoy.month)
print('Día actual:', hoy.day)
print('Día de la semana:', hoy.weekday()) # va de 0 a 6 empezando en lunes
```

## datetime.time

Un objeto de la clase `time` representa el tiempo local.


### Ejemplo: Representar la hora con un objeto `time`

Con el comando `time()` representamos un horario.

```python
from datetime import time

a = time()       # time(hour = 0, minute = 0, second = 0)
print('a =', a)

b = time(11, 34, 56)
print('b =', b)

c = time(hour = 11, minute = 34, second = 56)
print('c =', c)

                # time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print('d =', d)
```

Al correr el código vas a obtener lo siguiente:

```
a = 00:00:00
b = 11:34:56
c = 11:34:56
d = 11:34:56.234566
```


### Ejemplo: Imprimir horas, minutos, segundos y microsegundos

Una vez que creaste un objeto `time`, podés imprimir sus atributos así:

```python
from datetime import time

a = time(11, 34, 56)

print('hour =', a.hour)
print('minute =', a.minute)
print('second =', a.second)
print('microsecond =', a.microsecond)
```

Como no le pasaste ningún valor para el argumento `microsecond`, éste va a tomar el valor predeterminado, que es `0`.

## datetime.datetime

El módulo `datetime` tiene una clase llamada `datetime` que contiene información de fecha y hora a la vez.

### Ejemplo: Objeto datetime

```python
from datetime import datetime

#datetime(year, month, day)
a = datetime(2018, 11, 28)
print(a)

# datetime(year, month, day, hour, minute, second, microsecond)
b = datetime(2017, 11, 28, 23, 55, 59, 342380)
print(b)
```
Al correr el código vas a obtener:

```
2018-11-28 00:00:00
2017-11-28 23:55:59.342380
```


Los primeros tres argumentos, `year`, `month` y `day` del constructor `datetime()` son obligatorios.


### Ejemplo: Imprimir año, mes, día, hora, minutos, timestamp

```python
from datetime import datetime

a = datetime(2017, 11, 28, 23, 55, 59, 342380)
print('año =', a.year)
print('mes =', a.month)
print('día =', a.day)
print('hora =', a.hour)
print('minuto =', a.minute)
print('timestamp =', a.timestamp())
```

Al correr el código vas a obtener:

```
año = 2017
mes = 11
día = 28
hora = 23
minuto = 55
timestamp = 1511913359.34238
```


## datetime.timedelta

Un objeto `timedelta` representa una duración, es decir, la diferencia entre dos fechas o momentos.

### Ejemplo: Diferencia entre fechas y horarios

```python
from datetime import datetime, date

t1 = date(year = 2018, month = 7, day = 12)
t2 = date(year = 2017, month = 12, day = 23)
t3 = t1 - t2
print('t3 =', t3)

t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print('t6 =', t6)

print('type of t3 =', type(t3))
print('type of t6 =', type(t6))  
```

Al correr el código vas a obtener:

```
t3 = 201 days, 0:00:00
t6 = -333 days, 1:14:20
type of t3 = <class 'datetime.timedelta'>
type of t6 = <class 'datetime.timedelta'>
```

Observá que `t3` y `t6` son de tipo `<class 'datetime.timedelta'>`.


### Ejemplo: Diferencia entre objetos timedelta

```python
from datetime import timedelta

t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2

print('t3 =', t3)
```

Si corrés el código vas a obtener:


```
t3 = 14 days, 13:55:39
```


`t3` también es de tipo `<class 'datetime.timedelta'>`.


### Ejemplo: Imprimir objetos timedelta negativos

```python
from datetime import timedelta

t1 = timedelta(seconds = 33)
t2 = timedelta(seconds = 54)
t3 = t1 - t2

print('t3 =', t3)
print('t3 =', abs(t3))
```

Al correrlo vas a obtener:

```
t3 = -1 day, 23:59:39
t3 = 0:00:21
```


### Ejemplo: Duración en segundos

Podés obtener el tiempo medido en segundos usando el método `total_seconds()`.

```python
from datetime import timedelta

t = timedelta(days = 5, hours = 1, seconds = 33, microseconds = 233423)
print('total seconds =', t.total_seconds())
```
Al correrlo vas a obtener:

```
total seconds = 435633.233423
```


También podés sumar fechas y horarios usando el operador `+`. También podés multiplicar o dividir un objeto `timedelta` por números enteros o floats.


## Formato para fechas y horas

Hay diversas formas de representar el tiempo, que varían según el lugar, la organización, etc. Por ejemplo, en Argentina solemos usar `dd/mm/yyyy`, y en otros lugares es más común usar `mm/dd/yyyy`.

En Python tenemos los métodos `strftime()` y `strptime()` para manejar esto.


### Python strftime() - convertir un objeto datetime a string

El método `strftime()` está definido en las clases `date`, `datetime` y `time`. Este método crea una cadena con formato a partir estos objetos.


### Ejemplo: Formato de fecha usando strftime()

```python
from datetime import datetime

now = datetime.now()

t = now.strftime('%H:%M:%S')
print('time:', t)

s1 = now.strftime('%m/%d/%Y, %H:%M:%S')
# en formato mm/dd/YY H:M:S
print('s1:', s1)

s2 = now.strftime('%d/%m/%Y, %H:%M:%S')
# en formato dd/mm/YY H:M:S
print('s2:', s2)
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
from datetime import datetime

date_string = '21 June, 2018'
print('date_string =', date_string)

date_object = datetime.strptime(date_string, '%d %B, %Y')
print('date_object =', date_object)
```

Cuando lo corras, vas a obtener:

```
date_string = 21 June, 2018
date_object = 2018-06-21 00:00:00
```

El método `strptime()` toma dos argumentos:

* una cadena que representa una fecha y hora
* un código de formato correspondiente al primer argumento

Los códigos de formato `%d`, `%B`, `%Y` significan  `day`, `month` (full name) y `year` respectivamente.

Visitá [la documentación](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior) para más detalles.

## Ejercicios:

### Ejercicio 7.1: Segundos vividos
Escribí una función a la que le pasás tu fecha de nacimiento como cadena en formato 'dd/mm/AAAA' (año me día, con 4, 2 y 2 dígitos, separados con barras normales) y te devuelve la cantidad de segundos que viviste (asumiendo que naciste a las 00:00hs de tu fecha de nacimiento).

### Ejercicio 7.2: Cuánto falta
Escribí un programa que calcule cuántos días faltan para fin de año.

### Ejercicio 7.3: Calcular licencia
Si tenés una licencia por ma(pa)ternidad que empieza el 26 de septiembre de 2020 y dura 200 días, ¿qué día te reincorporás al trabajo?

### Ejercicio 7.4: Días hábiles
Escribí una función `dias_habiles(inicio, fin, feriados)` que calcule los días hábiles en un determinado lapso temporal. La función debe tener como argumentos el día inicial, el día final, y una lista con las fechas correspondientes a los feriados que haya en ese lapso, y debe devolver una lista con las fechas de días hábiles del período.

Consideramos día hábil a un día que no es feriado ni sábado ni domingo.


[Contenidos](../Contenidos.md) \| [Próximo (2 Manejo de carpetas)](02_Archivos_y_Directorios.md)

