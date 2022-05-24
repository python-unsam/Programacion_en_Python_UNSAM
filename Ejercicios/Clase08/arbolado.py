#%%
import pandas as pd

# %%
data_path = '/home/sebastian/coding/Programacion_en_Python_UNSAM/Ejercicios/Data/arbolado-publico-lineal-2017-2018.csv'

df_lineal_crudo = pd.read_csv(data_path)

cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']

df_lineal = df_lineal_crudo[cols_sel]
# %%
df_lineal
(df_lineal['nombre_cientifico'].value_counts()).head(10)

# %%
especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
df_lineal_especies = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]
df_lineal_especies

df_lineal_seleccion = df_lineal_especies
# %%

df_lineal_especies.boxplot('diametro_altura_pecho', by = 'nombre_cientifico')


# %%
import seaborn as sns
sns.pairplot(data = df_lineal_seleccion[cols_sel], hue = 'nombre_cientifico')

# %%
