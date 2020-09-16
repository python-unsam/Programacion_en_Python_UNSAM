[Contenidos](../Contenidos.md) \| [Anterior (3 Clases***)](03_Clases.md) \| [Próximo (5 Métodos especiales)](05_Métodos_Especiales.md)

# 8.4 Herencia***

Herencia entre clases es una herramienta muy usada para escribir programas extensibles. Exploraremos esa idea en esta sección.

### Introducción

Se usa herencia para crear objetos mas especializados a partir de objetos existentes.

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

Podés verlo como una forma de **extender** de tu codigo existente. Darle nuevos comportamientos, abarcar un abanico mas amplio de posibilidades ó aumentar su compatibilidad. 

### Ejemplo

Suponé que partís de la siguiente clase:

```python
class Cajon:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def cost(self):
        return self.cantidad * self.precio

    def sell(self, ncajones):
        self.cantidad -= ncajones
```
[oski] : # (si Cajon representa un unico cajon, ncajones tiene que ser n;umero de unidades de fruta vendida. )

Podés modificar no que necesites mediante herencia.

### Agregar un método nuevo

```python
class MiCajon(Cajon):
    def rematar(self):
        self.sell(self.cantidad)
```

Se puede usar así:

```python
>>> c = MiCajon('Pera', 100, 490.1)
>>> c.vender(25)
>>> c.cajones
75
>>> c.rematar()
>>> c.cajones
0
>>>
```

### Redefinir un método existente

```python
class MiCajon(Cajon):
    def precio(self):
        return 1.25 * self.cantidad * self.precio
```

Un ejemplo de uso:

```python
>>> c = MiCajon('Pera', 100, 490.1)
>>> c.precio()
61262.5
>>>
```

El método nuevo simplemente reemplaza al definido en la clase base. Los demás métodos y variables no son afectados. No es buenísimo ??

## Overriding

Hay veces en que una clase extiende el método de la superclase a la que pertenece, pero necesita ejecutar el método original como parte de la redefinición del método nuevo. Para referirte a la superclase, usá `super()`:

```python
class Cajon:
    ...
    def cost(self):
        return self.cantidad * self.precio
    ...

class MiCajon(Cajon):
    def precio(self):
        # Fijate como usamos `super`
        precio_actualizado = super().cost()
        return 1.25 * precio_actualizado
```

Use `super()` to call the previous version.


### El método `__init__` y herencia.

Al crear cada instancia se ejecuta `__init__`. Ahí reside el código importante para la creación de una instancia nueva. Si redefinís `__init__` siempre incluí un llamado al método `__init__` de la clase base para inicializarla también.

```python
class Cajon:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

class MiCajon(Cajon):
    def __init__(self, nombre, cantidad, precio, factor):
        # Fijate como es el llamado a `super().__init__()`
        super().__init__(name, cajones, precio)
        self.factor = factor

    def cost(self):
        return self.factor * super().precio()
```
Es necesario llamar al método `__init__()` en la clase base, es una forma de ejecutar la versión previa (vieja) del método que estamos redefiniendo, como mostramos recién.

### Usos de herencia

Uno de los usos de hacer una clase por herencia de otra es organizar objetos que están relacionados.

```python
class FiguraGeom:
    ...

class Circulo(FiguraGeom):
    ...

class Rectangulo(FiguraGeom):
    ...
```

Imaginate por ejemplo su uso en una jerarquía lógica, o taxonomica, en la que las clases tienen una relación natural tal que hace intuitivo derivar una de otra. 

Una aplicación mas común, y tal vez mas práctica, consiste en escribir código que es reusable y/o extensible. Podríamos definir una clase base para una interfase de transferencia de datos y permitir que cada fabricante de equipo de adquisición de datos implemente los detalles de comunicación con cada interfase en particular.

```python
class Procesador_de_datos(TCPHandler):
    def procesar_pedido(self):
        ...
        # Procesamiento de datos
```

La clase base contiene código de administración no específico. Cada clase hereda ese código y modifica las partes necesarias.

### Relación "es un"

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

*Importante: Idealmente, todo código que funcione con instancias de una clase base debería tambien funcionar con instancias de las clases derivadas de ella.*

### La clase base `object` 

Si una clase no tiene superclase, a veces se escribe  `object` como clase base.

```python
class Figura_geom(object):
    ...
```

`object` es la superclase de todo objeto en Python.

### Herencia múltiple.

Podés heredar un objeto de varias clases simultáneamente si los especificás en la definición de clase.

```python
class Madre:
    ...

class Padre:
    ...

class Hijo(Madre, Padre):
    ...
```

La clase `Hijo` hereda características de ambos padres. Algunos detalles son un poco delicados y no vamos a usar esa forma de heredar clases en este curso, aunque vas a encontrar un poco mas de información en la próxima sección.


## Ejercicios

El concepto de herencia es especialmente útil cuando uno está escribiendo código que va a ser extendido o adaptado, ya sea en bibliotecas o grandes sistemas configurables, pero también en pequeños paquetes de procesamiento de datos que pueden adquirir datos de diversas fuentes. Uno puede escribir las relaciones y comportamientos fundamentales y dejar los detalles de implementación de cada interfase cuando sean necesarios.


[oski]: # (Necesitamos darle una pasada a todo el texto y homogeneizar "name, cajones, precio, change")

```python
def imprimir_informe(informedata):
    '''
    Imprime una tabla prolija desde una lista de tuplas con (nombre, cantidad, precio, diferencia) 
    '''
    headers = ('Nombre','Cantidad','Precio','Diferencia')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10 + ' ')*len(headers))
    for row in informedata:
        print('%10s %10d %10.2f %10.2f' % row)
```

Al ejecutar tu programa `imprimir_informe()` la salida es algo parecido a esto: 

```python
>>> import informe
>>> informe.informe_camion('Data/camion.csv', 'Data/precios.csv')
      Name    Cajones     Precio Diferencia
---------- ---------- ---------- ----------
      Lima        100       9.22     -22.98
   Naranja         50     106.28      15.18
     Caqui        150      35.46     -47.98
 Mandarina        200      20.89     -30.34
   Durazno         95      13.48     -26.89
 Mandarina         50      20.89     -44.21
   Naranja        100     106.28      35.84
```

[oski]: # (no me gusta esta traducción : extensibility --> extenbsibilidad, pero no encuentro otra)

### Ejercicio 8.5: Un problema en extensibilidad
Imaginá que necesitás que la función `imprimir_informe()` pueda exportar el informe en una variedad de formatos. Texto simple, HTML, CSV ó XML. Podrías escribir una función enorme que resuelva todos los casos, pero resultaría en código repetido, y difícil de mantener. Esta es una oportunidad perfecta para usar herencia de objetos.

Vamos a enfocarnos en los pasos necesarios para crear una tabla. 

Al principio de la tabla tenemos los encabezados de las columnas. Después de éso, los datos de la tabla ordenados en una fila por ítem. Pongamos cada uno de esos pasos en una clase distinta. Creá un archivo llamado `formatotabla.py` y definí la siguiente clase:

```python
# formatotabla.py

class FormatoTabla:
    def headings(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
	raise NotImplementedError()

    def row(self, rowdata):
        '''
        Crear una única fila de datos de la tabla.
        '''
	raise NotImplementedError()
```

Por ahora la clase no hace nada, pero sirve como una especie de especificación de diseño para otras clases que vamos a definir. Una clase como ésta es a menudo llamada "clase abstracta base"

Ahora es necesario modificar la función `imprimir_informe` para que acepte como fuente de datos un objeto `formato_tabla` e invoque los métodos de este objeto para producir la tabla de salida. Algo así:

```python
# informe.py
...

def print_informe(informedata, formatter):
    '''
    Imprime una tabla prolija desde una lista de tuplas con (nombre, cantidad, precio, diferencia) 
    '''
    formatter.headings(['Nombre','Cantidad','Precio','Diferencia'])
    for name, cantidad, precio, diferencia in informedata:
        rowdata = [ name, str(cantidad), f'{precio:0.2f}', f'{diferencia:0.2f}' ]
        formatter.row(rowdata)
```

Como agregaste un argumento a `imprimir_informe()`, hay que modificar  también `informe_camion()`. Cambialo para que cree un objeto `
tableformatter` de este modo:

```python
# informe.py

import tableformat

...
def informe_camion(camionfile, preciofile):
    '''
    Crea un informe por camion a partir de archivos camion y precio.
    '''
    # Leer archivos con datos
    camion = leer_camion(camionfile)
    precios = read_precios(preciofile)

    # Crear los datos del informe
    informe = make_informe_data(camion, precios)

    # Generar informe
    formatter = tableformat.TableFormatter()
    print_informe(informe, formatter)
```

Ejecutá ese código:

```python
>>> ================================ RESTART ================================
>>> import informe
>>> informe.informe_camion('Data/camion.csv', 'Data/precios.csv')
... crashes ...
```

Debería dar inmediatamente una excepción de tipo `NotImplementedError`. No es nada maravilloso, pero es exactamente lo que esperábamos que sucediera, no ?   Sigamos...


### Ejercicio 8.6: Usemos herencia para cambiar la salida
La clase FormatoTabla que definiste en la primera parte es sólo la base de un sistema extensible. Este es el momento de extenderla. Definí una clase `FormatoTablaTXT` como sigue:

```python
# formatotabla.py
...
class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()
```

Modificá la función `informe_camion()` y probála: 

```python
# informe.py
...
def informe_camion(camionfile, preciofile):
    '''
    Crea un informe por camion a partir de archivos camion y precio.
    '''
    # Leer archivos con datos
    camion = leer_camion(camionfile)
    precios = leer_precios(preciofile)

    # Obtener los datos para un informe
    informe = make_informe_data(camion, precios)

    # Imprimir
    formatter = tableformat.TextTableFormatter()
    print_informe(informe, formatter)
```

Este código debería dar la misma salida que antes:

```python
>>> ========================REINICIAR INTERPRETE========================
>>> import informe
>>> informe.informe_camion('Data/camion.csv', 'Data/precios.csv')
    Nombre   Cantidad     Precio Diferencia
---------- ---------- ---------- ----------
      Lima        100       9.22     -22.98
   Naranja         50     106.28      15.18
     Caqui        150      35.46     -47.98
 Mandarina        200      20.89     -30.34
   Durazno         95      13.48     -26.89
 Mandarina         50      20.89     -44.21
   Naranja        100     106.28      35.84
>>>
```

Entonces cambiemos la salida a alguna otra cosa: Definí una nueva clase llamada `FormatoTablaCSV` que genere la salida en formato CSV:

```python
# formatotabla.py
...
class CSVTableFormatter(TableFormatter):
    '''
    Generar una tabla en formato CSV
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))
```

Modificá tu programa principal e este modo:

```python
def informe_camion(camionfile, preciofile):
    '''
    Crea un informe por camion a partir de archivos camion y precio.
    '''
    # Leer archivos con datos
    camion = leer_camion(camionfile)
    precios = read_precios(preciofile)

    # Obtener los datos para un informe
    informe = make_informe_data(camion, precios)

    # Imprimir
    formatter = tableformat.CSVTableFormatter()
    print_informe(informe, formatter)
```

Ahora la salida debería tener este aspecto:

```python
>>> ========================REINICIAR INTERPRETE========================
>>> import informe
>>> informe.informe_camion('Data/camion.csv', 'Data/precios.csv')
Nombre,Cantidad,Precio,Diferencia
Lima,100,9.22,-22.98
Naranja,50,106.28,15.18
Caqui,150,35.46,-47.98
Mandarina,200,20.89,-30.34
Durazno,95,13.48,-26.89
Mandarina,50,20.89,-44.21
Naranja,100,106.28,35.84
```

Usando las mismas ideas creá un objeto llamado `FormatoTablaHTML` que produzca un tabla de la siguiente forma:

```
<tr><th>Nombre</th><th>Cajones</th><th>Precio</th><th>Diferencia</th></tr>
<tr><td>Lima</td><td>100</td><td>9.22</td><td>-22.98</td></tr>
<tr><td>Naranja</td><td>50</td><td>106.28</td><td>15.18</td></tr>
<tr><td>Caqui</td><td>150</td><td>35.46</td><td>-47.98</td></tr>
<tr><td>Mandarina</td><td>200</td><td>20.89</td><td>-30.34</td></tr>
<tr><td>Durazno</td><td>95</td><td>13.48</td><td>-26.89</td></tr>
<tr><td>Mandarina</td><td>50</td><td>20.89</td><td>-44.21</td></tr>
<tr><td>Naranja</td><td>100</td><td>106.28</td><td>35.84</td></tr>
```

Para testear tu código, modificá el programa principal de modo que use un objeto de la clase `FormatoTablaHTML` en lugar de uno de la clase `FormatoTablaCSV` para darle formato a la tabla de salida. Fijate lo fácil que es cambiar el comportamiento de un programa cuando tenés objetos que son compatibles entre sí.

### Ejercicio 8.7: Polimorfismo en acción
Una de las grandes ventajas de la programación orientada a objetos es que podés cambiar un objeto por otro compatible y tu programa va a funcionar sin necesidad adaptar el código que usa esos objetos.

Si escribiste un programa diseñado para usar un objeto de la clase `FormatoTabla`, va a funcionar sin importar *que* objeto de esa clase uses. A este comportamiento particular, y la capacidad de usar la misma interfase con diferentes objetos de la misma clase, haciendo que el programa como un todo se porte distinto se lo llama polimorfismo.

Un problema potencial de usar polimorfismo en tus programas es diseñar un buen método para que el usuario final pueda decidir que objeto usar. No podés pedirle que reprograme tu código y cambie objetos o hablarle de los objetos por su nombre real, sería poco práctico. Lo que uno suele hacer es usar un `if` y permitir que el programa use diferentes objetos en base a decisiones del usuario, algo como esto:

```python
def informe_camion(camionfile, preciofile, fmt='txt'):
    '''
    Crea un informe por camion a partir de archivos camion y precio.
    '''
    # Leer archivos con datos
    camion = leer_camion(camionfile)
    precios = read_precios(preciofile)

    # Obtener los datos para un informe
    informe = make_informe_data(camion, precios)

    # Print it out
    if fmt == 'txt':
        formatter = tableformat.TextTableFormatter()
    elif fmt == 'csv':
        formatter = tableformat.CSVTableFormatter()
    elif fmt == 'html':
        formatter = tableformat.HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {fmt}')
    print_informe(informe, formatter)
```

In this code, the user specifies a simplified name such as `'txt'` or
`'csv'` to pick a format.  However, is putting a big `if`-statement in
the `informe_camion()` function like that the best idea?  It might
be better to move that code to a general purpose function somewhere
else.

In the `tableformat.py` file, add a function `create_formatter(name)`
that allows a user to create a formatter given an output name such as
`'txt'`, `'csv'`, or `'html'`.  Modify `informe_camion()` so that it
looks like this:

```python
def informe_camion(camionfile, preciofile, fmt='txt'):
    '''
    Crea un informe por camion a partir de archivos camion y precio.
    '''
    # Read data files
    camion = leer_camion(camionfile)
    precios = read_precios(preciofile)

    # Create the informe data
    informe = make_informe_data(camion, precios)

    # Imprimir
    formatter = tableformat.create_formatter(fmt)
    print_informe(informe, formatter)
```

Acordate de testear todas las ramas posibles del código para asegurarte de que está funcionando. Llamalo y pedile crear salidas en todos los formatos (podés ver el HTML con un webbrowser).

### Ejercicio 8.8: Volvamos a armar todo
Modificá tu programa `informe.py` de modo que la función `informe_camion()` acepte un parámetro opcionar que especifique el formato de salida deseado. Por ejemplo:

```python
>>> informe.informe_camion('Data/camion.csv', 'Data/precios.csv', 'txt')
    Nombre   Cantidad     Precio Diferencia
---------- ---------- ---------- ----------
      Lima        100       9.22     -22.98
   Naranja         50     106.28      15.18
     Caqui        150      35.46     -47.98
 Mandarina        200      20.89     -30.34
   Durazno         95      13.48     -26.89
 Mandarina         50      20.89     -44.21
   Naranja        100     106.28      35.84
>>>
```

Modificá el prgrama principal y usá `sys.argv()` para poder pedirle un formato particular directamente desde la línea de comandos (notá el último parámetro en este ejemplo):

```bash
bash $ python3 informe.py Data/camion.csv Data/precios.csv csv
Name,Cajons,Price,Change
Lima,100,9.22,-22.98
Naranja,50,106.28,15.18
Caqui,150,35.46,-47.98
Mandarina,200,20.89,-30.34
Durazno,95,13.48,-26.89
Mandarina,50,20.89,-44.21
Naranja,100,106.28,35.84
bash $
```

### Discusión

El caso que vimos es un ejemplo de uno de los usos mas comunes de herencia en programación orientada a objetos: escribir programas extensibles. Un sistema puede definir una interfase mediante una superclase base, y pedirte que escribas tus propias implementaciones derivadas de esa clase. Si escribis los métodos específicos para tu caso particular podes adaptar la función de un sistema general para resolver tu problema. 

Otro concepto, un poco mas interesante, es el de crear tus propias abstracciones. En los ejercicios de esta parte definimos *nuestra propia clase* para crear variaciones en el formato de un informe.

Tal vez estés diciendo "Debería usar una biblioteca para crear formatos ya escrita por otro !". Bueno, no. Deberías usar *tanto* tu propia clase *como* una biblioteca ya escrita. El hecho de usar tu propia clase te dá flexibilidad. 

Siempre que tu programa adhiera a la interfase de objetos definida por tu clase, podés cambiar la implementación interna en los objetos que escribas para que funcionen del modo que elijas. Podés escribir todo el código vos mismo ó usar bibliotecas escritas por otro, no importa. Cuando encuentres algo mejor, cambiás un código de terceros por el nuevo. Si la interfase está bien escrita no necesitas modificar el programa que usa las diferentes implementaciones. Simplemente funcionan si cumplen los contratos de la interfase. Es algo muy util y es una de los motivos por los que usar herencia puede resolverte los problemas de extensibilidad y diversidad a futuro.

Dicho esto, es cierto que diseñar un programa orientado a objetos puede volverse algo muy difícil. Si vas a encarar un proyecto grande con esta herramienta tal vez debieras consultar material específico sobre el diseño de estos sistemas. De todos modos, haber entendido lo que acabamos de hacer te va a servir para llegar bastante lejos.



[Contenidos](../Contenidos.md) \| [Anterior (3 Clases***)](03_Clases.md) \| [Próximo (5 Métodos especiales)](05_Métodos_Especiales.md)

