# -*- coding: utf-8 -*-

"""FUNCIONES - PROCEDIMIENTOS"""
def level_up(lista_nivel,lista_exp,lista_necesarios,posicion):
    if lista_exp[posicion]>=lista_necesarios[posicion]:
        lista_nivel[pos]+=1
        lista_necesarios[pos]+= round(lista_necesarios[pos]*1.05)
        #LA LISTA "NECESARIOS" REPRESENTA LA CANTIDAD DE EXPERIENCIA NECESARIA PARA CADA JUGADOR
        #PARA PODER SUBIR DE NIVEL, ESTAS CANTIDADES IRÁN AUMENTANDO CADA VEZ QUE SUBAN DE NIVEL
        
def calcular_fibra(recurso):
    cantidad_prima=0
    if recurso=='cáñamo':
        cantidad_prima=20
    elif recurso=='hierbasedosa':
        cantidad_prima=15
    elif recurso=='especias':
        cantidad_prima=10
    return cantidad_prima

def calcular_madera(recurso):
    cantidad_prima=0
    if recurso=='madera dura':
        cantidad_prima=30
    elif recurso=='madera de sino':
        cantidad_prima=60
    elif recurso=='pimpollo':
        cantidad_prima=45
    return cantidad_prima

def calcular_pieles(recurso):
    cantidad_prima=0
    if recurso=='jabalí':
        cantidad_prima=20
    elif recurso=='lobo':
        cantidad_prima=10
    elif recurso=='pavo':
        cantidad_prima=5
    return cantidad_prima

"""NOTAS PERSONALES"""
#-TENGO MIS DUDAS SOBRE LAS VERDADERAS RESPUESTAS CORRECTAS DE LAS EXPERIENCIAS.
#-QUISIERA SABER PUNTO POR PUNTO LOS ERRORES DE MI CODIGO, HE REALIZADO MUCHOS ANALISIS Y NO VEO EL ERROR.
"""MATERIAS PRIMAS"""
recursos=['jabalí','lobo','pavo','madera dura','madera de sino','pimpollo','cáñamo','hierbasedosa','especias']
productos= ['cuero','tablones','tela']
"""INVENTARIO"""
pieles=[]
maderas=[]
fibras=[]
total_tablones=0
menor=10**10
"""JUGADORES"""
players=[]
niveles=[]
experiencias=[]
necesarios=[]
"""LEER ARCHIVO"""
archivo= open("historial.txt","r",encoding='utf-8')
linea= archivo.readline().strip()
while linea!="":
    partes= linea.split(",")
    player= partes[0]
    objeto= partes[1].lower()
    #No se como se pusieron esos "Ticks" a la izquierda, ni idea qué presioné
    if player not in players:
        players.append(player)
        niveles.append(0)#TODOS COMIENZAN CON NIVEL 0
        experiencias.append(0)#TODOS COMIENZAN CON EXP 0
        necesarios.append(50)#CANTIDAD DE EXP NECESARIA PARA SUBIR DE NIVEL
        pieles.append(0)#SE AGREGARÁN 0 DEPENDIENDO DE LA CANTIDAD DE PLAYERS
        maderas.append(0)
        fibras.append(0)
        pos=players.index(player)#POSICION DEL JUGADOR
    else:
        pos=players.index(player)
        
    #IDENTIFICAR RECURSOS - CALCULO DE MATERIALES PRIMOS
    if objeto in recursos:
        recurso= partes[1].lower()
        experiencias[pos]+= 25+((niveles[pos])*10)
        
        if recurso=="jabalí" or recurso=="lobo" or recurso=="pavo":
            fabricacion= calcular_pieles(recurso)
            pieles[pos]+=fabricacion
            
        elif recurso=="madera dura" or recurso=="madera de sino" or recurso=="pimpollo":
            fabricacion= calcular_madera(recurso)
            maderas[pos]+=fabricacion
            
        elif recurso=="cáñamo" or recurso=="hierbasedosa" or recurso=="especias":
            fabricacion= calcular_fibra(recurso)
            fibras[pos]+=fabricacion
  
    #IDENTIFICAR PRODUCTOS - IMPRESIONES
    elif objeto in productos:
        producto= partes[1].lower()
        if producto=="cuero":
            materia_cuero= pieles[pos]//4
            if materia_cuero!=0:
                pieles[pos]= pieles[pos]%4
                experiencias[pos]+=materia_cuero*10
                print(f'{player} ha fabricado {materia_cuero} unidades de Cuero')
                
        elif producto=="tablones":
            materia_tablones= maderas[pos]//5
            if materia_tablones!=0:
                maderas[pos]= maderas[pos]%5
                total_tablones+=materia_tablones
                experiencias[pos]+=materia_tablones*10
                print(f'{player} ha fabricado {materia_tablones} unidades de Tablones') 
                
        elif producto=="tela":
            materia_tela= fibras[pos]//10
            if materia_tela!=0:
                fibras[pos]= fibras[pos]%10
                experiencias[pos]+=materia_tela*10
                print(f'{player} ha fabricado {materia_tela} unidades de Tela')
                
    level_up(niveles, experiencias, necesarios, pos)#CALCULAR EL NIVEL DE EXP
    linea= archivo.readline().strip()
if len(players)!=0:#CONTROL DE ERROR
    print("------------------------------")#RESPUESTAS A LAS PREGUNTAS
    print("2) Experiencia obtenida:")
    for i in range(len(players)):
        print(f"- {players[i]} nivel {niveles[i]} {experiencias[i]} xp")
    print()#ESPACIO VACÍO--------------------------------------------------
    print("3) Recursos:")
    for a in range(len(players)):
        print(f"- {players[a]} Piel {pieles[a]} Madera {maderas[a]} Fibra {fibras[a]}")
    print()#ESPACIO VACÍO--------------------------------------------------
    for b in range(len(players)):
        if maderas[b]<menor:
            menor=maderas[b]
            menor_player= players[b]
    print(f"4) El jugador que aprovechó mejor la madera fue: {menor_player}")
    print()#ESPACIO VACÍO--------------------------------------------------
    promedio= total_tablones/len(players)
    print(f"5) El promedio de Tablones fabricados fue: {promedio}")
else:
    print("No hay información")
