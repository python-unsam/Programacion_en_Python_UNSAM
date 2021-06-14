[Contenidos](../Contenidos.md) \| [Próximo (2 Scripting)](02_Scripts.md)

# 6.1 Repaso de temas pasados

A continuación dejamos unos links a unos videos sobre un par de ejercicios de la clase 5:

1. Ejercicio [Ejercicio 5.2](../05_Random_Plt_Dbg/01_Random.md#ejercicio-52-generala-no-necesariamente-servida) sobre la probabilidad de obtener una generala no servida resuelto por [Matias](https://youtu.be/D_mipwwZjhM) y por [Rafael](https://youtu.be/c2SO3-iSd04).
2. Ejercicio [Ejercicio 5.15](../05_Random_Plt_Dbg/03_Figuritas.md#ejercicio-515) del [álbum de Figuritas](https://youtu.be/lSVNxPoRLJA)

## Análisis de alternativas para *propagar*

Los siguientes tres ejercicios proponen diferentes soluciones al [Ejercicio 4.6](../04_Listas_y_Listas/02_IteradoresLista.md#ejercicio-46-propagación) de propagación del fuego. Vamos a analizar sus diferencias y comenzar a pensar en su eficiencia. Algunas soluciones tienen errores que deberás corregir oportunamente. ¡Usá el debugger de Python!

_Observación: Cuando te pidamos que cuentes cuántas operaciones hace una función, no nos va a importar el detalle de las constantes. Por ejemplo: si una función para una entrada de largo n hace n+2 operaciones y otra hace 3*n+5 nos va a importar que ambas hacen una cantidad **lineal** de operaciones en el tamaño de la entrada, pero no las constantes 2, 3 y 5 que figuran en cada caso. Diremos que la cantidad de operaciones es *O(n)* (se lee 'o de n'). En cambio, sí vamos a hacer una diferencia si una función hace n y otra hace n^2 operaciones (una va a tener complejidad *O(n)* y la otra O(n^2)*). Volveremos sobre estos temas más adelante._


### Ejercicio 6.1: Propagar por vecinos
El siguiente código propaga el fuego de cáda fósforo encendido a sus vecinos inmediatos (si son fósforos nuevos) a lo largo de toda la lista. Y repite esta operación mientras sea necesario. ¿Te animás a estimar cuántas operaciones puede tener que hacer, en el peor caso?

```python
def propagar_al_vecino(l):
    modif = False
    n = len(l)
    for i,e in enumerate(l):
        if e==1 and i<n-1 and l[i+1]==0:
            l[i+1] = 1
            modif = True
        if e==1 and i>0 and l[i-1]==0:
            l[i-1] = 1
            modif = True
    return modif

def propagar(l):
    m = l.copy()
    veces=0
    while propagar_al_vecino(l):
        veces += 1

    print(f"Repetí {veces} veces la función propagar_al_vecino.")
    print(f"Con input {m}")    
    print(f"Y obtuve  {l}")
    return m
#%%
propagar([0,0,0,0,1])
propagar([0,0,1,0,0])
propagar([1,0,0,0,0])
```

**Preguntas:**
1. ¿Por qué los tests `l[i+1]==0` y `l[i-1]==0` de la función `propagar_al_vecino` no causan un `IndexError` en los bordes de la lista?
2. ¿Por qué `propagar([0,0,0,0,1])` y `propagar([1,0,0,0,0])`, siendo entradas perfectamente simétricas, no generan la misma cantidad de repeticiones de llamadas a la función `propagar_al_vecino`?
3. Sobre la complejidad. Si te sale, calculá:
    * ¿Cuántas veces como máximo se puede repetir el ciclo while en una lista de largo n?
    * ¿Cuántas operaciones hace "propagar_al_vecino" en una lista de largo n?
    * Entonces, ¿cuántas operaciones hace como máximo esta versión de `propagar` en una lista de largo n? ¿Es un algoritmo de complejidad lineal o cuadrática?


### Ejercicio 6.2: Propagar por como el auto fantástico

El siguiente código propaga el fuego inspirado en las luces del [auto fantástico](https://youtu.be/oNeQi8-PXAU?t=11).
```python
def propagar_a_derecha(l):
    n = len(l)
    for i,e in enumerate(l):
        if e==1 and i<n-1:
            if l[i+1]==0:
                l[i+1] = 1
    return l
#%
def propagar_a_izquierda(l):
    return propagar_a_derecha(l[::-1])[::-1]
#%
def propagar(l):
    ld=propagar_a_derecha(l)
    lp=propagar_a_izquierda(ld)
    return lp
#%%
l = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
print("Estado original:  ",l)
print("Porpagando...")
lp=propagar(l)
print("Estado original:  ",l)
print("Estado propagado: ",lp)
```

**Preguntas:**
1. ¿Por qué se modificó la lista original? 
2. ¿Por qué no quedó igual al `estado propagado`? 
3. Corregí el código para que no cambie la lista de entrada.
4. ¿Cuántas operaciones hace como máximo `propagar_a_derecha` en una lista de largo n?
5. Sabiendo que invertir una lista (`[::-1]`) requiere una cantidad lineal de operaciones en la longitud de la lista ¿Cuántas operaciones hace como máximo `propagar` en una lista de largo n?


### Ejercicio 6.3: Propagar con cadenas
Esta versión usa métodos de _cadenas_ para resolver el problema separando los fósforos en _grupos sin fósforos quemados_ y analizando cada grupo. Sin embargo algo falla...

```python
def trad2s(l):
    '''traduce una lista con 1,0 y -1 
    a una cadena con 'f', 'o' y 'x' '''
    d={1:'f', 0 :'o', -1:'x'}
    s=''.join([d[c] for c in l])
    return s

def trad2l(ps):
    '''traduce cadena con 'f', 'o' y 'x'
    a una lista con 1,0 y -1'''
    inv_d={'f':1, 'o':0, 'x':-1}
    l = [inv_d[c] for c in ps]
    return l

def propagar(l, debug = True):
    s = trad2s(l)
    if debug:
        print(s)#, end = ' -> ')
    W=s.split('x')
    PW=[w if ('f' not in w) else 'f'*len(w) for w in W]
    ps=''.join(PW)
    if debug:
        print(ps)
    return trad2l(ps)

#%%
l = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
lp = propagar(l)
print("Estado original:  ",l)
print("Estado propagado: ",lp)
```

**Preguntas:**
1. ¿Porqué se acorta la lista? 
2. ¿Podés corregir el error agregando un solo caracter al código?
3. ¿Te parece que este algoritmo es cuadrático como el [Ejercicio 6.1](../06_Organización_y_Complejidad/01_Repaso.md#ejercicio-61-propagar-por-vecinos)
o lineal como el [Ejercicio 6.2](../06_Organización_y_Complejidad/01_Repaso.md#ejercicio-62-propagar-por-como-el-auto-fantástico)?




[Contenidos](../Contenidos.md) \| [Próximo (2 Scripting)](02_Scripts.md)

