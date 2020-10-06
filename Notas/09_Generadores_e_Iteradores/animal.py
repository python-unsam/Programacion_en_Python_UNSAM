
import random


class Animal(object):
    """docstring for Animal"""
    def __init__(self):
        super(Animal, self).__init__()
        self.reproducciones_pendientes = 3
        self.edad = 0
        self.sexo = None # Posible mejora para que no se puedan reproducir dos del mismo sexo
        self.autonomia_restante = self.autonomia


        #pass
        self.es_reproductore = False

    def pasar_una_etapa(self):
        self.edad += 1
        if (self.edad >= 2 and
            # self.edad <= self.edad_maxima * 0.8 and
            self.reproducciones_pendientes > 0):
            self.es_reproductore = True



        # pass
        self.autonomia_restante -= 1 # Se puede restar si no llega a comer

    def en_vida(self):
        return (self.edad <= self.edad_maxima) and self.autonomia_restante > 0

    def tiene_hambre(self):
        """Acá se puede poner comportamiento para que no tenga hambre todo el tiempo"""
        # return True pass
        # return self.autonomia_restante < self.autonomia - 2
        return self.autonomia_restante < self.autonomia - 4

    def es_leon(self):
        return False

    def es_antilope(self):
        return False

    def puede_reproducir(self):
        # pass
        return self.es_reproductore

    def tener_cria(self):
        """Acá se puede poner comportamiento que sucede al tener cria"""
        # pass
        self.reproducciones_pendientes -= 1
        self.es_reproductore = False

    def reproducirse(self, vecinos, libres):
        pos = None
        # vecinos = [ v for v in vecinos if v.es_leon()==self.es_leon() ]
        if vecinos:
            animal = random.choice(vecinos)
            if libres:
                animal.tener_cria()
                self.tener_cria()
                pos = random.choice(libres)

        return pos

    def alimentarse(self, animales_vecinos):
        self.autonomia_restante = self.autonomia
        return None

    def moverse(self, libres):
        pos = None
        if libres:
            pos = random.choice(libres)

        return pos

    def fila_str(self):
        return f"{self.edad:>3d}    {self.autonomia_restante:>3d}/{self.autonomia:<3d}       {self.es_reproductore!s:<5}"

    def __format__(self):
        return self.__repr__()

    def __str__(self):
        return self.__repr__()


class Leon(Animal):
    """docstring for Leon"""
    def __init__(self):
        self.autonomia = 10
        self.edad_maxima = 30
        super(Leon, self).__init__()

    def es_leon(self):
        return True

    def alimentarse(self, animales_vecinos):
        pos = None
        if self.tiene_hambre(): # no está lleno
            presas_cercanas = [ (pos,animal) for (pos, animal) in animales_vecinos if animal.es_antilope() ]
            if presas_cercanas: # hay presas cerca
                super(Leon, self).alimentarse(animales_vecinos)
                (pos, animal) = random.choice(presas_cercanas)

        return pos




    def __repr__(self):
        # return "L"
        return "L{}".format(self.edad)



class Antilope(Animal):
    """docstring for Antilope"""
    def __init__(self):
        self.autonomia = 8
        self.edad_maxima = 10
        super(Antilope, self).__init__()
        self.reproducciones_pendientes = 5

    def es_antilope(self):
        return True

    # def puede_reproducir(self):
        # return True


    def __repr__(self):
        # return "A"
        return "A{}".format(self.edad)







