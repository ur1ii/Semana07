#Multiplicacion de matrices cuadradas 2x2
matrizA = []
matrizB = []
matrizC = []

print("--- Ingrese los valores de la matriz #1")
for f in range(2):
    matrizA.append([])
    for c in range(2):
        n = int(input("Ingrese un numero: "))
        matrizA[f].append(n)
for f in matrizA:
    print(f)

print("--- Ingrese los valores de la matriz #2")
for f in range(2):
    matrizB.append([])
    for c in range(2):
        n = int(input("Ingrese un numero: "))
        matrizB[f].append(n)
for f in matrizB:
    print(f)

print("--- Multiplicacion ---")
for f in range(len(matrizA)):
    matrizC.append([])
    for j in range(len(matrizA)):
        matrizC[f].append(matrizA[f][c] * matrizB[f][c])

for f in matrizC:
    print(f)

