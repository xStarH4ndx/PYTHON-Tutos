# -*- coding: utf-8 -*-
"""
CICLO WHILE Y LECTURA DE ARCHIVO
"""

#VARIABLES GLOBALES
mayor=-1
mayorNombre= ""

mayorSpotify=-1
mayorNombreSpotify=""

mayorApple=-1
mayorNombreApple=""

archivo= open("artistas.txt","r",encoding="utf-8")
linea= archivo.readline().strip()

while (linea!=""):
    partes= linea.split(",")
    pais= partes[0]
    cant_artistas= int(partes[1])
    cant_lineas= cant_artistas * 2
    
    #VARIABLES TEMPORALES
    suma=0
    artista_anterior=""
    mayorPais=-1
    mayorNombrePais= ""
    for i in range(cant_lineas):
        linea= archivo.readline().strip()
        partes2= linea.split(",")
        artista_actual= partes2[0]
        plataforma= partes2[1].lower()
        oyentes= int(partes2[2])
        tipo= partes2[3]
        
        #SPOTIFY
        if (oyentes>mayorSpotify) and (plataforma == "spotify"):
            mayorSpotify=oyentes
            mayorNombreSpotify=artista_actual
        elif (oyentes>mayorApple) and (plataforma == "applemusic"):
            mayorApple= oyentes
            mayorNombreApple= artista_actual
        
        
        if (artista_anterior == "") or (artista_anterior== artista_actual):
            suma+=oyentes
            
            if(suma>mayorPais):
                mayorPais= suma
                mayorNombrePais= artista_anterior
        else:
            if(suma>mayor):
                mayor=suma
                mayorNombre=artista_anterior
            
                
            suma=oyentes
        artista_anterior= artista_actual
        
    print("El mayor artista de",pais,"es:",mayorNombrePais,"con",mayorPais,"oyentes")   
        
        
    linea= archivo.readline().strip()

print("\n --------------ARTISTA GLOBAL--------------")
print("El artista más grande es:",mayorNombre, mayor)

print("\n --------------SPOTIFY--------------")
print("El artista más grande de SPOTIFY es:",mayorNombreSpotify, mayorSpotify)
print("\n --------------APPLEMUSIC--------------")
print("El artista más grande de APPLEMUSIC es:",mayorNombreApple, mayorApple)
