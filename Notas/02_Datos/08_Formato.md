[Contenidos](../Contenidos.md) \| [Anterior (7 Arbolado porteño)](07_Arboles1.md) \| [Próximo (9 Cierre de la segunda clase)](09_CierreClase.md)

# 2.8 Impresión con formato

En esta sección se ven detalles técnicos sobre cómo hacer que la salida por pantalla sea más amena para el usuario. No es indispensable para el curso. Si te alcanza el tiempo está semana leela, sino no te preocupes podés volver a mirar acá en el futuro, cuando lo necesites.

Cuando trabajás con datos es usual que quieras imprimir salidas estructuradas (tablas, etc.). Por ejemplo:

```code
  Nombre      Cajones     Precio
----------  ----------  -----------
 Lima           100        32.20
 Naranja         50        91.10
 Caqui          150       103.44
 Mandarina      200        51.23
 Durazno         95        40.37
 Mandarina       50        65.10
 Naranja        100        70.44
```

### Formato de cadenas

Una excelente manera de darle formato a una cadena en Python (a partir de la versión 3.6) es usando `f-strings`.

```python
>>> nombre = 'Naranja'
>>> cajones = 100
>>> precio = 91.1
>>> f'{nombre:>10s} {cajones:>10d} {precio:>10.2f}'
'       Naranja        100      91.10'
>>>
```

La parte `{expresion:formato}` va a ser reemplazada. Usualmente los `f-strings` se usan con `print`.

```python
print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f}')
```

### Códigos de formato

Lo códigos de formato (lo que va luego de `:` dentro de `{}`) son similares a los que se usan en el `printf()` del lenguaje C. Los más comunes son:

```code
d       Entero decimal
b       Entero binario
x       Entero hexadecimal
f       Flotante como [-]m.dddddd
e       Flotante como [-]m.dddddde+-xx
g       Flotante, pero con uso selectivo de la notación exponencial E.
s       Cadenas
c       Caracter (a partir de un entero, su código)
```

Los modificadores permiten ajustar el ancho a imprimir o la precisión decimal (cantidad de dígitos luego del punto). Ésta es una lista parcial:

```code
:>10d   Entero alineado a la derecha en un campo de 10 caracteres
:<10d   Entero alineado a la izquierda en un campo de 10 caracteres
:^10d   Entero centrado en un campo de 10 caracteres
:0.2f   Flotante con dos dígitos de precisión
```

### Formato a diccionarios

Pores usar el método `format_map()` para aplicarle un formato a los valores de un diccionario:

```python
>>> s = {
    'nombre': 'Naranja',
    'cajones': 100,
    'precio': 91.1
}
>>> '{nombre:>10s} {cajones:10d} {precio:10.2f}'.format_map(s)
'       Naranja        100      91.10'
>>>
```

Usa los mismos códigos que los `f-strings` pero toma los valores que provee el diccionario.

### El método format()

Existe un método  `format()` que permite aplicar formato a argumentos.

```python
>>> '{nombre:>10s} {cajones:10d} {precio:10.2f}'.format(nombre='Naranja', cajones=100, precio=91.1)
'       Naranja        100      91.10'
>>> '{:10s} {:10d} {:10.2f}'.format('Naranja', 100, 91.1)
'       Naranja        100      91.10'
>>>
```

La verdad es que `format()` nos resulta un poco extenso y preferimos usar `f-strings`.

### Formato estilo C

También podés usar el operador  `%`.

```python
>>> 'The value is %d' % 3
'The value is 3'
>>> '%5d %-5d %10d' % (3,4,5)
'    3 4              5'
>>> '%0.2f' % (3.1415926,)
'3.14'
```

Esto requiere un solo ítem, o una tupla a la derecha. Los códigos están tambien inspirados en el `printf()` de C. Tiene la dificultad de que hay que contar posiciones y todas las variables van juntas al final.

## Ejercicios

### Ejercicio 2.29: Formato de números
Un problema usual cuando queremos imprimir números es especificar el número de dígitos decimales. Los f-strings nos permiten hacerlo. Probá los siguientes ejemplos:

```python
>>> value = 42863.1
>>> print(value)
42863.1
>>> print(f'{value:0.4f}')
42863.1000
>>> print(f'{value:>16.2f}')
        42863.10
>>> print(f'{value:<16.2f}')
42863.10
>>> print(f'{value:*>16,.2f}')
*******42,863.10
>>>
```


La documentación completa sobre los códigos de formato usados en f-strings puede consultarse [acá](https://docs.python.org/3/library/string.html#format-specification-mini-language). El formato puede aplicarse también usando el operador `%` de cadenas.

```python
>>> print('%0.4f' % value)
42863.1000
>>> print('%16.2f' % value)
        42863.10
>>>
```

La documentación sobre códigos usados con `%` puede encontrarse [acá](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting).

A pesar de que suelen usarse dentro de un `print`, el formato de cadenas no está necesariamente ligado a la impresión. Por ejemplo, podés simplemente asignarlo a una variable.

```python
>>> f = '%0.4f' % value
>>> f
'42863.1000'
>>>
```

### Ejercicio 2.30: Recolectar datos
En el [Ejercicio 2.15](../02_Datos/04_Contenedores.md#ejercicio-215-balances), escribiste un programa llamado `informe.py` que calculaba las ganancias o pérdidas de un camión que compra a productores y vende en el mercado. Dejá ese archivo para entregar al final de la clase y copiá su contenido en un archivo `tabla_informe.py`. En este ejercicio, vas a comenzar a modificarlo para producir una tabla como ésta:

```
 Nombre     Cajones     Precio     Cambio
---------- ---------- ---------- ----------
 Lima          100        32.2       8.02
 Naranja        50        91.1      15.18
 Caqui         150      103.44       2.02
 Mandarina     200       51.23      29.66
 Durazno        95       40.37      33.11
 Mandarina      50        65.1      15.79
 Naranja       100       70.44      35.84
```

En este informe, el "Precio" es el precio en el mercado y el "Cambio" es la variación respecto al precio cobrado por el productor.

Para generar un informe como el de arriba, primero tenés que recolectar todos los datos de la tabla. Escribí una función `hacer_informe()`
que recibe una lista de cajones y un diccionario con precios como input y devuelve una lista de tuplas conteniendo la información mostrada en la tabla anterior.

Agregá esta función a tu archivo `tabla_informe.py`. Debería funcionar como se muestra en el siguiente ejemplo:

```python
>>> camion = leer_camion('Data/camion.csv')
>>> precios = leer_precios('Data/precios.csv')
>>> informe = hacer_informe(camion, precios)
>>> for r in informe:
        print(r)

('Lima', 100, 32.2, 8.019999999999996)
('Naranja', 50, 91.1, 15.180000000000007)
('Caqui', 150, 103.44, 2.019999999999996)
('Mandarina', 200, 51.23, 29.660000000000004)
('Durazno', 95, 40.37, 33.11000000000001)
('Mandarina', 50, 65.1, 15.790000000000006)
('Naranja', 100, 70.44, 35.84)
...
>>>
```

### Ejercicio 2.31: Imprimir una tabla con formato
Volvé a hacer el ciclo `for` del ejercicio anterior pero cambiando la forma de imprimir como sigue:

```python
>>> for r in informe:
        print('%10s %10d %10.2f %10.2f' % r)

      Lima        100      32.20       8.02
   Naranja         50      91.10      15.18
     Caqui        150     103.44       2.02
 Mandarina        200      51.23      29.66
   Durazno         95      40.37      33.11
 Mandarina         50      65.10      15.79
   Naranja        100      70.44      35.84
...
>>>
```

O directamente usando  f-strings. Por ejemplo:

```python
>>> for nombre, cajones, precio, cambio in informe:
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f} {cambio:>10.2f}')

      Lima        100      32.20       8.02
   Naranja         50      91.10      15.18
     Caqui        150     103.44       2.02
 Mandarina        200      51.23      29.66
   Durazno         95      40.37      33.11
 Mandarina         50      65.10      15.79
   Naranja        100      70.44      35.84
...
>>>
```

Agregá estos últimos comandos a tu programa `tabla_informe.py`. Hacé que el programa tome la salida de la función `hacer_informe()` e imprima una tabla bien formateada.

### Ejercicio 2.32: Agregar encabezados
Suponete que tenés una tupla con nombres de encabezado como ésta:

```python
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
```

Agregá el código necesario a tu programa para que tome una tupla de encabezados como la de arriba y cree una cadena donde cada nombre de encabezado esté alineado a la derecha en un campo de 10 caracteres de ancho y separados por un solo espacio.

```python
'    Nombre    Cajones     Precio     Cambio'
```

Escribí el código que recibe los encabezados y crea una cadena de separación entre los encabezados y los datos que siguen. Esta cadena es simplemente una tira de caracteres "-" bajo cada nombre de campo. Por ejemplo:

```python
'---------- ---------- ---------- ----------'
```

Cuando esté listo, tu programa debería producir una tabla como esta:

```
    Nombre    Cajones     Precio     Cambio
---------- ---------- ---------- ----------
      Lima        100      32.20       8.02
   Naranja         50      91.10      15.18
     Caqui        150     103.44       2.02
 Mandarina        200      51.23      29.66
   Durazno         95      40.37      33.11
 Mandarina         50      65.10      15.79
   Naranja        100      70.44      35.84
```

### Ejercicio 2.33: Un desafío de formato
Por último, modificá tu código para que el precio mostrado incluya un símbolo de pesos ($) y la salida se vea como esta tabla:

```
    Nombre    Cajones     Precio     Cambio
---------- ---------- ---------- ----------
      Lima        100      $32.2       8.02
   Naranja         50      $91.1      15.18
     Caqui        150    $103.44       2.02
 Mandarina        200     $51.23      29.66
   Durazno         95     $40.37      33.11
 Mandarina         50      $65.1      15.79
   Naranja        100     $70.44      35.84
```

Guardá estos cambios en el archivo `tabla_informe.py` que más adelante los vas a necesitar.

### Ejercicio 2.34: Tablas de multiplicar
Escribí un programa `tablamult.py` que imprima de forma prolija las tablas de
multiplicar del 1 al 9 usando f-strings. Si podés, evitá usar la multiplicación, usando sólo sumas alcanza.

```python
       0   1   2   3   4   5   6   7   8   9
---------------------------------------------
 0:    0   0   0   0   0   0   0   0   0   0
 1:    0   1   2   3   4   5   6   7   8   9
 2:    0   2   4   6   8  10  12  14  16  18
 3:    0   3   6   9  12  15  18  21  24  27
 4:    0   4   8  12  16  20  24  28  32  36
 5:    0   5  10  15  20  25  30  35  40  45
 6:    0   6  12  18  24  30  36  42  48  54
 7:    0   7  14  21  28  35  42  49  56  63
 8:    0   8  16  24  32  40  48  56  64  72
 9:    0   9  18  27  36  45  54  63  72  81
```


[Contenidos](../Contenidos.md) \| [Anterior (7 Arbolado porteño)](07_Arboles1.md) \| [Próximo (9 Cierre de la segunda clase)](09_CierreClase.md)

