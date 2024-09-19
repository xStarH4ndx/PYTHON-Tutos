# -*- coding: utf-8 -*-
"""CONSEJOS
EL POP(x) me permite borrar el valor de una posicion en especifico "x"
EL REMOVE(y) me permite eliminar el primer valor que encuentre de lo que le pida "y"
el APPEND(z) es para agregar un objeto "z" a la ultima posicion de la lista
"""


"""DETECTAR MAYOR EN LA LISTA"""
def maximo(lista):
    maximo=-1
    for i in lista:
        if i >maximo:
            maximo=i
    return maximo
# lista=[1,5,7,8,2,59,36]
# mayor= maximo(lista)
# print(mayor)

"""CALCULAR PROMEDIO DE UNA LSITA"""
def calcularPromedio(lista):
    suma=0
    tamaño_lista=len(lista)
    for i in range(0,tamaño_lista):
        suma= suma + lista[i]
    promedio= suma/tamaño_lista
    return promedio

"""ESTA FUNCION LEERÁ EL ARCHIVO Y PONDRA LOS NOMBRES EN UNA LISTA"""
def leer_nombres():
    nombres=[]
    archivo= open("texto.txt","r",encoding="utf-8")
    linea= archivo.readline().strip()
    while linea!="":
        nombre=linea
        nombres.append(nombre)
        linea= archivo.readline().strip()
    return nombres


"""ESTAS FUNCIONES VAN DE LA MANO SIEMPRE"""

#me dice si la "palabra" existe en la lista (true/false)
def está(palabra,lista):
    for i in lista:
        if i== palabra:
            return True
    return False


def obtener_nombres_unicos(nombres):
    lista_nombres=[]
    for i in nombres:
        if not está(i,lista_nombres):
            lista_nombres.append(i)
    return lista_nombres

def print_nombres(nombres):
        for i in nombres:
            print(i)
        
# nombres= leer_nombres()
# nombres_unicos= obtener_nombres_unicos(nombres)
# print_nombres(nombres_unicos)

"""ORDENAMIENTO BURBUJA"""
# for a in range(len(lista)-1):#comienza del primero al penultimo valor
#     for b in range (a+1,len(lista)):#comienza del segundo hasta el ultimo valor
#         if lista[a]> lista[b]:
#             aux= lista[a]
#             lista[a]= lista[b]
#             lista[b]= aux

"""ORDENAMIENTO BURBUJA NIVEL 2 --------- MEJORADO"""
def intercambiar(lista_1,pos1,pos2):
    aux= lista_1[pos1]
    lista[pos1]= lista_1[pos2]
    lista_1[pos2]= aux

def imprimir(lista_1,lista_2):
    for i in range(len(lista_1)):
        print(lista_1[i],lista_2[i])

lista=[5,8,2,6,3,9]
nombres=["f","g","h","i","j","k"]
imprimir(nombres,lista)

for a in range(len(lista)-1):#comienza del primero al penultimo valor
    for b in range (a+1,len(lista)):#comienza del segundo hasta el ultimo valor
        if lista[a]> lista[b]:
            #ordenar lista 1
            intercambiar(lista,a,b)
            intercambiar(nombres,a,b)
            
            
print("listas ordenadas")
imprimir(nombres,lista)



"""PARA ENCONTRAR LA POSICION DE ALGO, USAMOS ESTO"""
def indice(lista,valor):
    for i in range(0,len(lista)): #0 es opcional, pero el len(lista) es obligatorio
        if valor == lista[i]:#si el valor es = al valor de la lista
            return i# esto me dará la posición
    return -1# si el valor no está en la lista, significa que no existe
#no podemos imprimir los valores que no existen en la lista, porque nos entregará la posicion del ultimo valor

'''BURBUJA AVANZADA NIVEL 3 ----------------- MUY BUENA OPCIÓN'''
def intercambiar(lista,pos1,pos2):
    aux= lista[pos1]
    lista[pos1]= lista[pos2]
    lista[pos2]= aux

def burbuja(lista,direccion):
    for a in range(len(lista)-1):#comienza del primero al penultimo valor
        for b in range (a+1,len(lista)):#comienza del segundo hasta el ultimo valor
            if direccion==True:#ORDEN DESCENDENTE
                if lista[a]<lista[b]:
                    #ordenar lista 1
                    intercambiar(lista,a,b)

            else:#ORDEN ASCENDENTE
                if lista[a]>lista[b]:
                    #ordenar lista 1
                    intercambiar(lista,a,b)







