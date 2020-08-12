[Contenidos](../Contenidos.md) \| [Anterior (5 Objetos)](05_Objetos.md) \| [Próximo (7 Cierre de la tercera clase)](07_Cierre.md)

# 3.6 Arbolado porteño y comprensión+

Seguimos aquí con el arbolado porteño. Vamos a plantear algunos ejercicios para hacer con la técnica de comprensión de listas introducida recientemente.


## Ejercicios

Seguimos trabajando con el archivo CSV de "[Arbolado en espacios verdes](https://data.buenosaires.gob.ar/dataset/arbolado-espacios-verdes)" que ya está en tu carpeta `Data`. Vamos a estudiar esta base de datos y responder algunas preguntas. Guardá los ejercicios de esta sección en un archivo `arboles2.py`.


### Ejercicio 3.14: Lectura de los árboles de un parque
Basándote en la función `leer_parque(nombre_archivo, parque)` del [Ejercicio 3.14](../03_Mas_Python/06_Arboles2.md#ejercicio-314-lectura-de-los-árboles-de-un-parque), escribí otra `leer_arboles(nombre_archivo)` que lea el archivo indicado y devuelva una **lista de diccionarios** con la información de todos los árboles. La función debe devolver, en una lista un diccionario con todos los datos por cada árbol del parque elegido (recordá que cada fila del csv es un árbol).

Vamos a llamar `arboleda` a esta lista.

### Ejercicio 3.15: Lista de altos de Jacarandá
Usando comprensión de listas y la variable `arboleda` podés por ejemplo armar la lista de los áltos de los árboles.

```python
H=[float(arbol['altura_tot']) for arbol in arbolado]
```

Usá los filtros (recordá la [Sección 3.4](../03_Mas_Python/04_Comprension_Listas.md#filtros)) para armar la lista de los altos de los Jacarnás solamente.

### Ejercicio 3.16: Lista de altos y diámetros de Jacarandá
En el ejercicio anterior usaste una sola linea para seleccionar los altos de los Jacarandás en parques porteños. Ahora te proponemos que armes una nueva lista que tenga pares (tuplas de longitud 2) conteniendo no solo el alto sino tambíen el diámetro de cada Jacarandá en la lista.

Esperamos que obtengas una lista similar a esta:
```
[(5.0, 10.0),
 (5.0, 10.0),
 ...
 (12.0, 25.0),
 ...
 (7.0, 97.0), 
 (8.0, 28.0), 
 (2.0, 30.0), 
 (3.0, 10.0), 
 (17.0, 40.0)]
```

### EXTENDER!

[Contenidos](../Contenidos.md) \| [Anterior (5 Objetos)](05_Objetos.md) \| [Próximo (7 Cierre de la tercera clase)](07_Cierre.md)

