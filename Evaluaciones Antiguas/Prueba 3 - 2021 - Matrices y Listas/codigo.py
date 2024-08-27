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

value_by_rarity = []    
for i in range(len(rarezas)):#sumare por filas
    sum_value = 0
    for j in range(len(continentes)):
        sum_value += matriz_precio[i][j]
    value_by_rarity.append(sum_value)

print("3) Colección con menor valor")    
menor=10**10
menor_N=''
for i in range(len(value_by_rarity)):
    if value_by_rarity[i]<menor:
        menor = value_by_rarity[i]
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


'''EJERCICIO 2'''

# def agregarDojo(participante,dojo):
#     if dojo == "Cobra Kai":
#         if participante not in cobra:
#             cobra.append(participante)
#     elif dojo =="Miyagi Do":
#         if participante not in miyagi:
#             miyagi.append(participante)
#     elif dojo == "Shotokan":
#         if participante not in shotokan:
#             shotokan.append(participante)
#     elif dojo == "Hito Do":
#         if participante not in hito:
#             hito.append(participante)
#     elif dojo == "Dragon":
#         if participante not in dragon:
#             dragon.append(participante)
        
# def DojoPertenece(ganador):
#     dojo=""
#     if ganador in cobra:
#         dojo = "Cobra Kai"
#     elif ganador in miyagi:
#         dojo = "Miyagi Do"
#     elif ganador in shotokan:
#         dojo ="Shotokan"
#     elif ganador in hito:
#         dojo = "Hito Do"
#     elif ganador in dragon:
#         dojo= "Dragon"
#     return dojo

  


# import numpy as np

# archivo = open("duelos.txt")
# linea = archivo.readline().strip()
# ganadores = np.zeros([32,32])
# perdedores = np.zeros([32,32])
# participantes=[]
# cobra=[]
# cobrag=0
# cobrap=0
# miyagi=[]
# miyagig=0
# miyagip=0
# hito=[]
# hitog=0
# hitop=0
# dragon=[]
# dragong=0
# dragonp=0
# shotokan=[]
# shotokang=0
# shotokanp=0

# while linea != "":
#     partes = linea.split(",")
#     part1 = partes[0]
#     dojo1 = partes[1]
#     part2 = partes[2]
#     dojo2 = partes[3]
    
#     agregarDojo(part1,dojo1)
#     agregarDojo(part2,dojo2)
#     if part1 not in participantes:
#             participantes.append(part1)
#     if part2 not in participantes:
#             participantes.append(part2)
    
#     ubic1 = participantes.index(part1)
#     ubic2 = participantes.index(part2)
#     ganadores[ubic1][ubic2] = 1
    
    
    
#     linea = archivo.readline().strip()
    
# amistosos=0   
# archivo2 = open("resultados.txt")
# linea2 = archivo2.readline().strip()
# while linea2 != "":
#     partes2 = linea2.split(",")
#     parti1 = partes2[0]
#     pto1=int(partes2[1])
#     parti2 = partes2[2]
#     pto2=int(partes2[3])
    
    
    
#     ubic1 = participantes.index(parti1)
#     ubic2 = participantes.index(parti2)
   
#     if ganadores[ubic1][ubic2] == 1:
    
#         if pto1 > pto2:
#             ganadores[ubic1][ubic2]=pto1
#             perdedores[ubic1][ubic2]=pto2
#             if parti1 in cobra:
#                 cobrag += 1
#             elif parti1 in miyagi:
#                 miyagig +=1
#             elif parti1 in hito:
#                 hitog += 1
#             elif parti1 in dragon:
#                 dragong += 1
#             elif parti1 in shotokan:
#                 shotokang +=1
                
#             if parti2 in cobra:
#                 cobrap += 1
#             elif parti2 in miyagi:
#                 miyagip +=1
#             elif parti2 in hito:
#                 hitop += 1
#             elif parti2 in dragon:
#                 dragonp += 1
#             elif parti2 in shotokan:
#                 shotokanp +=1
                
#         else:
#             ganadores[ubic2][ubic1]=pto2
#             perdedores[ubic2][ubic1]=pto1
            
#             if parti2 in cobra:
#                 cobrag += 1
#             elif parti2 in miyagi:
#                 miyagig +=1
#             elif parti2 in hito:
#                 hitog += 1
#             elif parti2 in dragon:
#                 dragong += 1
#             elif parti2 in shotokan:
#                 shotokang +=1
                
#             if parti1 in cobra:
#                 cobrap += 1
#             elif parti1 in miyagi:
#                 miyagip +=1
#             elif parti1 in hito:
#                 hitop += 1
#             elif parti1 in dragon:
#                 dragonp += 1
#             elif parti1 in shotokan:
#                 shotokanp +=1
#     else:
        
#         amistosos += 1
    
#     linea2 = archivo2.readline().strip()

# puntos=[]

# for fil in range (len(participantes)):
#     suma = 0
#     for col in range (len(participantes)):
#         suma += ganadores[fil][col]
#     puntos.append(suma)



# print("1.")
# maximo = max(puntos)

# for fil in range (len(participantes)):
#     if puntos[fil] == maximo:
#         ganador =participantes[fil]
#         print("EL campeón fue",ganador)
       
#         dojoG = DojoPertenece(ganador)
#         print("Dojo:",dojoG)
        
# fila = participantes.index(ganador)
# colum = participantes.index(ganador)
# print("Los rivales que le ganaron 2 puntos fueron:")
# for col in range(len(participantes)):
#     if perdedores [fila][col] == 2:
#         print(participantes[col])
# for fil in range(len(participantes)):
#     if perdedores [fil][colum] == 2:
#         print(participantes[fil])
# print("2.")
# print("EL dojo que más peleas perdio fue:")
# minimo = max(cobrap,miyagip,hitop,shotokanp,dragonp)



# if cobrap==minimo:
#     print("Cobra Kai")
# elif miyagip == minimo:
#     print ("Miyagi Do")
# elif hitop == minimo:
#     print ("Hito Do")
# elif shotokanp == minimo:
#     print("Shotokan")
# elif dragonp == minimo:
#     print("Dragon")
    
# print (minimo, "peleas perdidas")

# print("3.")


# print("Cobra Kai:", round((cobrag/ (cobrag + cobrap))*100,2),"%")
# print("Miyagi Do:", round((miyagig/ (miyagig + miyagip))*100,2),"%")
# print("Hito Do:", round((hitog/ (hitog + hitop))*100,2),"%")
# print("Shotokan", round((shotokang/ (shotokang + shotokanp))*100,2),"%")
# print("Dragon:", round((dragong/ (dragong + dragonp))*100,2),"%")

# print("4.")  
# print("La cantidad de duelos amistosos registrados es:",amistosos)
