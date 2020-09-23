[Contenidos](../Contenidos.md) \| [Anterior (4 Contratos: Especificación y Documentación)](04_Especificacion_y_Documentacion.md) \| [Próximo (6 La biblioteca matplotlib)](06_Matplotlib.md)

# 6.5 Estilos de codeo

## PEP 8 - La guía de estilo para Python

La comunidad de usuaries de Python ha adoptado una guía de estilo que facilita la lectura del código y la consistencia entre programas de distintos usuaries. Esta guía no es de seguimiento obligatorio, pero es altamente recomendable. El documento completo se denomina PEP 8 y está escrito originalmente en [inglés](https://www.python.org/dev/peps/pep-0008/), aunque hay alguna traducción al [castellano](http://recursospython.com/pep8es.pdf). 

A continuación presentamos un resumen con solo algunas recomendaciones.

### Indentación
Utilizar siempre 4 espacios y nunca mezclar tabuladores y espacios.

Si se continúa una línea hay dos opciones aceptables:

```python
# Correcto
# opción 1, indentar a la apertura del paréntesis:
foo = funcion_que_crea_bar(variable_1, variable2,
                           variable_3, variable_4)

# opcion 2, agregar 4 espacios:
foo = funcion_que_crea_bar(
    variable_1, variable2,
    variable_3)
```

```python
# Incorrecto, en cualquier lado.
foo = funcion_que_crea_bar(variable_1, variable2,
              variable_3)
```

### Tamaño máximo de línea
Las líneas deben limitarse a un máximo de 79 caracteres.

### Líneas en blanco
Separar las definiciones de las clases y funciones con dos líneas en blanco. Los métodos dentro de clases se separan con una línea en blanco. Se recomienda utilizar líneas en blanco para separar partes del código, por ejemplo dentro de una función, que realizan tareas diferenciadas.

### Imports
Los imports de distintos módulos deben estar en líneas diferentes:

```python
# Sí: 
import os
import sys
```

```python
# No:
import os, sys
```

Sí se pueden poner en una línea los elementos que se importan de un mismo módulo:

```python
from subprocess import Popen, PIPE
```

Los imports deben ponerse siempre al principio del archivo, justo después de los comentarios y de la documentación del archivo y antes de la definición de las variables globales y las constantes.

Los imports deben agruparse en el siguiente orden:

1. bibliotecas o módulos estándar. 
2. bibliotecas o módulos de terceros.
3. bibliotecas o módulos locales o propios.

Cada grupo de imports debe estar separado por una línea en blanco.

### Espacios en blanco en expresiones
Evitar espacios en blanco extra en:

Dentro de paréntesis, corchetes o llaves.
```python
# Sí: 
spam(ham[1], {eggs: 2})
```

```python
# No:  
spam( ham[ 1 ], { eggs: 2 })
```

Antes de una coma.
```python
# Sí: 
if x == 4: print x, y; x, y = y, x 
```

```python
# No: 
if x == 4 : print x , y ; x , y = y , x
```

Antes del paréntesis de una llamada a una función.
```python
# Sí: 
spam(1)
```

```python
# No, ese espacio es espantoso
spam (1)
```

Antes del corchete de un índice o clave.
```python
# Sí: 
dict['key'] = list[index]
```

```python
# No, ese espacio es igual de espantoso que el anterior
dict ['key'] = list [index]
```

Siempre separá los operadores binarios con un espacio simple a ambos lados: asignación (=), asignación aumentada (+=, -= , etc.), comparación (==, <, >, !=, <>, <=, >=, in, not in, is, is not), booleanos (and, or, not).

Usá espacios alrededor de operadores artiméticos:

```python
# Sí:
i = i + 1
submitted += 1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)
```

```python
# No:
i=i+1
submitted +=1
x = x*2 - 1 #no es recomendado pero a veces lo usamos
hypot2 = x*x + y*y
c = (a+b) * (a-b)
```



### Convenciones de nombres

Las convenciones de nombres en Python son un lío y probablemente nunca lograremos que todo sea consistente. Sin embargo, te damos algunas de las recomendaciones actuales sobre nombres. Los nuevos módulos deberían ser escritos respetándolos, aunque la consistencia interna es preferible para bibliotecas que ya tengan partes hechas...

### Estilos de nombres

Hay muchos estilos para nombrar variable, funciones, etc. Es útil reconocer qué estilo se está usando, independientemente de para qué se está usando.

Éstos son algunos estilos:

* b (una sola letra, en minúscula)
* B (una sola letra, en mayúscula)
* minusculas
* minusculas_con_guiones_bajos
* MAYUSCULAS
* MAYUSCULAS_CON_GUIONES_BAJOS
* PalabrasConMayusculas (también llamado estilo camello por las jorobas)
* mixedCase (difiere del camello en la inicial)
* Con_Mayusculas_Y_Guiones_Bajos (horrible!)

Se recomienda no usar acentos ni caracteres especiales de ningún tipo para evitar problemas de compatibilidadd. Los nombres de funciones y variables deberían estar escritos en minúsculas, eventualmente usando guiones bajos para mejorar la legibilidad. 

### Hay mucho más!

Esto es solo un breve resumen, mirá el [PEP 8](https://www.python.org/dev/peps/pep-0008/) para tener toda la información sobre estilo recomendado en Python.

## Zen de Pyhton

Ya que estamos hablando de los PEPs, queremos mencionar el PEP 20 (PEP viene de Python Enhancement Proposals), también conocido como el [Zen de Python](https://es.wikipedia.org/wiki/Zen_de_Python)

El Zen de Python es una colección de 20 principios de software que influyen en el diseño del lenguaje. El texto, que copiamos a continuación se puede encontrar en el sitio oficial de Python y también se incluye como sorpresa en  el intérprete de Python al escribir la instrucción `import this`.​

**Zen de Pyhton**

>Bello es mejor que feo.

>Explícito es mejor que implícito.

>Simple es mejor que complejo.

>Complejo es mejor que complicado.

>Plano es mejor que anidado.

>Espaciado es mejor que denso.

>La legibilidad es importante.

>Los casos especiales no son lo suficientemente especiales como para romper las reglas.

>Sin embargo la practicidad le gana a la pureza.

>Los errores nunca deberían pasar silenciosamente.

>A menos que se silencien explícitamente.

>Frente a la ambigüedad, evitá la tentación de adivinar.

>Debería haber una, y preferiblemente solo una, manera obvia de hacerlo.

>A pesar de que esa manera no sea obvia a menos que seas Holandés.

>Ahora es mejor que nunca.

>A pesar de que nunca es muchas veces mejor que *justo* ahora.

>Si la implementación es difícil de explicar, es una mala idea.

>Si la implementación es fácil de explicar, puede que sea una buena idea.

>Los espacios de nombres son una gran idea, ¡hagamos más de ellos!



[Contenidos](../Contenidos.md) \| [Anterior (4 Contratos: Especificación y Documentación)](04_Especificacion_y_Documentacion.md) \| [Próximo (6 La biblioteca matplotlib)](06_Matplotlib.md)

