# invlista.py
# %% Ejercicio 4.5: Invertir una lista
def invertir_lista(lista):
    invertida = []
    for e in lista:  # Recorro los indices de la lista de atras para adelante
        invertida.insert(
            0, e)  #agrego el elemento e al principio de la lista invertida
    return invertida
