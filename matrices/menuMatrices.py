import matriz1 as m1
import matriz2bien as m2
import matriz3 as m3
import matriz4 as m4
import matriz5Justin as m5
import os
import msvcrt

def menu():
    while True:
        os.system('cls')
        print("--- Menu ---")
        print("1. Ejemplos de matriz ")
        print("2. Ingresar los datos de una matriz ")
        print("3. Leer matrices 3x3 y sumar ")
        print("4. Multiplicacicion de matrices 2x2")
        print("5. Matriz de Identidad ")
        print("6. Salir")
        while True:
            try:
                op = int(input("Ingrese una opcion: "))
                if op > 0 and op < 7:
                    break
                else: print("Error, ingrese un numero en rango.")
            except ValueError:
                print("Error, ingrese un numero.")

        print("^"*60)      
        match op:
            case 1: 
                m1.sMatriz1()
            case 2:
                m2.sMatriz2()
            case 3:
                m3.sMatriz3()
            case 4:
                m4.sMatriz4()
            case 5:
                m5.sMatriz5()
            case 6:
                print("Adios...")
                break
        print("\nPresiona cualquier tecla para continuar...")
        msvcrt.getch() 

if __name__ == "__main__":
    menu()
