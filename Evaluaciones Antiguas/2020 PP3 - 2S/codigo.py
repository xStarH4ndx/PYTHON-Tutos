# -*- coding: utf-8 -*-
"""
ejercicio 1 - prueba
"""
import numpy as np

def swap(list_,a,b):
    aux = list_[a]
    list_[a] = list_[b]
    list_[b] = aux
    
def swapMatrix(matrix,a,b,c):
    aux =  matrix[c][a]
    matrix[c][a] = matrix[c][b]
    matrix[c][b] = aux   

def buscarAgregar(lista,elemento):
    if elemento not in lista:
        lista.append(elemento)
    return lista.index(elemento)

continentes=[]
rarezas=[]

matriz_precio=np.zeros([5,5])
matriz_cantidad= np.zeros([5,5])


archivo= open('tesoros.txt','r',encoding='utf-8')
linea= archivo.readline().strip()
while linea!='':
    partes= linea.split(",")
    if len(partes)== 4:
        codigo= partes[0]
        rareza= partes[1]
        continente= partes[2]
        valor= float(partes[3])
        
        fila= buscarAgregar(rarezas,rareza)
        columna= buscarAgregar(continentes,continente)
        matriz_precio[fila,columna]+= valor #ESTO SUMARA LOS VALORES DE LOS PRECIOS
        matriz_cantidad[fila,columna]+= 1 #ESTO SUMARA LA CANTIDADES POR RAREZA EN CADA CONTINENTE
        
    linea= archivo.readline().strip()

precio_por_continente=[]
for i in range(len(continentes)):
    sum_value = 0
    for j in range(len(rarezas)):
        sum_value += matriz_precio[j][i]
    precio_por_continente.append(sum_value)

for a in range(len(precio_por_continente)-1):
    for b in range(a + 1, len(precio_por_continente)):
        if precio_por_continente[a] > precio_por_continente[b]:#MATRIZ ORDENADA ASCENDENTEMENTE
            swap(precio_por_continente,a,b)
            swap(continentes,a,b)            
            for c in range(len(rarezas)):
                swapMatrix(matriz_precio,a,b,c)
                swapMatrix(matriz_cantidad,a,b,c)



print('1) Valor por continente:')
for i in range(len(precio_por_continente)):
    print(continentes[i])
    print(round(precio_por_continente[i],1))

print("2) Valor por rareza del continente con mayor valor")
print(continentes[len(continentes)-1])#EL ULTIMO VALOR ES EL MAS GRANDE PORQUE ESTA EN ASCENDENTE
for i in range(len(rarezas)):
    print(f" {rarezas[i]}: {round(matriz_precio[i][len(continentes)-1],1)}M")

precio_por_rareza = []    
for i in range(len(rarezas)):#sumare por filas
    sum_value = 0
    for j in range(len(continentes)):
        sum_value += matriz_precio[i][j]
    precio_por_rareza.append(sum_value)

print("3) Colección con menor valor")    
menor=10**10
menor_N=''
for i in range(len(precio_por_rareza)):
    if precio_por_rareza[i]<menor:
        menor = precio_por_rareza[i]
        menor_N= rarezas[i]
print(menor_N,menor)

print("4) Valor medio de la colección reliquia")#EL VALOR MEDIO ES EL PROMEDIO
pos= rarezas.index("reliquia")
suma_reliquias=0
cont_reliquias=0
for i in range(len(continentes)):
    suma_reliquias+= matriz_precio[pos,i]
    cont_reliquias+= matriz_cantidad[pos,i]
promedio= suma_reliquias/cont_reliquias
print(round(promedio,2),'M')

print("5) Cantidad de tesoros por continente")

for columnas in range(len(continentes)):#sumare por columnas
    suma_cantidades=0
    for filas in range(len(rarezas)):
        suma_cantidades+= matriz_cantidad[filas,columnas]
    
    print(continentes[columnas],':',round(suma_cantidades))


'''EJERCICIO 2 INCOMPLETO'''
