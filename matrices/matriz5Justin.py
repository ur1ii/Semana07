
from colorama import Fore, Style

n = 2
matriz = []

for i in range(n):
    fila = []
    for j in range(n):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)

for i in range(n):
    for j in range(n):
        if i == j:
            print(Fore.BLUE + str(matriz[i][j] + Style.RESET_ALL, end=" "))
        else:
            print(matriz[i][j], end=" ")
    print()