[Contenidos](../Contenidos.md) \| [Anterior (3 Métodos especiales)](03_Métodos_Especiales.md) \| [Próximo (5 Teledetección)](05_Teledeteccion.md)

# 8.4 Objetos, pilas y colas

En esta sección tendrás que resolver algunos ejercicios definiendo clases y objetos.

### Un ejercicio geométrico

Creá una clase llamada `Rectangulo` que va a estar definido por dos puntos. Para esos dos puntos, usá la clase Punto de la Sección anterior. El rectángulo es paralelo a los ejes, los puntos representan dos esquinas opuestas cualesquiera.
La clase debe tener un método constructor para crear el rectángulo a partir de dos puntos y los siguientes métodos:
* `base()` que dé la medida de la base del rectángulo.
* `altura()` que dé la medida de la altura del rectángulo.
* `area()` que dé la medida del área del rectángulo.
* Creá métodos especiales `__str__` y `__repr__`.
* `desplazar(desplazamiento)` que dado un desplazamiento (de tipo Punto) desplace el rectángulo en ambas coordenadas usando el método `add` de la clase Punto.
* `rotar()` que rote el rectángulo sobre su esquina inferior derecha 90 grados a la derecha.

Probá tu código:

```python
>>> ul = Punto(0,2)
>>> lr = Punto(1,0)
>>> ll = Punto(0,0)
>>> ur = Punto(1,2)
>>> rect1 = Rectangulo(ul,lr)
>>> rect2 = Rectangulo(ll,ur)
>>> rect1.base()
1
>>> rect1.base()
1
>>> rect2.altura()
2
>>> rect2.altura()
2
>>> rect1.rotar()
>>> rect2.rotar()
>>> rect1.base()
2
>>> rect2.base()
2
>>> rect1.altura()
1
>>> rect2.altura()
1
```


### Ejercicio 8.11: Canguros buenos y canguros malos
Este ejercicio está relacionado con un error muy común en Python. Escribí una definición de una clase `Canguro` que tenga:

*  Un método `__init__` que inicializa un atributo llamado `contenido_marsupio` como una lista vacía.
* Un método llamado `meter_en_marsupio` que, dado un objeto cualquiera, lo agregue a la lista `contenido_marsupio`.
* Un método `__str__` que devuelve una representación como cadena del objeto `Canguro` y de los contenidos de su marsupio.

Probá tu código creando dos objetos, `madre_canguro` y `cangurito` y guardá en el marsupio de la madre algunos objetos y al cangurito. 

Luego, mirá el ejemplo `canguro_malo.py` copiado a continuación. Este ejemplo tiene un bug. Analizalo, corregilo. Entregá como respuesta un archivo `canguros_buenos.py` conteniendo, perimero la clase definida por vos y luego una corrección de la clase definida en el ejemplo, junto con un comentario indicando dónde estaba el error y en qué constía.

 
```python
# canguro_malo.py
"""Este código continene un 
bug importante y dificil de ver
"""

class Canguro:
    """Un Canguro es un marsupial."""
    
    def __init__(self, nombre, contenido=[]):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        self.contenido_marsupio = contenido

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)

#%%
madre_canguro = Canguro('Madre')
cangurito = Canguro('gurito')
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio('llaves del auto')
madre_canguro.meter_en_marsupio(cangurito)

print(madre_canguro)

# Al ejecutar este código todo parece funcionar correctamente.
# Para ver el problema, imprimí el contenido de cangurito.
```

### Colas

Una **cola** es una estructura de datos. Se caracteriza por contener una secuencia de elementos y dos operaciones: encolar y desencolar. La primera, encolar, agrega un elemento al final de la secuencia que contiene la cola. Desencolar, por su parte, devuelve el primer elemento de la secuencia y lo elimina de la misma. 

Las colas también se llaman estructuras FIFO (del inglés First In First Out), debido a que el primer elemento en entrar a la cola será también el primero en salir. El nombre cola se le da por su analogía con las colas que hacemos (o hacíamos cuando podíamos salir de casa) para entrar al cine, por ejemplo.

<p align="center">
<img src="./colas.png" width="400">
</p>

Esta es una posible implementación de la clase `Cola`:
```python
class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0
```

### Ejercicio 8.12: Torre de Control
Usando un par de objetos de la clase Cola, escribí una nueva clase llamada `TorreDeControl` que modele el trabajo de una torre de control de un aeropuerto con una pista de aterrizaje. Los aviones que están esperando para aterrizar tienen prioridad sobre los que están esperando para despegar. La clase debe funcionar conforme al siguiente ejemplo:

```python
>>> torre = TorreDeControl()
>>> torre.nuevo_arribo('AR156')
>>> torre.nueva_partida('KLM1267')
>>> torre.nuevo_arribo('AR32')
>>> torre.ver_estado()
Vuelos esperando para aterrizar: AR156, AR32
Vuelos esperando para despegar: KLM1267
>>> torre.asignar_pista()
El vuelo AR156 aterrizó con éxito.
>>> torre.asignar_pista()
El vuelo AR32 aterrizó con éxito.
>>> torre.asignar_pista()
El vuelo KLM1267 despegó con éxito.
>>> torre.asignar_pista()
No hay vuelos en espera.
```

Guardá tu solución (conteniendo también la definición de la clase `Cola`) en `torre_control.py` para entregar al final de la clase.

### Pilas

Una **pila** (_stack_ en inglés) es una estructura de datos. Se trata de una lista ordenada que permite almacenar y recuperar datos, con un modo de acceso de tipo LIFO (del inglés Last In, First Out, «último en entrar, primero en salir»). Funcionan de manera opuesta que las colas que mencionamos antes. 

Las pilas y colas son estructuras de datos que se aplican en multitud de contextos debido a su simplicidad y capacidad de modelar diferentes procesos.

La operaciones (métodos) elementales de las pilas son _apilar_ (coloca un objeto en la pila) y _desapilar_ (retira el último elemento apilado). En inglés se llaman _push_ y _pop_ y son análogos al _encolar_ y el _desencolar_ de la colas. 

En cada momento solamente se tiene acceso a la parte superior de la pila, es decir, al último objeto apilado. La operación _desapilar_ justamente permite la obtención de este elemento, que es retirado de la pila.

<p align="center">
<img src="./pilas.png" width="400">
</p>


La **pila de llamadas** (en inglés _call stack_) de un lenguaje (por ejemplo Python), es una pila manejada por el intérprete que almacena la información sobre las subrutinas activas en cada instante. También se la conoce como pila de ejecución o pila de control y se usa para llevar registro de las funciones que se fueron llamando y el de las variables definidas en cada contexto. 

Por ejemplo, si definimos las siguientes funciones:

```python
def f():
    x = 50
    a = 20
    print("En f, x vale", x)

def g():
    x = 10
    b = 45
    print("En g, antes de llamar a f, x vale", x)
    f()
    print("En g, después de llamar a f, x vale", x)

```

la ejecución de `g()` resulta en:

```python
>>> g()
En g, antes de llamar a f, x vale 10
En f, x vale 50
En g, después de llamar a f, x vale 10. 
```

Para poder volver a recuperar el valor 10 para `x` en `g()` luego de llamar a `f()` se manejó adecuadamente la pila de llamadas. Podemos pensar que en la ejecución de `g()`, justo antes de llamar a `f()` había un _estado_ que podría ser resumido en `estado = {función: 'g', próxima_línea_a_ejecutar: 4, variables: {x: 10, b: 45}}`. Luego se ejecuta la cuarta línea de código. El intérprete incrementa `próxima_línea_a_ejecutar` y, antes de llamar a `f()`,  **apila** el `estado` en la pila de llamadas. Al llamar a `f()`, el nuevo estado pasa a ser `estado = {función: 'f', próxima_línea_a_ejecutar: 1, variables = {}}`. El intéreprete ejecuta las tres líneas de código de `f`, incrementando la variable `próxima_línea_a_ejecutar` en cada paso, y agregando `x:50` y luego `a:20` el estado de las variables. Por lo tanto, termina la ejecución de `f` en el `estado = {función: 'f', próxima_línea_a_ejecutar: 4, variables = {x: 50, a: 20}}`. Como ya no hay más código que ejecutar de `f()` el intérprete **desapila**  un estado y continúa con la ejecución usando `estado = {función: 'g', próxima_línea_a_ejecutar: 5, variables: {x: 10, b: 45}}`, y por lo tanto imprime:
```
En g, después de llamar a f, x vale 10. 
```

Estos conceptos son importantes para la clase próxima donde estudiaremos funciones que se llaman a sí mismas _recursivamente_. Si no fuera por la pila de llamadas, los valores de las variables de las diferentes instancias de una función recursiva correrían el riesgo de mezclarse y confundirse.

### Ejercicio 8.13: implementar el TAD pila
Implementá en una clase `Pila` el TAD descripto anteriormente con los métodos `apilar()`, `desapilar()` y `esta_vacia()`.

Usala para reproducir el siguiente código:

```python
def mostrar_x_del_estado(estado):
    print(f"Ejecutando {estado['función']}(), x vale {estado['variables']['x']}")


pila_de_llamadas = Pila()
#la ejecución está en la línea 3 de g(). El estado tiene x=10.
estado = {'función': 'g', 'próxima_línea_a_ejecutar': 3, 'variables': {'x': 10, 'b': 45}}
mostrar_x_del_estado(estado)
#sigo ejecutando, toca llamar a f(): incremento y apilo el estado.
estado['próxima_línea_a_ejecutar'] = 5
pila_de_llamadas.apilar(estado)
#llamo a f y ejecuto primeras líneas
estado = {'función': 'f', 'próxima_línea_a_ejecutar': 3, 'variables': {'x': 50, 'a': 20}}
mostrar_x_del_estado(estado)
#termina ejecución de f: se desapila el estado:
estado = pila_de_llamadas.desapilar()
mostrar_x_del_estado(estado)
```

Su ejecución debería dar:
```
Ejecutando g(), x vale 10
Ejecutando f(), x vale 50
Ejecutando g(), x vale 10
```

[Contenidos](../Contenidos.md) \| [Anterior (3 Métodos especiales)](03_Métodos_Especiales.md) \| [Próximo (5 Teledetección)](05_Teledeteccion.md)

