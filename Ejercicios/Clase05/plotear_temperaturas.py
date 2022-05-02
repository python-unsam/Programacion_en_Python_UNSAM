import matplotlib.pyplot as plt
import numpy as np
def plotar_temperaturas():
    temperaturas = np.load('/home/sebastian/coding/Programacion_en_Python_UNSAM/Ejercicios/Data/temperaturas.npy')
    plt.hist(temperaturas,bins=15)
    plt.show()

plotar_temperaturas()