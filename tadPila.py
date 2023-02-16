#TAD PILA

def crearPila():
    #Crea una pila
    pila=[]
    return pila

def esVacia(pila):
    #Retorna Verdadero si la cola no tiene elementos
    return len(pila)==0

def apilar(pila,elem):
    #Apila
    pila.append(elem)
    
def desapilar(pila):
    #Desapila
    elem=pila[len(pila)-1]
    pila.pop()
    return elem