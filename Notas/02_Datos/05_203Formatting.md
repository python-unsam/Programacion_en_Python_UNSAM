[Contenidos](../Contenidos.md) \| [Anterior (4 Contenedores)](04_202Containers.md) \| [Próximo (6 Sequences)](06_204Sequences.md)

# 2.5 Formatting

This section is a slight digression, but when you work with data, you
often want to produce structured output (tables, etc.). For example:

```code
      Name      Cajons        Price
----------  ----------  -----------
        Lima         100        32.20
       Naranja          50        91.10
       Caqui         150        83.44
      Mandarina         200        51.23
        Durazno          95        40.37
      Mandarina          50        65.10
       Naranja         100        70.44
```

### String Formatting

One way to format string in Python 3.6+ is with `f-strings`.

```python
>>> name = 'Naranja'
>>> cajones = 100
>>> precio = 91.1
>>> f'{name:>10s} {cajones:>10d} {precio:>10.2f}'
'       Naranja        100      91.10'
>>>
```

The part `{expression:format}` is replaced.

It is commonly used with `print`.

```python
print(f'{name:>10s} {cajones:>10d} {precio:>10.2f}')
```

### Format codes

Format codes (after the `:` inside the `{}`) are similar to C `printf()`.  Common codes
include:

```code
d       Decimal integer
b       Binary integer
x       Hexadecimal integer
f       Float as [-]m.dddddd
e       Float as [-]m.dddddde+-xx
g       Float, but selective use of E notation
s       String
c       Character (from integer)
```

Common modifiers adjust the field width and decimal precision.  This is a partial list:

```code
:>10d   Integer right aligned in 10-character field
:<10d   Integer left aligned in 10-character field
:^10d   Integer centered in 10-character field
:0.2f   Float with 2 digit precision
```

### Dictionary Formatting

You can use the `format_map()` method to apply string formatting to a dictionary of values:

```python
>>> s = {
    'name': 'Naranja',
    'cajones': 100,
    'precio': 91.1
}
>>> '{name:>10s} {cajones:10d} {precio:10.2f}'.format_map(s)
'       Naranja        100      91.10'
>>>
```

It uses the same codes as `f-strings` but takes the values from the
supplied dictionary.

### format() method

There is a method `format()` that can apply formatting to arguments or
keyword arguments.

```python
>>> '{name:>10s} {cajones:10d} {precio:10.2f}'.format(name='Naranja', cajones=100, precio=91.1)
'       Naranja        100      91.10'
>>> '{:10s} {:10d} {:10.2f}'.format('Naranja', 100, 91.1)
'       Naranja        100      91.10'
>>>
```

Frankly, `format()` is a bit verbose. I prefer f-strings.

### C-Style Formatting

You can also use the formatting operator `%`.

```python
>>> 'The value is %d' % 3
'The value is 3'
>>> '%5d %-5d %10d' % (3,4,5)
'    3 4              5'
>>> '%0.2f' % (3.1415926,)
'3.14'
```

This requires a single item or a tuple on the right.  Format codes are
modeled after the C `printf()` as well.

*Observación: This is the only formatting available on byte strings.*

```python
>>> b'%s has %n messages' % (b'Dave', 37)
b'Dave has 37 messages'
>>>
```

## Ejercicios

### Ejercicio 2.16: How to format numbers

A common problem with printing numbers is specifying the number of
decimal places. One way to fix this is to use f-strings. Try these
examples:

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

Full documentation on the formatting codes used f-strings can be found
[here](https://docs.python.org/3/biblioteca/string.html#format-specification-mini-language). Formatting
is also sometimes performed using the `%` operator of strings.

```python
>>> print('%0.4f' % value)
42863.1000
>>> print('%16.2f' % value)
        42863.10
>>>
```

Documentation on various codes used with `%` can be found
[here](https://docs.python.org/3/biblioteca/stdtypes.html#printf-style-string-formatting).

Although it’s commonly used with `print`, string formatting is not tied to printing.
If you want to save a formatted string. Just assign it to a variable.

```python
>>> f = '%0.4f' % value
>>> f
'42863.1000'
>>>
```

### Ejercicio 2.17: Collecting Data

In Ejercicio 2.7, you wrote a program called `reporte.py` that computed the gain/loss of a
cajon camion.  In this ejercicio, you're going to start modifying it to produce a table like this:

```
      Name     Cajons      Price     Change
---------- ---------- ---------- ----------
        Lima        100       9.22     -22.98
       Naranja         50     106.28      15.18
       Caqui        150      35.46     -47.98
      Mandarina        200      20.89     -30.34
        Durazno         95      13.48     -26.89
      Mandarina         50      20.89     -44.21
       Naranja        100     106.28      35.84
```

In this report, "Price" is the current cajon precio of the cajon and
"Change" is the change in the cajon precio from the initial purchase
precio.


In order to generate the above report, you’ll first want to collect
all of the data shown in the table.  Write a function `make_report()`
that takes a list of cajones and dictionary of precios as input and
returns a list of tuples containing the rows of the above table.

Add this function to your `reporte.py` file. Here’s how it should work
if you try it interactively:

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

### Ejercicio 2.18: Printing a formatted table

Redo the for-loop in Ejercicio 2.9, but change the print statement to
format the tuples.

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

You can also expand the values and use f-strings. For example:

```python
>>> for name, cajones, precio, change in report:
        print(f'{name:>10s} {cajones:>10d} {precio:>10.2f} {change:>10.2f}')

          Lima        100       9.22     -22.98
         Naranja         50     106.28      15.18
         Caqui        150      35.46     -47.98
        Mandarina        200      20.89     -30.34
...
>>>
```

Take the above statements and add them to your `reporte.py` program.
Have your program take the output of the `make_report()` function and print a nicely formatted table as shown.

### Ejercicio 2.19: Adding some headers

Suppose you had a tuple of header names like this:

```python
headers = ('Name', 'Cajons', 'Price', 'Change')
```

Add code to your program that takes the above tuple of headers and
creates a string where each header name is right-aligned in a
10-character wide field and each field is separated by a single space.

```python
'      Name     Cajons      Price      Change'
```

Write code that takes the headers and creates the separator string between the headers and data to follow.
This string is just a bunch of "-" characters under each field name. For example:

```python
'---------- ---------- ---------- -----------'
```

When you’re done, your program should produce the table shown at the top of this ejercicio.

```
      Name     Cajons      Price     Change
---------- ---------- ---------- ----------
        Lima        100       9.22     -22.98
       Naranja         50     106.28      15.18
       Caqui        150      35.46     -47.98
      Mandarina        200      20.89     -30.34
        Durazno         95      13.48     -26.89
      Mandarina         50      20.89     -44.21
       Naranja        100     106.28      35.84
```

### Ejercicio 2.20: Formatting Challenge

How would you modify your code so that the precio includes the currency symbol ($) and the output looks like this:

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

[Contenidos](../Contenidos.md) \| [Anterior (4 Contenedores)](04_202Containers.md) \| [Próximo (6 Sequences)](06_204Sequences.md)

