# -*- coding: utf-8 -*-

"""PROBLEMA 1"""

meses=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
categorias=['Muebles', 'Hombre', 'Mujer', 'Electro', 'Tecnología', 'Belleza', 'Dormitorio', 'Deportes', 'Juguetes', 'Niños']

def MenorCategoria_Mes(matriz,lista1,lista2):
    menor_lista=10**10
    for i in range(len(lista1)):
        if lista1[i]<menor_lista:
            menor_lista= lista1[i]
            menorC= categorias[i]#IDENTIFICAR EL MENOR PRECIO DE VENTA DE LA CATEGORIA
    
    menor=10*100
    for fila in range(len(categorias)):
        if categorias[fila]== menorC:
            for columna in range(len(meses)):
                if matriz[fila,columna]<=menor:
                    menor= matriz[fila,columna]
    for fila in range(len(categorias)):
        if categorias[fila]== menorC:
            for columna in range(len(meses)):
                if matriz[fila,columna]<=menor:
                    mes_menor= meses[columna]
                    lista2.append(mes_menor)
    print(menorC)
    imprimir(lista2)

def suma_listas(lista):
    suma=0
    for i in range(len(lista)):
        suma+= lista[i]
    return suma

def sumaDireccion3(lista,matriz,direccion):
    if direccion==True:#SI ES TRUE, SUMARA LOS VALORES DE LA COLUMNA
        for columnas in range(12):#tamaño de columnas
            suma=0
            for filas in range(10):
                suma= suma + matriz[filas][columnas]
            lista.append(suma)
        return lista
    else:#SI ES FALSE SUMARÁ LOS VALORES DE LA FILA
        for filas in range(10):#tamaño de columnas
            suma=0
            for columnas in range(12):
                suma= suma + matriz[filas][columnas]
            lista.append(suma)
        return lista

def imprimir(lista1):
    for i in range(len(lista1)):
        print('*',lista1[i])

def buscaragregar(lista,elemento):
    if elemento not in lista:
        lista.append(elemento)
    return lista.index(elemento)

'''matrices'''
import numpy as np
matriz_2019= np.zeros([10,12])
matriz_2020=np.zeros([10,12])
matriz=np.zeros([10,12])
matrizE_2019= np.zeros([10,12])
matrizE_2020= np.zeros([10,12])

archivo= open("ventas_2019.txt","r",encoding='utf-8')
linea= archivo.readline().strip()
while linea!='':
    partes= linea.split(",")
    mes= partes[0]
    categoria= partes[1]
    precio= int(partes[2])
    fila= buscaragregar(categorias,categoria)
    columna= buscaragregar(meses,mes)
    matriz_2019[fila,columna]+=precio
    linea= archivo.readline().strip()

archivo= open("ventas_2020.txt","r",encoding='utf-8')
linea= archivo.readline().strip()
while linea!='':
    partes= linea.split(",")
    mes= partes[0]
    categoria= partes[1]
    precio= int(partes[2])
    fila= buscaragregar(categorias,categoria)
    columna= buscaragregar(meses,mes)
    matriz_2020[fila,columna]+= precio
    linea= archivo.readline().strip()

'''Esta es la matriz con los datos sumados entre 2020 y 2019'''
for fila in range(len(categorias)):
    for columna in range(len(meses)):
        matriz[fila,columna]+= matriz_2020[fila,columna]+matriz_2019[fila,columna]#Matriz total

'''A'''
print("A)")
meses_2020=[]
mayor=-1
for fila in range(len(categorias)):
    if categorias[fila]=="Deportes":
        for columna in range(len(meses)):
            if matriz_2019[fila,columna]<matriz_2020[fila,columna]:
                mayor= meses[columna]
                meses_2020.append(mayor)
imprimir(meses_2020)

'''B'''

lista2019=[]
lista2020=[]
sumaDireccion3(lista2019, matriz_2019, False)
sumaDireccion3(lista2020, matriz_2020, False)

print('b)')
for i in range(len(lista2019)):
    if (lista2019[i]/12)<(lista2020[i]/12):
        direccion= 'Aumento'
    else:
        direccion= 'Disminución'        
    print(categorias[i],': Año 2019:',(lista2019[i]/12),'- Año 2020:',(lista2020[i]/12),direccion)

'''C'''
print('C)')
menores2019=[]
menores2020=[]
MenorCategoria_Mes(matriz_2019, lista2019, menores2019)
MenorCategoria_Mes(matriz_2020, lista2020, menores2020)

'''D'''
archivo= open("ventasE_2019.txt","r",encoding='utf-8')
linea= archivo.readline().strip()
while linea!='':
    partes= linea.split(",")
    mes= partes[0]
    categoria= partes[1]
    precio= int(partes[2])
    fila= buscaragregar(categorias,categoria)
    columna= buscaragregar(meses,mes)
    matrizE_2019[fila,columna]+=precio
    linea= archivo.readline().strip()
    
archivo= open("ventasE_2020.txt","r",encoding='utf-8')
linea= archivo.readline().strip()
while linea!='':
    partes= linea.split(",")
    mes= partes[0]
    categoria= partes[1]
    precio= int(partes[2])
    fila= buscaragregar(categorias,categoria)
    columna= buscaragregar(meses,mes)
    matrizE_2020[fila,columna]+= precio
    linea= archivo.readline().strip()

for fila in range(len(categorias)):
    for columna in range(len(meses)):
        matrizE_2019[fila,columna]-=matriz_2019[fila,columna]
        matrizE_2020[fila,columna]-=matriz_2020[fila,columna]

total2019=[]
total2020=[]
sumaDireccion3(total2019, matrizE_2019, True)    
sumaDireccion3(total2020, matrizE_2020, True)
envios_2019= suma_listas(total2019)
envios_2020= suma_listas(total2020)    

print('D)')
print('Año 2019:',envios_2019)
print('Año 2020:',envios_2020)
