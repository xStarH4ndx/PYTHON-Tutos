# -*- coding: utf-8 -*-
"""
ESTUDIO MATRICES PP3
"""

'''ordenamiento'''
def intercambiar_matriz(matrix,a,b,c):
    aux =  matrix[c][a]
    matrix[c][a] = matrix[c][b]
    matrix[c][b] = aux   

def intercambiar(lista,pos1,pos2):
    aux= lista[pos1]
    lista[pos1]= lista[pos2]
    lista[pos2]= aux

'''ENCONTRAR MAXIMO Y MINIMO VERSION 3.0'''
def max_matriz2(matriz,sentido):
    filas= matriz.shape[0]
    col= matriz.shape[1]
    
    if sentido==True:#True== mayor
        maximo=-10**10
        for i in range(filas):
            for j in range(col):
                if matriz[i,j]>maximo:
                    maximo= matriz[i,j]
        return maximo
    else:#esto encontrará el menor valor
        menor=10**10
        for i in range(filas):
            for j in range(col):
                if matriz[i,j]<menor:
                    menor= matriz[i,j]
        return menor
    
'''ENCONTRAR EL MAXIMO EN UNA MATRIZ'''
def max_matriz(matriz):
    filas= matriz.shape[0]
    col= matriz.shape[1]
    maximo=-10**10
    for i in range(filas):
        for j in range(col):
            if matriz[i,j]>maximo:
                maximo= matriz[i,j]
    return maximo

'''ENCONTRAR UN ELEMENTO EN LA MATRIZ'''
def encontrar_elemento(elemento,matriz):
    filas= matriz.shape[0]#el punto shape me devuelve el tamaño de la matriz
    columnas= matriz.shape[1]
    for i in range(filas):
        for j in range(columnas):
            if matriz[i,j]==elemento:
                return [i,j]
    return [-1,-1]

'''ENCONTRAR ELEMENTO NIVEL 2'''
def encontrar_elemento2(elemento,matriz):
    encontrados=[]
    filas= matriz.shape[0]#el punto shape me devuelve el tamaño de la matriz
    columnas= matriz.shape[1]
    for i in range(filas):
        for j in range(columnas):
            if matriz[i,j]==elemento:
                encontrados.append([i,j])
    return encontrados

# print(encontrar_elemento(78,matriz))#ESTO ME DIRÁ LA POSICION DEL ELEMENTO
# pos= encontrar_elemento(14,matriz)#ESTO GUARDARÁ LA POSICION DEL ELEMENTO
# print(matriz[pos[0],pos[1]])#ESTO VA A IMPRIMIR DIRECTAMENTE EL ELEMENTO QUE ESTÁ EN LAS CORDENADAS


'''buscar un elemento en la lista, y si no esta, se agrega'''
def buscarAgregar(elemento,lista):
    if elemento not in lista:
        lista.append(elemento)
    return lista.index(elemento)

'''FUNCION PARA SUMAR TODOS LOS DATOS DE LA COLUMNA'''
def sumaColumnas1(matriz):
    for columnas in range(3):#tamaño de columnas
        suma=0
        for filas in range(3):
            suma= suma + matriz[filas][columnas]
        print(suma)
    
'''funcion para sumar los valores VERSION 3.0'''
def sumaDireccion2(matriz,direccion):
    if direccion==True:#SI ES TRUE, SUMARA LOS VALORES DE LA COLUMNA
        for columnas in range(6):#tamaño de columnas
            suma=0
            for filas in range(10):
                suma= suma + matriz[filas][columnas]
            print(suma)
    else:#SI ES FALSE SUMARÁ LOS VALORES DE LA FILA
        for filas in range(10):#tamaño de columnas
            suma=0
            for columnas in range(6):
                suma= suma + matriz[filas][columnas]
            print(suma)
            
            
'''FUNCION PARA SUMAR VERSION 4.0 NEXT GEN'''
def sumaDireccion3(lista,matriz,direccion):
    if direccion==True:#SI ES TRUE, SUMARA LOS VALORES DE LA COLUMNA
        for columnas in range(6):#tamaño de columnas
            suma=0
            for filas in range(10):
                suma= suma + matriz[filas][columnas]
            lista.append(suma)
        return lista
    else:#SI ES FALSE SUMARÁ LOS VALORES DE LA FILA
        for filas in range(10):#tamaño de filas
            suma=0
            for columnas in range(6):
                suma= suma + matriz[filas][columnas]
            lista.append(suma)
        return lista
    
    
'''TRANSFORMAR UN ARCHIVO EN UNA MATRIZ'''
# import numpy as np
# matriz= np.zeros([5,5])

# fila=0
# archivo= open("numeros.txt",'r')
# linea=archivo.readline().strip()
# while linea!='':
#     partes=linea.split(',')
#     for columna in range(len(partes)):
#         matriz[fila,columna]= partes[columna]
    
#     fila+=1#me moveré entre las filas
#     linea=archivo.readline().strip()
# print(matriz)

''' SIGNIFICADO DE LOS PUNTOS'''
# #.ZEROS= MATRIZ CON CEROS
# #.ARRAY= CREA UNA MATRIZ USANDO LISTAS
# #.ones= CREA UNA MATRIZ CON UNOS

# #DEFINIR UNA MATRIZ
# import numpy as np
# matriz= np.zeros([3,3])
# print(matriz)

# ASIGNAR VALOR DENTRO DE LA MATRIZ
# import numpy as np
# datos=np.zeros([3,3])
# datos[0,2]=9
# print(datos)
# print(datos[0,2])

'''MOVERSE POR LA MATRIZ (POR COLUMNAS)'''
# import numpy as np
# valores= np.zeros([3,4])
# valores[0,2]=9
# valores[2,1]=4
# valores[2,3]=8
# print(valores)

# for columnas in range(4):
#     for filas in range(3):
#         print(valores[filas,columnas])

'''MOVERSE POR LA MATRIZ (POR FILAS)'''
# import numpy as np
# valores= np.zeros([3,4])
# valores[0,2]=9
# valores[2,1]=4
# valores[2,3]=8
# print(valores)

# for filas in range(3):
#     for columnas in range(4):
#         print(valores[filas,columnas])

# sumaColumnas(valores)

'''PARA SABER LA ULTIMA POSICION DE LA MATRIZ SE USA'''
# print("---------------------------")
# import numpy as np
# valores2= np.zeros([3,4])
# valores2[-1,-1]=9
# print(valores2)
# print(valores2[-1,-1])


# def imprimir(lista1,lista2):
#     for i in range(len(lista1)):
#         print(lista1[i], lista2[i])

# def calculoDens(tamañoPantalla,resolucionPantalla):
#     partes= resolucionPantalla.split("x")
#     ancho= int(partes[0])
#     alto= int(partes[1]) #'''para sacar la diagonal es la raiz de (a**2 + b**2)'''
#     densidad= ((ancho**2+alto**2)**(1/2))/tamañoPantalla
#     return densidad
    
# def intercambiar(lista,pos1,pos2):
#     aux= lista[pos1]
#     lista[pos1]= lista[pos2]
#     lista[pos2]= aux
    
# def burbuja(lista,direccion):
#     for a in range(len(lista)-1):
#         for b in range(a+1,len(lista)):
#             if direccion== True:#ORDEN DESCENDENTE
#                 if lista[a]<lista[b]:
#                     intercambiar(listaCantidades,a,b)
#                     intercambiar(listaMarcas,a,b)
#             else:#ORDEN ASCENDENTE
#                 if lista[a]>lista[b]:
#                     intercambiar(listaBaterias,a,b)
#                     intercambiar(listaCelulares,a,b)

# listaMarcas=[]
# listaCantidades=[]

# listaCelulares=[]
# listaBaterias=[]

# mayorDensidad=-1
# nombreMD=''

# mayorCamara=-1
# nombreMC=""

# archivo= open("celulares.txt","r",encoding="utf-8")
# linea= archivo.readline().strip()
# while linea!= '':
#     partes= linea.split("-")
#     marca= partes[0]
#     modelo=partes[1]
#     bateria= int(partes[2])
#     pantalla= float(partes[3])
#     res_pantalla= partes[4]
#     res_camara= int(partes[5])
#     densidad= calculoDens(pantalla,res_pantalla)
    
#     if densidad >mayorDensidad:
#         mayorDensidad= densidad
#         nombreMD= marca+" "+modelo
    
#     if res_camara>mayorCamara:
#         mayorCamara=res_camara
#         nombreMC= marca+" "+modelo
    
#     if marca not in listaMarcas:
#         listaMarcas.append(marca)
#         listaCantidades.append(0)
    
#     if bateria>=4000:
#         listaCelulares.append(marca+" "+modelo)
#         listaBaterias.append(bateria)
        
#     '''listas paralelas'''
#     for i in range(len(listaMarcas)):
#         if listaMarcas[i]== marca:
#             listaCantidades[i]+=1
            
#     linea= archivo.readline().strip()

# print("1) Celulares analizados:")
# burbuja(listaCantidades,True)
# imprimir(listaMarcas ,listaCantidades)

# print("2) Pantalla increible", nombreMD, round(mayorDensidad))
# print("3) Camara increible:", nombreMC, mayorCamara)

# burbuja(listaBaterias,False)
# print("4) Batería que dura mucho mas:")
# imprimir(listaCelulares, listaBaterias)
    