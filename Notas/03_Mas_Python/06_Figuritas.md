[Contenidos](../Contenidos.md) \| [Anterior (5 NumPy)](05_NumPy_Arrays.md) \| [Próximo (7 Cierre*)](07_Cierre.md)

# 3.6 El album de Figuritas+

## Las figuritas del mundial

Esta es una adaptación de una actividad que diseñaron nuetres colegas de Exactas-Programa y amablemente nos dejaron unsar aquí. 

El objetivo de esta actividad es hacer un programa en Python que responda la pregunta: **¿Cuántas figuritas hay que comprar para completar el álbum del Mundial?**

![Album de Figuritas](./completo.jpg)


Esta pregunta es noticia cada cuatro años:
- [Mundial de Brasil 2014](https://www.pagina12.com.ar/diario/contratapa/13-250187-2014-07-06.html)
- [Mundial de Rusia 2018](https://www.lanacion.com.ar/2125275-rusia-2018-cuantos-sobres-de-figuritas-hacen-falta-para-llenar-el-album-del-mundial)
- Incluso hay un paper que [salió referido en el diario](https://www.infobae.com/2014/05/29/1568512-dos-cientificos-calculan-cuantos-paquetes-hay-que-comprar-completar-el-album-del-mundial/)


### Datos:
1. Álbum con $670$ figuritas.
2. Cada figurita se imprime en cantidades iguales y se distribuye aleatoriamente.
3. Cada paquete trae cinco figuritas.

Vamos a utilizar este disparador para presentar conceptos claves.


### Herramientas útiles de Python

Para que estén disponibles más funciones de Python, tenés que usar el comando `import`.
En particular, en esta actividad vamos a usar dos módulos:
- El módulo `random` lo vamos a importar con el comando `import random` y lo vamos a usar para generar figuritas (pseudo) aleatoriamente.
- El módulo `numpy` lo vamos a importar con el comando `import numpy as np` y lo vamos a usar para operar numéricamente.


### El modelo del álbum de figuritas

Vamos a representar un álbum de n figuritas utilizando un vector de NumPy con posiciones numeradas de 0 a n-1.
Cada posición representa el estado de una figurita con dos valores: 0 para indicar que aún no la conseguimos y 1 para indicar que sí (o, si prefería, podés usar un número positivo para representar cuántas de esas figus tenés).

Por ejemplo, si tuviéramos un álbum de seis figuritas vacío lo vamos a representar como `[0, 0, 0, 0, 0, 0]`.
Cuando consigamos la figurita 3 tendremos que indicarlo poniendo un 1 en el tercer lugar de la lista, es decir `album[2]=1` y el álbum nos va a quedar  `[0, 0, 1, 0, 0, 0]`.



### Primera simplificación

Suponé por ahora que las figuritas se compran **individualmente** (de a una, no en un paquete con cinco).
En este caso, **la dinámica** del llenado es la siguiente:


- Iniciamos con un álbum vacío y sin haber comprado ninguna figurita
- Compramos figuritas (de a una) hasta llenar el álbum; es decir, se repite la acción (*el paso*) de comprar figuritas *mientras* (while) el álbum este incompleto.
- Al terminar nos interesa saber cuántas figuritas tuvimos que comprar para llenar el álbum.

## Ejercicios con figus sueltas

Vamos ahora a implementar computacionalmente este modelo. 

### Ejercicio 3.16: Crear
Implementá la función `crear_album(figus_total)` que devuelve un álbum *vacío* con `figus_total` espacios para pegar figuritas.


### Ejercicio 3.17: Incompleto
¿Cuál sería el comando de Python que nos dice si hay al menos un cero en la lista que representa el álbum? ¿Qué significa que haya al menos un cero en nuestro vector?

Implemente la función `album_incompleto(A)` que recibe un vector y devuelve `True` si la lista contiene el elemento `0`. En el caso en que no haya ceros debe devolver `False`. 


### Ejercicio 3.18: Comprar 
Alguna de las funciones que introdujimos en la [Sección 3.4](../03_Mas_Python/04_Random.md#valores-discretos)  sirve para devolver un número aleatorio dentro de un rango (¿cuál era?).
Implementá una función `comprar_una_figu(figus_total)` que recibe el número total de figuritas que tiene el álbum (dado por el parámetro `figus_total`) y devuelva un número entero aleatorio que representa la figurita que nos tocó.

### Ejercicio 3.19: Cantidad de compras 
Implementá la función `cuantas_figus(figus_total)` que, dado el tamaño del álbum (`figus_total`), simule su llenado y devuelva la cantidad de figuritas que se debieron adquirir para completarlo.

### Ejercicio 3.20:  
Ejecutá `n_repeticiones=1000` veces la función anterior utilizando `figusTotal=6` y guardá en una lista los resultados obtenidos en cada repetición.
Con los resultados obtenidos estimá cuántas figuritas hay que comprar, en promedio, para completar el álbum (de seis figuritas).

*Ayuda: El comando `np.mean(l)` devuelve el promedio de la lista `l`.*

### Ejercicio 3.21:  
Calculá `n_repeticiones=100` veces la función `cuantas_figus(figus_total=670)` y guardá los resultados obtenidos en cada repetición en una lista.
Con los resultados obtenidos estimá cuántas figuritas hay que comprar, en promedio, para completar el álbum (de 670 figuritas).

### Ahora con paquetes

Estos ejercicios te recomendamos que los pienses y discutas con un compañero o alguna de tus otras personalidades (si es que tenés):

1. ¿Cómo impacta en lo realizado tener paquetes con figuritas en lugar de figus sueltas?
2. ¿Cómo puede representarse un paquete?


## Ejercicios con paquetes

### Ejercicio 3.22:  
Simulá la generación de un paquete con cinco figuritas, sabiendo que el álbum es de 670. Notemos que, como en la vida real, pueden haber figuritas repetidas en un paquete.

### Ejercicio 3.23:  
Implementá una función `generar_paquete(figus_total, figus_paquete)` que, dado el tamaño del álbum (`figus_total`) y la cantidad de figuritas por paquete (`figus_paquete`), genere un paquete de figuritas al azar.

### Ejercicio 3.24:  
Implementá una función `cuantos_paquetes(figus_total, figus_paquete)` que dado el tamaño del álbum y la cantidad de fiugs por paquete, simule el llenado del álbum y devuelva cuántos paquetes se debieron adquirir para completarlo.

### Ejercicio 3.25:  
Calculá `n_repeticiones=100` veces la función `cuantos_paquetes`, utilizando `figus_total=670`, `figus_paquete=5`. Guarda los resultados obtenidos en una lista y calculá su promedio.

## Ejercicios un toque más estadísticos:

### Ejercicio 3.26:  
Utilizando lo implementado en el ítem anterior, **estimá** la probabilidad de completar el álbum con $850$ paquetes o menos.

### Ejercicio 3.27:  
Utilizando lo implementado, **estimá** cuántos paquetes habría que comprar para tener una chance del $90\%$ de completar el álbum.

### Ejercicio 3.28:  
Repetí suponiendo que no hay figuritas repetidas en un paquete. ¿Cuánto cambian las probabilidades?

### Ejercicio 3.29: 
Por último, suponé que cinco amigues se juntan y deciden compartir la compra de figuritas y el llenado de sus cinco álbumes solidariamente. Calculá cuántos paquetes deberían comprar si deben completar todos. Hace 100 repeticiones y compará el resultado con la compra individual que calculaste antes.

[Contenidos](../Contenidos.md) \| [Anterior (5 NumPy)](05_NumPy_Arrays.md) \| [Próximo (7 Cierre*)](07_Cierre.md)

