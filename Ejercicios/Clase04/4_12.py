#%% 4.12
import csv

path_data =  '/mnt/chromeos/removable/Disco/Programacion_en_Python_UNSAM/Ejercicios/Data'
types = [str,int,float]
with open(path_data+'/camion.csv') as archivo:
    filas = csv.reader(archivo)
    headers = next(filas)
    fila = next(filas)
    print(types[1](fila[1])**2)
    {name: func(val) for name, func, val in zip(headers,types,filas)}

# %%

