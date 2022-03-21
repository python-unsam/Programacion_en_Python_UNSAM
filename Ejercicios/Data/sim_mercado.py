# -*- coding: utf-8 -*-
'''
sim_mercado.py toma datos de "fruta", precio, volumen 
del archivo mcentral.csv
Genera un log de movimientos en mercadolog.csv
'''

import os
import time
import random

def leer_valores (filename):
    ''' 
    Arma una lista de productos a partir de filename
    Pera,1.22,10  --> nombre, precio, volumen
    '''
    
    prods=[]
    with open (filename, 'r') as f:
        for line in f:
            fields = line.split(',')
            nombre = fields[0].strip('"')
            precio = float(fields[1])
            volumen = int(fields[2])
            prods.append([nombre,precio,volumen])
    return prods        

def escribir_log(filename, prod):
    '''
    Escribe items de prod al azar con valores cambiados
    en filename 1 vez por segundo
    '''
    f= open(filename,'w')

    while True:
        p =random.choice(prod)
        nombre = p[0]
        precio = p[1] * random.normalvariate(p[1]*100,10)
        volumen= p[2] * random.randint(80, 120)
        out = f'"{nombre}", {precio:.2f}, {volumen:d}'
        print (out)
        #f.writel(out)
        f.write(out + "\n")
        f.flush()
        time.sleep(1)   
        continue

productos = leer_valores('Data/mcentral.csv') # ('Data/mcentral.csv')
escribir_log('Data/mercadolog.csv', productos) # ('Data/mercadolog.csv')


