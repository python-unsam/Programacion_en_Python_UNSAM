[Contenidos](../Contenidos.md) \| [Anterior (8 Cierre)](08_Cierre.md)

# 3.9 El album de Figuritas

Album de EXACTAS-PROGRAMA. [Salio en las noticias](https://www.infobae.com/2014/05/29/1568512-dos-cientificos-calculan-cuantos-paquetes-hay-que-comprar-completar-el-album-del-mundial/)


## Las figuritas del mundial

El objetivo de esta actividad será realizar un programa en Python que responda la pregunta:
**¿Cuántas figuritas hay que comprar para completar el álbum del Mundial?**


### Datos:
1. \'Album con $670$ figuritas.
2. Cada figurita se imprime en cantidades iguales y se distribuye aleatoriamente.
3. Cada paquete trae cinco figuritas.

Vamos a utilizar este disparador para presentar conceptos claves en cualquier lenguaje de programación.


### Otras herramientas útiles de Python

Para que estén disponibles más funciones de Python, tenemos que utilizar el comando `import`.
En particular, en esta actividad vamos a usar dos módulos:
1. El módulo `random` ya lo usamos en la actividad anterior, el comando es `import random`.
2.  Vamos a utilizar un nuevo módulo que se mucho para operar numéricamente: `numpy`. El comando es: `import numpy as np`.


## Primeros Ejercicios:

Experimentá los siguientes comandos *en la consola* (debés tener importados los módulos):

- `random.random()`
- `random.randint(1, 10)`
- `lista = np.arange(10)`
- `print(lista)`
- `np.mean(lista)`


### El modelo del álbum de figuritas

Vamos a representar un álbum de n figuritas utilizando una lista de n posiciones numeradas de 0 a n-1.
Cada posición representa el estado de una figurita con dos valores: 0 para indicar que aún no la conseguimos y 1 para indicar que sí.

Por ejemplo, si tuviéramos un álbum de seis figuritas vacío lo vamos a representar como `[0, 0, 0, 0, 0, 0]`.
Cuando consigamos la figurita 3 tendremos que indicarlo poniendo un 1 en el tercer lugar de la lista, es decir `album[2]=1` y el álbum nos va a quedar  `[0, 0, 1, 0, 0, 0]`.



### Primera simplificación

Suponga que las figuritas se compran **individualmente** (de a una, no en un paquete con varias).
En este caso, **la dinámica** del llenado es la siguiente:


- Iniciamos con un álbum vacío y sin haber comprado ninguna figurita
- Compramos figuritas (de a una) hasta llenar el álbum; es decir, se repite la acción (\textit{el paso`) de comprar figuritas \emph{mientras` el álbum este incompleto
- Al terminar nos interesa saber cuántas figuritas tuvimos que comprar para llenar el álbum

## Ejercicios

Vamos ahora a implementar computacionalmente este modelo:

### Ejercicio 3.11: 
Implemente la función `crear_album(figus_total)` que devuelve un álbum *vacío* con `figus_total` espacios para pegar figuritas.


### Ejercicio 3.12: 
Implemente la función `hay_ceros(l)` que recibe una lista y devuelve `True` si la lista contiene el elemento `0`.
En el caso en que no esté, debe devolver `False`. Piense qué hace esta función aplicada a un album.

### Ejercicio 3.13:  
Alguna de las funciones que probamos antes sirve para devolver un número aleatorio dentro de un rango (¿Cuál era?).
Implemente la función `comprar_una_figu(figus_total)` que recibe el número total de figuritas que tiene el álbum (dado por el parámetro `figus_total`) y devuelve un número entero aleatorio que representa la figurita que nos tocó.

### Ejercicio 3.14:  
Implemente la función `cuantas_figus(figus_total)` que, dado el tamaño del álbum (`figus_total`), simule su llenado y devuelva la cantidad de figuritas que se debieron adquirir para completarlo.

### Ejercicio 3.15:  
Calcule `n_repeticiones=1000` veces la función anterior utilizando `figusTotal=6` y guarde en una lista los resultados obtenidos en cada repetición.
Con los resultados obtenidos estime cuántas figuritas hay que comprar, en promedio, para completar el álbum (de seis figuritas).

**Ayuda: El comando `np.mean(a)` devuelve el promedio de la lista `a`.**

### Ejercicio 3.16:  
Calcule `n_repeticiones=100` veces la función `cuantas_figus(figus_total=670)` y guarde los resultados obtenidos en cada repetición en una lista.
Con los resultados obtenidos estime cuántas figuritas hay que comprar, en promedio, para completar el álbum (de 670 figuritas).

### Ahora con paquetes

Para pensar y discutir con su compañero o alguna de sus otras personalidades:

1. Describa en palabras cómo impacta en lo realizado tener paquetes con figuritas.

2. ¿Cómo puede representar un paquete?

## Ejercicios

### Ejercicio 3.17:  
Simule la generación de un paquete con cinco figuritas, sabiendo que el álbum es de 670. Notemos que, como en la vida real, pueden haber figuritas repetidas en un paquete.

### Ejercicio 3.18:  
Implemente una función `generar_paquete(figus_total, figus_paquete)` que, dado el tamaño del álbum (`figus_total`) y la cantidad de figuritas por paquete (`figus_paquete`), genere un paquete de figuritas al azar.

### Ejercicio 3.19:  
Implemente una función `cuantos_paquetes(figus_total, figus_paquete)` que dado el tamaño del álbum simule el llenado del álbum y devuelva cuántos paquetes se debieron adquirir para completarlo.

### Ejercicio 3.20:  
Calcule `n_repeticiones=100` veces la función `cuantos_paquetes`, utilizando `figus_total=670`, `figus_paquete=5` y guarde los resultados obtenidos en una lista y calcule su promedio.

## Ejericcios Optativos:

### Ejercicio 3.21:  
Utilizando lo implementado en el ítem anterior, estime la probabilidad de completar el álbum con $850$ paquetes o menos.

### Ejercicio 3.22:  
Utilizando lo implementado, estime cuántos paquetes debe comprar para tener una chance del $90\%$ de completar el álbum.

### Ejercicio 3.23:  
Repita suponiendo ahora que no hay figuritas repetidas en un paquete.


[Contenidos](../Contenidos.md) \| [Anterior (8 Cierre)](08_Cierre.md)

