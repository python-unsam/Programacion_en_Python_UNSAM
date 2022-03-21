#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: La funcion solo retorna el boleano respecto a la primera letra de la
# string. Lo corregi agregando una variable booleana false que se retorna por defecto
# en caso de que nunca se encuentre una a, y declare un break para que el loop se
# se corte al encontrar la letra a, asi no se continua iterando y perdiendo tiempo
# de corrida. Tambien es muy poco pythonica la manera en la que se escribio, 
# hay metodos como find() o index() para las strings que corren compilados 
# en el lenguaje base de python (creo que C) y por ende son mas rapidos.

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    tiene_letra_a = False
    while i<n:
        if expresion[i] == 'a':
            tiene_letra_a = True
            break
        i += 1
    return tiene_letra_a


#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: El error era de TAL tipo y estaba ubicado en TAL lugar.




#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: El error era de TAL tipo y estaba ubicado en TAL lugar.
...
...
...