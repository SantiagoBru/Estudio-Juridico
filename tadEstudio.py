# TAD ESTUDIO

def crearEstudio():
    #Crea un Estudio
    estudio=[]
    return estudio

def agregarExp(estudio,e):
    #agrega un estudio
    estudio.append(e)

def eliminarExp(estudio,e):
    #Elimina un estudio
    estudio.remove(e)

def existeExp(estudio, e):
    #Retorna True o False si el expediente a pertenece al estudio
    return e in estudio

def recuperarExp(estudio,i):
    #Retorna el expediente de la posicion iesima
    return estudio[i]

def tamanio(estudio):
    #Retorna la cantidad de expedientes del estudio
    return len(estudio)

def cantidadTotalExpedientes(estudio):
#Retorna la cantidad de Expedientes que hay en el estudio
    return len(estudio)

def recuperarPorPosicion(estudio,posicion):
#Retorna el expediente con posicion i del estudio
    return estudio[posicion]

