'''
PROBLEMA 1: ARTISTAS

- Debe de informar los artistas del momento del mes por país y mundial
- El archivo se llama artistas.txt

EL TXT CONTIENE: 
    Nombre del Artista
    Plataforma de publicación (Spotify o AppleMusic)
    Oyentes Semanales (Número generado de forma aleatoria entre un rango)
    Categoría del Artista (Urbano, Pop, Rock, etc.)
    Lugar de Nacimiento
'''

#VARIABLES PRINCIPALES
mayorGlobal=-1
mayorGlobalNombre=""

mayorSpotify=-1
mayorSpotifyNombre=""

mayorApple=-1
mayorAppleNombre=""

#LECTURA DE ARCHIVO
archivo= open("artistas.txt","r",encoding= 'utf-8')
linea= archivo.readline().strip()
while(linea!=''):
    partes= linea.split(',')
    pais= partes[0]
    cant_artistas= int(partes[1]) * 2
    
    #VARIABLES DINAMICAS
    mayorPais= -1
    mayorPaisNombre= ""
    
    for i in range(cant_artistas):
        linea= archivo.readline().strip()
        partes2= linea.split(',')
        artista= partes2[0]
        plataforma= partes2[1]
        oyentes= int(partes2[2])
        
        #CONDICIONALES
        if (oyentes>mayorGlobal):
            mayorGlobal= oyentes
            mayorGlobalNombre= artista
        
        if (oyentes>mayorPais):
            mayorPais= oyentes
            mayorPaisNombre= artista
        
        if (plataforma=="Spotify"):
            if(oyentes>mayorSpotify):
                mayorSpotify= oyentes
                mayorSpotifyNombre= artista
                
        elif (plataforma=="AppleMusic"):
            if(oyentes>mayorApple):
                mayorApple= oyentes
                mayorAppleNombre= artista
        
        categoria= partes2[3]
        
    print("El mejor artista del pais",pais,"es:",mayorPaisNombre,"con",mayorPais,"oyentes")
    linea= archivo.readline().strip()
    
#IMPRESIONES
print("-----")
print("El artista con más oyentes del mundo es:",mayorGlobalNombre,"\nCon",mayorGlobal,"oyentes")
print("\n---SPOTIFY---")
print("El artista con más oyentes es:",mayorSpotifyNombre,"\nCon",mayorSpotify,"oyentes")
print("\n---APPLEMUSIC---")
print("El artista con más oyentes es:",mayorAppleNombre,"\nCon",mayorApple,"oyentes")


