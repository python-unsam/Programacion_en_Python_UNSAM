#%% modulos
import random
from collections import Counter

#%% 5.1 generala servida
def tirar(n_dados):
    return [random.randint(1, 6) for i in range(n_dados)]


def es_generala(tirada):
    return (
        tirada[0] == tirada[1]
        and tirada[1] == tirada[2]
        and tirada[2] == tirada[3]
        and tirada[3] == tirada[4]
    )


# %%
N = 1000000
G = sum([es_generala(tirar(5)) for i in range(N)])
prob = G / N
print(f"Tiré {N} veces, de las cuales {G} saqué generala servida.")
print(f"Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.")

# -----------------------------------------
# generala.py
# %% Ejercicio 5.2: Generala no necesariamente servida

def prob_generala(N: int) -> float:
    generalas = 0
    for i in range(N):
        tirada = tirar(5)
        if es_generala(tirada):
            generalas += 1
        else:
            primer_tiro = me_quedo_dados(tirada)
            segundo_tiro = tirar(5 - len(primer_tiro))
            if es_generala(primer_tiro + segundo_tiro):
                generalas += 1
    return round(generalas/N,3)


def me_quedo_dados(tirada: list):
    dados = Counter(tirada)
    mas_frecuente = dados.most_common(1)[0]
    numero = mas_frecuente[0]
    cantidad = mas_frecuente[1]
    return [numero] * cantidad


# %% extra

def prob_generala_extra(N: int) -> float:
    generalas = 0
    for i in range(N):
        tirada = tirar(5)
        if es_generala(tirada):
            generalas += 1
        else:
            primer_tiro = me_quedo_dados(tirada)
            if len(primer_tiro) == 1:
                if es_generala(tirar(5)):
                    generalas += 1
                    continue
                continue

            segundo_tiro = tirar(5 - len(primer_tiro))
            if es_generala(primer_tiro + segundo_tiro):
                generalas += 1
    return round(generalas/N,3)

p_2tiros_todos_los_dados = prob_generala_extra(100000)
p_2tiros_dejando_dado = prob_generala(1000000)
print(f'La P dejando 1 dados si todos distintos es: {p_2tiros_dejando_dado}')
print(f'La P volviendo a tirar todos los dados es: {p_2tiros_todos_los_dados}')

# ------------------------------------------------------------
# %% Ej 5.3: cocumpleaños

def grupo_personas(N):
    return [random.randint(1,365) for i in range(N)]

def prob_cocumpleaños(N, cantidad_personas):
    casos_favorables = 0
    for i in range(N):
        grupo = Counter(grupo_personas(cantidad_personas))
        if grupo.most_common(1)[0][1] > 1:
            casos_favorables += 1
    return casos_favorables/N
    

dos_de_treinta = prob_cocumpleaños(10000, 30)
print(f'La probabilidad de que 2 personas de 30 tengan el mismo cumpleaños es: {dos_de_treinta:.3f}')


# %%
for i in range(30,2,-1):
    probabilidad = prob_cocumpleaños(10000,i)
    print(f'personas {i}, probabilidad {probabilidad}')
    if probabilidad < 0.5:
        print(f'para que 2 cumplan el mismo dia tiene que haber mas de {i+1} personas')
        break
# -------------------------------------------------------
# envido.py
# %% Ejercicio 5.4: Envido
valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]

# Se asume un partido de 4 jugadores
def prov_envido_alto(N):
    frecuencia_31 = 0
    frecuencia_32 = 0
    frecuencia_33 = 0

    for i in range(N):
        mazo = naipes.copy()
        mano = []
        for i in range(4):
            jugador = random.sample(mazo, k=3)
            mano.append(jugador)
            for carta in jugador:
                mazo.remove(carta)

        for mano_jugador in mano:
            if envido(mano_jugador) == 31:
                frecuencia_31 += 1
            if envido(mano_jugador) == 32:
                frecuencia_32 += 1
            if envido(mano_jugador) == 33:
                frecuencia_33 += 1

    print(f'''
La probabilidad de que en una mano algun jugador tenga 33 de envido es: {frecuencia_33/N}
La probabilidad de que en una mano algun jugador tenga 32 de envido es: {frecuencia_32/N}
La probabilidad de que en una mano algun jugador tenga 31 de envido es: {frecuencia_31/N}
    ''')         


def envido(cartas_tupla):
    envidos_posibles = [0]
    cartas = [list(carta) for carta in cartas_tupla]
    
    # 10,11,12 valen 0 en el envido
    for carta in cartas:
        if carta[0] in [10,11,12]:
            carta[0] = 0

    for carta in cartas:
        for carta2 in cartas:
            if carta == carta2:
                continue
            if carta[1] == carta2[1]:
                envidos_posibles.append(carta[0]+carta2[0]+20)

    return(max(envidos_posibles))

prov_envido_alto(1000000)
# %%
import numpy as np
# -------------------------------------------------------------------
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

#-------------------------------------------------------
# Plotear temperaturas
# %% Ejercicio 5.9: Empezando a plotear

import matplotlib.pyplot as plt
def plotar_temperaturas():
    temperaturas = np.load('/home/sebastian/coding/Programacion_en_Python_UNSAM/Ejercicios/Data/temperaturas.npy')
    plt.hist(temperaturas,bins=15)
    plt.show()

plotar_temperaturas()
# ----------------------------------------------------------
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
# %%
