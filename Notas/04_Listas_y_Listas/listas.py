#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 13:42:38 2021

@author: mlopez
"""

l1 = [x for x in range(10)]

[q for q in l1 if q%2==0]


lista_corta = ['adriana',
 'agostina',
 'agustin',
 'agustin',
 'agustin',
 'agustin leonel',
 'agustina', 'bautista', 'camila', 'daiana', 'esteban', 'fabiana alejandra', 'gabriel', 'hans', 'ian', 'jaquelina', 'karen', 'lara', 'macarena', 'nadia', 'olivia', 'pablo', 'quimey gabriel', 'r. magali', 'sabrina', 'tais', 'ubeiden', 'valentina', 'wanda', 'xavier agustin', 'yair', 'zoe']


a0_nombres = [nom for nom in lista_corta  ]
a1_inicial = [nom[0] for nom in lista_corta  ]
a2_iniciales = [nom[0:3] for nom in lista_corta  ]
a2_solo_si_e = [nom[0:3] for nom in lista_corta if "e" in nom[0:3]  ]
a3_reverso= [nom[::-1] for nom in lista_corta  ]
a32_reverso_de_a2= [nom[::-2] for nom in lista_corta  ]
a4_vocales = [nom for nom in lista_corta if nom[0] in "aeiou"]
a5_vocales = [a for nom in lista_corta for a in nom  if a in "aeiou"]


[ y for y in range(10) ]
[ [y] for y in range(10) ]
[ [x*y for x in range(10)] for y in range(10) ]
[ [sum([x for _ in range(y)]) for x in range(10)] for y in range(10) ]