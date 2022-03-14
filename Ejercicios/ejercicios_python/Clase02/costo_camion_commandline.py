from csv import reader
import sys

def costo_camion(file_path):
	with open(file_path,'rt') as file:
	    next(file)
	    csv = reader(file)
	    total_cost = 0.0
	    for line in csv:
	        total_cost += float(line[2])*int(line[1])
	    
	    return round(total_cost,2)


if len(sys.argv) == 2:
	nombre_archivo = sys.argv[1]
else:
	print('Argumento path_de_archivo faltante. Se utilizara "../Data/camion.csv" por defecto')
	nombre_archivo = '../Data/camion.csv'

print('Costo total', costo_camion(nombre_archivo))
