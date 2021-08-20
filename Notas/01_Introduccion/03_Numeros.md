# 1.3 Números

Esta sección introduce las operaciones matemáticas elementales. Acá te dejamos un breve [video](https://youtu.be/NTWF9KKaCm0) sobre el uso de la variables booleanas.

### Tipos de números

Python tiene 4 tipos de números:

* Booleanos
* Enteros
* Punto flotante
* Complejos (con parte real y parte imaginaria)

### Booleanos (bool)

Las variables booleanas se llaman así en honor al lógico inglés [George Boole](https://es.wikipedia.org/wiki/George_Boole). Pueden tomar dos valores: `True` y `False` (verdadero y falso).

```python
a = True
b = False
```

Internamente, son evaluados como enteros con valores `1`, `0`.

```python
c = 4 + True # 5
d = False
if d == 0:
    print('d is False')
```

*No escribas código basado en esta convención. Sería bastante raro.*

### Enteros (int)

Representan números enteros (positivos y negativos) de cualquier magnitud:

```python
a = 37
b = -299392993727716627377128481812241231
```
Incluso se pueden especificar en diferentes bases:
```python
c = 0x7fa8      # Hexadecimal
d = 0o253       # Octal
e = 0b10001111  # Binario
```

Operaciones usuales:

```
x + y      Suma
x - y      Resta
x * y      Multiplicación
x / y      División (da un float, no un int)
x // y     División entera (da un int)
x % y      Módulo (resto)
x ** y     Potencia
abs(x)     Valor absoluto
```

La unidad mínima de almacenamiento de una computadora es un bit, que puede valer 0 o 1. Los números, caracteres e incluso imágenes y sonido son almacenados en la máquina usando bits. Los números enteros positivos, en particular, suelen almacenarse mediante su representación binaria (o en base dos).

| Número        | Representación binaria       |
| ------------- |-------------|
| 1 | 1|
| 2 | 10|
| 3 | 11|
| 4 | 100|
| 5 | 101|
| 6 | 110|


Hay algunas operaciones primitivas que se pueden hacer con los enteros a partir de su representación como bits:
```python
x << n     Desplazamiento de los bits a la izquierda
x >> n     Desplazamiento de los bits a la derecha
x & y      AND bit a bit.
x | y      OR bit a bit.
x ^ y      XOR bit a bit.
~x         NOT bit a bit.
```

Al desplazar a la izquierda, simplemente agregamos un cero en la última posición. Así, por ejemplo si corremos el 1 dos lugares a la izquierda obtenemos un 4:

```python
>>> 1 << 2 # 1 << 2 -> 100
4
>>> 6 & 3 # 110 & 011 -> 010
2
```

Al desplazar los bits de un número a la derecha un lugar, el último bit "se cae".

```python
>>> 1 >> 1 # 1 -> 0
0
>>> 6 >> 1 # 110 -> 11
3
```




### Punto flotante (float)

Usá una notación con decimales o una notación científica para especificar un valor de tipo punto flotante:

```python
a = 37.45
b = 4e5 # 4 x 10**5 o 400,000
c = -1.345e-10
```

Los números de tipo floats son representados en la máquina como números de doble precisión usando la representación nativa del microprocesador que sigue el estándar [IEEE 754](https://es.wikipedia.org/wiki/IEEE_754).
Para los que los conozcan: es el mismo tipo que los `double` en el lenguaje C.

> Un `float` almacenan hasta 17 digitos con un
> exponente entre -308 to 308

Cuidado que la aritmética de los números de punto flotante no es exacta.

```python
>>> a = 2.1 + 4.2
>>> a == 6.3
False
>>> a
6.300000000000001
>>>
```

Esto **no es un problema de Python**, si no el resultado de la forma en que el hardware de nuestras computadoras almacena los números de punto flotante.

Operaciones usuales:

```
x + y      Suma
x - y      Resta
x * y      Multiplicación
x / y      División (da un float, no un int)
x // y     División entera (da un float, pero con ceros luego del punto)
x % y      Módulo (resto)
x ** y     Potencia
abs(x)     Valor absoluto
```

Estas son las mismas operaciones que con los enteros. Otras operaciones usuales se encuentran en el módulo `math`.

```python
import math
a = math.sqrt(x)
b = math.sin(x)
c = math.cos(x)
d = math.tan(x)
e = math.log(x)
```

El módulo `math` también tiene constantes (`math.e`, `math.pi`), entre otras cosas.


### Comparaciones

Las siguientes comparaciones (suelen llamarse *operadores relacionales* ya que expresan una relación entre dos elementos) funcionan con números:

```
x < y      Menor que
x <= y     Menor o igual que
x > y      Mayor que
x >= y     Mayor o igual que
x == y     Igual a
x != y     No igual a
```

Observá que el `==` se usa para comparar dos elementos mientras que el `=` se usa para asignar un valor a una variable. Son símbolos distintos que cumplen funciones diferentes.

Podés formar expresiones booleanas más complejas usando

`and`, `or`, `not`

Acá mostramos algunos ejemplos:

```python
if b >= a and b <= c:
    print('b está entre a y c')

if not (b < a or b > c):
    print('b sigue estando entre a y c')
```

### Conversión de números

El nombre de un tipo (de datos) puede ser usado para convertir valores:

```python
a = int(x)    # Convertir x a int
b = float(x)  # Convertir x a float
```

Probalo.

```python
>>> a = 3.14159
>>> int(a)
3
>>> b = '3.14159' # También funciona con cadenas que representan números.
>>> float(b)
3.14159
>>>
```

*Cuidado: el separador decimal en Python es el punto, como en inglés, y no la coma del castellano. Por eso el comando `float(3,141592)` da un `ValueError`.*

## Ejercicios

Recordatorio: Asumimos que estás trabajando en el subdirectorio `ejercicios_python/Clase01/`. Buscá el archivo `hipoteca.py` y hacé los ejercicios en ese archivo, usando un editor de texto. Ejecutalo desde la línea de comandos.

### Ejercicio 1.7: La hipoteca de David
David solicitó un crédito a 30 años para comprar una vivienda, con una tasa fija nominal anual del 5%. Pidió $500000 al banco y acordó un pago mensual fijo de $2684,11.

El siguiente es un programa que calcula el monto total que pagará David a lo largo de los años:

```python
# hipoteca.py

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual

print('Total pagado', round(total_pagado, 2))
```

Copiá este código y correlo. Deberías obtener `966279.6` como respuesta.

### Ejercicio 1.8: Adelantos
Supongamos que David adelanta pagos extra de $1000/mes durante los primeros 12 meses de la hipoteca.

Modificá el programa para incorporar estos pagos extra y que imprima el monto total pagado junto con la cantidad de meses requeridos.

Cuando lo corras, este nuevo programa debería dar un pago total de  `929965.62` en 342 meses.

Aclaración: aunque puede parecer sencillo, este ejercicio requiere que agregues una variable *mes* y que prestes bastante atención a cuándo la incrementás, con qué valor entra al ciclo y con qué valor sale del ciclo. Una posiblidad es inicializar *mes* en 0 y otra es inicializarla en 1. En el primer caso es problable que la variable salga del ciclo contando la cantidad de pagos que se hicieron, en el segundo, ¡es probable que salga contando la cantidad de pagos más uno!

### Ejercicio 1.9: Calculadora de adelantos
¿Cuánto pagaría David si agrega $1000 por mes durante cuatro años, comenzando en el sexto año de la hipoteca (es decir, luego de 5 años)?

Modificá tu programa de forma que la información sobre pagos extras sea incorporada de manera versátil. Agregá las siguientes variables antes del ciclo, para definir el comienzo, fin y monto de los pagos extras:

```python
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
```

Hacé que el programa tenga en cuenta estas variables para calcular el total a pagar apropiadamente.

### Ejercicio 1.10: Tablas
Modicá tu programa para que imprima una tabla mostrando el mes, el total pagado hasta el momento y el saldo restante. La salida debería verse aproximadamente así:

```bash
1 2684.11 499399.22
2 5368.22 498795.94
3 8052.33 498190.15
4 10736.44 497581.83
5 13420.55 496970.98
...
308 874705.88 3478.83
309 877389.99 809.21
310 880074.1 -1871.53
Total pagado:  880074.1
Meses:  310
```

### Ejercicio 1.11: Bonus
Ya que estamos, corregí el código anterior de forma que el pago del último mes se ajuste a lo adeudado.

Asegurate de guardar en el archivo  `hipoteca.py` esta última versión en tu directorio `ejercicios_python/Clase01/`. Vamos a volver a trabajar con él.

### Ejercicio 1.12: Un misterio
Las funciones `int()` y `float()` pueden usarse para convertir números. Por ejemplo,

```python
>>> int("123")
123
>>> float("1.23")
1.23
>>>
```

Con esto en mente, ¿podrías explicar el siguiente comportamiento?

```python
>>> bool("False")
True
>>>
```

### Ejercicio 1.13: El volumen de una esfera
En tu directorio de trabajo de esta clase, escribí un programa llamado `esfera.py` que le pida a le usuarie que ingrese por teclado el radio *r* de una esfera y calcule e imprima el volumen de la misma. *Sugerencia: recordar que el volumen de una esfera es 4/3 πr^3*.

Finalmente, ejecutá el programa desde la línea de comandos para responder ¿cuál es el volumen de una esfera de radio 6? Debería darte `904.7786842338603`.


