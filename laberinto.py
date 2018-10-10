def leer_archivo(archivo):
    return ([x.split(" ") for x in [y.strip("\n") for y in open(archivo).readlines()]])

def laberinto(archivo):
    return (leer_archivo(archivo)[:-2])

def coordenadas_iniciales(archivo):
    return ([int(x) for x in leer_archivo(archivo)[-2][0].split(",")])

def coordenadas_finales(archivo):
    return ([int(x) for x in leer_archivo(archivo)[-1][0].split(",")])

def posicion_inicial(coordenadas_iniciales, laberinto):
    if laberinto[coordenadas_iniciales[0]][coordenadas_iniciales[1]] == "1": return False
    return True
def posicion_final(coordenadas_finales, laberinto):
    if laberinto[coordenadas_finales[0]][coordenadas_finales[1]] == "1": return False
    return True

##Aqui se empieza a crear el arbol con las posiciones que se han recorrido del laberinto

def validacion():
    if posicion_inicial(coordenadas_iniciales("laberinto.txt"), laberinto("laberinto.txt")) == False: return False
    elif posicion_final(coordenadas_finales("laberinto.txt"), laberinto("laberinto.txt")) == False: return False
    else:
        

class ArbolNario:
    def __init__(self,valor,hijos=[]):
        self.valor = valor
        self.hijos = hijos

def agregarANivel(arbol,valor, nivel):
    if nivel==2:
        return arbol.hijos.append(ArbolNario(valor))
    else:
        return agregarANivel(arbol.hijos[0],valor, nivel-1)

def agregarANodo(arbol,valor, nodo):
    if nodo==arbol.valor:
        return arbol.hijos.append(ArbolNario(valor))
    else:
        return agregarNodoAux(arbol.hijos,valor,nodo)

def agregarNodoAux(lista,valor,nodo):
    if lista==[]:
        return False
    else:
        return agregarANodo(lista[0],valor,nodo) or agregarNodoAux(lista[1:],valor,nodo) 




#print validacion_final()
