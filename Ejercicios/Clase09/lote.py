
#%%


class Lote:
    def __init__(self,fruta,cantidad,precio):
        self.nombre = fruta
        self.cajones = cantidad
        self.precio = precio
    
    def costo(self):
        return self.cajones * self.precio
    
    def vender(self,cantidad):
        if cantidad <= self.cajones:
            self.cajones -= cantidad
        else:
            print(f'Solo hay {self.cajones}, te los vendo todos')
            self.cajones = 0


# %%
#a = Lote('Pera', 100, 490.10)
#b = Lote('Manzana', 50, 122.34)
#c = Lote('Naranja', 75, 91.75)
#
#lotes = [a,b,c]
#
#for c in lotes:
#    print(f'{c.nombre:>10s} {c.cajones:>10d} {c.precio:>10.2f}')
#
#print('costo:',a.costo())
#print(a.cajones)
#a.vender(25)
#print(a.cajones)
## %%
#
#import fileparse
#with open('../Data/camion.csv') as lineas:
#    camion_dicts = fileparse.parse_csv(lineas, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
#
#camion = [Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
## %%
#