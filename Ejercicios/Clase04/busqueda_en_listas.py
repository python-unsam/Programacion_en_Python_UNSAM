# busqueda_en_listas.py


# %% Ejercicio 4.3: Búsquedas de un elemento
def buscar_u_elemento(lista: list, elemento):
    ultima_posicion = -1
    for posicion, elemento_lista in enumerate(lista):
        if elemento_lista == elemento:
            ultima_posicion = posicion
    return ultima_posicion


def buscar_n_elemento(lista: list, elemento):
    cantidad_elemento = 0
    for elemento_lista in lista:
        if elemento_lista == elemento:
            cantidad_elemento += 1
    return cantidad_elemento


assert buscar_u_elemento([1, 2, 4], 3) == -1
assert buscar_u_elemento([1, 2, 3, 4], 3) == 2
assert buscar_u_elemento([1, 2, 3, 3, 4, 5, 6, 7, 3, 8, 9], 3) == 8
assert buscar_u_elemento([], 3) == -1
assert buscar_n_elemento([2, 2, 2, 2], 2) == 4
assert buscar_n_elemento([], 2) == 0
assert buscar_n_elemento([2, 2, 2, 2], 3) == 0

# %% Ejercicio 4.4: Búsqueda de máximo y mínimo
import math


def maximo(lista: list) -> int:
    maximo_elemento = -math.inf
    for elemento_lista in lista:
        if elemento_lista > maximo_elemento:
            maximo_elemento = elemento_lista
    return maximo_elemento


assert maximo([1, 2, 7, 2, 3, 4]) == 7
assert maximo([1, 2, 3, 4]) == 4
assert maximo([-5, 4]) == 4
assert maximo([-5, -4]) == -4
assert maximo([-math.inf, -math.inf]) == -math.inf
