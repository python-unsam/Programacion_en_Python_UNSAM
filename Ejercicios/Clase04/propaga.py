
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
