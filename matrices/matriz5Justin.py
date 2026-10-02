def sMatriz5():
    print("Matriz de identidad")
    print("^"*60)
    from colorama import Fore, Style

    n = 3
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
                print(Fore.BLUE + str(matriz[i][j]) + Style.RESET_ALL, end=" ")
            else:
                print(matriz[i][j], end=" ")
        print()
    print("^"*60)