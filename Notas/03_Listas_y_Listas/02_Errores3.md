[Contenidos](../Contenidos.md) \| [Anterior (1 Entorno de desarrollo integrado)](01_IDE.md) \| [Próximo (3 Listas y búsqueda lineal)](03_IteradoresLista.md)

# 3.2 Errores

## Tres tipos de errores:

Programando nos podemos encontrar con tres tipos de errores.

Los *errores sintácticos* son los que se dan cuando escribimos incorrectamente. Por ejemplo si queremos escribir `x = (a + b) * c` pero en vez de eso escribimos `x = (a + b] * c`, el programa no va a correr.

Un segundo tipo de error lo forman los errores *en tiempo de ejecución*, que se dan cuando el programa empieza a ejecutarse pero se produce un error durante su ejecución. Por ejemplo si le pedimos al usuarie que ingrese su edad esperando un número entero e ingresa "veintiséis años", es probable que el programa dé un error. Si leemos un archivo CSV y una fila tiene datos faltantes, el programa puede dar un error. Este tipo de errores pueden administrarse adecuadamente, como veremos más adelante.

El tercer tipo de error es el más difícil de encontrar y de entender. Son los *errores semánticos*, que se dan cuando el programa no hace lo que está diseñado para hacer. Tienen que ver con el sentido de las instrucciones. En estos casos el programa se ejecuta pero da un resultado incorrecto o inesperado. En general, la mejor forma de encontrar estos errores es correr paso a paso el código que genera un resultado inesperado, tratando de entender dónde está la falla.

### Ejercicio 3.1: tres tipos de errores
Determiná los errores de los siguientes códigos y corregilos en un archivo `tres_errores.py` comentando brevemente los errores. ¿Qué tipo de errores tiene cada uno?

¿Anda bien en todos los casos de testeo?
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
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')
```

¿Anda bien en todos los casos de testeo?
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

¿Anda bien en todos los casos de testeo?
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

La siguiente suma no da lo que debería:
```python
def suma(a,b):
    c = a + b
    
c = 0
a = 2
b = 3
suma(a,b)
print(f"La suma da {a} + {b} = {c}")
```

El siguiente ejemplo usa el dataset de la clase anterior, pero no lo imprime como corresponde, ¿podés determinar por qué y explicarlo brevemente en la versión corregida?
```python
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion("Data/camion.csv")
pprint(camion)
```

_Ayuda: Primero tratá de pensarlo, pero si este último se te hace muy difícil, podés mirar un poco de la teoría relacionada con esto [un par de secciones más adelante](https://github.com/python-unsam/UNSAM_2020c2_Python/blob/master/Notas/03_Mas_Python/05_Objetos.md#ejemplo-de-asignaci%C3%B3n)._



En el archivo `tres_errores.py` separá las correcciones de los distintos códigos con una línea que contenga solamente los símbolos `#%%` seguido de una o varias líneas comentadas indicando el ejercicio y el problema que tenía. Al terminar, debería verse así tu archivo:

```python
#tres_errores.py
#Ejercicios de errores en el código
#%%
#Función tiene_a(), primera versión
#Comentario: El error era de TAL tipo y estaba ubicado en TAL lugar.
#    Lo corregí cambiando esto por aquello.
#    A continuación va el código corregido
...
...

#%%
#Función tiene_a(), segunda versión
#Comentario: El error era de TAL tipo y estaba ubicado en TAL lugar.
...
...

#%%
#Función tiene_uno()
#Comentario: El error era de TAL tipo y estaba ubicado en TAL lugar.
...
...
...
```

[Contenidos](../Contenidos.md) \| [Anterior (1 Entorno de desarrollo integrado)](01_IDE.md) \| [Próximo (3 Listas y búsqueda lineal)](03_IteradoresLista.md)

