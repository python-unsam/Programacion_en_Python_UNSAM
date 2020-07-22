[Contenidos](../Contenidos.md) \| [Próximo (2 Comprensión de listas)](02_List_comprehension.md)

# 3.1 El módulo collections

El módulo `collections` ofrece objetos útiles para manejar datos. En esta sección introducimos brevemente los contadores, que son solo una de las clases incluída en este módulo.

### Ejemplo: Contar cosas

Digamos que querés hacer una tabla con el total de cajones de cada fruta.

```python
camion = [
    ('Pera', 100, 490.1),
    ('Naranja', 50, 91.1),
    ('Caqui', 150, 83.44),
    ('Naranja', 100, 45.23),
    ('Pera', 75, 572.45),
    ('Lima', 50, 23.15)
]
```

Hay dos entradas de `Naranja` y dos de  `Pera` en esta lista. Estos cajones deben ser combinados juntos de alguna forma.

### Contadores

Solución: Usá un  `Counter` (contador).

```python
from collections import Counter
total_cajones = Counter()
for nombre, n_cajones, precio in camion:
    total_cajones[nombre] += n_cajones

total_cajones['Naranja']     # 150
```

## Ejercicios

En este ejercicio vas a probar contadores en un par de ejemplos simple. Cargá tu programa `reporte.py` y ejecutalo en el intperprete de forma de tener los datos del camión con cajones cargado en modo interactivo.

Podés usar el interprete desde la línea de comandos ejecutando:
```bash
bash % python3 -i reporte.py
```
O podés cargarlo en el Spyder y correrlo.


### Ejercicio 3.1: Contadores
Vamos a suar un contador (objeto `Counter`) para contar cajones de frutas. Probalo:

```python
>>> camion = leer_camion('Data/camion.csv')
>>> from collections import Counter
>>> tenencias = Counter()
>>> for s in camion:
        tenencias[s['nombre']] += s['cajones']

>>> tenencias
Counter({'Mandarina': 250, 'Naranja': 150, 'Caqui': 150, 'Lima': 100, 'Durazno': 95})
>>>
```

Observá que la entradas múltiples como `Mandarina`  y `Naranja` en `camion` se combinan en una sola entrada.

Podés usar el contador como un diccionario para recuperar valores individuales:

```python
>>> tenencias['Naranja']
150
>>> tenencias['Mandarina']
250
>>>
```

Podés listar las tres frutas con mayores tenenciasa:

```python
>>> # Get three most held cajones
>>> tenencias.most_common(3)
[('Mandarina', 250), ('Naranja', 150), ('Caqui', 150)]
>>>
```

Carguemos los datos de otro camión con cajones de fruta en un nuevo contador:

```python
>>> camion2 = leer_camion('Data/camion2.csv')
>>> tenencias2 = Counter()
>>> for s in camion2:
          tenencias2[s['nombre']] += s['cajones']

>>> tenencias2
Counter({'Frambuesa': 250, 'Durazno': 125, 'Lima': 50, 'Mandarina': 25})
>>>
```

Y finalmente combinemos las tenencias de ambos camiones con una operación simple:

```python
>>> tenencias
Counter({'Mandarina': 250, 'Naranja': 150, 'Caqui': 150, 'Lima': 100, 'Durazno': 95})
>>> tenencias2
Counter({'Frambuesa': 250, 'Durazno': 125, 'Lima': 50, 'Mandarina': 25})
>>> combinada = tenencias + tenencias2
>>> combinada
Counter({'Mandarina': 275, 'Frambuesa': 250, 'Durazno': 220, 'Lima': 150, 'Naranja': 150, 'Caqui': 150})
>>>
```

Esto es solo una pequeña muestra de lo que se puede hacer con contadores. El módulo  `collections` es muy poderoso pero meterse a ver sus detalles sería una distracición ahora. Sigamos con nuestro curso...

[Contenidos](../Contenidos.md) \| [Próximo (2 Comprensión de listas)](02_List_comprehension.md)

