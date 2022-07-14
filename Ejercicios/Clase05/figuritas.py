import random
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

# figuritas.py
# %% 5.10,11,12,13,14 crear

def crear_album(figus_total:int)->np.array:
    return np.zeros(figus_total)

def album_incompleto(album:np.array)->bool:
    return np.any(album < 1)

def comprar_figu(figu_total):
    return random.randint(0,figu_total-1)

def cantidad_de_compras(figus_total:int)->int:
    album = crear_album(figus_total)
    figus_compradas = 0
    while album_incompleto(album):
        album[comprar_figu(figus_total)] += 1
        figus_compradas += 1
    
    return figus_compradas

def experimento_figus(n_repeticiones,figus_total):
    simulacion = np.array([cantidad_de_compras(figus_total) for i in range(n_repeticiones)])
    return simulacion.mean()

experimento_figus(100,670)

#--------------------------------------
# Ejercicios con paquetes
# %% 5.17
def comprar_paquete(figus_total, figus_paquete):
    return [random.randint(0,figus_total-1) for i in range(figus_paquete)]

def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
    paquetes = 0
    while album_incompleto(album):
        np.put(album,comprar_paquete(figus_total,figus_paquete),1)
        paquetes += 1
    return paquetes

def experimento_figus_paquetes(n_repeticiones,figus_total,figus_paquete):
    simulacion = np.array([cuantos_paquetes(figus_total,figus_paquete) for i in range(n_repeticiones)])
    return simulacion.mean()

experimento_figus_paquetes(1000,670,5)

# %%
def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

figus_total = 670
figus_paquete = 5

plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()