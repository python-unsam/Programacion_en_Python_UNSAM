
with open('../Data/camion.csv','rt') as file:
    next(file)
    total_cost = 0.0
    for line in file:
        line_parsed = line.split(',')
        line_parsed[1] = int(line_parsed[1])
        line_parsed[2] = float(line_parsed[2].lstrip('\n'))
        total_cost += line_parsed[2]
    print('Costo total', round(total_cost,2))
