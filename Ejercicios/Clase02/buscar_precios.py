
def buscar_precio(fruta:str):
    with open('../Data/precios.csv','rt') as file:
        match = False

        # Se itera linea a linea
        for line in file:
            # Cuando una linea conteine el substring dado por el argumento fruta
            # Se parsea y se imprime el resultado. Luego se corta la funcion retornando 0 como resultado exitoso
            if line.lower().find(fruta.lower()) != -1:
                match = True
                line_parsed = line.split(',')
                precio = line_parsed[1].lstrip('\n')
                print(f'El precio de un cajón de {fruta} es: {precio}')
                return 0
        # En el caso de que no se encuentre un reultado el booleano match seguira siendo False, y se imprira la string correspondiente
        # Y se retornara 1 como resultado fallido
        if not match:
            print(f'{fruta} no figura en el listado de precios.')
            return 1

buscar_precio('frambuesa')