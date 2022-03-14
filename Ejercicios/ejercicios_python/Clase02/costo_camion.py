from csv import reader

def costo_camion(file_path):
	with open(file_path,'rt') as file:
	    next(file)
	    csv = reader(file)
	    total_cost = 0.0
	    for line in csv:
	        total_cost += float(line[2])*int(line[1])
	    
	    return round(total_cost,2)


print('Costo total', costo_camion('../Data/camion.csv'))
