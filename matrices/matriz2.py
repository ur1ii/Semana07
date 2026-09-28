matrizP = []
for i in range (4):
    matrizA = int(input(f"Ingrese los dato #{i+1} de la matriz: "))
    matrizP.append(matrizA)
    
matriz = [
    [matrizP[0], matrizP[1]],
    [matrizP[2], matrizP[3]]
    ]
for fila in matriz:
    print(fila)



