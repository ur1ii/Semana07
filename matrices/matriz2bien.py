def sMatriz2():
    print("Matriz modificable")
    print("^"*60)
    matriz = []
    filas = int(input("Ingrese el numero de filas: "))
    colunmas = int(input("Ingrese el numero de columnas: "))

    for f in range(filas):
        matriz.append([])
        for c in range(colunmas):
            num = int(input("Ingrese un numero: "))
            matriz[f].append(num)
    for f in matriz:
        print(f)
    print("^"*60)

