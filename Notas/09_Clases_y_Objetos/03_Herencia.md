# 9.3 Herencia

Esta sección tiene [un video](https://youtu.be/n7CxhdOmHb8) donde introducimos el tema de herencia.

La herencia entre clases es una herramienta muy usada para escribir programas extensibles. Exploraremos esta idea a continuación.

### Introducción

Se usa herencia para crear objetos más especializados a partir de objetos existentes.

```python
class Padre:
    ...

class Hijo(Padre):
    ...
```
Se dice que `Hijo` es una clase derivada o subclase. La clase `Padre` es conocida como la clase base, o superclase. La expresión `class Hijo(Padre):` significa que estamos creando una clase llamada `Hijo` que es derivada de la clase `Padre`. 


### Extensiones

Al usar herencia podés tomar una clase existente y ...

* Agregarle métodos
* Redifinir métodos existentes
* Agregar nuevos atributos

Podés verlo como una forma de **extender** de tu codigo existente. Darle nuevos comportamientos, abarcar un abanico más amplio de posibilidades ó aumentar su compatibilidad. 

### Ejemplo

Suponé que partís de la siguiente clase:

```python
class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio

    def costo(self):
        return self.cajones * self.precio

    def vender(self, ncajones):
        self.cajones -= ncajones
```

Podés modificar lo que necesites mediante herencia.

### Agregar un método nuevo

```python
class MiLote(Lote):
    def rematar(self):
        self.vender(self.cajones)
```

Se puede usar así:

```python
>>> c = MiLote('Pera', 100, 490.1)
>>> c.vender(25)
>>> c.cajones
75
>>> c.rematar()
>>> c.cajones
0
>>>
```

Esta clase heredó los atributos y métodos de `Lote` y la extendío con un nuevo método (`rematar()`).

### Redefinir un método existente

```python
class MiLote(Lote):
    def costo(self):
        return 1.25 * self.cajones * self.precio
```

Un ejemplo de uso:

```python
>>> c = MiLote('Pera', 100, 490.1)
>>> c.costo()
61262.5
>>>
```

El método nuevo simplemente reemplaza al definido en la clase base. Los demás métodos y atributos no son afectados. ¿No es buenísimo?

### Utilizar un método prevalente

Hay veces en que una clase extiende el método de la superclase a la que pertenece, pero necesita ejecutar el método original como parte de la redefinición del método nuevo. Para referirte a la superclase, usá `super()`:

```python
class Lote:
    ...
    def costo(self):
        return self.cajones * self.precio
    ...

class MiLote(Lote):
    def costo(self):
        # Fijate cómo usamos `super`
        costo_orig = super().costo()
        return 1.25 * costo_orig
```

Usá `super()` para llamar al método de la clase base (del la cual ésta es heredera).

### El método `__init__` y herencia.

Al crear cada instancia se ejecuta `__init__`. Ahí reside el código importante para la creación de una instancia nueva. Si redefinís `__init__` siempre incluí un llamado al método `__init__` de la clase base para inicializarla también.

```python
class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
    ...


class MiLote(Lote):
    def __init__(self, nombre, cajones, precio, factor):
        # Fijate como es el llamado a `super().__init__()`
        super().__init__(nombre, cajones, precio)
        self.factor = factor

    def costo(self):
        return self.factor * super().costo()
```

Es necesario llamar al método `__init__()` en la clase base. Es una forma de ejecutar la versión previa del método que estamos redefiniendo, como mostramos recién.

### Usos de herencia

Uno de los usos de definir una clase como heredera de otra es organizar jerárquicamente objetos que están relacionados.

Un ejemplo: Las figuras geométricas pueden tener ciertos métodos y atributos que luego son refinados en casos concretos como círculos o rectángulos.

```python
class FiguraGeom:
    ...

class Circulo(FiguraGeom):
    ...

class Rectangulo(FiguraGeom):
    ...
```

Imaginate por ejemplo su uso en una jerarquía lógica, o taxonómica, en la que las clases tienen una relación natural tal que hace intuitivo derivar una de otra. 

Una aplicación más común, y tal vez más práctica, consiste en escribir código que es reutilizable y/o extensible. Podríamos definir una clase base para una interfaz de transferencia de datos y permitir que cada fabricante de equipo de adquisición de datos implemente los detalles de comunicación con cada interfaz en particular.

```python
class Procesador_de_datos(TCPHandler):
    def procesar_pedido(self):
        ...
        # Procesamiento de datos
```

La clase base contiene código de administración no específico. Cada clase hereda ese código y modifica las partes necesarias.

### Relación "isinstance"

La herencia establece una relación de clases.

```python
class FiguraGeom:
    ...

class Circulo(FiguraGeom):
```

Preguntamos si un objeto es una instancia de cierta clase:

```python
>>> f = Circulo(4.0)
>>> isinstance(f, FiguraGeom)
True
>>>
```

*Importante: Idealmente, todo código que funcione con instancias de una clase base debería también funcionar con instancias de las clases derivadas de ella.*

### La clase base `object` 

Si una clase no tiene superclase, a veces se escribe  `object` como clase base.

```python
class Figura_geom(object):
    ...
```

`object` es la superclase de todo objeto en Python.

### Herencia múltiple.

Podés heredar de varias clases simultáneamente si los especificás en la definición de clase.

```python
class Madre:
    ...

class Padre:
    ...

class Hijo(Madre, Padre):
    ...
```

La clase `Hijo` hereda características de ambos padres. Algunos detalles son un poco delicados y no vamos a usar esa forma de heredar clases en este curso, aunque vas a encontrar un poco más de información en la próxima sección.


## Ejercicios

El concepto de herencia es especialmente útil cuando estás escribiendo código que va a ser extendido o adaptado, ya sea en bibliotecas o grandes sistemas configurables, pero también en pequeños paquetes de procesamiento de datos que pueden adquirir datos de diversas fuentes. Como ya dijimos antes, uno puede escribir las relaciones y comportamientos fundamentales y dejar los detalles de implementación de cada interfaz para cuando sean necesarios.

Para verlo mejor volvamos a la función `imprimir_informe()` que figura en el programa `informe_final.py`. Tenía más o menos este aspecto:

```python
def imprimir_informe(data_informe):
    '''
    Imprime una tabla prolija desde una lista de tuplas con (nombre, cajones, precio, cambio) 
    '''
    headers = ('Nombre','Cajones','Precio','Cambio')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10 + ' ')*len(headers))
    for row in data_informe:
        print('%10s %10d %10.2f %10.2f' % row)
```

Al ejecutar tu programa `informe_final.py` la salida es algo parecido a esto: 

```python
>>> import informe_final
>>> informe_final.informe_camion('../Data/camion.csv', '../Data/precios.csv')
    Nombre    Cajones     Precio     Cambio
 ---------- ---------- ---------- ----------
      Lima        100      $32.2       8.02
   Naranja         50      $91.1      15.18
     Caqui        150    $103.44       2.02
 Mandarina        200     $51.23      29.66
   Durazno         95     $40.37      33.11
 Mandarina         50      $65.1      15.79
   Naranja        100     $70.44      35.84
```

A continuación vamos a trabajar con herencias relacionadas con este código.

### Ejercicio 9.5: Un problema de extensibilidad
Imaginá que necesitás que la función `imprimir_informe()` pueda exportar el informe en una variedad de formatos: texto plano, HTML, CSV ó XML. Podrías escribir una función enorme que resuelva todos los casos, pero resultaría en código repetido, y difícil de mantener. Ésta es una oportunidad perfecta para usar herencia de objetos.

Vamos a enfocarnos en los pasos necesarios para crear una tabla. 

Al principio de la tabla tenemos los encabezados de las columnas. Después de eso, los datos de la tabla ordenados en una fila por ítem. Pongamos cada uno de esos pasos en una clase distinta. Creá un archivo nuevo llamado `formato_tabla.py` y definí la siguiente clase:

```python
# formato_tabla.py

class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        raise NotImplementedError()

    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        raise NotImplementedError()
```

Por ahora la clase no hace nada, pero sirve como una especie de especificación de diseño para otras clases que vamos a definir. Una clase como ésta es a menudo llamada "clase base abstracta".

Ahora es necesario modificar la función `imprimir_informe()` para que acepte como fuente de datos un objeto `FormatoTabla` e invoque los métodos de este objeto para producir la tabla de salida. Algo así:

```python
# informe_final.py
import formato_tabla

...

def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)
```

Como agregaste un argumento a `imprimir_informe()`, hay que modificar también `informe_camion()`. Cambialo para que cree un objeto `formateador` de este modo:

```python
# informe_final.py

import formato_tabla

...

def informe_camion(archivo_camion, archivo_precios):
    '''
    Crea un informe a partir de un archivo de camión
    y otro de precios de venta.
    '''
    # Leer archivos con datos
    camion = leer_camion(archivo_camion)
    precios = dict(leer_precios(archivo_precios))

    # Crear los datos para el informe
    data_informe = hacer_informe(camion, precios)

    # Imprimir el informe
    formateador = formato_tabla.FormatoTabla()
    imprimir_informe(data_informe, formateador)
```

Ejecutá este código:

```python
>>> ================================ RESTART ================================
>>> import informe_final
>>> informe_final.informe_camion('../Data/camion.csv', '../Data/precios.csv')
... crashes ...
```

Debería dar inmediatamente una excepción de tipo `NotImplementedError`. No es nada maravilloso, pero es exactamente lo que esperábamos que sucediera, ¿no?   Sigamos...


### Ejercicio 9.6: Usemos herencia para cambiar la salida
La clase FormatoTabla que definiste en la primera parte es sólo la base de un sistema extensible. Éste es el momento de extenderla. Definí una clase `FormatoTablaTXT` como sigue:

```python
# formato_tabla.py

...

class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()
```

Modificá la función `informe_camion()` y probala: 

```python
# informe_final.py

...

def informe_camion(archivo_camion, archivo_precios):
    '''
    Crea un informe por camion a partir de archivos camion y precio.
    '''
    # Leer archivos con datos
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    # Obtener los datos para un informe
    data_informe = hacer_informe(camion, precios)

    # Imprimir
    formateador = formato_tabla.FormatoTablaTXT()
    imprimir_informe(data_informe, formateador)
```

Este código debería dar la misma salida que antes:

```python
>>> ========================REINICIAR INTERPRETE========================
>>> import informe_final
>>> informe_final.informe_camion('../Data/camion.csv', '../Data/precios.csv')
    Nombre   Cantidad     Precio     Cambio 
---------- ---------- ---------- ---------- 
      Lima        100      32.20       8.02 
   Naranja         50      91.10      15.18 
     Caqui        150     103.44       2.02 
 Mandarina        200      51.23      29.66 
   Durazno         95      40.37      33.11 
 Mandarina         50      65.10      15.79 
   Naranja        100      70.44      35.84    
>>>
```

Ahora probemos otras variantes. Definí, para empezar, una nueva clase llamada `FormatoTablaCSV` que genere la salida en formato CSV:

```python
# formato_tabla.py
...
class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))
```

Modificá tu programa `informe_final.py` de este modo:

```python
def informe_camion(archivo_camion, archivo_precios):
    '''
    Crea un informe por camion a partir de archivos camion y precio.
    '''
    # Leer archivos con datos
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    # Obtener los datos para un informe
    data_informe = hacer_informe(camion, precios)

    # Imprimir
    formateador = formato_tabla.FormatoTablaCSV()
    imprimir_informe(data_informe, formateador)
```

Ahora la salida debería tener este aspecto:

```python
>>> ========================REINICIAR INTERPRETE========================
>>> import informe_final
>>> informe_final.informe_camion('../Data/camion.csv', '../Data/precios.csv')
Nombre,Cantidad,Precio,Cambio
Lima,100,32.20,8.02
Naranja,50,91.10,15.18
Caqui,150,103.44,2.02
Mandarina,200,51.23,29.66
Durazno,95,40.37,33.11
Mandarina,50,65.10,15.79
Naranja,100,70.44,35.84
```

Usando las mismas ideas creá la clase `FormatoTablaHTML` que produzca un tabla de la siguiente forma:

```
<tr><th>Nombre</th><th>Cajones</th><th>Precio</th><th>Cambio</th></tr>
<tr><td>Lima</td><td>100</td><td>32.20</td><td>8.02</td></tr>
<tr><td>Naranja</td><td>50</td><td>91.10</td><td>15.18</td></tr>
<tr><td>Caqui</td><td>150</td><td>103.44</td><td>2.02</td></tr>
<tr><td>Mandarina</td><td>200</td><td>51.23</td><td>29.66</td></tr>
<tr><td>Durazno</td><td>95</td><td>40.37</td><td>33.11</td></tr>
<tr><td>Mandarina</td><td>50</td><td>65.10</td><td>15.79</td></tr>
<tr><td>Naranja</td><td>100</td><td>70.44</td><td>35.84</td></tr>
```

Para testear tu código, modificá el programa principal de modo que use un objeto de la clase `FormatoTablaHTML` en lugar de uno de la clase `FormatoTablaCSV` para darle formato a la tabla de salida. Fijate lo fácil que es cambiar el comportamiento de un programa cuando tenés objetos que son compatibles entre sí.

### Ejercicio 9.7: Polimorfismo en acción
Una de las grandes ventajas de la programación orientada a objetos es que podés cambiar un objeto por otro compatible y tu programa va a funcionar sin necesidad de adaptar el código que usa esos objetos.

Si escribiste un programa diseñado para usar un objeto de la clase `FormatoTabla`, va a funcionar sin importar *qué* objeto de esa clase uses. A este comportamiento particular se lo llama polimorfismo. Está relacionado con la capacidad de usar la misma interfaz con diferentes objetos de la misma clase, haciendo que el programa como un todo se porte distinto.

Ahora bien, un potencial problema es cómo diseñar tu programa de manera que el usuarie final pueda elegir el formato. Usar los nombres de las clases de formateadores no resultaría cómodo. Una solución posible es considerar un condicional:


```python
def informe_camion(archivo_camion, archivo_precios, fmt = 'txt'):
    '''
    Crea un informe con la carga de un camión
    a partir de archivos camion y precio.
    El formato predeterminado de la salida es txt
    Alternativas: csv o html
    '''
    # Leer archivos con datos
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    # Obtener los datos para un informe
    data_informe = hacer_informe(camion, precios)

    # Elige formato
    if fmt == 'txt':
        formateador = formato_tabla.FormatoTablaTXT()
    elif fmt == 'csv':
        formateador = formato_tabla.FormatoTablaCSV()
    elif fmt == 'html':
        formateador = formato_tabla.FormatoTablaHTML()
    else:
        raise RuntimeError(f'Unknown format {fmt}')
    imprimir_informe(data_informe, formateador)
```

En este código, el usuarie especifica un nombre simplificado como `txt` o
`csv` para elegir el formato. Pero bancá. ¿Es una buena idea poner un gran bloque `if` en la función `informe_camion()`? ¿O quizás sería mejor ponerla directamente en una función de propósito general en otro lado?

En el archivo `formato_tabla.py`, agregá la función `crear_formateador(nombre)` que permita crear un objeto formateador dado un tipo de salida como `txt`, `csv`, o `html`.  Modificá `informe_camion()` para que se vea así:

```python
def informe_camion(archivo_camion, archivo_precios, fmt = 'txt'):
    '''
    Crea un informe con la carga de un camión
    a partir de archivos camion y precio.
    El formato predeterminado de la salida es .txt
    Alternativas: .csv o .html
    '''
    # Lee archivos de datos
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    # Crea la data del informe
    data_informe = hacer_informe(camion, precios)

    # Imprime el informe
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)
```

Acordate de testear todas las ramas posibles del código para asegurarte de que está funcionando. Llamalo y pedile crear salidas en todos los formatos (podés ver el HTML con tu browser).

### Ejercicio 9.8: Volvamos a armar todo
Modificá tu programa `informe_final.py` de modo que la función `informe_camion()` acepte un parámetro opcional que especifique el formato de salida deseado. Por ejemplo:

```python
>>> informe_final.informe_camion('../Data/camion.csv', '../Data/precios.csv', fmt = 'txt')
    Nombre    Cajones     Precio     Cambio 
---------- ---------- ---------- ---------- 
      Lima        100      32.20       8.02 
   Naranja         50      91.10      15.18 
     Caqui        150     103.44       2.02 
 Mandarina        200      51.23      29.66 
   Durazno         95      40.37      33.11 
 Mandarina         50      65.10      15.79 
   Naranja        100      70.44      35.84
>>>
```

Modificá el programa principal y usá `sys.argv()` para poder definir un formato particular directamente desde la línea de comandos. En el siguiente ejemplo se ve un caso de uso. Idealmente, ese parámetro debería ser opcional y, si no se lo pasás, debería andar como antes.

```bash
bash $ python3 informe_final.py ../Data/camion.csv ../Data/precios.csv csv
Nombre,Cajones,Precio,Cambio
Lima,100,32.20,8.02
Naranja,50,91.10,15.18
Caqui,150,103.44,2.02
Mandarina,200,51.23,29.66
Durazno,95,40.37,33.11
Mandarina,50,65.10,15.79
Naranja,100,70.44,35.84

```

Esta versión de `informe_final.py` preparala para entregarla.

### Discusión

El caso que vimos es un ejemplo de uno de los usos más comunes de herencia en programación orientada a objetos: escribir programas extensibles. Un sistema puede definir una interfaz mediante una superclase base, y pedirte que escribas tus propias implementaciones derivadas de esa clase. Si escribís los métodos específicos para tu caso particular podés adaptar la función de un sistema general para resolver tu problema. 

Otro concepto, un poco más interesante, es el de crear tus propias abstracciones. En los ejercicios de esta parte definimos *nuestra propia clase* para crear variaciones en el formato de un informe.
Tal vez estés pensando "¡Debería usar una biblioteca para crear formatos ya escrita por otre!". Bueno, no. Está bueno que puedas *tanto* crear tu propia clase *como* usar una biblioteca ya escrita. El hecho de usar tu propia clase te da flexibilidad.

Siempre que tu programa adhiera a la interfaz de objetos definida por tu clase, podés cambiar la implementación interna en los objetos que escribas para que funcionen del modo que elijas. Podés escribir todo el código vos o usar bibliotecas ya escritas, no importa. Cuando encuentres algo mejor, cambiás tu implementación para que llame al nuevo código. Si la interfaz que hiciste está bien escrita, no vas a necesitar modificar el programa que usa las diferentes implementaciones. Simplemente funcionan si cumplen los contratos de la interfaz. Es algo muy útil y es uno de los motivos por los que usar herencia puede resolverte los problemas de extensibilidad y diversidad a futuro.

Dicho esto, es cierto que diseñar un programa en el paradigma orientado a objetos puede resultar algo muy difícil. Si vas a encarar proyectos grandes con esta herramienta, consultá libros sobre patrones de diseño en POO. De todos modos, haber entendido lo que acabamos de hacer te permite llegar bastante lejos.


