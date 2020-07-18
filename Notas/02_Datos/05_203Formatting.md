[Contenidos](../Contenidos.md) \| [Anterior (4 Contenedores)](04_202Containers.md) \| [Próximo (6 Secuencias)](06_204Sequences.md)

# 2.5 Impresión con formato

Esta sección es una pequeña disgresión. Cuando trabajás con datos es usual que quieras imprimir salidas estructuradas (tablas, etc.). Por ejemplo:

```code
  Nombre      Cajones     Precio
----------  ----------  -----------
 Lima           100        32.20
 Naranja         50        91.10
 Caqui          150        83.44
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

La parte `{expresion:formato}` va a ser reemplazada.

Usualmente los `f-strings` se usan con `print`.

```python
print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f}')
```

### Códigos de formato

Lo códigos de formato (lo que va luego de `:` dentro de `{}`) son similares s los que se usan en el `printf()` del lenguaje C. Los más comunes son:

```code
d       Entero decimal
b       Entero binario
x       Entero hexadecimal
f       Floatante como [-]m.dddddd
e       Floatante como [-]m.dddddde+-xx
g       Floatante, pero con uso selectivo de la notaciṕn exponencial E.
s       Cadenas
c       Caracter (a partir de un entero, su código)
```

Los modificadores permiten ajustar el ancho a imprimir o la precisión decimal (cantidad de dígitos luego del punto). Esta es una lista parcial:

```code
:>10d   Entero alineado a la derecha en un campo de 10 caracteres
:<10d   Entero alineado a la inquierda en un campo de 10 caracteres
:^10d   Entero centrado  en un campo de 10 caracteres
:0.2f   Flotante con dos dígitos de precisión
```

### Formato a diccionarios

Pores usar el métido `format_map()` para aplicarle un formato a los valores de un diccionario:

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

Usa los mismos códigos que los `f-strings` pero toma los valores que provée el diccionario.

### El método format()

Existe un método  `format()` que permite aplicar formato a argumentos.

```python
>>> '{name:>10s} {cajones:10d} {precio:10.2f}'.format(name='Naranja', cajones=100, precio=91.1)
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

Esto requiere un solo item, o una tupla a la derecha. Los códigos están tambien inspirados en el `printf()` de C. Tiene la dificultad que hay que contar posiciones y todas las variables van juntas al final.

## Ejercicios

### Ejercicio 2.16: Formato de números
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


La documentación completa sobre los códigos de formato usados en f-strings puede consultarse [aquí](https://docs.python.org/3/library/string.html#format-specification-mini-language). El formato puede aplicarse también usando el operador `%` de cadenas.

```python
>>> print('%0.4f' % value)
42863.1000
>>> print('%16.2f' % value)
        42863.10
>>>
```

La documentación sobre códigos usados con `%` puede encontrarse [ be found
[aquí](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting).

A pesar de que suelen usarse dentre de un `print`, el formato de cadenas no está necesariamente ligao a la impresión. Por ejemplo, podés simplemente asignarlo a una variable.

```python
>>> f = '%0.4f' % value
>>> f
'42863.1000'
>>>
```

### Ejercicio 2.17: Recolectar datos
En el [Ejercicio 2.15](../02_Datos/04_202Containers.md#ejercicio-215-balances), escribiste un programa llamado `reporte.py` que calculaba las ganancias o pérdidas de un camión que compra a productores y venden en el mercado. En este ejercicio, vas a comenzas a modificarlo para producir una tabla como esta:

```
 Nombre     Cajones     Precio     Cambio
---------- ---------- ---------- ----------
 Lima          100        9.22     -22.98
 Naranja        50      106.28      15.18
 Caqui         150       35.46     -47.98
 Mandarina     200       20.89     -30.34
 Durazno        95       13.48     -26.89
 Mandarina      50       20.89     -44.21
 Naranja       100      106.28      35.84
```

En este reporte, el "Precio" es el precio en el mercado y el "Cambio" es la variación respecto al precio cobrado por el productor.

Para generar un reporte como el de arriba, primero tenés que recolectar todos los datos de la tabla. Escribí una función `hacer_reporte()`
que recibe una lista de cajones y un diccionario con precios como input y devuelve una lista de tuplas conteniendo la información mostrada en la tabla anterior.

Agregá esta función a tu archivo `reporte.py`. Debería funcionar como se muestra en el siguiente ejemplo:

```python
>>> camion = leer_camion('Data/camion.csv')
>>> precios = read_precios('Data/precios.csv')
>>> report = make_report(camion, precios)
>>> for r in report:
        print(r)

('Lima', 100, 9.22, -22.980000000000004)
('Naranja', 50, 106.28, 15.180000000000007)
('Caqui', 150, 35.46, -47.98)
('Mandarina', 200, 20.89, -30.339999999999996)
('Durazno', 95, 13.48, -26.889999999999997)
...
>>>
```

### Ejercicio 2.18: Imprimir una tabla con formato
Volvé a hacer el del ciclo `for` del ejercicio anterior pero cambiando la forma de imprimir como sigue:

```python
>>> for r in report:
        print('%10s %10d %10.2f %10.2f' % r)

          Lima        100       9.22     -22.98
         Naranja         50     106.28      15.18
         Caqui        150      35.46     -47.98
        Mandarina        200      20.89     -30.34
...
>>>
```

O directamente usando  f-strings. Por ejemplo:

```python
>>> for nombre, cajones, precio, cambio in reporte:
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f} {change:>10.2f}')

      Lima        100       9.22     -22.98
   Naranja         50     106.28      15.18
     Caqui        150      35.46     -47.98
 Mandarina        200      20.89     -30.34
...
>>>
```

Agregá estos últimos comando a tu programa `reporte.py`. Hacé que el programa tome la salida de la función `hacer_reporte()` e imprima una tabla bien formateada.

### Ejercicio 2.19: Agregar encabezados
Suponete que tenés una tupla con nombres de encabezado como esta:

```python
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
```

Agregá el código necesario a tu programa para que tome una tupla de encabezados como la de arriba y crée una cadena donde cada nombre de encabezado esté alineado a la derecha en un campo de 10 caracteres de ancho y separados por un solo espacio.

```python
'    Nombre    Cajones     Precio     Cambio'
```

Escribí el código que recibe los encabezados y crea una cadena de separación entre los encabezados y los datos que siguen. Esta cadena es simplemente una tira de caracteres "-" bajo cada nombre de campo. Por ejemplo:

```python
'---------- ---------- ---------- -----------'
```

Cuando esté listo, tu programa debería producir una tabla como esta:

```
    Nombre    Cajones     Precio     Cambio
---------- ---------- ---------- ----------
      Lima        100       9.22     -22.98
   Naranja         50     106.28      15.18
     Caqui        150      35.46     -47.98
 Mandarina        200      20.89     -30.34
   Durazno         95      13.48     -26.89
 Mandarina         50      20.89     -44.21
   Naranja        100     106.28      35.84
```

### Ejercicio 2.20: Un desafío de formato
Por último, modificá tu código para que el precio mostrado incluya un símbolo de pesos ($) y la salida se vea como esta tabla:

```
      Name     Cajons      Price     Change
---------- ---------- ---------- ----------
      Lima        100      $9.22     -22.98
   Naranja         50    $106.28      15.18
     Caqui        150     $35.46     -47.98
 Mandarina        200     $20.89     -30.34
   Durazno         95     $13.48     -26.89
 Mandarina         50     $20.89     -44.21
   Naranja        100    $106.28      35.84
```

Guardá estos cambios en el archivo `reporte.py` que más adelante los vas a necesitar.

[Contenidos](../Contenidos.md) \| [Anterior (4 Contenedores)](04_202Containers.md) \| [Próximo (6 Secuencias)](06_204Sequences.md)

