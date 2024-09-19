# -*- coding: utf-8 -*-

'''Problema 2'''
import numpy as np
matriz= np.zeros([6,8])
cantidad_personas= np.zeros([6,8])
matriz_clientes= np.zeros([6,8])
multas= np.zeros([6,8])#matriz final con las multas

def imprimir(lista_1,lista_2):
    for i in range(len(lista_1)):
        print(lista_1[i],': $',lista_2[i])

def sumaDireccion3(lista,matriz):
    for columnas in range(8):#tamaño de columnas
        suma=0
        for filas in range(6):
            suma= suma + matriz[filas][columnas]
        lista.append(suma)
    return lista

def buscaragregar(lista,elemento):
    if elemento not in lista:
        lista.append(elemento)
    return lista.index(elemento)

tiendas=['Hites', 'Ripley', 'H&M', 'La Polar', 'Falabella', 'Paris']
ciudades=['Antofagasta', 'Iquique', 'La Serena', 'Coquimbo', 'Valparaiso', 'Concepción', 'Talca', 'Santiago']
infraccion= 150000
archivo= open('metrajes.txt','r',encoding='utf-8')
linea= archivo.readline().strip()
while linea!='':
    partes= linea.split('-')
    ciudad= partes[0]
    tienda= partes[1]
    metros_cuadrados= int(partes[2])
    fila= buscaragregar(tiendas, tienda)
    columna= buscaragregar(ciudades, ciudad)
    matriz[fila,columna]+= metros_cuadrados
    linea= archivo.readline().strip()

# CALCULO EL LIMITE DE LAS PERSONAS QUE PUEDEN ESTAR EN LAS TIENDAS
for fila in range(len(tiendas)):
    for columna in range(len(ciudades)):
        cantidad_personas[fila,columna]+= matriz[fila,columna]//8

archivo2= open('fiscalizaciones.txt','r',encoding='utf-8')
linea2= archivo2.readline().strip()
while linea2!='':
    partes= linea2.split('-')
    ciudad= partes[0]
    tienda= partes[1]
    clientes= int(partes[2])
    filas= buscaragregar(tiendas, tienda)
    columnas= buscaragregar(ciudades, ciudad)
    matriz_clientes[filas,columnas]+= clientes
    linea2= archivo2.readline().strip()

'''------------A--------------'''
# calculamos la diferencia para ver cuanto se pasaron
print('a)')
for fila in range(len(tiendas)):
    for columna in range(len(ciudades)):
        if cantidad_personas[fila,columna]<matriz_clientes[fila,columna]:
            print(tiendas[fila],'-',ciudades[columna])
'''-------------B----------------'''
print('b)')
for fila in range(len(tiendas)):
    for columna in range(len(ciudades)):
        if cantidad_personas[fila,columna]<matriz_clientes[fila,columna]:
            multas[fila,columna]+= matriz_clientes[fila,columna]- cantidad_personas[fila,columna]

for fila in range(len(tiendas)):
    for columna in range(len(ciudades)):
        multas[fila,columna]*=infraccion

infracciones=[]
resultado= sumaDireccion3(infracciones, multas)
imprimir(ciudades, resultado)

'''-------------C-----------------'''
print('c)')
mayor=-1
mayorT=''
mayorC=''
for fila in range(len(tiendas)):
    for columna in range(len(ciudades)):
        if cantidad_personas[fila,columna]>mayor:
            mayor= cantidad_personas[fila,columna]
            mayorT= tiendas[fila]
            mayorC= ciudades[columna]

menor=10**10
menorT=''
menorC=''
for fila in range(len(tiendas)):
    for columna in range(len(ciudades)):
        if cantidad_personas[fila,columna]<menor:
            menor= cantidad_personas[fila,columna]
            menorT= tiendas[fila]
            menorC= ciudades[columna]

print('El aforo máximo en una tienda es de',mayor)
print(mayorT, 'Ubicada en la ciudad de',mayorC)
print('El aforo mínimo en una tienda es de',menor)
print(menorT, 'Ubicada en la ciudad de',menorC)
