#TAD EXPEDIENTE

#   Expediente = {
#       nroExp: Int
#       titular: String
#       tramite: String
#       fechaPres: datetime
#       horaPres: datetime
#   }


def crearExpediente():
    #Crea una instancia vacia del expediente
    e = [0,'','','','']
    return e

def cargarExpediente(e,ne,tit,tr,fp,hp):
    #Carga los datos en la instancia del expediente
    e[0]=ne
    e[1]=tit
    e[2]=tr
    e[3]=fp
    e[4]=hp

def verNroExp(e):
    #Retorna el numero del expediente
    return e[0]

def verTitular(e):
    #Retorna el titular del expediente
    return e[1]

def verTramite(e):
    #Retorna el expediente
    return e[2]

def verFechaPresentacion(e):
    #Retorna la fecha de presentacion de un expediente
    return e[3]

def verHoraPresentacion(e):
    #Retorna la fecha de presentacion de un expediente
    return e[4]

def modificarNroExp(e,ne):
    #Modifica el numero de un Expediente
    e[0]=ne

def modificarTitular(e,tit):
    #Modifica el titular de un Expediente
    e[1]=tit

def modificarTramite(e,tr):
    #Modifica el tramite de un Expediente
    e[2]=tr

def modificarFechaPresentacion(e,fp):
    #Modifica la fecha de ingreso del expediente 
    e[3]=fp

def modificarHoraPresentacion(e,hp):
    #Modifica la hora de ingreso del expediente 
    e[4]=hp

