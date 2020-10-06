
## El mundo

Documentación del archivo [mundo.py](../mundo.py)

El mundo será el encargado de hacerse de un tablero que usará de soporte, llenarlo de animales y ordenarlos a estos que se comporten de cierta forma en cada etapa que implemente.

### Constructor

En el constructor se define el tamaño del mundo, la cantidad inicial de Leones y Antílopes, tiene la opción de que imprima información de lo que va sucediendo con el parámetro `debug`.

```python
    def __init__(self, columnas, filas, n_leones, n_antilopes, debug=False):
        super(Mundo, self).__init__()

        self.debug = debug

        self.etapa = 0
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

La etapa de movimiento, para cada posición ocupada del tablero, se le indican cuales son sus vecinos libres y se lo manda a moverse, en caso de que el animal responda con una posición, se lo mueve a la posición indicada

```python
    def etapa_movimiento(self):
        print_debug(f"Iniciando Movimiento en etapa {self.etapa}", self.debug)
        for p in self.tablero.posiciones_ocupadas():
            animal = self.tablero.posicion(p)

            posiciones_libres = self.tablero.posiciones_vecinas_libre(p)
            nueva_posicion = animal.moverse(posiciones_libres)
            if nueva_posicion:
                self.tablero.mover(p, nueva_posicion)
```

En la etapa de alimentación, es similar a la anterior, salvo que se le indican cuales son sus vecinos ocupados y se los manda a alimentarse, en caso de que el animal responda con una posición, se lo mueve a la posición indicada.

```python
    def etapa_alimentacion(self):
        print_debug(f"Iniciando Alimentación en etapa {self.etapa}", self.debug)
        for p in self.tablero.posiciones_ocupadas():
            animal = self.tablero.posicion(p)
            animales_cercanos = self.tablero.posiciones_vecinas_con_ocupantes(p)
            desplazo = animal.alimentarse(animales_cercanos)
            if desplazo:
                self.tablero.ubicar(desplazo, self.tablero.retirar(p))
```

La etapa de reproducción no está implementada. Se deben pasar los animales vecinos. En este punto se debe realizar una importante decisión de modelado. ¿Quién es el encargado de que sólo se apareen animales de la misma especie? ¿El mundo?¿O cada animal?
En base a esto se deberá quizás modificar código existente.

```python
    def etapa_reproduccion(self):
        print_debug(f"Iniciando Reproducción en etapa {self.etapa}", self.debug)
        pass
```

Finalmente el método que cierra una etapa, haciendo que todos los animales cumplan una etapa y retirando los que ya no están con vida.

```python
    def pasar_una_etapa(self):
        print_debug(f"Concluyendo etapa {self.etapa}", self.debug)
        for p in self.tablero.posiciones_ocupadas():
            animal = self.tablero.posicion(p)
            animal.pasar_una_etapa()
            if not animal.en_vida():
                self.tablero.retirar(p)
        self.etapa += 1
```

Los 4 métodos están para ser llamados todos juntos con:

```python
    def pasar_un_ciclo(self):
        self.etapa_movimiento()
        self.etapa_alimentacion()
        self.etapa_reproduccion()
        self.pasar_una_etapa()
```

### Tips para pruebas

Una forma para probar el funcionamiento es tener el siguiente código que corre el mundo varias veces con una pausa de tiempo para poder verlo.

```python
m = Mundo(12, 6, 5, 15, debug=True)

import time
for i in range(20):
    m.pasar_un_ciclo()
    time.sleep(1)
    print(i +1)
    print(m)
```









