
## El tablero

Documentación del archivo [tablero.py](../tablero.py)

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

El método `posiciones_vecinas` es el que define la topología del terreno. En este caso, una celda tiene como vecinos a las 8 celdas con las que comparte un borde o un vértice (excepto en los bordes). Es posible modificar la dinámica del mundo modificando esta función.

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


