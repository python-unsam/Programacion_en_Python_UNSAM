[Contenidos](../Contenidos.md) \| [Anterior (1 Manejo de fechas y horas)](01_Fechas.md) \| [Próximo (3 Ordenar archivos en Python)](03_Ordenando_archivos.md)

# 7.2 Manejo de archivos y carpetas

## Manejo de archivos y directorios

Una carpeta o directorio es una colección de archivos y directorios. Python tiene el módulo `os` que ofrece muchas herramientas útiles para trabajar con directorios y archivos.

En esta sección vas a aprender cómo crear un directorio, renombrarlo, listar todos sus archivos y subdirectorios, etc.


### Obtener el directorio actual

Para obtener el directorio de trabajo actual, usamos el función `getcwd()` (_get current working directory_) del módulo `os`.

Esta función te devuelve el directorio actual en forma de cadena.

```python
>>> import os
>>> os.getcwd()
'/home/usuario/ejercicios_python'

```

Es importante ver que la salida dependerá del sistema operativo que estés usando. Por ejemplo, en Windows podrías obtener algo así: `C:\\usuario\\ejercicios_python`.



### Cambiar el directorio de trabajo

Podés cambiar de directorio usando la función `chdir()` (_change directory_). Los directorios pueden ser relativos o absolutos (en sistemas operativos basados en Unix '.' es el directorio actual, '..' es el anterior, '/' es el directorio raíz).

```python
>>> os.chdir('./Data')              # entro en Data, subdirectorio del actual
>>> print(os.getcwd())
/home/usuario/ejercicios_python/Data
>>> os.chdir('..')                  # subo un nivel
>>> os.chdir('..')                  # subo otro nivel
>>> print(os.getcwd())
/home/usuario/
>>> os.chdir('/home')
>>> print(os.getcwd())
/home
```

Para cambiar de directorio, le pasás el nuevo directorio como cadena a esta función.

En diferentes sistemas operativos las barras de directorio se escriben de diferentes maneras. Es recomendable usar el comando `os.path.join` como en el siguiente ejemplo de manera que tu código funcione independientemente del sistema operativo en el que se lo corra.

```python
>>> directorio = os.path.join('/home', 'usuario', 'ejercicios_python')
>>> os.chdir(directorio)
```
En caso de usarlo en Windows, será similar a:
```python
>>> directorio = os.path.join('c:\\', 'usuario', 'ejercicios_python')
>>> os.chdir(directorio)
```

Usar directorios relativos al actual (que comienzan con './') y no absolutos (que comienzan con '/') facilita la portabilidad del código de una compu a otra.

## Listar directorios y archivos

La función `listdir()` toma un directorio (_path_ o camino) y devuelve una lista con todos los archivos y subdirectorios de un directorio. Si no se le pasa ningún parámetro, devuelve los del directorio de trabajo actual.

```python
>>> os.getcwd()
'/home/usuario/ejercicios_python'
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
 'arbolado-en-espacios-verdes.csv']
```

## Crear un nuevo directorio

Podés crear un directorio con la función `mkdir()`.

Esta función toma como argumento el path del nuevo directorio. Si no se especifica el path absoluto, el directorio nuevo se crea en el directorio de trabajo actual.

```python

>>> os.mkdir('test')          # creo el directorio test
>>> os.mkdir(os.path.join('test', 'carpeta'))  # creo el subdirectorio carpeta dentro de test
>>> os.listdir('test')
['carpeta']
```

## Renombrar un directorio o un archivo

Para renombrar un directorio o archivo, la función `rename()` toma dos argumentos, el viejo nombre y el nuevo nombre.

```python
>>> os.chdir('test')                     # entro en el directorio test
>>> os.listdir()
['carpeta']
>>> os.rename('carpeta','carpeta_nueva') # cambio el nombre de carpeta
>>> os.listdir()
['carpeta_nueva']
```

Esto mismo se puede hacer trabajando desde el directorio `Ejercicios`, sin entrar en 'test', marcando el camino hacia la carpeta que queremos renombrar.

```python
>>> os.chdir('..')                          # subo un nivel
>>> os.listdir('test')                      # miro qué hay en test
['carpeta_nueva']
>>> os.rename(os.path.join('test', 'carpeta_nueva'), os.path.join('test','carpeta_vieja'))
>>> os.listdir('test')
['carpeta_vieja']
```

La función `rename()` también es útil para mover un archivo o directorio, cambiando el camino (_path_) de acceso al archivo. Probá hacer esto:

```python
>>> os.rename(os.path.join('test','carpeta_vieja'), 'carpeta_vieja') # cambio el path
>>> os.listdir('test')                                  # test quedó vacío
[]
```

La carpeta 'carpeta' ahora se encuentra en 'Ejercicios', y no dentro de 'Ejercicios/test'.

**Ojo**: `rename()` funciona cuando el archivo (o directorio) no se cambia de disco (o más específicamente de una partición). Si querés mover un archivo del disco a un pendrive, por ejemplo, lo correcto es copiar el archivo al pendrive y luego borrarlo del disco. `rename()` no hace esto: no copia y borra, simplemente cambia el nombre. Para renombrar en caso que se pueda o copiar y borrar si lo primero no es posible, podés usar la función `move()` del módulo `shutil`. Este módulo es de más alto nivel y usa las primitivas de bajo nivel del módulo `os`. Al usar `os` tenemos un control más estricto de las operaciones. Las funciones de `shutil` pueden resultar más cómodas, pero en el camino pueden invocar a diversas funciones de bajo nivel del módulo `os`.


## Eliminar un directorio o un archivo

> :warning: **A continuación usaremos comandos que borran archivos sin pasar por ninguna papelera de reciclaje. Estas acciones no pueden deshacerse**: Usar con precaución, _un gran poder conlleva una gran responsabilidad_.


Podés eliminar un archivo usando la función `remove()`. También podés eliminar un directorio vacío usando `rmdir()`.

En el siguiente código trabajaremos en una carpeta que tiene esta estructura:
```
otra_carpeta
├── archivo.txt
└── subcarpeta
```

```python
>>> os.chdir('otra_carpeta')    # entro otra carpeta que tiene
                                # una subcarpeta y un archivo de texto
>>> os.listdir()
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
>>> os.mkdir(os.path.join('test','carpeta'))                # creo nuevamente una carpeta
                                                            # dentro de test
>>> os.mkdir(os.path.join('test','carpeta', 'subcarpeta'))  # creo una subcarpeta en carpeta
>>> os.chdir('test')                                        # entro en test
>>> os.rmdir('carpeta')                                     # quiero eliminar carpeta
Traceback (most recent call last):

  File "<ipython-input-277-c4255042d84c>", line 1, in <module>
    os.rmdir('carpeta')

OSError: [Errno 39] Directory not empty: 'carpeta'

>>> import shutil

>>> shutil.rmtree('carpeta')
>>> os.listdir()
[]
```

## Recorriendo directorios con `os.walk()`

La función `walk()` del módulo `os` genera una lista con los nombres de todos los archivos del árbol de subdirectorios de un directorio dado. Es decir, lista los archivos de un directorio dado y luego entra en cada subdirectorio y hace lo mismo, recursivamente (_top-down_).

La función `walk()` recibe como único parámetro obligatorio el directorio donde comenzar a mirar (la raíz del árbol).

### Ejemplo

En este ejemplo se ve cómo se usa `os.walk()`.

```python
import os
for root, dirs, files in os.walk("."):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))
```


## Cambiar atributos de un archivo

Dependiendo del sistema operativo, un archivo puede tener asociadas diferentes fechas (de creación original, de modificación del contenido, de cambio en sus metadatos, de acceso para lectura).

Vamos a cambiar la fecha de modificación de un archivo. Para ello necesitás importar `os` y `datetime`. Después, converís la fecha elegida a `timestamp` y se la asocías al archivo con `utime`, como se muestra acá abajo:

```python
import os
import datetime
import time

camino = './rebotes.py'

stats_archivo = os.stat(camino)
print(time.ctime(stats_archivo.st_atime))

fecha_acceso = datetime.datetime(year = 2017, month = 9, day = 21, hour = 19, minute =51, second = 0)
fecha_modifi = datetime.datetime(year = 2012, month = 9, day = 24, hour = 12, minute =9, second = 24)

ts_acceso = fecha_acceso.timestamp()
ts_modifi = fecha_modifi.timestamp()
os.utime(camino, (ts_acceso, ts_modifi))

stats_archivo = os.stat(camino)
print(time.ctime(stats_archivo.st_atime))
```

Si mirás la información del archivo `./rebotes.py` desde tu gestor de archivos deberías ver las modificaciones.


[Contenidos](../Contenidos.md) \| [Anterior (1 Manejo de fechas y horas)](01_Fechas.md) \| [Próximo (3 Ordenar archivos en Python)](03_Ordenando_archivos.md)

