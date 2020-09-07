[Contenidos](../Contenidos.md) \| [Anterior (1 Control de errores)](01_Excepciones.md) \| [Próximo (3 Temas de diseño)](03_306Design_discussion.md)

# 6.2 El módulo *main* (principal)
 
en esta sección  introducimos el concepto de un programa principal o un módulo proncipal. 

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
Se refiere a la primer función que es ejecutada cuando corremos un programa.

### Módulo principal en Python

Python no tiene una función o método principal. En su lugar existe un *módulo principal* y éste será el archivo con código fuente que se ejecuta primero.

```bash
bash % python3 prog.py
...
```

El archivo que le pases al intérprete al invocarlo será el módulo principal. No importa cómo lo llames.

### Chequear `__main__` 

Es una práctica estándard usar la siguiente convención en módulos que son ejecutados como scripts principales: 

```python
# prog.py
...
if __name__ == '__main__':
    # Soy el programa principal ...
    comandos
    ...
```

Los comandos dentro del `if` constituyen el *programa principal*

### Programa principal vs. módulo importado

Cualquier archivo.py puede ejecutarse ya sea como el programa principal o como un módulo importado:  

```bash
bash % python3 prog.py # Corriendo como principal
```

```python
import prog   # Corriendo como módulo importado
```

En ambos casos, `__name__` es el nombre del módulo. Sin embargo `__name__` sólo valdrá `__main__` si ese módulo está siendo ejecutado como el script principal. 

Normalmente deseamos que los comandos que son parte del comportamiento del script en modo *principal* sólo se ejecuten si efectivamente el script es el módulo principal. No queremos que esos comandos se ejecuten si el módulo fué importado.

Por lo tanto es comun escribir una condición `if` que decida cómo se va a portar el código cuando éste puede ser usado de ambas maneras.  

```python
if __name__ == '__main__':
    # Esto no se ejecuta en un módulo importado ...
```

### Modelo de programa

Este es un modelo común para escribir un programa en Python:

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

Python es muy usado para ejecutar herramientas desde la línea de comandos, como hemos visto en clase:

```bash
bash % python3 informe.py camion.csv precios.csv
```
Lo cual significa que los scripts pueden ser ejecutados desde la terminal para casos como automatización de procesos, ejecutar tareas en "el fondo", etc.

### Argumentos en la línea de comandos

La línea de comandos es una lista de cadenas de texto.

```bash
bash % python3 informe.py camion.csv precios.csv
```

Podemos acceder a esta lista de cadenas a través de `sys.argv`.

```python
# Llamado como recién, sys.argv contiene
sys.argv # ['informe.py, 'camion.csv', 'precios.csv']
```

Este es un ejemplo simple para procesar los argumentos recibidos al invocar un script desde la terminal:

```python
import sys

if len(sys.argv) != 3:
    raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile preciofile')
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

Por omisión, la salida impresa es dirigida a `sys.stdout`, la entrada se lee de `sys.stdin`, y la recapitulación de errores es dirigida a `sys.stderr`.

Las entradas y salidad de *stdio* pueden estar ligadas a una terminal, a la pantalla, a archivos o incluir cosas más extrañas como pipes, etc.

```bash
bash % python3 prog.py > resultados.txt
# ó sino
bash % cmd1 | python3 prog.py | cmd2
```

(Esta syntaxis se llama "piping" o redireccionamiento y significa: ejecutar cmd1, enviar su salida como entrada a prog.py invocado desde la terminal, y la salida de éste será la entrada para cmd2)

### Terminación del programa

La terminación y salida del programa se administran a traves de excepciones.

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

Es estándard que un codigo de salida de `0` indica que no hubo problemas y otro valor, que los hubo. 

### El comando `#!` 

Bajo Unix (Linux es un Unix) una línea que comienza con `#!` ejecutará un script en el intérprete Python.

```python
#!/usr/bin/env python3
# prog.py
...
```

Para ello el archivo prog.py requiere permiso de ejecución asignado. Puede permitirse así: 

```bash
bash % chmod +x prog.py
# Ahora lo podés ejecutar
bash % prog.py
... salida ...
```

*Observación: Al iniciar un script Python en Windows, se lee la línea que comienza con `#!` dentro del script para saber qué versión del intérprete invocar.*

### Modelo de script con parámetros

Para terminar, este es un modelo de un programa en Python que se ejecuta como si fuera un script invocado desde la terminal.

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
def main(argv):
    # Analizar la línea de comandos, etc.
    ...

if __name__ == '__main__':
    import sys
    main(sys.argv)
```

## Ejercicios

### Ejercicio 6.4: Función `main()`
En tu programa `informe.py` agregá una función `main()` que acepte una lista de opciones en la línea de comandos y produzca la misma salida que antes. Deberías ahora ser capas de ejecutarlo del siguiente modo:

```python
>>> import informe
>>> informe.main(['informe.py', 'Data/camion.csv', 'Data/precios.csv'])
      Name    Cajones     Precio     Cambio
---------- ---------- ---------- ----------
      Lima        100       9.22     -22.98
   Naranja         50     106.28      15.18
     Caqui        150      35.46     -47.98
 Mandarina        200      20.89     -30.34
   Durazno         95      13.48     -26.89
 Mandarina         50      20.89     -44.21
   Naranja        100     106.28      35.84
>>>
```

Modificá el archivo `costo_camion.py` para que incluya una función similar `main()` que te permita hacer esto:

```python
>>> import costo_camion
>>> costo_camion.main(['costo_camion.py', 'Data/camion.csv'])
Total cost: 47671.15
>>>
```

### Ejercicio 6.5: Hacer un script
Modificá tus programas `informe.py` y `costo_camion.py` para que puedan ser ejecutados como scripts desde la línea de comandos:

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


[Contenidos](../Contenidos.md) \| [Anterior (1 Control de errores)](01_Excepciones.md) \| [Próximo (3 Temas de diseño)](03_306Design_discussion.md)

