#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 10:19:00 2020

@author: rgrimson
"""

#%%

s = "ejemplo de cadena"
s.upper() #un método de la clase cadena
c = "otro ejemplo"
c.upper()


lista = [0,1,2,3]
lista.index(2) #un método que no modifica el objeto
lista.append(4) #un método que sí modifica el objeto
#%%
##############
##  CLASES  ##
##############

class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

#%% constructores
a = Punto(1,1)
a.x
a.y

b = Punto(3,4)
b.x
b.y

#%% más métodos
import numpy as np

class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_origen(self):
        n = np.sqrt(self.x**2 + self.y**2)
        return n

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

#%%
#defino una instancia
a = Punto(1,1)
a.x
a.y
a.dist_origen()

#defino otra instancia
b = Punto(3,4)
b.dist_origen()

#%%
a.mover(1,1)
a.x
a.y
a.dist_origen()

#%%
b.x
print(b)


#%% 
###############
##  Met Esp  ##
###############

#%% __str__

class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def dist_origen(self):
        return np.sqrt(self.x**2 + self.y**2)
    
    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f'({self.x},{self.y})'

#%% con print queda lindo, pero el objeto sigue viendose feo
b = Punto(3,4)
print(b)
b
#%% __repr__
class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def dist_origen(self):
        return np.sqrt(self.x**2 + self.y**2)

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f'({self.x},{self.y})'

    def __repr__(self):
        return f'Punto({self.x},{self.y})'

#%%
b = Punto(3,4)
print(b)
b

#%% __add__

class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def dist_origen(self):
        return np.sqrt(self.x**2 + self.y**2)

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f'({self.x},{self.y})'

    def __repr__(self):
        return f'Punto({self.x},{self.y})'
    
    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)

#%%
a = Punto(1,1)
b = Punto(3,4)
c = a + b
print(c)
c.dist_origen()

#%%
################
##  herencia  ##
################
class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def dist_origen(self):
        return np.sqrt(self.x**2 + self.y**2)

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f'({self.x},{self.y})'

    def __repr__(self):
        return f'Punto({self.x},{self.y})'
    
    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)


class Circulo(Punto):
    
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        
    def radio(self):
        return self.r
    
    def area(self):
        return np.pi*self.r*self.r


#%%
c=Circulo(1,2,3)
print(c)
c.area()
c.mover(1,1)
print(c)

#%%
######################
##  Perros y Gatos  ##
######################

class Animal():
    def __init__(self, nombre):
        self.nombre = nombre
        
        
    def comer(self, comida):
        print(f'{self.nombre} come {comida}.')
        

#%%
laika = Animal('Laika')
laika.comer('carne')

#%% definamos un par de tipos de animales concretos
class Perro(Animal):
    def ladrar(self):
        print(f'{self.nombre} está ladrando.')

    def traer(self, objeto):
        print(f'{self.nombre} salio corriendo a buscar el {objeto}.')


class Gato(Animal):
    def maullar(self):
        print(f'{self.nombre} está maullando.')

#%% probemos

laika = Perro('Laika')
felix = Gato('Felix')

laika.comer('carne')
felix.comer('pescado') 

laika.ladrar()
felix.maullar()

laika.maullar()

#%% polimorfismo
class Animal():
    def __init__(self, nombre):
        self.nombre = nombre
        
        
    def comer(self, comida):
        print(f'{self.nombre} come {comida}.')
        
    def mostrar_afecto(self):
        pass

class Perro(Animal):
    def ladrar(self):
        print(f'{self.nombre} está ladrando.')
        
    def traer(self, objeto):
        print(f'{self.nombre} salio corriendo a buscar el {objeto}.')
        
    def mostrar_afecto(self):
        print(f'{self.nombre} mueve la cola.')
                    

class Gato(Animal):
    def maullar(self):
        print(f'{self.nombre} está maullando.')

    def mostrar_afecto(self):
        print(f'{self.nombre} se sienta upa y ronronea.')

#%%

laika = Perro('Laika')
felix = Gato('Felix')

laika.comer('carne')
felix.comer('pescado') 

laika.mostrar_afecto()
felix.mostrar_afecto()


#%%
#####################
##  Pilas y Colas  ##
#####################


#%%
##########################
##  Teledetección y AA  ##
##########################

