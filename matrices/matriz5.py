#Dada una matriz de Identidad nxn, mostrar el color azul solo si la diagonal es 1
from colorama import Fore, init
init(autoreset=True)
matriz = []
matrizI = []
for i in range(3):
    matriz.append([])
    for k in range(3):
        n = int(input(Fore.BLUE + "Ingrese un numero: "))
        matriz[i].append(n)
for i in matriz:
    print(i)

for k in range(len(matriz)):
    for j in range(len(matriz)):
            colorM = []
            if i ==j: 
                colorM = matriz[i][j]
                print(Fore.BLUE + (f"{colorM}"))

