# Ejercicio 1.18: Geringoso rústico

cadena = 'Geringoso'
capadepenapa = ''

for letra in cadena:
    if letra in ['a','e','i','o','u']:
        capadepenapa += letra + 'p' + letra
    else:
        capadepenapa += letra

print(capadepenapa)