# -*- coding: utf-8 -*-
"""
PROBLEMA "ALMA's Tour" - Nicki Nicol

arriba del ciclo = guardar
abajo del ciclo = cambiar
"""



'''VARIABLES GLOBALES'''
total=0
mayor_pais=-1
mayor_pais_nombre=''


archivo= open("conciertos.txt","r",encoding="utf-8")
linea= archivo.readline().strip()
while (linea!=''):
    partes= linea.split(",")
    pais= partes[0]
    cant_ciudades= int(partes[1])
    
    #variables Locales nivel 1
    suma_pais=0
    mayor_ciudad=-1
    mayor_ciudad_nombre=""
    
    print()
    print("#País:",pais)
    for i in range(cant_ciudades):
        linea= archivo.readline().strip()
        partes2= linea.split(",")
        ciudad= partes2[0]
        cant_comunas= int(partes2[1])
        
        #variables Locales nivel 2
        suma_comunas=0
        mayor_comuna=-1
        mayor_comuna_nombre=""
        
        for j in range(cant_comunas):
            linea= archivo.readline().strip()
            partes3= linea.split(",")
            comuna= partes3[0]
            oyentes= int(partes3[1])
            
            suma_pais+= oyentes
            suma_comunas+= oyentes
            
            if(oyentes>mayor_comuna):
                mayor_comuna= oyentes
                mayor_comuna_nombre=comuna
        
        print("La Comuna con más oyentes en",ciudad,"fue:",mayor_comuna_nombre,"con",mayor_comuna)
        
        if (suma_comunas>mayor_ciudad):
            mayor_ciudad= suma_comunas
            mayor_ciudad_nombre= ciudad
    print("-------------------------------------------------------------")
    print("La Ciudad con más oyentes en",pais,"fue:",mayor_ciudad_nombre,"con",mayor_ciudad)
    
    if(suma_pais>mayor_pais):
        mayor_pais= suma_pais
        mayor_pais_nombre= pais
    
    linea= archivo.readline().strip()
print()
print("------ Conclusión Final ------")
print("El país con más oyentes fue:",mayor_pais_nombre,"con:",mayor_pais,"oyentes")
