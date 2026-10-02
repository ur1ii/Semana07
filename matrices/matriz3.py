#Leer 2 matrices 3x3 y sumar en una matriz

def sMatriz3():
    print("Leer 2 matrices 3x3 y sumar en una matriz")
    print("^"*60)
    print("--- Matriz 1 ---")
    matriz1 = []
    for i in range(3):
        matriz1.append([])
        for j in range(3):
            elemento = int(input(f"Ingrese un numero para el elemento {i}, {j}: "))
            matriz1[i].append(elemento)
    for i in matriz1:
        print(i)
    print("="*25)
    print("--- Matriz 2 ---")
    matriz2 = []
    for i in range(3):
        matriz2.append([])
        for j in range(3):
            elemento = int(input(f"Ingrese un numero para el elemento {i}, {j}: "))
            matriz2[i].append(elemento)
    for i in matriz2:
        print(i)
    print("="*25)
    print("--- Suma matriz ---")
    matrizSum = []
    for i in range(len(matriz1)):
        matrizSum.append([])
        for j in range(len(matriz1)):
            matrizSum[i].append(matriz1[i][j] + matriz2[i][j])
    for i in matrizSum:
        print(i)
    print("="*25)
    print("^"*60)

