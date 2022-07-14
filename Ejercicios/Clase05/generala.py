# generala.py

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
    return round(generalas / N, 3)


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
    return round(generalas / N, 3)


p_2tiros_todos_los_dados = prob_generala_extra(100000)
p_2tiros_dejando_dado = prob_generala(1000000)
print(f"La P dejando 1 dados si todos distintos es: {p_2tiros_dejando_dado}")
print(f"La P volviendo a tirar todos los dados es: {p_2tiros_todos_los_dados}")
