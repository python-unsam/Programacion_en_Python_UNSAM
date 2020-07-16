[Contenidos](../Contenidos.md) \| [Anterior (9 Algoritmos de búsqueda)](09_Algo_BSec_BBin.md) \| [Próximo (11 Búsqueda de raíces de funciones)](11_Opt_Biseccion.md)

# 2.10 Cierre de la segunda clase

En esta segunda clase aprendimos a trabajar con datos. Manejamos archivos CSV y estructuras un poco más complejas como tuplas, conjuntos y diccionarios y profundizamos un poco más en las listas.

Para cerrar esta clase te pedimos dos cosas:
* Que nos mandes por mail a <python@unsam.edu.ar> los programas de los siguientes ejercicios:
    1. [Ejercicio 2.15](../02_Datos/04_202Containers.md#ejercicio-215-balances) Sobre calcular el costo de camion por linea de comandos `costo_camion.py` con warnings. 
    2. [Ejercicio 2.20](../02_Datos/05_203Formatting.md#ejercicio-220-deafío-de-formato) (o [Ejercicio 2.19](../02_Datos/05_203Formatting.md#ejercicio-219-agregar-encabezados)) Balance con formato `reporte.py` y lectura de encabezados.
    3. [Ejercicio 2.26](../02_Datos/08_Algo_IteradoresLista.md#ejercicio-226-búsqueda-del-máximo) `maximo.py`
    4. [Ejercicio 2.27](../02_Datos/08_Algo_IteradoresLista.md#ejercicio-227-invertir-una-lista) `invlista.py`
    5. [Ejercicio 2.28](../02_Datos/08_Algo_IteradoresLista.md#ejercicio-228-tablas-de-multiplicar) `tablamult.py`
    6. [Ejercicio 2.29](../02_Datos/08_Algo_IteradoresLista.md#ejercicio-229-propagación) `propaga.py`
    7. [Ejercicio 2.30](../02_Datos/09_Algo_BSec_BBin.md#ejercicio-230-búsqueda-secuencial) Búsqueda secuencial `b_sec.py`
    8. [Ejercicio 2.31](../02_Datos/09_Algo_BSec_BBin.md#ejercicio-231-búsqueda-binaria) Búsqueda binaria `b_bin.py`

* Que completes [este formulario](link) usando como identificación tu dirección de mail.
 

Acordate, usá siempre la misma dirección de mail con la que te inscribiste al curso así podemos llevar registro de tus entregas.

Observación: Si el enunciado de un ejercicio te pide que lo corras con un input particular, por favor poné la salida que obtuviste como comentario en tu código. El mail que nos mandes tiene que tener tema (subject) con el siguiente formato: 
> f"Entrega Clase 2 {Apellido}, {Nombre}" 

Por último te recordamos que si te quedaron dudas, querés discutir algún tema de interés o pedirnos a los docentes que resolvamos un ejercicio particular para la próxima clase, podés hacelo en el [grupo de Slack](../Slack.md).

### Los Ejercicios Opcionales

Para profundizar en algunos conceptos y explorar intereses y aplicaciones particular incluímos en este curso una serie de ejercicios opcionales al final de cada clase.

En este caso se trata de dos métodos numéricos para buscar raíces reales de funciones. Uno es el método de bisección que para encontrar una raíz de una función *f* de la que se sabe que *f(a)<0* y que *f(b)>0*. El método evalúa la función en el medio del intervalo *c=(a+b)/2* y, salvo que haya encontrado la raíz (*f(c)=0*), se queda con la mitad del intervalo en el que la función cambia de signo. Iterando este proceso se va formando un *encaje de intervalos*que siempre contiene un cero de la función (por ser contínua) y cuyo tamaño se reduce tanto como uno quiera (iterando suficientes veces) hasta tener una expresion decimal de la raíz buscada con tanta precisión como se quiera.

El otro es el método de Newton-Raphson que se basa en usar la recta tangente a la función para determinar una aproximación cada vez mejor a la raíz de la función *f*.

[Contenidos](../Contenidos.md) \| [Anterior (9 Algoritmos de búsqueda)](09_Algo_BSec_BBin.md) \| [Próximo (11 Búsqueda de raíces de funciones)](11_Opt_Biseccion.md)

