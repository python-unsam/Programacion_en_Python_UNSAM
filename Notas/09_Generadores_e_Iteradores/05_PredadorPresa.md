[Contenidos](../Contenidos.md) \| [Anterior (4 Más sobre generadores)](04_Mas_generadores.md) \| [Próximo (6 Cierre de la novena clase)](06_Cierre.md)

# 9.5 Predador Presa

Los [modelos de depredación y competencia](https://es.wikipedia.org/wiki/Ecuaciones_Lotka%E2%80%93Volterra) forman parte de la batería de herramientas clásicas del ecólogo. Vito Volterra en Italia y Alfred Lotka en Estados Unidos fueron los precursores en este tema y crearon modelos que, con diversas modificaciones y mejoras, seguimos usando hoy en día.
El modelo de Volterra para depredación comienza suponiendo la existencia de dos poblaciones de animales, una de las cuales (el depredador) se alimenta de la otra (la presa). Se supone que las dos poblaciones están formadas por individuos idénticos, mezclados en el espacio.

La gran mayoría de los modelos usualmente estudiados tienen solamente en cuenta la dinámica temporal, desatendiendo la dinámica espacial. Con la excusa de implementar una versión espacio-temporal de este modelo, proponemos un ejercicio guiado que usa fuertemente programación orientada a objetos.

Lo que sigue es un ejercicio optativo. Como decíamos, el ejercicio está muy guiado y toda la estructura del modelo está basada en objetos. La idea es recrear un mundo que imaginaremos como un valle rodeado de montañas en el que existen depredadores (que llamaremos Leones) y presas (que llamaremos Antílopes). Este valle será bidimensional, y lo representaremos por medio de una grilla rectangular que llamaremos tablero.

El modelo inicial con el que trabajaremos tiene definidas 4 etapas que determinan un ciclo:

- **Etapa de movimiento**: en esta etapa cada animal se desplaza a alguna posición vecina desocupada (si es que existe, sino permanece en el lugar). La decisión de a cuál desplazarse será responsabilidad del animal, que, sabiendo las disponibles, elegirá una al azar.

- **Etapa de alimentación**: en esta etapa los animales se alimentan. Los antílopes comerán pasto en su lugar, mientras que los leones buscarán un antílope en las posiciones vecinas y, de existir, se lo comerán. Esta acción de un león se verá reflejada en el tablero con su desplazamiento a la posición del antílope, el cual ya no será más parte de nuestro mundo.

- **Etapa de reproducción**: cada animal buscará en sus posiciones vecinas alguien de su misma especie. Si lo encuentra y además hay una posición vacía en el tablero se incluirá un nuevo animal (de la misma especie) en el tablero. Nuevamente la elección de la pareja y del lugar del nuevo animal serán aleatorias. Este modelo inicial no prevee el atributo sexo, ni un límite entre la cantidad reproducciones en las que puede participar un animal por etapa.

- **Cierre de ciclo**: en la última etapa de un ciclo todos los animales "envejecen" en 1 unidad, aquellos que se reprodujeron y siguen en edad reproductiva vuelven a ser fértiles. Si alguno alcanzó la edad máxima de su especie se considera que ya puede retirárselo del mundo (es decir, se muere). Sucede lo mismo si, al pasar una etapa, alcanza el límite de etapas sin alimentarse, en cuyo caso muere de hambre.

# Clases del modelo inicial:

El modelo inicial te lo podés bajar de [acá](./modelo.zip). Ya tiene definidas la clase `Animal` de la que heredan dos nuevas clases: `León` y `Antílope`. También tiene definida una clase `Tablero`. Todas estas clases se integran en una clase `Mundo`. Vamos a ver una por una estas clases y te indicaremos algunos métodos faltantes que tendrás que implementar vos y otros que te proponemos mejorar.

## Animales

Esta clase está definida en el archivo `animal.py`.

La clase `Animal` será una clase abstracta, de la cual heredarán la clase León y la clase Antílope. Los métodos y atributos comunes que representen a un animal deberán estar en esta clase.

### Constructor

El constructor no recibe parámetros, sólo instancia los atributos iniciales. En esta documentación se instancian algunos.

```python
    def __init__(self):
        super(Animal, self).__init__()
        self.edad = 0
        self.energia = self.energia_maxima # cantidad de ciclos que aguanta sin alimentarse
```

### Consultas

A continuación se muestran los métodos para obtener información del animal. Es importante notar que un animal en sí, no es ni León ni Antílope, por eso ambas preguntas devuelven `False`.

Estos métodos definen a su vez el comportamiento, no siendo unicamente una observación de las variables, sino que definen que un animal está vivo únicamente si no alcanzó la edad máxima y además no pasó el límite de tiempo que puede estar sin alimentarse.

Lo mismo sucede con `tiene_hambre` que podría modificarse para que un animal que ya se alimentó no necesite alimentarse instantáneamente. Se pueden agregar métodos como `puede_tener_cria` y cualquier otra consulta que sea pertinente para un animal.

```python
    def en_vida(self):
        return (self.edad <= self.edad_maxima) and self.energia > 0

    def tiene_hambre(self):
        """Acá se puede poner comportamiento para que no tenga hambre todo el tiempo
        debería depender de la diferencia entre su nivel de energía y su energía máxima"""
        return True

    def es_leon(self):
        return False

    def es_antilope(self):
        return False
```

### Modificadores

A continuación presentamos algunos métodos modificadores del objeto.

```python
    def pasar_un_ciclo(self):
        self.energia -= 1 # consume energía
        self.edad += 1    # envejece 
        if self.edad >= 2 and self.reproducciones_pendientes > 0:
            self.es_reproductore = True #se puede reproducir

    def tener_cria(self):
        """Acá se puede poner comportamiento que sucede al tener cria
        y que evita que tengas más de una cria por ciclo, ¿quizas tener_cria consume más energía que un ciclo común?"""
        pass

    def alimentarse(self, animales_vecinos = None):
        self.energia = self.energia_maxima
        return None

    def reproducirse(self, vecinos, lugares_libres):
        pos = None
        if vecinos:
            pareja = random.choice(vecinos)
            if lugares_libres:
                self.tener_cria()
                pareja.tener_cria()
                pos = random.choice(lugares_libres)

        return pos

    def moverse(self, lugares_libres):
        pos = None
        if lugares_libres:
            pos = random.choice(lugares_libres)
        return pos
```

## León

Al heredar de `Animal`, la clase `Leon` es pequeña:

```python
class Leon(Animal):
```

Todas los métodos y atributos definidos allí están disponibles. Se hace un *override* del metodo `es_leon` para aclarar que en este caso SÍ es un león. Y como el león es carnívoro, también se extiende el método alimentarse que sólo sucede cuando puede comer.

```python
    def __init__(self):
        super(Leon, self).__init__()
        self.autonomia = 3
        self.edad_maxima = 5

    def es_leon(self):
        return True

    def alimentarse(self, animales_vecinos):
        # Se alimenta si puede e indica la posición del animal que se pudo comer
        pos = None
        if self.tiene_hambre(): # no está lleno
            presas_cercanas = [ (pos,animal) for (pos, animal) in animales_vecinos if animal.es_antilope() ]
            if presas_cercanas: # y hay presas cerca
                super(Leon, self).alimentarse()
                (pos, animal) = random.choice(presas_cercanas)

        return pos

```

### Ejemplo: Un León

Probá las siguientes instrucciones:

```python
L = Leon()
L.energia
L.edad
L.es_leon()
L.es_antilope()
L.pasar_un_ciclo()
L.energia
L.edad
L.tiene_hambre()
```


## Antílope

La clase `Antilope` es más pequeña aún y unicamente indica que es un Antílope. Acá se asume fuertemente que el antílope come pasto y que pasto hay siempre.

```python
    def __init__(self):
        self.autonomia = 8
        self.edad_maxima = 8
        super(Antilope, self).__init__()

    def es_antilope(self):
        return True
```

### Ejemplo: Un León y dos Antílopes

Agregá ahora dos antílopes:

```python
A1 = Antilope()
A2 = Antilope()
A1.energia
A1.edad
A1.es_antilope()
```

Y hacé que el León, que ya tiene hambre, se coma alguno de los dos antílopes (aleatoriamente):
```python
vecinos = [(1,A1),(2,A2)]
pos = L.alimentarse(vecinos)
if pos:
    print(f'El león se come al antílope A{pos}')
else:
    print(f'El león no come')
```

Fijate que el método alimentarse no mata al antílope, solo devuelve su posición. *Alguien más* deberá ocuparse de retirarlo del mundo.

Si corrés este código varias veces, vas a ver que el León obtiene energía máxima al comer, pero sigue comiendo. Implementá adecuadamente el método `tiene_hambre()` de la clase `Animal` de manera que solo tenga hambre cuando su energía baje. Volvé a probar el código. El león debería comer solo cuando pase al menos un ciclo desde la última vez que comió.


### Ejemplo: Un León y una Leona

Definamos ahora una leona `M` y hagamos que pasen unos ciclos hasta que sea reproductora.

```python
M = Leon()
M.puede_reproducir()
M.pasar_un_ciclo()
M.puede_reproducir()
```
Repetí hasta que `L` y `M` sean reproductores.

Luego ponelos cerca. Digamos que `M` tiene como vecinos a los dos antílopes y al león `L` de antes. Supongamos que las crias pueden ocupar algunos lugares libres en nuestro mundo (aún no definido):

```python
vecinos = [L]
lugares_libres = [4,5,6,7,8]
L.puede_reproducir()
M.puede_reproducir()
```

Están dadas las condiciones, que se reproduzcan:
```python
pos = M.reproducirse(vecinos, lugares_libres)
print(f'nace un nuevo leoncito en la posición {pos}')
M.puede_reproducir()
M.pasar_un_ciclo()
M.puede_reproducir()
```

Vemos que el método `reproducirse` nos devuelve una de las posiciones que le dijimos que estaban libres y que los leones no pueden volverse a reproducir en el mismo ciclo pero sí en el siguiente.

Pasemos ahora a ver cómo se estructura el tablero.

## El tablero

### Constructor

La clase tablero tendrá un único constructor que recibirá los atributos que darán lugar al tablero del tamaño deseado:

```python
    def __init__(self, filas, columnas):
        super(Tablero, self).__init__()
        self.filas = filas
        self.columnas = columnas
        self.posiciones = {}
        self.n_posiciones_libres = self.filas * self.columnas
```

Esta clase tendrá 4 atributos: el número de filas, el de columnas, un diccionario donde se almacenará el contenido, y la cantidad de celdas vacías. El diccionario tendrá unicamente las posiciones con algún contenido. La cantidad de celdas vacías es un atributo que podría calcularse a partir de los 3 primeros atributos, pero se decidió tenerlo precalculado por ser un valor que se usará mucho.

### Modificadores

El tablero no tiene una gran complejidad, permite ser modificado de 2 maneras: ubicar un elemento en el tablero, y retirar un elemento del tablero. Se provee además de la funcionalidad que combina estas cosas bajo el nombre de mover (cambia de lugar un elemento).

```python
    def ubicar(self,  pos, elem):
        if not self.ocupada(pos):
            self.n_posiciones_libres -= 1
        self.posiciones[pos] = elem
        return pos in self.posiciones

    def retirar(self, pos):
        self.n_posiciones_libres += 1
        return self.posiciones.pop(pos)

    def mover(self, p_origen, p_destino):
        self.ubicar(p_destino, self.retirar(p_origen))
```


### Getters

Además la clase tablero provee métodos para consultar sobre estado de posiciones y los valores que se encuentran en el tablero.

```python
    def posicion(self, pos):
        #devuele qué hay en pos
        return self.posiciones[pos]

    def ocupada(self,  pos):
        return pos in self.posiciones

    def libre(self,  pos):
        return pos not in self.posiciones

    def elementos(self):
        return list(self.posiciones.values())

    def hay_posiciones_libres(self):
        return self.n_posiciones_libres > 0

```

### Modificadores complejos

Una de las funcionalidades deseables para que se pueda usar un tablero, es la posibilidad de ubicar al azar un elemento en algún lugar del mismo (que esté libre). El tablero provee esa funcionalidad:

```python
    def ubicar_en_posicion_vacia(self, elem):
        if not self.hay_posiciones_libres():
            raise RuntimeError("Estás intentado agregar algo al tablero y está lleno")

        pos = choice(self.posiciones_libres())
        self.ubicar(pos, elem)
```

### Consultas

También ofrece consultas más complejas:

```python
    def posiciones_ocupadas(self):
        res = []
        for f in range(self.filas):
            for c in range(self.columnas):
                if self.ocupada((f,c)):
                    res.append((f,c))

        return res

    def posiciones_libres(self):
        res = []
        for f in range(self.filas):
            for c in range(self.columnas):
                if self.libre((f,c)):
                    res.append((f,c))

        return res

    def posiciones_vecinas_libre(self, pos):
        res = self.posiciones_vecinas(pos)
        res = [ p for p in res if self.libre(p)]

        return res

    def posiciones_vecinas_con_ocupantes(self, pos):
        res = self.posiciones_vecinas(pos)
        res = [ (p, self.posicion(p)) for p in res if self.ocupada(p)]

        return res
```

### Auxiliares

El método `posiciones_vecinas` es el que define la topología del terreno. En este caso, una celda tiene como vecinos a las 8 celdas con las que comparte un borde o un vértice (excepto en los bordes). Es posible modificar la dinámica del mundo modificando esta función (por ejemplo, hacerlo cilíndrico, esférico o toroidal).

```python
    def posiciones_vecinas(self, pos):
        desp=[(-1, -1), (-1, 0), (-1, 1),(0, 1), (1, 1), (1, 0),(1, -1), (0, -1)]

        for i in range(len(desp)):
            f = (desp[i][0] + pos[0])
            c = (desp[i][1] + pos[1])
            desp[i] = (f, c)

        desp = [ (f,c) for f,c in desp if (0<=f and f<self.filas) and (0<=c and c<self.columnas) ]

        return desp
```

Se pueden definir como adyacentes sólo las que compartan un borde, o las que estén a 2 celdas de distancia, incluso es posible definir que en el borde del tablero vuelva a empezar del otro lado (condiciones periódicas).

## El mundo

El mundo será el encargado de hacer un tablero que usará de soporte, llenarlo de animales y ordenarlos para que se comporten de cierta forma en cada etapa que se implemente.

### Constructor

En el constructor se define el tamaño del mundo, la cantidad inicial de Leones y Antílopes, tiene la opción de que imprima información de lo que va sucediendo con el parámetro `debug`.

```python
    def __init__(self, columnas, filas, n_leones, n_antilopes, debug=False):
        super(Mundo, self).__init__()

        self.debug = debug

        self.ciclo = 0
        self.tablero = Tablero(filas, columnas)
        self.llenar_mundo(n_leones, n_antilopes)
```

El constructor delega la tarea de llenar el tablero al método `llenar_mundo`:

```python
    def llenar_mundo(self, n_leones, n_antilopes):
        for _ in range(n_leones):
            if self.tablero.hay_posiciones_libres():
                print_debug("ubicando un leon", self.debug)
                self.tablero.ubicar_en_posicion_vacia(Leon())

        for _ in range(n_antilopes):
            if self.tablero.hay_posiciones_libres():
                print_debug("ubicando un Antilope", self.debug)
                self.tablero.ubicar_en_posicion_vacia(Antilope())
```

### Modelado de la dinámica

En la etapa de movimiento, para cada posición ocupada del tablero, se indican cuales son sus vecinos libres y se lo manda a moverse, en caso de que el animal responda con una posición, se lo mueve a la posición indicada.

```python
    def etapa_movimiento(self):
        print_debug(f"Iniciando Movimiento en ciclo {self.ciclo}", self.debug)
        for p in self.tablero.posiciones_ocupadas():
            animal = self.tablero.posicion(p)

            posiciones_libres = self.tablero.posiciones_vecinas_libre(p)
            nueva_posicion = animal.moverse(posiciones_libres)
            if nueva_posicion:
                self.tablero.mover(p, nueva_posicion)
```

En la etapa de alimentación, es similar a la anterior, salvo que se indican cuales son sus vecinos ocupados y se los manda a alimentarse, en caso de que el animal responda con una posición, se lo mueve a la posición indicada.

```python
    def etapa_alimentacion(self):
        print_debug(f"Iniciando Alimentación en ciclo {self.ciclo}", self.debug)
        for p in self.tablero.posiciones_ocupadas():
            animal = self.tablero.posicion(p)
            animales_cercanos = self.tablero.posiciones_vecinas_con_ocupantes(p)
            desplazo = animal.alimentarse(animales_cercanos)
            if desplazo:
                self.tablero.ubicar(desplazo, self.tablero.retirar(p))
```


La etapa de reproducción no está implementada. Más adelante te pediremos que la implementes. Se deben pasar los animales vecinos. En este punto se debe realizar una importante decisión de modelado. ¿Quién es el encargado de que sólo se apareen animales de la misma especie? ¿El mundo?¿O cada animal?
En base a esto se deberá quizás modificar código existente.

```python
    def etapa_reproduccion(self):
        print_debug(f"Iniciando Reproducción en ciclo {self.ciclo}", self.debug)
        pass
```

Finalmente el método que cierra un ciclo haciendo que todos los animales cumplan años, gasten energía y retirando los que ya no están con vida.

```python
    def cerrar_un_ciclo(self):
        print_debug(f"Concluyendo ciclo {self.ciclo}", self.debug)
        for p in self.tablero.posiciones_ocupadas():
            animal = self.tablero.posicion(p)
            animal.pasar_un_ciclo() #envejecer, consumir alimento
            if not animal.en_vida():
                self.tablero.retirar(p)
        self.ciclo += 1
```

Los 4 métodos están para ser llamados todos juntos con:

```python
    def pasar_un_ciclo(self):
        self.etapa_movimiento()
        self.etapa_alimentacion()
        self.etapa_reproduccion()
        self.cerrar_un_ciclo()
```

## Probando el modelo completo

Una forma para probar el funcionamiento es tener el siguiente código que corre el mundo varias veces con una pausa de tiempo para poder verlo.

```python
m = Mundo(12, 6, 5, 15, debug=True)

import time
for i in range(20):
    m.pasar_un_ciclo()
    time.sleep(2)
    print(i +1)
    print(m)
```

Para empezar a explorar más en serio el modelo deberías completar los métodos que estén indicados con `pass` y otros detalles, según te indicamos en los siguientes ejercicios. Agregá además cualquier método que consideres necesario para obtener información, o modelar algún comportamiento.

### Ejercicio 9.17: Etapa de reproducción
Implementá el método `etapa_reproduccion` en la clase `Mundo`.

### Ejercicio 9.18: Acotando la reproducción
Implementá la lógica necesaria para que los animales pueden reproducirse únicamente una vez por año (ya sean los que inician la reproducción o los que son compañeres).

### Ejercicio 9.19: Alcanzando la madurez
Implementá la lógica necesaria para que un animal sólo puede reproducirse cuando ya tiene 2 años cumplidos.

Si llegaste hasta acá, por favor guardá todo junto en un solo archivo `simulacion.py` y entregalo al finalizar la clase.

Una vez realizado esto hay diversas opciones para usarlo y expandirlo.

### Extensiones del modelo

A continuación una lista no exhaustiva de las extensiones posibles al modelo, podés incorporar algunas, o todas:

  - Ningún animal se alimenta más de una vez en una etapa. Modifića el método `tiene_hambre()` de la clase `Animal` para que no siempre tenga hambre.

  - Si un animal se alimenta en una etapa, no necesita alimentarse más por un turno entero.

  - Cuando un León ataca un Antílope, no siempre se lo come, a veces el Antílope logra escapar. Modelar esto con 3 posibles escenarios:

      - Existe una probabilidad p (fija), de que el León tenga éxito (con el módulo `random` se puede hacer `random.random() > p`)

      - La probabilidad es variable dependiendo de la edad del León, siendo muy baja cuando es cachorro, alta cuando es adulto, y baja de nuevo en su vejez.

      - La probabilidad es variable dependiendo de la edad del León, igual al anterior, y la edad del Antílope, siendo la probabilidad de que escape muy baja cuando es cachorro, alta cuando es adulto, y baja de nuevo en su vejez. Una forma de calcular esto es: ![\begin{align*}
p_{comer} = p_{leon}(edadLeon) \times (1 - p_{antilope}(edadAntilope))
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Ap_%7Bcomer%7D+%3D+p_%7Bleon%7D%28edadLeon%29+%5Ctimes+%281+-+p_%7Bantilope%7D%28edadAntilope%29%29%0A%5Cend%7Balign%2A%7D%0A)

      - Se puede hacer uso de los vecinos para modificar esta probabilidad, entonces si los Antílopes están en manada, que la probabilidad de comer del León sea más baja aún.


  - Extender la vecindad a un radio de 2 para todos los animales.

  - Extender la vecindad para distinto radio dependiendo la especie.

  - Que el Antílope pueda visualizar Leones a cierta distancia (ej. radio 3), y desplazarse en otra dirección.


### Exploraciones

  - Analizar distintos valores para la construcción del mundo a lo largo del tiempo. ¿Es posible encontrar un equilibrio entre la cantidad de leones y antílopes?

  - ¿Qué sucede con la supervivencia si se modifican los atributos propios de la clase León y Antílope de manera de que tengan mayor (o menor) autonomía, o sean más longevos?

  - ¿Se detectan ciclos de mayoría de una especie y después de la otra?¿Hay dominación?



[Contenidos](../Contenidos.md) \| [Anterior (4 Más sobre generadores)](04_Mas_generadores.md) \| [Próximo (6 Cierre de la novena clase)](06_Cierre.md)

