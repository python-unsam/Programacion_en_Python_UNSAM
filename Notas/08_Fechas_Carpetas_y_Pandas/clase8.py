#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 10:04:23 2020

@author: rgrimson
"""


#%%
#Esta clase tiene 4 temas:
# 1) datetime
# 2) os y shutil
# 3) pandas
# 4) series temporales

#%%
########################
# PARTE 1 ### Fechas ###
########################

import datetime

fecha_y_hora = datetime.datetime.now()
print(fecha_y_hora)
repr(fecha_y_hora)

#%%
datetime.datetime(2020,9,21)
datetime.datetime(2020,9,21,12,30)
print(datetime.datetime(2020,9,21,12,30,45,10))


#%% Relación con strings

#imprimir como quiera
datetime.datetime.now().strftime('Son las %H horas, %M mintos, %S segundos')

#leer con formato
cadena_con_fecha= '21 September, 2021'
object_fecha = datetime.datetime.strptime(cadena_con_fecha, '%d %B, %Y')
print('objeto_fecha =', object_fecha)

#leer con formato
cadena_con_fecha= '2020 # 09 # 30'
object_fecha = datetime.datetime.strptime(cadena_con_fecha, '%Y # %m # %d')
print('objeto_fecha =', object_fecha)

#%%
#Atributos de la clase datetime
fecha_y_hora.year
fecha_y_hora.month
fecha_y_hora.day

# métodos de la clase datetime
#(año, semana, dia)
fecha_y_hora.isocalendar()
#el número de segundos transcurridos desde el primero de enero de 1970
fecha_y_hora.timestamp()  
#%%

#Time deltas
parcial_inicio = datetime.datetime(2020,9,16,14)
parcial_fin = datetime.datetime(2020,9,16,15,30)

duracion = parcial_fin - parcial_inicio
print(duracion)
repr(duracion)

duracion.total_seconds()


#%%
#######################
# PARTE 2 ### Files ###
#######################
#Archivos y directorios:
    
import os

print(os.getcwd())

os.mkdir("mi_dir") #creo 
os.chdir("mi_dir") #cambio de directrorio, relativo al actual
print(os.getcwd())

os.chdir("..")
os.rmdir("mi_dir") #borro el directorio, debe estar vacío
print(os.getcwd())

os.chdir(".")
print(os.getcwd())

#%%
os.listdir('Data')
os.listdir('./Data')

#%%

os.mkdir("mi_dir") #creo 
[n for n in os.listdir() if "mi_" in n]
os.rename("mi_dir", "mi_directorio")
[n for n in os.listdir() if "mi_" in n]
os.rmdir("mi_directorio") #borro


#%% mover un archivo

#lo llevo a otro directorio
os.rename("mi_modulo.py", "./Data/mi_modulo.py")
[n for n in os.listdir() if "mi_" in n]

#lo traigo de vuelta
os.rename("./Data/mi_modulo.py", "mi_modulo.py")
[n for n in os.listdir() if "mi_" in n]


#%%
#El módulo os de es bajo nivel
#El módulo shutil es de mas alto nivel y usa las primitivas de os

import shutil

os.mkdir("mi_dir") #creo 
shutil.copy("mi_modulo.py", "./mi_dir/mi_modulo.py")
os.rmdir("mi_dir") #da error, debe estar vacío

[n for n in os.listdir() if "mi_" in n]

shutil.rmtree("./mi_dir") #borra el subarbol, vacio o no (cuidado!)
[n for n in os.listdir() if "mi_" in n]

# Pasa algo análogo con el os.rename() vs el shutil.move()
# os es de bajo nivel, shutil de más alto nivel.
#%%
# el os.path.join
  
directorio = "ordenar\\imgs" #?
directorio = "ordenar/imgs" #?

directorio = os.path.join("ordenar","imgs")
os.listdir(directorio)

#%%
# el os.walk

import os
for root, dirs, files in os.walk("ordenar"):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))    

#%%    
########################
# PARTE 3 ### Pandas ###
########################
import pandas as pd
import os

directorio = 'Data'
archivo = 'arbolado-en-espacios-verdes.csv'
fname = os.path.join(directorio,archivo)
df = pd.read_csv(fname)

#%%
df

df.head()

df.columns

#%%

#vista
dg = df[['nombre_com','altura_tot', 'diametro', 'inclinacio']]
dg
dg.describe()

#%%
#listar los nombres
df['nombre_com'].unique()

#cuales son ombú?
df['nombre_com'] == 'Ombú'

#contarlos
(df['nombre_com'] == 'Ombú').sum()

#%%
#contar ejemplares
cant_ejemplares = df['nombre_com'].value_counts()
cant_ejemplares.head(10)

# mirá lo indices de los dataframes

#%%
#Filtros booleanos
#selecciono filas
df_jacarandas = df[df['nombre_com'] == 'Jacarandá']

#selecciono columnas
cols = ['altura_tot', 'diametro', 'inclinacio']
df_jacarandas = df_jacarandas[cols]

#miro
df_jacarandas.tail(10)
df_jacarandas.describe()

#copio si lo quiero modificar:
df_jacarandas = df[df['nombre_com'] == 'Jacarandá'][cols].copy()

#%%
#graficar en pandas
df_jacarandas.plot.scatter(x = 'diametro', y = 'altura_tot')

#%%
#metamos seaborn
import seaborn as sns

sns.scatterplot(data = df_jacarandas, x = 'diametro', y = 'altura_tot')

#%%
list(cant_ejemplares[1:4].index)
especies_seleccionadas = list(cant_ejemplares[1:4].index)
df_seleccion = df[df['nombre_com'].isin(especies_seleccionadas)]

sns.scatterplot(data = df_seleccion, x = 'diametro', y = 'altura_tot', hue = 'nombre_com',alpha=0.3)

#%%

#boxplots

df_seleccion.boxplot('diametro', by = 'nombre_com')

sns.boxplot(data = df_seleccion, y = 'diametro', x = 'nombre_com')
sns.boxplot(data = df_seleccion, y = 'altura_tot', x = 'nombre_com')


#%%

#pairplot
cols = ['altura_tot', 'diametro', 'nombre_com']
sns.pairplot(data = df_seleccion[cols], hue = 'nombre_com', hue_order=['Tipa blanca', 'Palo borracho rosado', 'Jacarandá', ])
sns.pairplot(data = df_seleccion[cols], hue = 'nombre_com', hue_order=['Tipa blanca', 'Jacarandá', 'Palo borracho rosado'])

#Ejercicio más exigente: comparar crecimiento entre veredas y parques para una misma especie.

#%%
########################
# PARTE 4 ### Series ###
########################

#mareas en el rio de la plata
import pandas as pd

df = pd.read_csv('Data/OBS_SHN_SF-BA.csv')

df.head()
df.index

#%%
#leo con fechas como indice
df = pd.read_csv('Data/OBS_SHN_SF-BA.csv', index_col=['Time'], parse_dates=True)
df.head()
df.index
#%%
# mirá como se puede seleccionar

df['1-18-2014 9:00':'1-18-2014 18:00']
df['12-25-2014':]
df['12-25-2014':].plot()


df['H_BA']['10-15-2014':'12-15-2014'].plot()

#Buscar desplazamientos horizontales y verticales.
# 1) A mano
# 2) Optativo: con fft, colaboración de O. Bruzzone.

# dos páginas sobre FFT: 
    # http://www.jezzamon.com/fourier/
    # https://musiclab.chromeexperiments.com/Spectrogram/