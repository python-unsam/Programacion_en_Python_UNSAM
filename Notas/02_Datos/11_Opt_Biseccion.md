[Contenidos](../Contenidos.md) \| [Anterior (10 Cierre de la segunda clase)](10_CierreClase.md)

# 2.11 Búsqueda de raíces de funciones

Ejercicios opcionales de la clase 2. Profundizar en algunos conceptos.

### Insertar un elemento en una lista
Uno de los problemas de la búsqueda binaria es que requiere que la lista esté ordenada. Si la lista se encuentra ordenada podemos mantener el orden evitando adjuntar nuevos elementos de forma desordenada.

Escribí una función `insertar(l,e)` que recibe una lista ordenada *l* y un elemento y *e*. Si el elemento se encuentra en la lista solamente devuelve su posición; si no se encuentra en la lista, lo inserta en la posición correcta para mantener el orden. En ambos casos debe devolver su posición.

Usá la función `busqueda_binaria(l,e)` del [Ejercicio 2.31](../02_Datos/09_Algo_BSec_BBin.md#ejercicio-231-búsqueda-binaria) para determinar si $e$ se encuentra en $l$.


### Búsqueda secuencial de raíces

Buscar una raíz de una función real tiene ciertas similitudes con buscar un elemento en una lista. Para fijar ideas vamos a buscar una raíz de la función *f(x)=x^2-25* aunque otras funciones pueden considerarse fácilmente.

Considerá el siguiente código:

```python
#Busqueda secuencial
    
x = 25
epsilon = 0.01
paso = epsilon**2
sol = 0.0
totPasos = 0
while abs(sol**2 -x) >= epsilon and sol<x: #Salgo cuando hallo la solucion con poco error o cuando me paso
    sol += paso
    totPasos += 1
    
    
if abs(sol**2 -x) < epsilon: #si encontre la solucion
    print("La raiz de  %f es %f"%(x,sol))
    print("La solucion fue encontrada en %d pasos"%totPasos)
else:
    print("Luego de %d pasos no encontre la solucion"%totPasos)
```
¿Cuántos pasos tarda en encontrar una raíz de 25? ¿Cuántos pasos tarda en encontrar una raíz de 30? ¿Cuál es la precisión del método? ¿Si quisiera duplicar la precisión (es decir, dividir por dos el error máximo que puedo cometer) cuántos pasos más me tomaría hallar la raíz de 30?

### Método de bisección

La analogía entre la búsqueda de una raiz de una función real y la búsqueda de un elemento en un a lista se puede extender también a la búsqueda binaria. La pregunta adecuada --en aquel caso, comparar con el elemento central-- nos permite descartar la mitad de la lista. En la búsqueda de una raíz real, el [Teorema del valor intermedio](https://es.wikipedia.org/wiki/Teorema_del_valor_intermedio) nos garantiza que si una función contínua es positiva en un extremo de un intervalo y negativo en el otro, entonces vale cero en al menos un punto de su interior. Evaluando la función *f* en el centro *c* del intervalo podemos, dependiendo del signo de *f(c)* asegurar que la raíz se encuentra en uno de las dos mitades y así ir reduciendo el tamaño del intervalo que contiene la raíz hasta la precisión que queramos.

Considerá el siguiente código:

```python
#Busqueda por bisección

x = 25
epsilon = 0.0001
totPasos = 0

cota_inf=0
cota_sup=max(x,1.0)
sol = (cota_inf+cota_sup)/2

while abs(sol**2 -x) >= epsilon: #Salgo cuando hallo la solución con un error tolerable
    print("busco en [%f, %f], valor medio: %f"%(cota_inf,cota_sup,sol))
    totPasos += 1
    if sol**2 < x:
        cota_inf = sol
    else:
        cota_sup = sol
    sol = (cota_inf + cota_sup) / 2
    
print("busco en [%f, %f], valor medio: %f"%(cota_inf,cota_sup,sol))    
print("La raiz de  %f es %f"%(x,sol))
print("La solucion fue encontrada en %d pasos"%totPasos)
```

¿Cuántos pasos tarda en encontrar una raíz de 25? ¿Cuántos pasos tarda en encontrar una raíz de 30? ¿Cuál es la precisión del método? ¿Si quisiera duplicar la precisión (es decir, dividir por dos el error máximo que puedo cometer) cuántos pasos más me tomaría hallar la raíz de 30?

**Algo sobre la complejidad**


[Contenidos](../Contenidos.md) \| [Anterior (10 Cierre de la segunda clase)](10_CierreClase.md)

