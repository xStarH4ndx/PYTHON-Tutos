# -*- coding: utf-8 -*-

"""Problema 1"""
votos_gob1=0
votos_gob2=0
votos_gob3=0

mayor_gob=""
mayor_votos_gob=-1

tota_votos=0
suma_votos=0

mayor_votos_alcalde=-1
mayor_alcalde=""
total_votos_alcalde=0

menor_votos_alcalde=10**10
menor_alcalde=""

print("Bienvenidos al sistema de votaciones")

print("La ciudad es Coquimbo") 
#GOBERNADOR
print("Ingresar votos del candidato gobernador Zulantay")
votos_gobernador= int(input())
while votos_gobernador<0:
    votos_gobernador= int(input("Ingrese votos validos: "))
votos_gob1+=votos_gobernador
suma_votos+=votos_gobernador

print("Ingresar votos del candidato gobernador Naranjo")
votos_gobernador= int(input())
while votos_gobernador<0:
    votos_gobernador= int(input("Ingrese votos validos: "))
votos_gob2+=votos_gobernador
suma_votos+=votos_gobernador

print("Ingresar votos del candidato gobernador Cifuentes")
votos_gobernador= int(input())
while votos_gobernador<0:
    votos_gobernador= int(input("Ingrese votos validos: "))
votos_gob3+=votos_gobernador
suma_votos+=votos_gobernador

#ALCALDES
print("Ingresar nombre del candidato a alcalde 1")
alcalde_1= input().lower()

print("Ingresar cantidad de votos para",alcalde_1)
votos_alcalde=int(input())
while votos_alcalde<0:
    votos_alcalde= int(input("Ingrese votos validos: "))

if votos_alcalde>mayor_votos_alcalde:
    mayor_votos_alcalde= votos_alcalde
    mayor_alcalde= alcalde_1
if votos_alcalde<menor_votos_alcalde:
    menor_votos_alcalde= votos_alcalde
    menor_alcalde=alcalde_1
    
suma_votos+=votos_alcalde    
total_votos_alcalde+=votos_alcalde

print("Ingresar nombre del candidato a alcalde 2")
alcalde_2= input().lower()

print("Ingresar cantidad de votos para",alcalde_2)
votos_alcalde=int(input())
while votos_alcalde<0:
    votos_alcalde= int(input("Ingrese votos validos: "))

if votos_alcalde>mayor_votos_alcalde:
    mayor_votos_alcalde= votos_alcalde
    mayor_alcalde= alcalde_2
if votos_alcalde<menor_votos_alcalde:
    menor_votos_alcalde= votos_alcalde
    menor_alcalde=alcalde_2

suma_votos+=votos_alcalde 
total_votos_alcalde+=votos_alcalde

print("Ingresar nombre del candidato a alcalde 3")
alcalde_3= input().lower()

print("Ingresar cantidad de votos para",alcalde_3)
votos_alcalde=int(input())
while votos_alcalde<0:
    votos_alcalde= int(input("Ingrese votos validos: "))

if votos_alcalde>mayor_votos_alcalde:
    mayor_votos_alcalde= votos_alcalde
    mayor_alcalde= alcalde_3
if votos_alcalde<menor_votos_alcalde:
    menor_votos_alcalde= votos_alcalde
    menor_alcalde=alcalde_3

suma_votos+=votos_alcalde 
total_votos_alcalde+=votos_alcalde

print("Ingresar nombre del candidato a alcalde 4")
alcalde_4= input().lower()

print("Ingresar cantidad de votos para",alcalde_4)
votos_alcalde=int(input())
while votos_alcalde<0:
    votos_alcalde= int(input("Ingrese votos validos: "))

if votos_alcalde>mayor_votos_alcalde:
    mayor_votos_alcalde= votos_alcalde
    mayor_alcalde= alcalde_4
if votos_alcalde<menor_votos_alcalde:
    menor_votos_alcalde= votos_alcalde
    menor_alcalde=alcalde_4

suma_votos+=votos_alcalde 
total_votos_alcalde+=votos_alcalde

print("Ingresar votos blancos para alcaldes")
votos_blancos= int(input())
while votos_blancos<0:
    votos_blancos= int(input("Ingrese votos validos: "))

suma_votos+=votos_blancos
total_votos_alcalde+=votos_blancos

print("Ingresar votos nulos para alcaldes")
votos_nulos= int(input())
while votos_nulos<0:
    votos_nulos= int(input("Ingrese votos validos: "))

suma_votos+=votos_nulos
total_votos_alcalde+=votos_nulos

porcentaje= 100*(mayor_votos_alcalde/total_votos_alcalde)
porcentaje2= 100*(menor_votos_alcalde/total_votos_alcalde)
print("Total de votos: ",suma_votos)
print("El alcalde ganador es",mayor_alcalde,"con",mayor_votos_alcalde,"votos con",round(porcentaje,0),"% de un total de",total_votos_alcalde,"sumando los blancos",votos_blancos)
print("Menor votos",menor_alcalde,"con",menor_votos_alcalde,"y un porcentaje del ",round(porcentaje2,0),"del total de votos")
print("Cantidad de blancos",votos_blancos)
print("Cantidad de nulos",votos_nulos)
print("La ciudad es Coquimbo")


"""--------------------------------------LA SERENA---------------------------------------"""
print("La ciudad es La Serena") 
#GOBERNADOR
print("Ingresar votos del candidato gobernador Zulantay")
votos_gobernador= int(input())
while votos_gobernador<0:
    votos_gobernador= int(input("Ingrese votos validos: "))

votos_gob1+=votos_gobernador  
suma_votos+=votos_gobernador

print("Ingresar votos del candidato gobernador Naranjo")
votos_gobernador= int(input())
while votos_gobernador<0:
    votos_gobernador= int(input("Ingrese votos validos: "))
votos_gob2+=votos_gobernador
suma_votos+=votos_gobernador

print("Ingresar votos del candidato gobernador Cifuentes")
votos_gobernador= int(input())
while votos_gobernador<0:
    votos_gobernador= int(input("Ingrese votos validos: "))
votos_gob3+=votos_gobernador
suma_votos+=votos_gobernador

#ALCALDES
print("Ingresar nombre del candidato a alcalde 1")
alcalde_1= input().lower()

print("Ingresar cantidad de votos para",alcalde_1)
votos_alcalde=int(input())
while votos_alcalde<0:
    votos_alcalde= int(input("Ingrese votos validos: "))

if votos_alcalde>mayor_votos_alcalde:
    mayor_votos_alcalde= votos_alcalde
    mayor_alcalde= alcalde_1
if votos_alcalde<menor_votos_alcalde:
    menor_votos_alcalde= votos_alcalde
    menor_alcalde=alcalde_1
    
suma_votos+=votos_alcalde    
total_votos_alcalde+=votos_alcalde

print("Ingresar nombre del candidato a alcalde 2")
alcalde_2= input().lower()

print("Ingresar cantidad de votos para",alcalde_2)
votos_alcalde=int(input())
while votos_alcalde<0:
    votos_alcalde= int(input("Ingrese votos validos: "))

if votos_alcalde>mayor_votos_alcalde:
    mayor_votos_alcalde= votos_alcalde
    mayor_alcalde= alcalde_2
if votos_alcalde<menor_votos_alcalde:
    menor_votos_alcalde= votos_alcalde
    menor_alcalde=alcalde_2

suma_votos+=votos_alcalde 
total_votos_alcalde+=votos_alcalde

print("Ingresar nombre del candidato a alcalde 3")
alcalde_3= input().lower()

print("Ingresar cantidad de votos para",alcalde_3)
votos_alcalde=int(input())
while votos_alcalde<0:
    votos_alcalde= int(input("Ingrese votos validos: "))

if votos_alcalde>mayor_votos_alcalde:
    mayor_votos_alcalde= votos_alcalde
    mayor_alcalde= alcalde_3
if votos_alcalde<menor_votos_alcalde:
    menor_votos_alcalde= votos_alcalde
    menor_alcalde=alcalde_3

suma_votos+=votos_alcalde 
total_votos_alcalde+=votos_alcalde

print("Ingresar nombre del candidato a alcalde 4")
alcalde_4= input().lower()

print("Ingresar cantidad de votos para",alcalde_4)
votos_alcalde=int(input())
while votos_alcalde<0:
    votos_alcalde= int(input("Ingrese votos validos: "))

if votos_alcalde>mayor_votos_alcalde:
    mayor_votos_alcalde= votos_alcalde
    mayor_alcalde= alcalde_4
if votos_alcalde<menor_votos_alcalde:
    menor_votos_alcalde= votos_alcalde
    menor_alcalde=alcalde_4

suma_votos+=votos_alcalde 
total_votos_alcalde+=votos_alcalde

print("Ingresar votos blancos para alcaldes")
votos_blancos= int(input())
while votos_blancos<0:
    votos_blancos= int(input("Ingrese votos validos: "))

suma_votos+=votos_blancos
total_votos_alcalde+=votos_blancos

print("Ingresar votos nulos para alcaldes")
votos_nulos= int(input())
while votos_nulos<0:
    votos_nulos= int(input("Ingrese votos validos: "))

suma_votos+=votos_nulos
total_votos_alcalde+=votos_nulos

porcentaje= 100*(mayor_votos_alcalde/total_votos_alcalde)
porcentaje2= 100*(menor_votos_alcalde/total_votos_alcalde)
print("Total de votos: ",suma_votos)
print("El alcalde ganador es",mayor_alcalde,"con",mayor_votos_alcalde,"votos con",round(porcentaje,0),"% de un total de",total_votos_alcalde,"sumando los blancos",votos_blancos)
print("Menor votos",menor_alcalde,"con",menor_votos_alcalde,"y un porcentaje del ",round(porcentaje2,0),"del total de votos")
print("Cantidad de blancos",votos_blancos)
print("Cantidad de nulos",votos_nulos)
print("La ciudad es La Serena")

if votos_gob1>votos_gob2 and votos_gob1>votos_gob3:
    mayor_gob="Zulantay"
    mayor_votos_gob=votos_gob1
elif votos_gob2>votos_gob1 and votos_gob2>votos_gob3:
    mayor_gob="Naranjo"
    mayor_votos_gob=votos_gob2
elif votos_gob3>votos_gob1 and votos_gob3>votos_gob2:
    mayor_gob= "Cifuentes"
    mayor_votos_gob=votos_gob3

print("Resultados gobernadores")
print("Votos totales para Zulantay",votos_gob1)
print("Votos totales para Naranjo",votos_gob2)
print("Votos totales para Cifuentes",votos_gob3)
print("Gobernador con mayor votos",mayor_gob,"con",mayor_votos_gob)





