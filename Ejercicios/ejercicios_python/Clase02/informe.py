import csv
from pprint import pprint

def leer_camion(nombre_archivo:str)->dict:
	camion = list()
	with open(nombre_archivo,'rt') as archivo:
		archivo_csv = csv.reader(archivo)
		headers = next(archivo_csv)
		for renglon in archivo_csv:
			camion.append({headers[0]:renglon[0],headers[1]:int(renglon[1]),headers[2]:float(renglon[2])})
	return camion	 

def leer_precios(nombre_archivo:str)->dict:
	precios = dict()
	with open(nombre_archivo,'rt') as archivo:
		archivo_csv = csv.reader(archivo)
		for renglon in archivo_csv:
			if len(renglon) == 2:
				precios[renglon[0]] = float(renglon[1])
			# No me convence usar Try - Except - Pass puede traer bugs en el codigo, como por ejemplo
			# indexar un renglon erroneo, que tenga 3 entrdas. Con if tiene mas sentido y es menos probable que
			# aparezcan bugs. Tambien se podria validar los datos antes de introducirlos en el diccionario.

	return precios	 

precios = leer_precios('../Data/precios.csv')
camion = leer_camion('../Data/camion.csv')

costo_camion = 0
venta = 0

for fruta in camion:
	cajones = fruta.get('cajones')
	precio_cajon = fruta.get('precio')
	venta_cajon = precios.get(fruta.get('nombre')) 
	costo_camion += cajones * precio_cajon
	venta += cajones * venta_cajon

print(f'Costo del camion: {round(costo_camion,2)}\nVentas recaudadas: {round(venta,2)}\nBalance: {round(venta - costo_camion,2)}')