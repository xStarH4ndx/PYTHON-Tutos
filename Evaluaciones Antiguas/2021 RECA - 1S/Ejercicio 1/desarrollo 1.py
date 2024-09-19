# -*- coding: utf-8 -*-

'''Problema 1'''
#win= 3pts
#empate= 1 pts c/u
#loser= 0 pts

def buscaragregar(lista,elemento):
    if elemento not in lista:
        lista.append(elemento)
    return lista.index(elemento)

G=0
P=0
puntos_local=0
puntos_visita=0

cont_local=0
cont_visita=0
equipos=[]
archivo= open('resultados.txt','r', encoding='utf-8')
linea= archivo.readline().strip()
while linea!='':
    partes= linea.split(',')
    
    #LEER EQUIPOS LOCAL Y VISITA
    if len(partes)== 3:
        E_local= partes[0]
        E_visita= partes[1]
        fecha= partes[2]
        buscaragregar(equipos, E_local)
        buscaragregar(equipos, E_visita)
    
    #LEER GOLES
    if len(partes)==2:
        equipo= partes[0]
        if equipo== 'Local':
            cont_local+=1
        elif equipo== 'Visita':
            cont_visita+=1
        
        if cont_local>cont_visita:
            puntos_local+=3
            
        elif cont_visita>cont_local:
            puntos_visita+=3
        elif cont_local== cont_visita:
            puntos_local+=1
            puntos_visita+=1
            
    #LEER TARJETAS
    if len(partes)==4:
        tarjeta= partes[0]
        equipo= partes[1]
        nombre= partes[2]
        numero= int(partes[3])
    
    
    linea= archivo.readline().strip()


print('Tabla de posiciones')
print("Nombre de equipos",'|ptj|')
for i in range(len(equipos)):
    print(equipos[i],'|ptj|')