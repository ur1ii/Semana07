def sMatriz1():
    print("Primer ejemplo matriz")
    print("^"*60)
    print("Matriz")
    matriz = [
        [1, 2],
        [3, 4]
    ]

    for fila in matriz:
        print(fila)

    #Escalar
    k = 20
    matrizB = []
    for i in range(len(matriz)):
        matrizB.append([])
        for j in range(len(matriz)):
            matrizB[i].append(k * matriz[i][j])

    print("="*30)
    print("Escalar", k)

    for fila in matrizB:
        print(fila)
    print("^"*60)

