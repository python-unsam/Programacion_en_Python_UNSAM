import csv

def costo_camion(nombre_archivo):
    costo_total = 0
    with open(nombre_archivo,'rt') as archivo:
        archivo_csv = csv.reader(archivo)
        headers = next(archivo_csv)
        for nro_fila, fila in enumerate(archivo_csv, start=1):
            registro = dict(zip(headers, fila))
            print(registro)
            try:
                costo_total += int(registro['cajones'])+float(registro['precio'])
            except ValueError:
                print(f'Fila {nro_fila}: No es interpretable: {fila}')
    print('Costo del camion: ', costo_total)
    return costo_total


def leer_camion(nombre_archivo:str)->dict:
	camion = list()
	with open(nombre_archivo,'rt') as archivo:
		archivo_csv = csv.reader(archivo)
		headers = next(archivo_csv)
		for nro_fila, renglon in enumerate(archivo_csv, start=1):
			# Es necesario que el renglon tenga contenido.
			if len(renglon) > 0:
				entrada_fruta = dict(zip(headers,renglon))
				# Se validan los datos en tipado
				try:
					entrada_fruta['cajones'] = int(entrada_fruta['cajones'])
					entrada_fruta['precio'] = float(entrada_fruta['precio'])
				except ValueError:
					print(f'Fila {nro_fila}: No es interpretable: {renglon}')
				
				camion.append(entrada_fruta)
			

	return camion	 

def leer_precios(nombre_archivo:str)->dict:
    # Precios no tiene encabezados, mantengo el mismo formato que en informe.py Porque va a ser hardcodeado de cualquier manera.
	precios = dict()
	with open(nombre_archivo,'rt') as archivo:
		archivo_csv = csv.reader(archivo)
		for renglon in archivo_csv:
			if len(renglon) == 2:
				precios[renglon[0]] = float(renglon[1])
			# No me convence usar Try - Except puede traer bugs en el codigo, como por ejemplo
			# indexar un renglon erroneo, que tenga 3 entrdas. Con if tiene mas sentido y es menos probable que
			# aparezcan bugs. Tambien se podria validar los datos antes de introducirlos en el diccionario.

	return precios	 

precios = leer_precios('../Data/precios.csv')
camion = leer_camion('../Data/fecha_camion.csv')

costo_camion_total= 0
venta = 0

for fruta in camion:
	cajones = fruta.get('cajones')
	precio_cajon = fruta.get('precio')
	venta_cajon = precios.get(fruta.get('nombre')) 
	costo_camion_total += cajones * precio_cajon
	venta += cajones * venta_cajon

print(f'Costo del camion: {round(costo_camion_total,2)}\nVentas recaudadas: {round(venta,2)}\nBalance: {round(venta - costo_camion_total,2)}')