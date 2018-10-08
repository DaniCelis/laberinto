
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


print (posicion_inicial(coordenadas_iniciales("laberinto.txt"), laberinto("laberinto.txt")))

#print(coordenadas_iniciales("laberinto.txt"))
