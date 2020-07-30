[Contenidos](../Contenidos.md) \| [Anterior (4 Random+)](04_Random.md) \| [Próximo (6 NumPy: the absolute basics for beginners)](07_NumPy_Arrays.md)

# 3.5 Errores

Podemos decir que hay diferentes tipos de errores. Si escribimos mal una ecuación, un comando, un nombre, se trata de un *error sintáctico*. Por ejemplo si queremos poner `x = (a + b) * c` pero ponemos `x = (a + b] * c` el programa no va a correr. Un segundo tipo de error lo forman los errores en tiempo de ejcución. Por ejemplo si le pedimos al usuario que ingrese su edad esperando un número entero e ingresa "veintiseis años" es probable que el programa de un error. O si leemos un archivo CSV y una fila tiene datos faltantes, el programa puede dar un error. Este tipo de errores pueden administrarse adecuadamente, como veremos más adelante. El tercer tipo de error es el más dificil de encontrar y de entender. Son los errores semánticos. Tienen que ver con el sentido. El programa muy probablemente corra pero de un resultado incorrecto o inesperado. En general, la mejor forma de encontrar estos errores es correr paso a paso el código que genera un resultado inesperado tratando de entender dónde está la falla.

###  Ejercicio: tres tipos de errores

Determiná los errores de los siguientes códigos y correjilos. ¿Qué tipo de errores tiene cada uno?

```python
def tiene_a(palabra):
    n = len(palabra)
    i = 0
    while i<n:
        if palabra[i] == 'a':
            return True
        else:
            return False
        i += 1
```

```python
def tiene_a(palabra)
    n = len(palabra)
    i = 0
    while i<n
        if palabra[i] = 'a'
            return True
        i += 1
    return Falso
```

```python
def tiene_uno(palabra):
    n = len(palabra)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if palabra[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)
```



[Contenidos](../Contenidos.md) \| [Anterior (4 Random+)](04_Random.md) \| [Próximo (6 NumPy: the absolute basics for beginners)](07_NumPy_Arrays.md)

