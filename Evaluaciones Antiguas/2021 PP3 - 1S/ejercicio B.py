# -*- coding: utf-8 -*-

'''EJERCICIO 2'''
import numpy as np
matriz= np.zeros([6,6])
despachos=np.zeros([6,6])

def encontrar_elemento(elemento,matriz):
    filas= matriz.shape[0]#el punto shape me devuelve el tamaño de la matriz
    columnas= matriz.shape[1]
    for i in range(filas):
        for j in range(columnas):
            if matriz[i,j]==elemento:
                return [i,j]
    return [-1,-1]

def max_matriz(matriz):
    filas= matriz.shape[0]
    col= matriz.shape[1]
    maximo=-10**10
    for i in range(filas):
        for j in range(col):
            if matriz[i,j]>maximo:
                maximo= matriz[i,j]
    return maximo

def intercambiar(lista,pos1,pos2):
    aux= lista[pos1]
    lista[pos1]= lista[pos2]
    lista[pos2]= aux

def imprimir(lista_1,lista_2):
    for i in range(len(lista_1)):
        print(lista_1[i],lista_2[i])

def sumaDireccion(lista,matriz,direccion):
    if direccion==True:#SI ES TRUE, SUMARA LOS VALORES DE LA COLUMNA
        for columnas in range(6):#tamaño de columnas
            suma=0
            for filas in range(6):
                suma= suma + matriz[filas][columnas]
            lista.append(suma)
        return lista
    else:#SI ES FALSE SUMARÁ LOS VALORES DE LA FILA
        for filas in range(6):#tamaño de columnas
            suma=0
            for columnas in range(6):
                suma= suma + matriz[filas][columnas]
            lista.append(suma)
        return lista

def buscarAgregar(lista,elemento):
    if elemento not in lista:
        lista.append(elemento)
    return lista.index(elemento)

sectores=['1','2','3','4','5','6']#6 sectores COLUMNAS
costos=[125,325,198,635,312,185]#COSTOS POR SECTORES
zonas= ['A','B','C','D','E','F']#6 zonas FILAS
contador_envios=0
suma_costos=[]
suma_despachos=[]
items_pendientes=[]

archivo= open('recibidos.txt','r')
linea= archivo.readline().strip()
while linea!='':
    partes= linea.split(';')
    fecha= partes[0]
    partes3= fecha.split("-")
    año=int(partes3[0])
    mes= int(partes3[1])
    dia=int(partes3[2])
    bodega= partes[1]
    partes2= bodega.split('-')
    zona= partes2[0]
    sector= partes2[1]
    cantidad_items= int(partes[2])#tengo que sumar las cantidades en cada ubicacion
    fila= buscarAgregar(zonas, zona)
    columna= buscarAgregar(sectores, sector)
    matriz[fila,columna]+= cantidad_items
    linea= archivo.readline().strip()

'''detectar los envios que se hicieron'''
for fila in range(len(zonas)):
    for columna in range(len(sectores)):
        if matriz[fila,columna]>=100:
            envios= round((matriz[fila,columna]//100))
            despachos[fila,columna]+= envios
            matriz[fila,columna]-= 100

for fila in range(len(zonas)):
    for columna in range(len(sectores)):
        if despachos[fila,columna]>0:
            print("Se ha realizado un despacho en",zonas[fila],sectores[columna],"el",fecha)

sumaDireccion(suma_despachos, despachos, True)
for i in suma_despachos:
    contador_envios+=i
print("2) Los envios por zona- secotr en el mes fueron:")
print(despachos)

for fila in range(len(zonas)):
    for columna in range(len(sectores)):
        despachos[fila,columna]*=costos[columna]
        
sumaDireccion(suma_costos, despachos, True)
total=0
for i in suma_costos:
    total+=i
print("3) El costo total de los",contador_envios," es", total)
for fila in range(len(zonas)):
    for columna in range(len(sectores)):
        if matriz[fila,columna]>=100:
            matriz[fila,columna]-= 100

print("4) Las ubicaciones con la mayor cantidad de items pendientes son:")
maximo= max_matriz(matriz)
pos= encontrar_elemento(maximo,matriz)
print(pos,maximo)


sumaDireccion(items_pendientes, matriz, False)
for a in range(len(items_pendientes)-1):#comienza del primero al penultimo valor
    for b in range (a+1,len(items_pendientes)):#comienza del segundo hasta el ultimo valor
        if items_pendientes[a]< items_pendientes[b]:
            intercambiar(items_pendientes,a,b)
            intercambiar(zonas,a,b)
print("5) El total de items pendientes por zonas es:")
imprimir(zonas,items_pendientes)
