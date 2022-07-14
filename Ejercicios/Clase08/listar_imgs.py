import os

def archivos_png(directorio:str)->list:
    lista_archivos_png = list()
    for root, dirs, files in os.walk(directorio):
        for file in files:
            if file.find('.png') != -1:
                lista_archivos_png.append(file)
    return lista_archivos_png

def main():
    import sys
    print(archivos_png(sys.argv[1]))

if __name__ == '__main__':
    main()
