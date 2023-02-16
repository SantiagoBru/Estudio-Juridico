from datetime import time, date
from tadPila import *
from tadExpediente import *
from tadEstudio import *
import os
est = crearEstudio()
pilaExp = crearPila()
rta = 's'

while rta == 's':
    os.system('cls' if os.name == 'nt' else 'clear')
    opcion = 0
    print('''
            A- Agregar expediente
            B- Modificar expediente
            C- Eliminar expediente por n°
            D- Listado de expedientes
            E- Modificar hs de los expedientes que se encuentren entre 2 fechas dadas
            F- Generar una pila de expedientes que se encuentren entre 2 fechas dadas
            G- Eliminar expedientes de un mes determinado
        ''')

    opcion=input("Ingrese una opcion:").lower()
    os.system('cls' if os.name == 'nt' else 'clear')
    if opcion == 'a':
        rta2 = 's'
        while rta2 == 's':
            numeroExp=int(input("Ingrese el numero de expediente: "))
            titular=input("Ingrese el titular del expediente: ")
            tramite=input("Ingrese el tramite del expediente: ")
            bandera = 1
            while (bandera == 1):
                try: 
                    print("Ingrese la fecha 1 con formato DD/MM/YYYY")
                    dia = int(input())
                    mes = int(input())
                    anio = int(input()) 
                    fecha = datetime.date(anio, mes, dia)
                    bandera = 0
                except: 
                    print("Hubo un error en los datos ingresados. Reintente...")
                    bandera = 1
            bandera1 = 1
            while (bandera1 == 1):
                try:
                    print("Ingrese la hora con formato HH:MM")
                    h = int(input())
                    min = int(input())
                    hora = datetime.time( h, min)
                    bandera1 = 0
                except:
                    print ("hubo un error en los datos ingresados. Reintente...")
                    bandera1 = 1        
                      
            expediente = crearExpediente()
            cargarExpediente(expediente,numeroExp,titular,tramite,fecha,hora)

            agregarExp(est,expediente)
            print("Expediente agregado y cargado con exito")

            rta2=input("Desea agregar otro expediente? S/N ").lower()
        os.system('cls' if os.name == 'nt' else 'clear')

    elif opcion == 'b':
        rta2 = 's'
        numeroExp=input("Ingrese el numero de expediente que desea modificar: ")
        while rta2 == 's':
            
            for i in range(cantidadTotalExpedientes(est)):
                expediente = recuperarPorPosicion(est,i)
                if (verNroExp(expediente)) == numeroExp:
                    print('N° Expediente: ',verNroExp(expediente))
                    nuevoNro= input('Ingrese el nuevo numero: ')
                    modificarNroExp(expediente,nuevoNro)
                    print('Titular: ',verTitular(expediente))
                    nuevoTit= input('Ingrese el nuevo titular: ')
                    modificarTitular(expediente,nuevoTit)
                    print('Tramite: ',verTramite(expediente))
                    nuevoTramite= input('Ingrese el nuevo tramite: ')
                    modificarTramite(expediente,nuevoTramite)
                    print('Fecha de Presentacion: ',verFechaPresentacion(expediente))
                    bandera = 1
                    while (bandera == 1):
                        try: 
                            print("Ingrese la nueva fecha con formato DD/MM/YYYY")
                            dia = int(input())
                            mes = int(input())
                            anio = int(input()) 
                            fecha = datetime.date(anio, mes, dia)
                            bandera = 0
                        except: 
                            print("Hubo un error en los datos ingresados. Reintente...")
                            bandera = 1
                    modificarFechaPresentacion(expediente,fecha)
                    print("Ingrese la nueva hora con formato HH:MM")
                    h = int(input())
                    min = int(input())
                    hora = datetime.time( h, min)                
                    modificarHoraPresentacion(expediente,hora)  
                os.system('cls' if os.name == 'nt' else 'clear')
                print('El expediente fue modificado con éxito!!')
            rta2=input("Desea modificar otro expediente? S/N ").lower()
        os.system('cls' if os.name == 'nt' else 'clear')


    elif opcion == 'c':
        numeroExp=input("Ingrese el numero de expediente que desea eliminar: ")
        
        i=0
        while i != cantidadTotalExpedientes(est):
            expediente = recuperarPorPosicion(est,i)
        if ((verNroExp(expediente)) == numeroExp):                  			
            eliminarExp(est,expediente)
            print('El expediente fue eliminado con éxito!!')
            i=0
        else:
        	i+=1
        os.system('cls' if os.name == 'nt' else 'clear')


    elif opcion == 'd':
        for i in range(cantidadTotalExpedientes(est)):
            expediente = recuperarPorPosicion(est,i)
            print('**********')
            print('N° Expediente: ',verNroExp(expediente))
            print('Titular: ',verTitular(expediente))
            print('Tramite: ',verTramite(expediente))
            print('Fecha de Presentacion: ',verFechaPresentacion(expediente))
            print('Hora de Presentacion: ',verHoraPresentacion(expediente))

            print('**********')
            caracter = input()
        os.system('cls' if os.name == 'nt' else 'clear')


    elif opcion == 'e':
        os.system('cls' if os.name == 'nt' else 'clear')
        rta2 = 's'
        while rta2 == 's': 
            bandera = 1
            while (bandera == 1):
                try: 
                    print("Ingrese la fecha 1 con formato DD/MM/YYYY")
                    dia = int(input())
                    mes = int(input())
                    anio = int(input()) 
                    fecha1 = datetime.date(anio, mes, dia)
                    bandera = 0
                except: 
                    print("Hubo un error en los datos ingresados. Reintente...")
                    bandera = 1
            bandera1 = 0        
            while (bandera1 == 1):
                try: 
                    print("Ingrese la fecha 2 con formato DD/MM/YYYY")
                    dia = int(input())
                    mes = int(input())
                    anio = int(input())
                    fecha2 = datetime.date(anio, mes, dia)  
                    bandera1 = 0
                except: 
                    print("Hubo un error en los datos ingresados. Reintente...")
                    bandera1 = 0   
            if fecha1<fecha2 :
                for i in range(cantidadTotalExpedientes(est)):
                    expediente = recuperarPorPosicion(est,i)    
                    fecha = verFechaPresentacion(expediente) 
                    if((fecha1 < fecha)and(fecha<fecha2)):
                        print("Ingrese la hora con formato HH:MM que desee modificar")
                        h = int(input())
                        min = int(input())
                        hora = datetime.time(h, min)                
                        modificarHoraPresentacion(expediente,hora)
            else :
                print('Fecha ingresada invalida')
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Los expedientes fueron modificados con éxito!!')
        
        rta2=input("Desea modificar en otra fechas? S/N ").lower()
        os.system('cls' if os.name == 'nt' else 'clear')

    elif opcion == 'f':
        os.system('cls' if os.name == 'nt' else 'clear')
        rta2 = 's'
        while rta2 == 's' :
            bandera = 1
            while (bandera == 1):
                try: 
                    print("Ingrese la fecha 1 con formato DD/MM/YYYY")
                    dia = int(input())
                    mes = int(input())
                    anio = int(input()) 
                    fecha1 = datetime.date(anio, mes, dia)
                    bandera = 0
                except: 
                    print("Hubo un error en los datos ingresados. Reintente...")
                    bandera = 1
            bandera1 = 1        
            while (bandera1 == 1):
                try: 
                    print("Ingrese la fecha 2 con formato DD/MM/YYYY")
                    dia = int(input())
                    mes = int(input())
                    anio = int(input())
                    fecha2 = datetime.date(anio, mes, dia)  
                    bandera1 = 0
                except: 
                    print("Hubo un error en los datos ingresados. Reintente...")
                    bandera1 = 0   
            if fecha1<fecha2 :
                for i in range(cantidadTotalExpedientes(est)):
                    expediente = recuperarPorPosicion(est,i)    
                    fecha = verFechaPresentacion(expediente) 
                    if((fecha1 < fecha)and(fecha<fecha2)):
                       apilar(pilaExp,expediente)
            else:
                print('Fecha ingresada invalida')
            os.system('cls' if os.name == 'nt' else 'clear')

            print('La lista fue creada con éxito!!')

            rta2=input("Desea armar una lista nueva? S/N ").lower()
        os.system('cls' if os.name == 'nt' else 'clear')

    elif opcion == 'g':
        os.system('cls' if os.name == 'nt' else 'clear')
        rta2 = 's'
        while rta2 == 's':
            print('''
                01- Enero 
                02- Febrero 
                03- Marzo 
                04- Abril 
                05- Mayo 
                06- Junio 
                07- Julio 
                08- Agosto 
                09- Septiembre 
                10- Octubre
                11- Noviembre
                12- Diciembre
                ''')
            m=int(input("Ingrese una opcion:"))
            os.system('cls' if os.name == 'nt' else 'clear')

            flag=True
            i=0
            while i != cantidadTotalExpedientes(est):
                expediente = recuperarPorPosicion(est,i)
                fecha = verFechaPresentacion(expediente)
            if(fecha.month == m):                   			
                eliminarExp(est,expediente)
                print('Los expedientes se eliminaron con éxito!!')
                i=0
                flag=False
            else:
        	    i+=1

            os.system('cls' if os.name == 'nt' else 'clear')

    else:
        print("Opcion incorrecta")

    os.system('cls' if os.name == 'nt' else 'clear')

    rta=input('Desea realizar otra operacion? s/n \n\r').lower()
os.system("pause")