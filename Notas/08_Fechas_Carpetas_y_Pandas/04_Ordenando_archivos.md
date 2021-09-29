# 8.4 Ordenar archivos en Python

En esta sección vamos a integrar las últimas dos secciones con lo que veníamos viendo antes del parcial. La idea es que descomprimas [este archivo](./ordenar.zip) en tu carpeta `../Data` y escribas un script que trabaje con estos archivos.

Esta sección tiene un ejercicio para entregar y luego otro más complejo que es optativo.

### Ejercicio 8.5: Recorrer el árbol de archivos
Definí una función llamada `archivos_png(directorio)` que arme una lista de todos los archivos .png que se encuentren en algún subdirectorio directorio dado.

Probá tu función con distintos directorios. Por ejemplo

```python
>>> archivos_png('../Data/ordenar')
['good_code_20190621.png',
 'git_20190503.png',
 'correlation_20200924.png',
 'duty_calls_20180321.png',
 'pregnant_20200102.png',
 'ppx_20180917.png',
 'twitter_bot_20181225.png',
 'standards_20190421.png',
 'unicode_20200718.png',
 'sandwich_20201002.png',
 'python_20190812.png']
```

Escribí un programa que dado un directorio, imprima en pantalla los nombres de todos los archivos `.png` que se encuentren en *algún* subdirectorio del él. Tu programa debe poder ejecutarse desde la línea de comandos recibiendo como parámetro el directorio a leer original. Para esto, organizá tu código como lo indicamos en la [Sección 7.3](../07_Plt_Especificacion_y_Documentacion/03_Modulo_principal.md#modelo-de-script-con-parámetros). Primero los imports, luego las funciones (en este caso solamente la función `archivos_png()`), y luego el bloque con las instrucciones para el caso `__name__ == '__main__'`.

Guardá el script resultante en un archivo `listar_imgs.py`. 

Probá el programa desde la terminal, pasándole distintos directorios como parámetro.


### Ejercicio 8.6: Ordenar el árbol de archivos (optativo)
Escribí un programa que te permita ordenar las imágenes PNG de esta carpeta. Guardalo en un archivo `ordenar_imgs.py`.

1. Creá un nuevo directorio `../Data/imgs_procesadas/`.
2. Usá `os.walk()` para recorrer los archivos en la carpeta `../Data/ordenar/` (y sus subcarpetas).
3. Cuando encuentres archivos con extensión `png` los vas a *procesar*. En este caso *procesar* significa:
    * Leer la fecha que se encuentra codificada en los últimos 8 caracteres de su nombre en el formato AAAAMMDD (año en 4 dígitos, mes en 2 y día en 2).
    * Usar la fecha obtenida para setear la fecha de última modificación (y de último acceso si no usás Windows).
    * Cambiarle el nombre al archivo para que no tenga más esos dígitos (ni el guión bajo).
    * Mover el archivo a la carpeta  `../Data/imgs_procesadas/`.
4. Los archivos que no son `png` no los modifiques.
5. Borrá todas las subcarpetas de `../Data/ordenar/` que hayan quedado vacías.

_Observación:_ Al final, tu script debería poder ejecutarse desde la línea de comandos recibiendo como parámetro el directorio a leer original y un directorio destino (que debería ser creado si no existe).

_Observación:_ Este tipo de tareas se repite con mucha frecuencia. Tener la capacidad de automatizarlas mediante un script de Python te puede ahorrar muchísimo tiempo.


**Algunos puntos importantes:**

  * Te pedimos que modularices el procesamiento de los archivos `png`. Para eso, definí por un lado una función `procesar_nombre(fname)` que tome el nombre de un archivo y devuelva la fecha y el nombre corregido, y por el otro una función `procesar(fname)` que procese cada archivo (que use la función anterior para renombrar, mover y modificar la fecha de cada archivo). La modularización del código es clave para que otras personas lo puedan entender y que sea sencillo de mantener.

```python
>>> procesar_nombre('correlation_20200924.png')
('correlation.png', datetime.datetime(2020, 9, 24, 0, 0))
```

  * Usá docstrings y comentarios en tu código de manera que sea legible.

  * Al terminar de usar el código, comentá todas las instrucciones salvo los imports y las definiciones de funciones, para poder entregarlo al cierre de la clase.


