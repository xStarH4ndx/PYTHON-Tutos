# -*- coding: utf-8 -*-



suma_Mes=0
suma_Hora_Mes=0
archivo= open("ventas.txt","r",encoding='utf-8')
linea=archivo.readline().strip()
while(linea!=''):
    partes= linea.split(",")
    usuario= partes[0]
    categoria= partes[1].lower()

    
    costo= int(partes[2])
    
    #SEPARAR FECHAS
    fecha= (partes[3]).split("/")
    dia= fecha[0]
    mes= fecha[1]
    año= fecha[2]
    
    
    #SEPARAR HORARIO
    horario= (partes[4]).split(":")
    hora= horario[0]
    minutos= horario[1]
    
    
    if(mes=="10" and categoria=="muebles"):
        suma_Mes+=costo
        print(suma_Mes)
    
    
    
    linea= archivo.readline().strip()


    
print("El gasto del mes de Octubre fue de:",suma_Mes)





