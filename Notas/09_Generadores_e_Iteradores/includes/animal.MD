
## Animales

Documentación del archivo [animal.py](../animal.py)

La clase Animal será una clase abstracta, de la cual heredarán la clase León y la clase Antílope. Los métodos y atributos comunes que representen a un animal deberán estar en esta clase.

### Constructor

El constructor no recibe parámetros, sólo instancia los atributos iniciales. En esta documentación se instancian algunos.

```python
    def __init__(self):
        super(Animal, self).__init__()
        self.edad = 0
        self.autonomia_restante = self.autonomia
```

### Consultas

A continuación se muestran los métodos para obtener información del animal. Es importante notar que un animal en sí, no es ni León ni Antílope, por eso ambas preguntas devuelven `False`.

Estos métodos definen a su vez el comportamiento, no siendo unicamente una observación de las variables, sino que definen que un animal está vivo únicamente si no alcanzó la edad máxima y además no pasó el límite de tiempo que puede estar sin alimentarse.

Lo mismo sucede con `tiene_hambre` que podría modificarse para que un animal que ya se alimentó no necesite alimentarse instantáneamente. Se pueden agregar métodos como `puede_tener_cria` y cualquier otra consulta que sea de un animal.

```python
    def en_vida(self):
        return (self.edad <= self.edad_maxima) and self.autonomia_restante > 0

    def tiene_hambre(self):
        """Acá se puede poner comportamiento para que no tenga hambre todo el tiempo"""
        return True

    def es_leon(self):
        return False

    def es_antilope(self):
        return False
```

### Modificadores

Algunos modificadores.

```python
    def pasar_una_etapa(self):
        self.edad += 1
        # self.autonomia_restante -= 1 Se pued restar si no llega a comer

    def tener_cria(self):
        """Acá se puede poner comportamiento que sucede al tener cria"""
        pass

    def alimentarse(self, animales_vecinos):
        self.autonomia_restante = self.autonomia
        return None

    def reproducirse(self, vecinos, libres):
        pos = None
        if vecinos:
            animal = random.choice(vecinos)
            if libres:
                animal.tener_cria()
                self.tener_cria()
                pos = random.choice(libres)

        return pos

    def moverse(self, libres):
        pos = None
        if libres:
            pos = random.choice(libres)

        return pos
```

## León

La clase `Leon` es pequeña, al heredar de Animal:

```python
class Leon(Animal):
```
todas los métodos y atributos definidos allí están disponibles. Se hace un `override` del metodo `es_leon` para aclarar que en este caso SÍ es un león. Y como el león es carnívoro, también se extiende el método alimentarse que sólo sucede cuando puede comer.

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
            if presas_cercanas: # hay presas cerca
                super(Leon, self).alimentarse()
                (pos, animal) = random.choice(presas_cercanas)

        return pos

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









class Leon(Animal):
    """docstring for Leon"""


    def __repr__(self):
        # return "L"
        return "L{}".format(self.edad)



class Antilope(Animal):
    """docstring for Antilope"""
    def __init__(self):
        super(Antilope, self).__init__()
        self.autonomia = 8
        self.edad_maxima = 8

    def es_antilope(self):
        return True

    def __repr__(self):
        # return "A"
        return "A{}".format(self.edad)








