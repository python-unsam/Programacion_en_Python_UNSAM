[Contenidos](../Contenidos.md) \| [Próximo (2 Comprensión de listas)](02_List_comprehension.md)

# 3.1 Errores

Programando nos podemos encontrar con tres tipos de errores.

Los *errores sintácticos* son los que se dan cuando escribimos incorrectamente. Por ejemplo si queremos escribir `x = (a + b) * c` pero en vez escribimos `x = (a + b] * c`, el programa no va a correr.

Un segundo tipo de error lo forman los errores *en tiempo de ejecución*, que se dan cuando el programa empieza a ejecutarse pero se produce un error durante su ejecución. Por ejemplo si le pedimos al usuarie que ingrese su edad esperando un número entero e ingresa "veintiséis años", es probable que el programa dé un error. Si leemos un archivo CSV y una fila tiene datos faltantes, el programa puede dar un error. Este tipo de errores pueden administrarse adecuadamente, como veremos más adelante.

El tercer tipo de error es el más difícil de encontrar y de entender. Son los *errores semánticos*, que se dan cuando el programa no hace lo que está diseñado para hacer. Tienen que ver con el sentido de las instrucciones. En estos casos el programa se ejecuta pero da un resultado incorrecto o inesperado. En general, la mejor forma de encontrar estos errores es correr paso a paso el código que genera un resultado inesperado, tratando de entender dónde está la falla.

### Ejercicio 3.1: tres tipos de errores
Determiná los errores de los siguientes códigos y corregilos en un archivo `tres_errores.py`. ¿Qué tipo de errores tiene cada uno?

```python
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            return False
        i += 1

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')
```

```python
def tiene_a(expresion)
    n = len(expresion)
    i = 0
    while i<n
        if expresion[i] = 'a'
            return True
        i += 1
    return Falso

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')
```

```python
def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)
```



[Contenidos](../Contenidos.md) \| [Próximo (2 Comprensión de listas)](02_List_comprehension.md)

