[Contenidos](../Contenidos.md) \| [Anterior (4 Random+)](04_Random.md) \| [Próximo (6 Numpy básico**)](07_NumPy_Arrays.md)

# 3.5 Errores+

###  Ejercicio: tres tipos de errores

Errores sintácticos, semánticos y *en tiempo de ejecución*.


Determine los errores de los siguientes códigos y corríjalos. ¿Qué tipo de errores tiene cada uno?

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



[Contenidos](../Contenidos.md) \| [Anterior (4 Random+)](04_Random.md) \| [Próximo (6 Numpy básico**)](07_NumPy_Arrays.md)

