'''
Clase 1
Condicionales y Ciclos For

Contexto: Elaborar un programa que calcule si el alumno aprobó o reprobó sus asignaturas
'''

'''FORMA 1'''

# '''VARIABLES GLOBALES'''
# nombre= input("Ingrese el nombre del estudiante: ")
# cant_ramos= int(input("Ingrese cantidad de ramos: "))

# for i in range(cant_ramos):
#     nota1= float(input("Ingrese nota 1: "))
#     nota2= float(input("Ingrese nota 2: "))
#     suma_notas= (nota1*0.45)+(nota2*0.55)
    
#     print("----")
#     print("El promedio es:",round(suma_notas,2))
#     if(suma_notas>=4):
#         print("Aprobado")
#     elif(suma_notas<4):
#         print("Reprobado")
#     elif(suma_notas>3.4 and suma_notas<4):
#         print("Recalificación")
    

'''Variables globales'''
nombre= input("Ingrese el nombre del estudiante: ")
cant_ramos= int(input("Ingrese cantidad de ramos: "))

promedio_general=0
for j in range(cant_ramos):
    ramo= input("Asignatura: ")
    suma_notas=0
    
    for k in range(2):
        nota= float(input(f"Ingrese nota: {k+1}: "))
        
        if(k==0):
            nota*=0.45
        else:
            nota*=0.55
            
        suma_notas+= nota
    
    promedio_general+=suma_notas
    
    print("----")
    print("El promedio en",ramo,"es:",round(suma_notas,2))
    if(suma_notas>=4):
        print("Aprobado")
    elif(suma_notas>3.4 and suma_notas<4):
        print("Recalificación")
    else:
        print("Reprobado")

promedio_general/=cant_ramos
print("------------")
print("El promedio general es de:",round(promedio_general,2))



