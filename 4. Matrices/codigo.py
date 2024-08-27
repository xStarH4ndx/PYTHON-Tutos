# -*- coding: utf-8 -*-
"""

"""

import numpy as np
mx= np.zeros([4,3])

ciudades=[]#fila
marcas=[]#columna

archivo= open("datos.txt","r",encoding='utf-8')
linea= archivo.readline().strip()
while linea!='':
    partes= linea.split(" ")
    if(len(partes)==1):
        ciudad= partes[0]
        if(ciudad not in ciudades):
            ciudades.append(ciudad)
    else:
        marca= partes[0]
        if(marca not in marcas):
            marcas.append(marca)
    
        for fila in range(len(ciudades)):
            for col in range(len(marcas)):
                if(ciudades[fila]==ciudad and marcas[col]==marca):
                    mx[fila,col]+=1
    
    linea= archivo.readline().strip()

print(mx)