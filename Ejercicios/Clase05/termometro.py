#%% modulos
import random
from collections import Counter
import numpy as np

# termometro.py
# %% 5.6 gaussiana 

def medir_temp(n):
    return [37.5+random.normalvariate(0,0.2) for i in range(n)]

def mediana(lista):
    ordenada = lista.copy()
    ordenada.sort()
    if len(lista)%2 != 0:
        return ordenada[len(ordenada)//2]
    else:
        return (ordenada[(len(ordenada)-1)//2] + ordenada[((len(ordenada)-1)//2)+1])/2

def resumen_temp(n):
    mediciones = medir_temp(n)
    return (max(mediciones),min(mediciones),sum(mediciones)/n, mediana(mediciones))
# %% Ejercicio 5.8: Guardar temperaturas

data = '/home/sebastian/coding/Programacion_en_Python_UNSAM/Ejercicios/Data'

def medir_temp(n, path):
    mediciones = np.array([37.5+random.normalvariate(0,0.2) for i in range(n)])
    np.save(path+'/temperaturas.npy', mediciones)
    return mediciones