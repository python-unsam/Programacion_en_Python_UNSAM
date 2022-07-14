import csv


def leer_camion(nombre_archivo: str) -> dict:
    camion = list()
    with open(nombre_archivo, 'rt') as archivo:
        archivo_csv = csv.reader(archivo)
        headers = next(archivo_csv)
        for nro_fila, renglon in enumerate(archivo_csv, start=1):
            # Es necesario que el renglon tenga contenido.
            if len(renglon) > 0:
                entrada_fruta = dict(zip(headers, renglon))
                # Se validan los datos en tipado
                try:
                    entrada_fruta['cajones'] = int(entrada_fruta['cajones'])
                    entrada_fruta['precio'] = float(entrada_fruta['precio'])
                except ValueError:
                    print(f'Fila {nro_fila}: No es interpretable: {renglon}')

                camion.append(entrada_fruta)

    return camion


def leer_precios(nombre_archivo: str) -> dict:
    # Precios no tiene encabezados, mantengo el mismo formato que en informe.py Porque va a ser hardcodeado de cualquier manera.
    precios = dict()
    with open(nombre_archivo, 'rt') as archivo:
        archivo_csv = csv.reader(archivo)
        for renglon in archivo_csv:
            if len(renglon) == 2:
                precios[renglon[0]] = float(renglon[1])
            # No me convence usar Try - Except puede traer bugs en el codigo, como por ejemplo
            # indexar un renglon erroneo, que tenga 3 entrdas. Con if tiene mas sentido y es menos probable que
            # aparezcan bugs. Tambien se podria validar los datos antes de introducirlos en el diccionario.

    return precios


def hacer_informe(cajones: list, precios: dict) -> list:
    tabla = list()
    for entrada in cajones:
        nombre_fruta = entrada['nombre']
        cajones = entrada['cajones']
        precio_venta = precios[entrada['nombre']]
        cambio = precio_venta - entrada['precio']
        tabla.append((nombre_fruta,cajones,precio_venta,cambio))
    return tabla



camion = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')
informe = hacer_informe(camion, precios)

headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')

def generar_encabezado(justificado:int, encabezado:tuple)->str:
    
    formato_encabezado = ''
    for titulo in encabezado:
        formato_encabezado += f'{titulo:>10s} '
    
    separador = ''
    for i in range(len(encabezado)):
        for i in range(justificado):
            separador += '-'
        separador += ' '

    print(formato_encabezado)
    print(separador)

generar_encabezado(10, headers)

for nombre, cajones, precio, cambio in informe:
        precio = '$'+str(round(precio,2))
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')