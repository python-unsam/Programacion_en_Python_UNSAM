[Contenidos](../Contenidos.md) \| [Anterior (4 Más sobre generadores)](04_Mas_generadores.md) \| [Próximo (6 Cierre de la novena clase)](06_Cierre.md)

# 9.5 Predador Presa

Los modelos de depredación y competencia forman parte de la batería de herramientas clásicas del ecólogo. Vito Volterra en Italia y Alfred Lotka en Estados Unidos fueron los precursores en este tema y crearon modelos que, con diversas modificaciones y mejoras, seguimos usando hoy en día.
El modelo de Volterra para depredación comienza suponiendo la existencia de dos poblaciones de animales, una de las cuales (el depredador) se alimenta de la otra (la presa). Se supone que las dos poblaciones están formadas por individuos idénticos, mezclados en el espacio.

La gran mayoría de los modelos estudiados tienen en cuenta principalmente la dinámica temporal de estos sistemas.
Esta ejercicio tiene como objetivo implementar una versión diferente: intentaremos analizar tanto el aspecto temporal como espacial del modelo.

Se trata de un ejercicio optativo para entregar. La idea es recrear un mundo que imaginaremos como un valle rodeado de montañas en el que existen depredadores (que llamaremos Leones) y presas (que llamaremos Antílopes). Este valle será bidimensional, y lo representaremos por medio de una grilla rectangular que llamaremos tablero.

El modelo inicial con el que trabajaremos tiene definidas 4 etapas que determinan un ciclo:

- **Etapa de movimiento**: en esta etapa cada animal se desplaza a alguna posición vecina desocupada (si es que existe, sino permanece en el lugar). La decisión de a cuál desplazarse será responsabilidad del animal, que sabiendo las disponibles elegirá una al azar.

- **Etapa de alimentación**: en esta etapa los animales se alimentan. Los antílopes comerán pasto en su lugar, mientras que los leones buscarán un antílope en las posiciones vecinas y de existir se lo comerán. Esta acción de un león se verá reflejada en el tablero con su desplazamiento a la posición del antílope, el cual ya no será más parte de nuestro mundo.

- **Etapa de reproducción**: cada animal buscará en sus posiciones vecinas alguien de su misma especie. Si lo encuentra y además hay una posición vacía en el tablero se incluirá un nuevo animal (de la misma especie) en el tablero. Nuevamente la elección de la pareja y del lugar del nuevo animal serán aleatorias. Este modelo inicial no prevee el atributo sexo, ni un límite entre la cantidad reproducciones en las que puede participar un animal por etapa.

- **Etapa de envejecimiento**: en la última etapa de un ciclo todos los animales "envejecen" en 1 unidad. Si alguno alcanzó la edad máxima de su especie se considera que ya puede retirárselo del mundo (es decir, se muere). Sucede lo mismo si al pasar una etapa alcanza el límite de etapas sin alimentarse, en cuyo caso muere de hambre.

## Clases del modelo inicial:

* [Tablero](./includes/tablero.MD)
* [Animal, León, Antílope](./includes/animal.MD)
* [Mundo](./includes/mundo.MD)


### Ejercicio 9.17: 
Para empezar a explorar el modelo, se deberá completar todos los métodos que estén indicados con `pass`.

Agregar además cualquier método que consideres necesario para obtener información, o modelar algún comportamiento.

  1. Implementar el método `etapa_reproduccion` en la clase `Mundo`.

  1. Implementar la lógica necesaria para que los animales pueden reproducirse unicamente una vez por año (ya sean los que inician la reproducción o los que son compañeres)

  1. Implementar la lógica necesaria para que un animal sólo puede reproducirse cuando ya tiene 2 años cumplidos

  1. Implementar la lógica que hace que un animal, si se alimentó en la etapa actual no se alimente en la siguiente.


Una vez realizado esto hay diversas opciones para usarlo y expandirlo:

### Extensiones del modelo

A continuación una lista no exhaustiva de las extensiones posibles al modelo, podés incorporar algunas, o todas:

  - Ningún animal se puede reproducir antes de haber vivido 3 etapas

  - Ningún animal se alimenta o se reproduce más de una vez en una etapa

  - Si un animal se alimenta en una etapa, no necesita alimentarse más por un turno entero

  - Cuando un León ataca un Antílope, no siempre se lo come, a veces el Antílope logra escapar. Modelar esto con 3 posibles escenarios:

      - Existe una probabilidad p (fija), de que el León tenga éxito (con el módulo `random` se puede hacer `random.random() > p`)

      - La probabilidad es variable dependiendo de la edad del León, siendo muy baja cuando es cachorro, alta cuando es adulto, y baja de nuevo en su vejez.

      - La probabilidad es variable dependiendo de la edad del León, igual al anterror, y la edad del Antílope, siendo la probabilidad de que escape muy baja cuando es cachorro, alta cuando es adulto, y baja de nuevo en su vejez. Una forma de calcular esto es: ![\begin{align*}
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

