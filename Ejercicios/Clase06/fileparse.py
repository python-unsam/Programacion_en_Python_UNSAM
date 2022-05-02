# fileparse.py
import csv


def parse_csv(nombre_archivo, select=None, types=None, has_headers=True):
    """
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    """
    with open(nombre_archivo) as f:
        registros = []

        filas = csv.reader(f)

        if not has_headers:
            for fila in filas:
                if not fila:
                    continue

                try:
                    if types:
                        if len(types) != len(fila):
                            print(
                            "ERROR: types list has different size than desired columns in file"
                            )
                            return 1
                        fila = [func(val) for func, val in zip(types, fila)]
                except:
                    print("ERROR: Incorrect type deffinition or the file DO have headers")

                registros.append(tuple([elemento for elemento in fila]))
            return registros

        encabezados = next(filas)

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []

        for fila in filas:
            if not fila:
                continue
            if indices:
                fila = [fila[index] for index in indices]

            try:

                if types:
                    if len(types) != len(fila):
                        print("ERROR: Types list has different size than desired columns in file")
                        return 1                
                    fila = [func(val) for func, val in zip(types, fila)]
            except:
                print("ERROR: Incorrect type deffinition")

            registro = dict(zip(encabezados, fila))
            registros.append(registro)

    return registros



