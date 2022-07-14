#%% fileparse.py

#%% Imports
import csv
#%% 
def parse_csv(iterable, select=None, types=None, has_headers=True, silence_errors=False):
    """
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    """
    if select != None and has_headers == False:
        raise RuntimeError('Para seleccionar necesito encabezados.')

    filas = csv.reader(iterable)
    registros = []
    
    if not has_headers:
        for fila in filas:
            if not fila:
                continue
        
            if types:
                fila = [func(val) for func, val in zip(types, fila)]
            
            registros.append(tuple([elemento for elemento in fila]))
        return registros
    encabezados = next(filas)
    if select:
        indices = [encabezados.index(nombre_columna) for nombre_columna in select]
        encabezados = select
    else:
        indices = []
    for nro_fila,fila in enumerate(filas):
        try:
            if indices:
                fila = [fila[index] for index in indices]
            if types:
                fila = [func(val) for func, val in zip(types, fila)]
            registro = dict(zip(encabezados, fila))
            registros.append(registro)
        except Exception as motivo:
            if silence_errors:
                print(f'Fila {nro_fila}: No pude convertir {fila}')
                print(f'Fila {nro_fila}: Motivo: {motivo}')
    return registros


# %%
