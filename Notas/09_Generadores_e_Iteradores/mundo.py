

from animal import Animal, Leon, Antilope
from tablero import Tablero
import os


def print_debug(msg, print_flag=False):
    if print_flag:
        print(msg)

class Mundo(object):
    """docstring for Mundo"""

    def __init__(self, columnas, filas, n_leones, n_antilopes, debug=False):
        super(Mundo, self).__init__()

        self.debug = debug

        self.etapa = 0
        self.tablero = Tablero(filas, columnas)
        self.llenar_mundo(n_leones, n_antilopes)


    def llenar_mundo(self, n_leones, n_antilopes):
        for _ in range(n_leones):
            if self.tablero.hay_posiciones_libres():
                print_debug("ubicando un leon", self.debug)
                self.tablero.ubicar_en_posicion_vacia(Leon())

        for _ in range(n_antilopes):
            if self.tablero.hay_posiciones_libres():
                print_debug("ubicando un Antilope", self.debug)
                self.tablero.ubicar_en_posicion_vacia(Antilope())

    def cant_leones(self):
        return sum([1 for x in self.tablero.elementos() if x.es_leon()])

    def cant_antilopes(self):
        return sum([1 for x in self.tablero.elementos() if x.es_antilope()])

    def etapa_movimiento(self):
        print_debug(f"Iniciando Movimiento en etapa {self.etapa}", self.debug)
        for p in self.tablero.posiciones_ocupadas():
            animal = self.tablero.posicion(p)

            posiciones_libres = self.tablero.posiciones_vecinas_libre(p)
            nueva_posicion = animal.moverse(posiciones_libres)
            if nueva_posicion:
                self.tablero.mover(p, nueva_posicion)

    def etapa_alimentacion(self):
        print_debug(f"Iniciando Alimentación en etapa {self.etapa}", self.debug)
        for p in self.tablero.posiciones_ocupadas():
            animal = self.tablero.posicion(p)
            animales_cercanos = self.tablero.posiciones_vecinas_con_ocupantes(p)
            desplazo = animal.alimentarse(animales_cercanos)
            if desplazo:
                self.tablero.ubicar(desplazo, self.tablero.retirar(p))

    def etapa_reproduccion(self):
        print_debug(f"Iniciando Reproducción en etapa {self.etapa}", self.debug)
        # pass
        for p in self.tablero.posiciones_ocupadas():
            animal = self.tablero.posicion(p)
            if animal.puede_reproducir():
                posiciones_libres = self.tablero.posiciones_vecinas_libre(p)
                animales_cercanos = [vecino for (_,vecino) in self.tablero.posiciones_vecinas_con_ocupantes(p) if
                        vecino.es_leon()==animal.es_leon() and vecino.puede_reproducir()]
                nacimiento = animal.reproducirse(animales_cercanos, posiciones_libres)
                if nacimiento:
                    self.tablero.ubicar(nacimiento, Leon() if animal.es_leon() else Antilope())

    def pasar_una_etapa(self):
        print_debug(f"Concluyendo etapa {self.etapa}", self.debug)
        for p in self.tablero.posiciones_ocupadas():
            animal = self.tablero.posicion(p)
            animal.pasar_una_etapa()
            if not animal.en_vida():
                self.tablero.retirar(p)
        self.etapa += 1

    def pasar_un_ciclo(self):
        self.etapa_movimiento()
        self.etapa_alimentacion()
        self.etapa_reproduccion()
        self.pasar_una_etapa()


    def __repr__(self):
        res = str(self.tablero)
        res += f"\nEstamos en la etapa {self.etapa}"
        res += f"\nCon {self.cant_leones()} Leones, y {self.cant_antilopes()} antilopes."
        if False:
            res += '\nEspecie   Posicion   años  autonomia puede_reproduc\n'
            for p in self.tablero.posiciones_ocupadas():
                animal = self.tablero.posicion(p)
                res += f'{"Leon    " if animal.es_leon() else "Antilope"} {str(p):^10s} {animal.fila_str()}\n'

        return res

    def __str__(self):
        return self.__repr__()


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from matplotlib.ticker import AutoMinorLocator

img_leon = mpimg.imread('img/leon.png')
img_antilope = mpimg.imread('img/antilope.png')

class MundoMatPlotLib(Mundo):
    """docstring for MundoMatPlotLib"""
    def __init__(self, columnas, filas, n_leones, n_antilopes, debug=False):
        super(MundoMatPlotLib, self).__init__(columnas, filas, n_leones, n_antilopes, debug)
        self.contador_bichos = {}
        self.v_iniciales = (columnas, filas, n_leones, n_antilopes)

    def pasar_un_ciclo(self):
        super(MundoMatPlotLib, self).pasar_un_ciclo()
        self.contador_bichos[self.etapa] = {"Leones": self.cant_leones(), "Antilopes": self.cant_antilopes()}

    def graficar_historia(self, save=False):
        fig, ax = plt.subplots()
        q = [ ((k,v["Leones"]),(k,v["Antilopes"])) for k,v in  self.contador_bichos.items()]
        l,a = zip(*q)
        plt.plot(*zip(*l), label = "Leones")
        plt.plot(*zip(*a), label = "Antilopes")
        plt.suptitle('Evolución en el tiempo',fontsize=16, y=1)
        plt.title('Cond. iniciales: Tablero {}x{} con {} Leones y {} Antilopes'.format(*self.v_iniciales),fontsize=10)
        plt.legend()

        if save:
            if not os.path.exists('output'):
                os.makedirs('output')
            plt.savefig('output/simulation_c{:03d}_f{:03d}_l{:03d}_a{:03d}.png'.format(*self.v_iniciales), bbox_inches='tight')
            plt.close()
        else:
            plt.show(block=False)


    def ver_plot(self):
        fig, ax = plt.subplots()
        ax.set_xlim(-1, self.tablero.n_columnas())
        ax.set_ylim(-1, self.tablero.n_filas())

        ax_width = ax.get_window_extent().width
        fig_width = fig.get_window_extent().width
        fig_height = fig.get_window_extent().height
        poo_size = ax_width/(fig_width*(self.tablero.n_columnas()+1))
        ax.set_xticks(np.arange(0, self.tablero.n_columnas(), 1.0))
        ax.set_yticks(np.arange(0, self.tablero.n_filas(), 1.0))
        minor_locator = AutoMinorLocator(2)
        plt.gca().xaxis.set_minor_locator(minor_locator)
        plt.gca().yaxis.set_minor_locator(minor_locator)
        plt.grid(which='minor')
        # plt.grid(b=True, which='major', color='#666666', linestyle='-')

        pos_ocupadas = self.tablero.posiciones_ocupadas()
        poo_axs = [None for i in range(len(pos_ocupadas))]

        for i, (f,c) in enumerate(pos_ocupadas):
            loc = ax.transData.transform((c, f))
            poo_axs[i] = fig.add_axes([loc[0]/fig_width-poo_size/2, loc[1]/fig_height-poo_size/2,
                                       poo_size, poo_size], anchor='C')

            temp_img = img_leon if self.tablero.posicion((f,c)).es_leon() else img_antilope

            poo_axs[i].imshow(temp_img)
            poo_axs[i].axis("off")

        # ax = fig.gca()
        plt.draw()

        # plt.grid(True)
        if False:
            plt.savefig('output/board_{:03d}_{}.png'.format(mundo_actual.etapa, extra_num), bbox_inches='tight')
        else:
            plt.show()
        plt.close()


if __name__ == "__main__":
    # m = MundoMatPlotLib(10, 10, 10, 10, debug=True)

    # import time
    # for i in range(20):
    #     m.pasar_un_ciclo()
    #     # m.ver_plot()
    #     # time.sleep(1)
    #     print(i +1)
    #     print(m)

    # for c in [10, 20, 30, 50, 75, 100, 150]:
    historia_l = []
    historia_a = []
    for c in [30]:
        # for f in [10, 20, 30, 50, 75, 100, 150]:
        for f in [30]:
            # for l in [10, 20, 30, 50, 75, 100, 150, 500]:
            for l in [20]:
                # for a in [10, 20, 30, 50, 75, 100, 150, 500]:
                for a in [50]:
                    print(c,f,l,a)
                    if c*f > l + a:
                        for iteracion in range(10):
                            print("Mundo {}".format(iteracion))
                            m = MundoMatPlotLib(c, f, l, a, debug=False)
                            for _ in range(200):
                                m.pasar_un_ciclo()
                            q = [ (v["Leones"],v["Antilopes"]) for k,v in  m.contador_bichos.items()]
                            leones,antilopes= zip(*q)
                            historia_l.append(leones)
                            historia_a.append(antilopes)
                        # m.graficar_historia(save=True)


    median_leones = [np.median([x[i] for x in historia_l]) for i in range(len(historia_l[0]))]
    median_antilopes = [np.median([x[i] for x in historia_a]) for i in range(len(historia_a[0]))]
    median_libres = [(f*c-(median_leones[i]+median_antilopes[i])) for i in range(len(historia_a[0]))]
    plt.plot(range(len(historia_l[0])), median_leones, label="Leones")
    plt.plot(range(len(historia_a[0])), median_antilopes, label="Antilopes")
    plt.plot(range(len(historia_a[0])), median_libres, label="Libres")
    plt.legend()
    plt.show()
