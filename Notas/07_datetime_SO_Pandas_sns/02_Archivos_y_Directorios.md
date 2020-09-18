[Contenidos](../Contenidos.md) \| [Anterior (1 Manejo de fechas y horas)](01_Fechas.md) \| [Próximo (3 Ordenar archivosen Python**)](03_Ordenando_archivos.md)

# 7.2 Manejo de archivos y carpetas

## Manejo de archivos y directorios

Una carpeta o directorio es una colección de archivos y subdirectorios. Python tiene el módulo `os` que provee muchos métodos útiles para trabajar con directorios y archivos.
En esta sección vas a aprender a manejar archivos y directorios con Python, es decir, cómo crear un directorio, renombrarlo, listar todos los subdirectorios, trabajar con ellos.


### Obtener el directorio actual

Para obtener el directorio de trabajo actual, usamos el método `getcwd()` (_get current working directory_) del módulo `os`.

Este método te devuelve el directorio actual en forma de cadena.

```python
>>> import os
>>> os.getcwd()
'/home/usuario/ejercicios_python'

```

### Cambiar de directorio de trabajo

Podés cambiar de directorio usando el método `chdir()` (_change directory_). Los directorios pueden ser relativos o absolutos ('.' es el directorio actual, '..' es el anterior, '/' es el directorio raíz).

```python
>>> os.chdir('./Data')
>>> print(os.getcwd())
/home/usuario/ejercicios_python/Data
>>> os.chdir('..')
>>> os.chdir('..')
>>> print(os.getcwd())
/home/usuario/
>>> os.chdir('/home')
>>> print(os.getcwd())
/home
```

El nuevo path al que quiera cambiar se le pasa como una cadena a este método. 

En diferentes sistemas operativos las barras de directorio se escriben de diferentes maneras. Es recomendable usar el comando `os.path.join` como en el siguiente ejemplo de manera que tu código funcione correctamente en diferentes computadoras.

```python
>>> directorio = os.path.join('/home','usuario','ejercicios_python')
>>> os.chdir(directorio)
```

## Listar directorios y archivos

El método `listdir()` toma un _path_ (camino) y devuelve una lista con todos los archivos y subdirectorios de un directorio. Si no se le pasa ningún path, devuelve los del directorio de trabajo actual.

```python
>>> os.listdir('Data')

['camion2.csv',
 'missing.csv',
 'precios.csv',
 'camion.csv',
 'camion.dat',
 'temperaturas.npy',
 'camion_blancos.csv',
 'camion.csv.gz',
 'dowstocks.csv',
 'fecha_camion.csv',
 'arbolado-en-espacios-verdes.csv',
 'stocksim.py']
```

## Crear un nuevo directorio

Podés crear un directorio con el método `mkdir()`.

Este método toma como argumento el path del nuevo directorio. Si no se especifica el path absoluto, el directorio nuevo se crea en el directorio de trabajo actual.

```python

>>> os.mkdir('test')          # creo el directorio test
>>> os.mkdir('test/carpeta')  # creo el subdirectorio carpeta dentro de test
>>> os.listdir('test')
['carpeta']

```

## Renombrar un directorio o un archivo

Para renombrar un directorio o archivo, el método `rename()` toma dos argumentos, el viejo nombre y el nuevo nombre.

```python
>>> os.chdir('test')                     # entro en el directorio test
>>> os.listdir()
['carpeta']
>>> os.rename('carpeta','carpeta_nueva') # cambio el nombre de carpeta
>>> os.listdir()
['carpeta_nueva']

```


## Eliminar un directorio o un archivo

Podés eliminar un archivo usando el método `remove()`. También podés eliminar un directorio vacío usando `rmdir()`.

```python
>>> os.listdir('otra_carpeta')  # entro en otra carpeta que tiene 
                                # una subcarpeta y un archivo de texto
['subcarpeta', 'archivo.txt']

>>> os.remove('archivo.txt')    # elimino el archivo
>>> os.listdir()
['subcarpeta']

>>> os.rmdir('subcarpeta')      # elimino la subcarpeta
>>> os.listdir()
[]
```

**Ojo**: `rmdir()` solamente puede borrar directorios si están vacíos.

Para eliminar un directorio no vacío, podés usar `rmtree()` del módulo `shutil`.

```python
>>> os.mkdir('test/carpeta')                # creo nuevamente una carpeta
                                            # dentro de test
>>> os.mkdir('test/carpeta/subcarpeta')     # creo una subcarpeta en carpeta
>>> os.chdir('test')                        # entro en test
>>> os.rmdir('carpeta')                     # quiero eliminar carpeta
Traceback (most recent call last):

  File "<ipython-input-277-c4255042d84c>", line 1, in <module>
    os.rmdir('carpeta')

OSError: [Errno 39] Directory not empty: 'carpeta'

>>> import shutil

>>> shutil.rmtree('carpeta')
>>> os.listdir()
[]
```

## Recorriendo directorios

`os.walk()`

**Descripción**

El método `walk()` genera los nombres de todos los archivos del árbol de subdirectorios de un directorio dado. Es decir, lista los archivos de un directorio dado y luego entra en cada subdirectorio y hace lo mismo, recursivamente (_top-down_) o al revés, desde las hojas del árbol de direcotorios hasta la raiz (_bottom-up_).


**Following is the syntax for walk() method −**

```
os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
Parameters
top − Each directory rooted at directory, yields 3-tuples, i.e., (dirpath, dirnames, filenames)
```

`topdown` toma el valor True salvo que se especifique lo contrario. 

`onerror` − This can show error to continue with the walk, or raise the exception to abort the walk.

`followlinks` − This visits directories pointed to by symlinks, if set to true.

`Return Value`
This method returns value.

### Ejemplo

En este ejemplo se ve cómo se usa `os.walk()`.

```python
import os
for root, dirs, files in os.walk(".", topdown = False):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))
```


## Determinar el momento de última modificación

El momento de modificación muestra cuándo un archivo fue modificado por última vez. A veces se confunde con el momento de creación del archivo, pero en realidad son muy diferentes. El momento de creación normalmente se guarda en el sistema operativo, cuando se crea el archivo. Si te bajás un archivo de internet, el momento de creación va a figurar como el momento en que lo descargaste. Puede no ser muy útil. En cambio el momento de modificación se guarda _en el archivo_.

******************************
File modification times show when a file was last edited. This can sometimes be confused with creation time but these are very different. Creation time is normally held by the operating system and states when a file was created. This means if you download a file from the internet, the creation time will change and be the time it was downloaded. Thus the creation time isn't very helpful.

File modification time is different however as it is stored in the file. Even though the operating system still manages these, they can still be easily changed as opposed to creation time.

The modification date can be found by right-clicking on a file and selecting properties.
***---------------------------------------

Para editar el momento de modificación de un archivo necesitás importar os, time y datetime. Después, definís la fecha elegida, y llamás a `utime` como se muestra acá:

```python 
import os 
import time
import datetime
path = 'test/carpeta'
date = datetime.datetime(year = 2020, month = 9, day = 24, hour = 19, minute =50, second = 0)
mod_time = time.mktime(date.timetuple())
os.utime(path, (mod_time, mod_time))
```

Si mirás la información de la carpeta `carpeta` dentro de `test`, debe haber cambiado el momento de modificación.

__________________________________
```python
import os
import time
import datetime

fileLocation = r""
year = 2017
month = 11
day = 5
hour = 19
minute = 50
second = 0

date = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
modTime = time.mktime(date.timetuple())

os.utime(fileLocation, (modTime, modTime))
```

__________________________________

[Contenidos](../Contenidos.md) \| [Anterior (1 Manejo de fechas y horas)](01_Fechas.md) \| [Próximo (3 Ordenar archivosen Python**)](03_Ordenando_archivos.md)

