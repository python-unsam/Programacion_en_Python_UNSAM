[Contenidos](../Contenidos.md) \| [Próximo (2 Un primer programa)](02_Hello_world.md)

# 1.1 Python

### ¿Qué es Python?

Python es un lenguaje interpretado de alto nivel. Frecuentemente se lo clasifica como lenguaje de ["scripting"](https://es.wikipedia.org/wiki/Script). La sintaxis del Python tiene elementos de lenguaje C de programación.

Python fue creado por Guido van Rossum a principios de la década del '90 y lo nombró así en honor de  Monty Python.

### ¿Dónde conseguir Python?

Te recomendamos instalar Python 3.6 o más nuevo. En la documentación previa  hablamos sobre [cómo instalar Python para este curso](../../Notas/Instalacion.md).

### ¿Para qué fue creado Python?

El objetivo original de su autor fue crear un lenguaje de programación con el que pudiera realizar las tareas de administración de un sistema fácilmente. En algún sentido los scripts de la terminal no eran suficientemente poderosos y programar esas tareas en C resultaba demasiado tedioso. Python fue creado para llenar ese hueco en el medio.

### ¿Cómo ejecuto Python en mi máquina?

Existen diferentes entornos en los que podés correr Python en tu computadora. Es importante saber que Python está instalado normalmente como un programa que se ejecuta desde la consola. Desde la terminal deberías poder ejecutar `python` así:

```
bash $ python
Python 3.8.1 (default, Feb 20 2020, 09:29:22)
[Clang 10.0.0 (clang-1000.10.44.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print("hello world")
hello world
>>>
```

Si es la primera vez que ves una consola o terminal, sería conveniente que pares aquí, leas [un tutorial corto](https://tutorial.djangogirls.org/es/intro_to_command_line/) sobre cómo usar la consola de tu sistema operativo y luego vuelvas para seguir leyendo.

Existen diversos entornos fuera de la terminal en los que se puede escribir y ejecutar código Python. Pero para nosotros es importante que primero aprendas a usarlo desde la terminal: si lo sabés usar bien desde la terminal (que es su entorno natural) lo podrás usar en cualquier otro entorno. Ya en la próxima clase usarás Python dentro de un entorno de desarrollo. Por ahora, te recomendamos usarlo de esta manera que  acabamos de explicar.

## Ejercicios

### Ejercicio 1.1: Python como  calculadora
En tu máquina, iniciá Python y usalo como calculadora para resolver el siguiente problema:

* ¿Cuántas horas son 105 minutos?
* ¿Cuántos kilómetros son 20 millas? (un kilómetro corresponde a 0,6214 millas)



```python
>>> 105/60
1.75
>>> 20 / 0.6214
32.1853878339234
```

tip: Usá el guión bajo (underscore, \_) para referirte al resultado del último cálculo.

* Si alguien corre una carrera de 20 millas en 105 minutos, ¿cuál fue tu velocidad promedio en km/h?

```python
>>> _/1.75
18.391650190813372
```

### Ejercicio 1.2: Obtener ayuda
Ver [Ejercicio 1.1](../01_Introduccion/01_Python.md#ejercicio-11-python-como-calculadora) y  [Ejercicio 1.2](../01_Introduccion/01_Python.md#ejercicio-12-obtener-ayuda) y [Sección 1.1](../01_Introduccion/01_Python.md#dónde-conseguir-python)


Usá el comando `help()` para obtener ayuda sobre la función  `abs()`. Luego, usá el `help()` para obtener la ayuda sobre la función `round()`. Tipeá `help()` sólo para entrar en la ayuda en modo  interactivo.

El `help()` no funciona con los comandos básicos de Python como`for`, `if`, `while`, etc. Si tipeás `help(for)` vas a obtener un error. Podés probar usando comillas como en  `help("for")`, en algunos entornos funciona bien. Si no, siempre podés hacer una búsqueda en internet. 

La documentación oficial en inglés de Python se encuentra en <http://docs.python.org>. Por ejemplo, encontrá ahí la documentación sobre la función `abs()` (ayuda: está dentro de "library reference" y relacionado a las "built-in functions").

### Ejercicio 1.3: Copy-paste
Este curso está estructurado como una serie de páginas web tradicionales en las que los incentivamos a probar interactivamente fragmentos de código en sus intérpretes de Python **escribiéndolos a mano**. Si estás aprendiendo Python por primera vez, esta forma "lenta" de hacer las cosas es la que recomendamos. Vas a entender mejor yendo lento y escribiendo los comandos vos mismo mientras pensás en lo que estás tipeando.

Es importante que tipées los comandos a mano. Para usar copy-paste quizás mejor ni hacerlos. Parte del objetivo de los ejercicios es entrenar tus manos, tus ojos y tu cabeza en leer, escribir y mirar código tal como dice [Zed Shaw en su libro](https://learntocodetogether.com/learn-python-the-hard-way-free-ebook-download/). Usar copy-paste excesivamente es como hacerte trampa a vos misme. Es como tratar de aprender a tocar la guitarra escuchando discos: es probable que no aprendas nunca.

Si en algún momento necesitás hacer "copy-paste" de fragmentos de código, seleccioná el código que viene luego del símbolo `>>>` y hasta la siguiente linea en blanco o el siguiente `>>>` (el que aparezca primero). Seleccioná "copy" en el navegador (Ctrl-C), andá al intérprete de Python y poné "paste" (Ctrl-V o Crtl-shift-V) para pegarlo. Para ejecutar el código es posible que tengas que apretar "Enter" luego de pegarlo.

Usá copy-paste para ejecutar los siguientes comandos:

```python
>>> 12 + 20
32
>>> (3 + 4
         + 5 + 6)
18
>>> for i in range(5):
        print(i)

0
1
2
3
4
>>>
```

Advertencia: No es posible pegar más de un comando de Python (comandos que aparecen luego del símbolo `>>>`) por vez en el entorno básico de Python.



[Contenidos](../Contenidos.md) \| [Próximo (2 Un primer programa)](02_Hello_world.md)

