#%% 4.1
#def invertir_lista(lista):
#    '''Recibe una lista L y la develve invertida.'''
#    invertida = []
#    i = len(lista)
#    while i > 0:    # tomo el último elemento 
#        i = i-1
#        invertida.append (lista.pop(i))  # PASO CLAVE
#    return invertida
# 
# l = [1, 2, 3, 4, 5]    
# m = invertir_lista(l)
# print(f'Entrada {l}, Salida: {m}')
# %% 4.2
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion = []
    registro = {}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)

# %% Busqueda lineal 
def busqueda_lineal(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    return pos

# busqueda_en_listas.py

# %% Ejercicio 4.3: Búsquedas de un elemento
def buscar_u_elemento(lista:list, elemento):
    ultima_posicion = -1
    for posicion, elemento_lista in enumerate(lista):
        if elemento_lista == elemento:
            ultima_posicion = posicion
    return ultima_posicion

def buscar_n_elemento(lista:list, elemento):
    cantidad_elemento = 0
    for elemento_lista in lista:
        if elemento_lista == elemento:
            cantidad_elemento += 1
    return cantidad_elemento

assert buscar_u_elemento([1,2,4],3) == -1
assert buscar_u_elemento([1,2,3,4],3) == 2
assert buscar_u_elemento([1,2,3,3,4,5,6,7,3,8,9],3) == 8
assert buscar_u_elemento([],3) == -1
assert buscar_n_elemento([2,2,2,2],2) == 4
assert buscar_n_elemento([],2) == 0
assert buscar_n_elemento([2,2,2,2],3) == 0

# %% Ejercicio 4.4: Búsqueda de máximo y mínimo
import math 

def maximo(lista:list)->int:
    maximo_elemento = -math.inf
    for elemento_lista in lista:
        if elemento_lista > maximo_elemento:
            maximo_elemento = elemento_lista
    return maximo_elemento

assert maximo([1,2,7,2,3,4]) == 7
assert maximo([1,2,3,4]) == 4
assert maximo([-5,4]) == 4
assert maximo([-5,-4]) == -4
assert maximo([-math.inf,-math.inf]) == -math.inf

# invlista.py
# %% Ejercicio 4.5: Invertir una lista
def invertir_lista(lista):
    invertida = []
    for e in lista: # Recorro los indices de la lista de atras para adelante
        invertida.insert(0,e) #agrego el elemento e al principio de la lista invertida
    return invertida


# propaga.py
# %% Ejercicio 4.6: Propagación

def propagar(fosforos:list)->list:
    fosforos_propagados = fosforos
    for posicion, fosforo in enumerate(fosforos_propagados):
        if posicion == 0:
            if fosforo == 1 or fosforo == -1:
                continue
            if fosforo == 0 and (fosforos_propagados[posicion+1] == 1):
                fosforos_propagados[posicion] = 1

        elif posicion == len(fosforos)-1:
            if fosforo == 1 or fosforo == -1:
                continue
            if fosforo == 0 and fosforos_propagados[posicion-1] == 1:
                fosforos[posicion] = 1

        else:
            if fosforo == 1 or fosforo == -1:
                continue
            if fosforo == 0 and (fosforos_propagados[posicion-1] == 1 or fosforos_propagados[posicion+1] == 1):
                fosforos_propagados[posicion] = 1
    return fosforos_propagados

# %%

