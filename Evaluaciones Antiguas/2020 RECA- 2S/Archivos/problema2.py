# -*- coding: utf-8 -*-


"""CODIGO INCOMPLETO EJERCICIO 2"""


import numpy as np
matriz=np.zeros([60,100])

def buscaragregar(lista,elemento):
    if elemento not in lista:
        lista.append(elemento)
    return lista.index(elemento)
    
# def leer_archivo(nombre):
#     lista=[]
#     archivo= open(nombre+".txt","r",encoding='utf-8')
#     linea= archivo.readline().strip()
#     while linea!='':
#         lista.append(linea)
#         linea= archivo.readline().strip()
#         return lista

# def crear_matriz(nombre):
#     marcas=[]
#     colores=[]
#     padron= leer_archivo(nombre)
#     for i in padron:
#         partes= i.split(",")
#         # vin= partes[0]
#         marca= partes[1]
#         color= partes[2]
#         # año= int(partes[3])
#         fila= buscaragregar(marcas, marca)
#         columna= buscaragregar(colores, color)
#         matriz[fila,columna]+= 1
        
#     return matriz

lista=[]
archivo= open("padron1.txt","r",encoding='utf-8')
linea= archivo.readline().strip()
while linea!='':
    lista.append(linea)
    linea= archivo.readline().strip()

marcas=[]
colores=[]

for i in lista:
    partes= i.split(",")
    vin= partes[0]
    marca= partes[1]
    color= partes[2]
    año= int(partes[3])
    # fila= buscaragregar(marcas, marca)
    # columna= buscaragregar(colores, color)
    # matriz[fila,columna]=año
    
    print(marca)