
def diccionario_geringoso(palabras:list)->dict:
	diccionario = dict()
	for palabra in palabras:
		palabra_en_geringoso = ''
		for letra in palabra:
		    if letra in ['a','e','i','o','u']:
		        palabra_en_geringoso += letra + 'p' + letra
		    else:
		        palabra_en_geringoso += letra
		diccionario[palabra] = palabra_en_geringoso
	return diccionario

print(diccionario_geringoso(['manzana', 'banana', 'pera', 'geringoso']))