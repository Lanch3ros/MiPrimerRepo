'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y Programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Estudiante: Lancheros José, Valero Daniel
Lenguaje: Python

Referencia: Tarea No. 15

11. Obtener la suma de los números que hay por debajo de la diagonal secundaria de una matriz cuadrada.
    La matriz de índices le puede ayudar.

'''

MCF = 20  # Máxima cantidad de filas.
MCC = 20  # Máxima cantidad de columnas.

def pide_ent_pos_msj(msj):
    n = -1	
    while n < 1:
        print(msj, "(>0)", end=" ")
        n = int(input())
    return n

def leemat_e(matriz, fil, col):
    for f in range(fil):
        for c in range(col):
            matriz[f][c] = int(input("\tNúmero entero: "))
    return matriz

def escribe_mat_msj(matriz, fil, col, msj):
    print(msj) 
    for f in range(fil):
        for c in range(col):
            print(matriz[f][c], end=" ")
        print("\n")

def suma_bajo_diagonal_secundaria(matriz, n):
    suma = 0
    for f in range(n):
        for c in range(n):
            if f + c > n - 1:
                suma += matriz[f][c]
    return suma

def resultados(matriz, n, suma):
    escribe_mat_msj(matriz, n, n, "\nMatriz ingresada:")
    print(f"\nLa suma de los elementos debajo de la diagonal secundaria es: {suma}")

def main():
    matriz = [[0 for c in range(MCC)] for f in range(MCF)]
    print("\nSuma de elementos debajo de la diagonal secundaria de una matriz cuadrada.\n")
    n = pide_ent_pos_msj("Ingrese el tamaño de la matriz cuadrada (n x n)")
    matriz = leemat_e(matriz, n, n)
    suma = suma_bajo_diagonal_secundaria(matriz, n)
    resultados(matriz, n, suma)
    print("\nFin del programa.\n")

main()

