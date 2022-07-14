#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
# Comentario: La funcion solo retorna el boleano respecto a la primera letra de la
# string. Lo corregi agregando una variable booleana false que se retorna por defecto
# en caso de que nunca se encuentre una a, y declare un break para que el loop se
# se corte al encontrar la letra a, asi no se continua iterando y perdiendo tiempo
# de corrida. Tambien es muy poco pythonica la manera en la que se escribio, 
# hay metodos como find() o index() para las strings que corren compilados 
# en el lenguaje base de python (creo que C) y por ende son mas rapidos.

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    tiene_letra_a = False
    while i<n:
        if expresion[i] == 'a':
            tiene_letra_a = True
            break
        i += 1
    return tiene_letra_a


#%%
# Ejercicio 3.2. Función tiene_a() no tenia ":" delimitando las operaciones, usaba '=' para
# definir una evaluacion (se usa "==") y tenia un error de tipeo en False. 

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False




#%%
# Ejercicio 3.3. Función tiene_uno() no convertia al argumento expresion en string
# por lo tanto no era una cadena iterable. Al convertior expresion a str corre como debe.

def tiene_uno(expresion):
    expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene

# %%
# Ejercicio 3.4 Alcances. La funcion no tenia retorno, entonces como esta buscandose usar no tenia
# sentido. La arregle generando que retorne a+b, de modo que se guarde en c como se buscaba.
# Si quisiera que la funcion modifique una variable por fuera de la funcion, la misma tiene que ser declarada
# previamente a que se ejecute la funcion, y dentro de la funcion deberia declarar la variable como global
# para luego modificarla.

def suma(a,b):
    return a+b

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")
# %%
# Ejercicio 3.5
# Al parecer, las listas no almacenan valores, sino pointers, por lo tanto append agregaba una y otra vez
# pointers al mismo registro, el cual modificabamos con todas las asignaciones. Por lo tanto
# la lista al final tenia el mismo diccionario repetido por cada fila, quedandose con la ultima fila.
# Entonces, para que esto no suceda, hice que se genere un diccionario nuevo por cada iteracion del for.

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('/home/sebastian-chromebook/disco/Programacion_en_Python_UNSAM/Ejercicios/Data/camion.csv')
pprint(camion)
# %%
