[Contenidos](../Contenidos.md) \| [Anterior (4 El album de Figuritas)](04_Figuritas.md) \| [Próximo (6 Cierre de la cuarta clase)](08_Cierre.md)

# 4.5 Gráficos del Arbolado porteño

## Ploteando datos reales

En esta sección retomamos el dataset del arbolado porteño para hacer algunos gráficos que nos permitan visualizar los datos.
Seguiremos trabajando en el archivo `arboles.py`.


```python
import os
os.path.join('Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles(nombre_archivo)
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas = medidas_de_especies(especies, arboleda)
```

### Ejercicio 4.26: Scatterplot

Usando lo generado en [Ejercicio 3.20](../03_Listas_y_Listas/06_Arboles2_LC.md#ejercicio-320-lista-de-altos-y-diámetros-de-jacarandá), pasarlo a un `np.array` y plotear con `plt.scatterplot()`


### Ejercicio 4.27: Hacer histogramas de altos especie

### Ejercicio 4.28: Hacer boxplots comparando altos de especies



[Contenidos](../Contenidos.md) \| [Anterior (4 El album de Figuritas)](04_Figuritas.md) \| [Próximo (6 Cierre de la cuarta clase)](08_Cierre.md)

