# %%
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
# %%
path_data = '/home/sebastian-chromebook/disco/Programacion_en_Python_UNSAM/Ejercicios/Data'
path_arbolado_lineal = os.path.join(
    path_data, 'arbolado-publico-lineal-2017-2018.csv')
path_arbolado_parques = os.path.join(
    path_data, 'arbolado-en-espacios-verdes.csv')

df_parques = pd.read_csv(path_arbolado_parques)
df_veredas = pd.read_csv(path_arbolado_lineal)


# %% Indexado de veredas
columnas = ['altura_arbol', 'diametro_altura_pecho']
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'].str.normalize(
    'NFKD').str.contains('tipuana tipu', case=False)].copy()
df_tipas_veredas = df_tipas_veredas[columnas]
# %% Indexado de parques
columnas_parques = ['altura_tot', 'diametro']
df_tipas_parques = df_parques[df_parques['nombre_cie'].str.normalize(
    'NFKD').str.contains('tipuana tipu', case=False)].copy()
df_tipas_parques = df_tipas_parques[columnas_parques]
# %%
df_tipas_veredas.rename(columns={
                        'altura_arbol': 'altura', 'diametro_altura_pecho': 'diametro'}, inplace=True)
df_tipas_parques.rename(columns={'altura_tot': 'altura'}, inplace=True)

# %%
df_tipas_parques.insert(2, 'ambiente', 'parque')
# %%
df_tipas_veredas.insert(2, 'ambiente', 'vereda')

# %%
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

# %%
df_tipas.boxplot('diametro', by='ambiente')

# %%
sns.boxplot(x='ambiente', y='altura', data=df_tipas)
plt.figure()
sns.boxplot(x='ambiente', y='diametro', data=df_tipas)
# %%
