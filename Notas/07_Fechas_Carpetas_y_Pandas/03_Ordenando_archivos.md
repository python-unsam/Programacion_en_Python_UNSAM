[Contenidos](../Contenidos.md) \| [Anterior (2 Manejo de archivos y carpetas)](02_Archivos_y_Directorios.md) \| [Próximo (4 Introducción a Pandas)](04_Pandas.md)

# 7.3 Ordenar archivos en Python

En esta sección vamos a integrar las últimas dos secciones con lo que veníamos viendo antes del parcial. La idea es que descomprimas [este archivo](./ordenar.zip) en tu carpeta `Data/` y escribas un script que trabaje con estos archivos.

Esta sección tiene un ejercicio para entregar y luego otro más complejo que es optativo.

### Ejercicio 7.5: Recorrer el árbol de archivos
Escribí un programa que dado un directorio, imprima en pantalla los nombres de todos los archivos `.png` que se encuentren en *algún* subdirectorio del él.

_Observación:_ Al final, tu script debería poder ejecutarse desde la línea de comandos recibiendo como parámetro el directorio a leer original. En la [Sección 6.2](../06_Plt_Especificacion_y_Documentacion/02_Modulo_principal.md#modelo-de-script-con-parámetros) dimos un modelo de script que te puede servir.

Guardá el script resultante en un archivo `listar_imgs.py`. 

### Ejercicio 7.6: Ordenar el árbol de archivos (optativo)
Escribí un programa que te permita ordenar las imágenes PNG de esta carpeta. Guardalo en un archivo `ordenar_imgs.py`.

1. Creá un nuevo directorio `Data/imgs_procesadas/`.
2. Usá `os.walk()` para recorrer los archivos en la carpeta `Data/ordenar/` (y sus subcarpetas).
3. Cuando encuentres archivos con extensión `png` los vas a *procesar*. En este caso *procesar* significa:
    * Leer la fecha que se encuentra codificada en los últimos 8 caracteres de su nombre en el formato AAAAMMDD (año en 4 dígitos, mes en 2 y día en 2).
    * Usar la fecha obtenida para setear la fecha de última modificación (y de último acceso si no usás Windows).
    * Cambiarle el nombre al archivo para que no tenga más esos dígitos (ni el guión bajo).
    * Mover el archivo a la carpeta  `Data/imgs_procesadas/`.
4. Los archivos que no son `png` no los modifiques.
5. Borrá todas las subcarpetas de `Data/ordenar/` que hayan quedado vacías.

_Observación:_ Al final, tu script debería poder ejecutarse desde la línea de comandos recibiendo como parámetro el directorio a leer original y un directorio destino (que debería ser creado si no existe).

_Observación:_ Este tipo de tareas se repite con mucha frecuencia. Tener la capacidad de automatizarlas mediante un script de Python te puede ahorrar muchísimo tiempo.


**Algunos puntos importantes:**

  * Te recomendamos que modularices el procesamiento de los archivos `png`. Podés, por ejemplo, escribir una función que manipule strings (que tome el nombre de un archivo y devuelva la fecha y el nombre corregido) y otra función que precese cada archivo (que use la función anterior para renombrar, mover y modificar la fecha de cada archivo). La modularización del código es clave para que otras personas lo puedan entender y que sea sencillo de mantener.
  * Usá docstrings y comentarios en tu código de manera que sea legible.


[Contenidos](../Contenidos.md) \| [Anterior (2 Manejo de archivos y carpetas)](02_Archivos_y_Directorios.md) \| [Próximo (4 Introducción a Pandas)](04_Pandas.md)

