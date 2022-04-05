#%%
import csv

path_datos_arboles = '/mnt/chromeos/removable/Disco/Programacion_en_Python_UNSAM/Ejercicios/Data/arbolado-en-espacios-verdes.csv'
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

