# rebotes.py

altura = 100 # altura inicial de la pelota
rebotes = 0
tasa_decaimiento_altura = 3/5

while rebotes < 10:
    rebotes += 1
    altura *= tasa_decaimiento_altura
    print(rebotes, round(altura,4))
