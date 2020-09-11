import os
from random import randint, uniform 
#randint => genera numeros enteros
#uniform => genera numeros reales

#funciones
def pedir_entero():
    correcto= False
    num = 0
    while(not correcto):
        try:
            num = int(input("Elige un nivel: "))
            correcto=True
        except ValueError:
            print("Opción no valida")
    return num

def rand_integer():
    nz = randint(1,6)
    return nz


#menu de niveles

opcion = 0
juno=0
jdos=0
duno=0
ddos=0

os.system("cls")

while opcion != 4:
    print ("Nivel 1")
    print ("Nivel 2")
    print ("Nivel 3")
    print ("Salir")

    opcion = pedir_entero()

    if opcion == 1:
        juno=0
        jdos=0
        print ("Nivel 1 consta de 50 casillas, quién llegue primero gana.")
        while juno <= 50 or jdos <= 50:
            os.system("cls")
            input("Presione enter para tirar dados de jugador uno")
            duno = rand_integer()
            ddos = rand_integer()
            print ("jugador uno sacó " , duno ,"y ", ddos)
            juno = juno + duno + ddos

            input("Presione enter para tirar dados de jugador dos")
            duno = rand_integer()
            ddos = rand_integer()
            print ("jugador dos sacó " , duno ,"y ", ddos)
            jdos = jdos + duno + ddos

            if juno >= 50:
                print ("El jugador uno ganó")
                break
            elif jdos >= 50:
                print ("El jugador dos ganó")
                break
                
            print ("Totales hasta el momento")
            print ("jugador uno: ", juno)
            print ("jugador dos: ", jdos)
            
    if opcion == 2:
        juno=0
        jdos=0
        print ("Nivel 1 consta de 70 casillas, quién llegue primero gana.")
        while juno <= 70 or jdos <= 70:
            os.system("cls")
            input("Presione enter para tirar dados de jugador uno")
            duno = rand_integer()
            ddos = rand_integer()
            print ("jugador uno sacó " , duno ,"y ", ddos)
            juno = juno + duno + ddos

            input("Presione enter para tirar dados de jugador dos")
            duno = rand_integer()
            ddos = rand_integer()
            print ("jugador dos sacó " , duno ,"y ", ddos)
            jdos = jdos + duno + ddos

            if juno >= 70:
                print ("El jugador uno ganó")
                break
            elif jdos >= 70:
                print ("El jugador dos ganó")
                break
                
            print ("Totales hasta el momento")
            print ("jugador uno: ", juno)
            print ("jugador dos: ", jdos)

    if opcion == 3:
        juno=0
        jdos=0
        print ("Nivel 1 consta de 100 casillas, quién llegue primero gana.")
        while juno <= 100 or jdos <= 100:
            os.system("cls")
            input("Presione enter para tirar dados de jugador uno")
            duno = rand_integer()
            ddos = rand_integer()
            print ("jugador uno sacó " , duno ,"y ", ddos)
            juno = juno + duno + ddos

            input("Presione enter para tirar dados de jugador dos")
            duno = rand_integer()
            ddos = rand_integer()
            print ("jugador dos sacó " , duno ,"y ", ddos)
            jdos = jdos + duno + ddos

            if juno >= 100:
                print ("El jugador uno ganó")
                break
            elif jdos >= 100:
                print ("El jugador dos ganó")
                break
                
            print ("Totales hasta el momento")
            print ("jugador uno: ", juno)
            print ("jugador dos: ", jdos)
            
    if opcion > 3:
        print ("Adiós")
        opcion = 4

            
        
        
        
    
