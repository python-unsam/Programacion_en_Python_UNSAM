[Contenidos](../Contenidos.md) \| [Anterior (2 Manejo de archivos y carpetas)](02_Archivos_y_Directorios.md) \| [Próximo (4 Introducción a Pandas)](04_Pandas_basico.md)

# 7.3 Ordenar archivos en Python

Este es un ejercicio guiado en el que vamos a integrar las últimas dos secciones con lo que veníamos viendo antes del parcial. La idea es que descromprimas [este archivo](./ordenar.zip) en tu carpeta `Data/` y escribas un script que te permita ordenar las imágenes PNG de esta carpeta.

1. Creá un nuevo directorio `Data/imgs_ordendas/`.
2. Usá `os.walk()` para recorrer los archivos en la carpeta `Data/ordenar/` (y sus subcarpetas).
3. Cuando encuentres archivos con extensión PNG los vas a *procesar*. En este caso *procesar* significa:
    * Leer la fecha que tiene en los últimos 8 caracteres de su nombre y usarla para setear la fecha de última modificación y de último acceso.
    * Cambiarle el nombre al archivio para que no tenga más esos dígitos (ni el guión bajo).
    * Mover el archivo a la carpeta  `Data/imgs_ordendas/`.
4. Los archivos que no son PNG no los modifiques.
5. Borrá todas las subcarpetas de `Data/ordenar/` que hayan quedado vacías.

Este es un ejercicio simple y un poco caprichoso. Pero este tipo de tareas se repiten con mucha frecuencia y tener la capacidad de programar un script de python que realice este tipo de tareas te puede ahorrar muchísimo tiempo.

**Algunos puntos importantes:**
* El *procesamiento* de un archivo PNG lo debería hacer una función. 
* Tu script debería poder ejecutarse desde la línea de comandos recibiendo dos parámetros: el directorio origianl y el directorio a crear. En la [Sección 6.2](../06_Plt_Especificacion_y_Documentacion/02_Modulo_principal.md#modelo-de-script-con-parámetros) dimos un modelo de script que te puede servir.
* Usa docstrings y comentarios en tu código de manera que sea legible. 
* Guradá el script resultante en un archivo `ordennar_imgs.py`. Te lo vamos a pedir y va a ser el tema de la corrección de pares de esta clase.




[Contenidos](../Contenidos.md) \| [Anterior (2 Manejo de archivos y carpetas)](02_Archivos_y_Directorios.md) \| [Próximo (4 Introducción a Pandas)](04_Pandas_basico.md)

