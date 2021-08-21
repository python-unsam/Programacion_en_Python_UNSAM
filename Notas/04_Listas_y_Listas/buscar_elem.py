#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 13:21:40 2021

@author: mlopez
"""

def buscar_elem(lista, e):
    i = 0
    pos = -1
    while i < len(lista):
        if lista[i] == e:
            pos = i
            #break
        i += 1
    return pos
    

def buscar_elem2(lista, e):
    p = len(lista) - 1
    while p >= 0 and lista[p] != e:
        p -= 1
    return p
    
def buscar_elem3(lista, e):
    pos = -1
    for i in range(len(lista)):
        if lista[i] == e:
            pos = i
            break
    return pos
            
def buscar_elem4(lista, e):
    pos = -1
    for idx,elem in enumerate(lista):
        if elem == e:
            pos = idx
            break
    return pos
            
    
l = [3,6,7,1,9,-2]

l2 = [3,6,-2, 7,1,9,-2, -3]