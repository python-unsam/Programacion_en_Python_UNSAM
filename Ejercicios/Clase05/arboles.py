#%%
import csv

path_datos_arboles = '/home/sebastian/coding/Programacion_en_Python_UNSAM/Ejercicios/Data/arbolado-en-espacios-verdes.csv'
#%% 4.15 lectura de arboles
def leer_arboles(nombre_archivo:str)->list:
    with open(nombre_archivo,'rt') as archivo:
        archivo_csv = csv.reader(archivo)
        headers = next(archivo_csv)
        return [dict(zip(headers,data)) for data in archivo_csv]

# %% 4.16 lista de altos de jacaranda

arboleda = leer_arboles(path_datos_arboles)

altura_jacaranda = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']


# %% 4.17 lista de altos y diametros de jacaranda

altura_diametro_jacaranda = [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
# %% 4.18 diccionario con medidas

def medidas_de_especies(especies:list,arboleda:list)->dict:
    return {especie: [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie] for especie in especies}

# Testeos correspondientes
medidas = medidas_de_especies(['Eucalipto','Palo borracho rosado','Jacarandá'],arboleda)
assert len(medidas['Eucalipto']) == 4112
assert len(medidas['Palo borracho rosado']) == 3150
assert len(medidas['Jacarandá']) == 3255

#%% Ejercicio 5.25: Histograma de altos de Jacarandás

import os
import matplotlib.pyplot as plt
plt.hist(altura_jacaranda,bins=25)
# %% Ejercicio 5.26: Scatterplot (diámetro vs alto) de Jacarandás
import numpy as np
def scatter_hd(lista_de_pares):
    altura_diametro = np.array(lista_de_pares)
    plt.figure()
    plt.scatter(altura_diametro[:,0],altura_diametro[:,1],alpha=0.2)
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.xlim(0,30) 
    plt.ylim(0,100) 

scatter_hd(altura_diametro_jacaranda)
# %% Ejercicio 5.27: Scatterplot para diferentes especies
for nrofig, arbol in enumerate(medidas.keys()):
    scatter_hd(medidas.get(arbol))
    plt.title(f"Relación diámetro-alto para {arbol}")

# %%
