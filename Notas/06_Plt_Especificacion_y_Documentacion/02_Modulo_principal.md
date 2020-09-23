[Contenidos](../Contenidos.md) \| [Anterior (1 Control de errores)](01_Excepciones.md) \| [Próximo (3 Cuestiones de diseño)](03_Flexibilidad.md)

# 6.2 El módulo principal
 
En esta sección introducimos el concepto de **módulo principal**. 

### Función principal

En muchos lenguajes de programación existe el concepto de método o función *principal*. 

```c
// c / c++
int main(int argc, char *argv[]) {
    ...
}
```

```java
// java
class myprog {
    public static void main(String args[]) {
        ...
    }
}
```
Se refiere a la primera función que es ejecutada cuando corremos un programa.

### Módulo principal en Python

Python no tiene una función o método principal. En su lugar existe un *módulo principal* y éste será el archivo con código fuente que se ejecuta primero.

```bash
bash % python3 prog.py
...
```

El archivo que le pases al intérprete al invocarlo será el módulo principal. No importa cómo lo llames.

### Chequear `__main__` 

Es una práctica estándar usar la siguiente convención en módulos que son ejecutados como scripts principales: 

```python
# prog.py
...
if __name__ == '__main__':
    # Soy el programa principal ...
    comandos
    ...
```

Los comandos dentro del `if` constituyen el *programa principal*



### Módulo principal vs. módulo importado

Cualquier archivo .py puede ejecutarse ya sea como el programa principal o como un módulo importado:  

```bash
bash % python3 prog.py # Corriendo como principal
```

```python
import prog   # Corriendo como módulo importado
```

La variable `__name__` es el nombre del módulo. Sin embargo, esta variable  `__name__` valdrá `__main__` si ese módulo está siendo ejecutado como el script principal. 

Normalmente deseamos que los comandos que son parte del comportamiento del script en modo *principal* sólo se ejecuten si efectivamente el script es el módulo principal. No queremos que esos comandos se ejecuten si el módulo fue importado.

Por lo tanto es común escribir una condición `if` que decida cómo se va a portar el código cuando éste puede ser usado de ambas maneras.  

```python
if __name__ == '__main__':
    # Esto no se ejecuta en un módulo importado ...
```

### Modelo de programa

Éste es un modelo usual para escribir un programa en Python:

```python
# prog.py
# Comandos import (bibliotecas o módulos)
import modules

# Funciones
def spam():
    ...

def blah():
    ...

# Función principal
def main():
    ...

if __name__ == '__main__':
    main()
```

### Herramientas para la consola 

Python se usa muy frecuentemente para correr herramientas desde la línea de comandos. En clase vimos algún ejemplo:

```bash
bash % python3 informe.py camion.csv precios.csv
```

Esto permite que los scripts sean ejecutados desde la terminal para correr ciertos procesos automáticos, ejecutar tareas en segundo plano, etc.

### Argumentos en la línea de comandos

Python interpreta una línea de comandos como una lista de cadenas de texto.

```bash
bash % python3 informe.py camion.csv precios.csv
```

Como el script `informe.py` no está preparado para leer parámetros, no los va a usar. Igual, podés acceder a esta lista de cadenas usando `sys.argv`. Por ejemplo, si usas el parámetro `-i` para invocar a python de modo que el intérprete interactivo no termine luego de llamar a `informe.py` con los parámetros anteriores

```bash
bash % python3 -i informe.py camion.csv precios.csv
```
luego podrás ver el contenido de esta lista:

```python
# Llamado como recién, sys.argv contiene
import sys
sys.argv # ['informe.py, 'camion.csv', 'precios.csv']
```

Ahora vamos a hacer que los tenga en cuenta. El siguiente es un ejemplo de script simple para procesar los argumentos recibidos al invocarlo desde la terminal. Te permite usar tu script para generar el informe con archivos de diferentes camiones o precios, pasados como parámetros por la línea de comandos:

```python
import sys

if len(sys.argv) != 3:
    raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion archivo_precios')
camion = sys.argv[1]
precios = sys.argv[2]
...
```

### Standard I/O

Los archivos de entrada y salida estándard (Standard Input / Output (stdio)) son archivos que se portan como archivos normales, pero están definidos por el sistema operativo.

```python
sys.stdout
sys.stderr
sys.stdin
```

Por omisión, la salida impresa es dirigida a `sys.stdout` (usualmente la pantalla), la entrada se lee de `sys.stdin` (usualmente el teclado), y la recapitulación de errores es dirigida a `sys.stderr` (usualmente, la pantalla otra vez).

Las entradas y salidas de *stdio* pueden estar ligadas al teclado, a la pantalla, a una impresora, a diferentes archivos o incluir cosas más extrañas como pipes, etc.

```bash
bash % python3 prog.py > resultados.txt
# o si no
bash % cmd1 | python3 prog.py | cmd2
```

Esta sintaxis se llama "piping" o redireccionamiento y significa: ejecutar cmd1, enviar su salida como entrada a prog.py invocado desde la terminal, y la salida de éste será la entrada para cmd2.

### Terminación del programa

La terminación y salida del programa se administran a través de excepciones.

```python
raise SystemExit
raise SystemExit(codigo_salida)
raise SystemExit('Mensaje informativo')
```

O, alternativamente:

```python
import sys
sys.exit(codigo_salida)
```

Es estándar que un codigo de salida de `0` indica que no hubo problemas y otro valor, que los hubo. 

### El comando `#!` 

Bajo Unix (Linux es un Unix) una línea que comienza con `#!` ejecutará un script en el intérprete Python. Por ejemplo, si agregás la siguiente línea al comienzo de tu script podés ejecutar directamente el script (sin invocar manualmente a Python en la misma línea).


```python
#!/usr/bin/env python3
# prog.py
...
```

Para porder ser ejecutado, el archivo `prog.py` requiere permiso de ejecución asignado. Podés asignarle este permiso así: 

```bash
bash % chmod +x prog.py
# Ahora lo podés ejecutar
bash % ./prog.py
... salida ...
```

*Observación: Al iniciar un script Python en Windows, se lee la línea que comienza con `#!` dentro del script para saber qué versión del intérprete invocar.*

### Modelo de script con parámetros

Para terminar, éste es un modelo usual de programa en Python que se ejecuta invocado desde la terminal.

```python
#!/usr/bin/env python3
# prog.py

# Import (bibliotecas)
import modules

# Funciones
def spam():
    ...

def blah():
    ...

# Funcion principal
def main(parametros):
    # Analizar la línea de comandos, 
    # usando la variable parámetros en lugar 
    # de sys.argv, donde corresponda
    ...

if __name__ == '__main__':
    import sys
    main(sys.argv)
```

_Observación: Este modelo es flexible en el sentido que te permite escribir programas que podés llamar desde la terminal pasándole parámetros o ejecutar directamente dentro de un intérprete usando `import` y llamando a su función `main` como veremos en los siguientes ejercicios._

## Ejercicios

Recordá trabajar siempre con las últimas versiones de tus archivos.

### Ejercicio 6.2: Función `main()`
Usando estas ideas, agregá a tu programa `informe.py` una función `main()` que tome una lista de parámetros en la línea de comandos y produzca la misma salida que antes.

```bash
bash % python3 informe.py Data/camion.csv Data/precios.csv
```

También deberías poder ejecutarlo del siguiente modo dentro del intérprete interactivo de Python:

```python
>>> import informe
>>> informe.main(['informe.py', 'Data/camion.csv', 'Data/precios.csv'])

    Nombre    Cajones     Precio     Cambio
 ---------- ---------- ---------- ----------
      Lima        100      $32.2       8.02
   Naranja         50      $91.1      15.18
     Caqui        150    $103.44       2.02
 Mandarina        200     $51.23      29.66
   Durazno         95     $40.37      33.11
 Mandarina         50      $65.1      15.79
   Naranja        100     $70.44      35.84

>>>
```

Análogamente, modificá el archivo `costo_camion.py` para que incluya una función similar `main()` que te permita hacer esto:

```python
>>> import costo_camion
>>> costo_camion.main(['costo_camion.py', 'Data/camion.csv'])
Total cost: 47671.15
>>>
```

### Ejercicio 6.3: Hacer un script
Finalmente, modificá tus programas `informe.py` y `costo_camion.py` para que puedan ser ejecutados como scripts desde la línea de comandos:

```bash
bash $ python3 informe.py Data/camion.csv Data/precios.csv
    Nombre    Cajones     Precio     Cambio
 ---------- ---------- ---------- ----------
      Lima        100      $32.2       8.02
   Naranja         50      $91.1      15.18
     Caqui        150    $103.44       2.02
 Mandarina        200     $51.23      29.66
   Durazno         95     $40.37      33.11
 Mandarina         50      $65.1      15.79
   Naranja        100     $70.44      35.84

bash $ python3 costo_camion.py Data/camion.csv
Costo total: 47671.15
```

_Aclaración:_  En el ejercicio anterior ya agregaste una función `main()` a tu código. En este simplemente deberías verificar si `__name__ == '__main__'` y llamar a esa función para que se ejecute automáticamente cuando llames a tu programa desde la línea de comandos. 

[Contenidos](../Contenidos.md) \| [Anterior (1 Control de errores)](01_Excepciones.md) \| [Próximo (3 Cuestiones de diseño)](03_Flexibilidad.md)

