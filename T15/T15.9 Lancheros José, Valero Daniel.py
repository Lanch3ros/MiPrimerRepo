'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y Programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Estudiante: Lancheros José, Valero Daniel
Lenguaje: Python

Referencia: Tarea No. 15

9.  Intercambiar el contenido de dos filas cualesquiera f1 y f2 de una matriz en la misma matriz.
    - La matriz no es necesariamente cuadrada.
    - La matriz de índices le podría ser útil.
    - La matriz se debe escribir antes y después del intercambio. 

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

def intercambiar_filas(matriz, f1, f2):
    matriz[f1], matriz[f2] = matriz[f2], matriz[f1]

def main():
    matriz = [[0 for c in range(MCC)] for f in range(MCF)]
    print("\nIntercambiar dos filas en una matriz.\n")
    filas = pide_ent_pos_msj("# Filas")
    columnas = pide_ent_pos_msj("# Columnas")
    matriz = leemat_e(matriz, filas, columnas)
    print("\nMatriz antes del intercambio:")
    escribe_mat_msj(matriz, filas, columnas, "")
    f1 = int(input("Ingrese el índice de la primera fila a intercambiar: "))
    f2 = int(input("Ingrese el índice de la segunda fila a intercambiar: "))
    if 0 <= f1 < filas and 0 <= f2 < filas:
        intercambiar_filas(matriz, f1, f2)
        print("\nMatriz después del intercambio:")
        escribe_mat_msj(matriz, filas, columnas, "")
    else:
        print("Error: Los índices de fila ingresados están fuera del rango.")
    print("\nFin del programa.\n")

main()

