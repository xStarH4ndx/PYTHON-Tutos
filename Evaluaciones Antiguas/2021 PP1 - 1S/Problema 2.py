# -*- coding: utf-8 -*-

"""EJERCICIO 2"""
#promedio de marzo
suma_precio_marzo=0
suma_precio_cont=0

#menor volumen
menor_volumen=10**10
menor_fecha=""

#encontrar variacion mayor
diferencia=0
mayor_variacion=-1
mayor_fecha= ""

max_precio=-1
max_fecha=""

cont_dias=0
suma_volumen=0

suma_meses_pares=0
suma_meses_impares=0

mayor_año=-1
mayor_mes=-1
mayor_dia=-1
cont_doge=0

archivo= open("doge.txt","r")
linea= archivo.readline().strip()
while linea!= "":
    partes2= linea.split(",")
    fecha= partes2[0]
    #año-mes-dia
    partes= fecha.split("-")
    año= int(partes[0])
    mes=int( partes[1])
    dia= int(partes[2])
    #archivo entero por bloques ","
    apertura= float(partes2[1])
    alto= float(partes2[2])
    bajo= float(partes2[3])
    cierre= float(partes2[4])
    ajustado= float(partes2[5])
    volumen= float(partes2[6])
    
    """CALCULO"""    
    #precio del mes de marzo
    if mes== 3:
        suma_precio_marzo+= ajustado
        suma_precio_cont+=1
        
    #volumen menor
    if volumen<menor_volumen:
        menor_volumen= volumen
        menor_fecha= fecha
        
    #calculando la variacion
    if apertura>cierre:    
        diferencia= apertura - cierre
    elif apertura<cierre:
        diferencia= cierre- apertura
        
    #variacion mas alta
    if diferencia> mayor_variacion:
        mayor_variacion= round(diferencia,4)
        mayor_fecha= fecha
        
    #precio mas alto
    if alto> max_precio:
        max_precio= alto
        max_fecha= fecha
    
    #calcular promedio de transacciones por dia
    suma_volumen+= (volumen*((alto+bajo)/2))
    cont_dias+=1
    
    """pregunta 6"""
    #meses pares
    if mes%2==0:
        if dia==20:
            suma_meses_pares+=(420*alto)
            cont_doge+=1
    #meses impares
    elif mes%2!=0:
        if dia==1:
            suma_meses_impares+= (330*bajo)
            cont_doge+=1
            
    #LEER ULTIMA FECHA
    if año>mayor_año:
        mayor_año=año
        if mes>mayor_mes:
            mayor_mes= mes
            if dia> mayor_dia:
                mayor_dia= dia
                
    
    linea= archivo.readline().strip()

"""RESPUESTAS"""
inversion= suma_meses_impares+ suma_meses_pares
promedio_marzo= round((suma_precio_marzo/suma_precio_cont),4)
promedio_transaccion= (suma_volumen/cont_dias)/1000000#lo dividimos en 1 millon
print("1) El precio promedio ajustado de marzo es de ",promedio_marzo )
print("2) El menor volumen fue de",menor_volumen,"en la fecha",menor_fecha)
print("3) El día con la mayor variacion fue el",mayor_fecha,"con una variacion de",mayor_variacion)
print("4) El maximo valor fue el",max_fecha,"con un monto de",max_precio)
print("5) El promedio anual de transaccion diaria es de ",round((promedio_transaccion),4))
#ejercicio 6 incompleto
print("6) Nuestro amigo vendio {total} dogecoins por un total de {total2} dolares con una inversion de",inversion,"obtuvo una utilidad de {utilidad} dolares")



