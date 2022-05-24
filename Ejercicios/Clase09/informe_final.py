import csv
import fileparse
from lote import Lote
import formato_tabla

def leer_camion(nombre_archivo: str) -> dict:
    with open(nombre_archivo) as iterador:
        camion = fileparse.parse_csv(iterador,types=[str,int,float])
        camion_lote = camion = [Lote(d['nombre'], d['cajones'], d['precio']) for d in camion]    
    return camion_lote


def leer_precios(nombre_archivo: str) -> dict:
    precios = dict()
    with open(nombre_archivo) as iterador:
        precios_lista_tuplas = fileparse.parse_csv(iterador,has_headers=False,types=[str,float])
    for fruta in precios_lista_tuplas:
        precios[fruta[0]] = fruta[1] 
    return precios


def hacer_informe(cajones: list, precios: dict) -> list:
    tabla = list()
    for entrada in cajones:
        nombre_fruta = entrada.nombre
        cajones = entrada.cajones
        precio_venta = precios[entrada.nombre]
        cambio = precio_venta - entrada.precio
        tabla.append((nombre_fruta, cajones, precio_venta, cambio))
    return tabla


def generar_encabezado(justificado: int, encabezado: tuple) -> str:

    formato_encabezado = ""
    for titulo in encabezado:
        formato_encabezado += f"{titulo:>10s} "

    separador = ""
    for i in range(len(encabezado)):
        for i in range(justificado):
            separador += "-"
        separador += " "

    print(formato_encabezado)
    print(separador)


def imprimir_informe(informe: list) -> None:
    headers = ("Nombre", "Cajones", "Precio", "Cambio")
    generar_encabezado(10, headers)
    for nombre, cajones, precio, cambio in informe:
        precio = "$" + str(round(precio, 2))
        print(f"{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}")


def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)

#informe_camion('/home/sebastian/coding/Programacion_en_Python_UNSAM/Ejercicios/Data/camion.csv','/home/sebastian/coding/Programacion_en_Python_UNSAM/Ejercicios/Data/precios.csv')

def f_principal(argumentos:list):
    informe_camion(argumentos[1],argumentos[2])

if __name__ == '__main__':
    import sys
    f_principal(sys.argv) 

