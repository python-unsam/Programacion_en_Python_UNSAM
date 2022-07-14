#%% Librerias importadas
from ast import increment_lineno
import csv
from collections import Counter

path_a_datos = '/home/sebastian/coding/Programacion_en_Python_UNSAM/Ejercicios/Data/arbolado-en-espacios-verdes.csv'


#%% Leer parque
def leer_parque(nombre_archivo:str, parque:str)-> list:
    arboles_parque = list()
    with open(nombre_archivo,'rt') as archivo:
        archivo_procesado = csv.reader(archivo)
        headers = next(archivo_procesado)
        # Busco indexar solamente el parque, para no tener
        # que iterar el diccionario.
        indice_esp_verde = headers.index('espacio_ve')
        for nro_fila, fila in enumerate(archivo_procesado):
            try:
                if fila[indice_esp_verde].lower() == parque.lower():
                    arboles_parque.append(dict(zip(headers,fila)))
            except:
                print(f'La fila {nro_fila} no pudo ser indexada.\n{fila}')

    return arboles_parque

#%% Especies
def especies(lista_arboles:list)->set:
    especies_set = set()
    for arbol in lista_arboles:
        especies_set.add(arbol['nombre_com'])
    return especies_set

# %% Contar ejemplares
def contar_ejemplares(lista_arboles:list())->dict:
    cantidad_arboles = Counter()
    for arbol in lista_arboles:
        cantidad_arboles[arbol.get('nombre_com')] += 1
    return cantidad_arboles

#%% Arboles mas comunes
def arboles_mas_comunes(nombre_archivo:str,parques:list)->str:
    ejemplares_parques = dict()
    for parque in parques:
        ejemplares = contar_ejemplares(leer_parque(nombre_archivo,parque))
        ejemplares_parques[parque] = ejemplares.most_common(5)

    titulo = ''
    for parque in parques:
        titulo += f'{parque:>25s}'
    print(titulo)

    separador = '-'*len(titulo)
    print(separador)

    for i in range(len(ejemplares_parques[parques[0]])):
        renglon = ''
        for parque in parques:
            ejemplar = ejemplares_parques[parque]
            entrada = f'{ejemplar[i][0]:>20.20s}:{ejemplar[i][1]:<5d}'
            renglon += f'{entrada:25s}'
        print(renglon)

arboles_mas_comunes(path_a_datos, ['GENERAL PAZ','ANDES, LOS','CENTENARIO'])

# %% Alturas de una especie
def obtener_alturas(lista_arboles, especie):
    alturas = []
    for arbol in lista_arboles:
        if arbol['nombre_com'].lower() == especie.lower():
            alturas.append(float(arbol['altura_tot']))
    return alturas

gral_paz = leer_parque(path_a_datos,'GENERAL PAZ')
los_andes = leer_parque(path_a_datos,'ANDES, LOS')
centenario = leer_parque(path_a_datos, 'CENTENARIO')

def summary_alturas(parque,especie):
    alturas = obtener_alturas(parque, especie)
    print(f'Medida Maxima: {max(alturas)}')
    print(f'Medida Promedio: {round(sum(alturas)/len(alturas),2)}')

print('General Paz	')
summary_alturas(gral_paz, 'jacarandá')
print('Los Andes')
summary_alturas(los_andes, 'jacarandá')
print('Centenario')
summary_alturas(centenario, 'jacarandá')


# %% 3.22 inclinaciones por especie
def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = []
    for arbol in lista_arboles:
        if arbol['nombre_com'].lower() == especie.lower():
            inclinaciones.append(float(arbol['inclinacio']))
    return inclinaciones



# %% 3.23: Especie con el ejemplar más inclinado

def especimen_mas_inclinado(lista_arboles):
    # No puedo usar especie() de ninguna manera logica, porque retorna un conjunto no una lista.
    # Se me ocurren algoritmos usandola pero son muy costosos, sin sentido, ya que 
    # tanto especie() como buscar inclinacion() iteran toda la tabla. Esta funcion como mucho
    # deberia recorrer la tabla 1 vez. 
    arbol_mas_inclinado = ''
    inclinacion = 0.0
    for arbol in lista_arboles:
        if float(arbol.get('inclinacio')) > inclinacion:
            inclinacion = float(arbol.get('inclinacio'))
            arbol_mas_inclinado = arbol.get('nombre_com')
    print(f'El arbol mas inclinado es {arbol_mas_inclinado} en {inclinacion}°')
    return (arbol_mas_inclinado, inclinacion)

# %%

def especie_promedio_mas_inclinada(lista_arboles):
    especies = list()
    for arbol in lista_arboles:
        especies.append(arbol['nombre_com'])

    especies_con_inclinacion = dict()

    for especie in especies:
        especies_con_inclinacion[especie] = obtener_inclinaciones(lista_arboles, especie)
    
    especie_prom_mas_inclinada = ''
    inclinacion_promedio = 0.0

    for especie in especies_con_inclinacion.keys():
        inclinaciones = especies_con_inclinacion[especie]
        promedio = sum(inclinaciones)/len(inclinaciones)
        if inclinacion_promedio < promedio:
            inclinacion_promedio = promedio
            especie_prom_mas_inclinada = especie
        
    print(f'La especie {especie_prom_mas_inclinada} tiene en promedio {inclinacion_promedio}° de inclinación, y es en promedio la mas inclinada del parque.')

    return (especie_prom_mas_inclinada,inclinacion_promedio)


