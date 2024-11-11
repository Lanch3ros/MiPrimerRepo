'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y Programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Estudiante: Lancheros José, Valero Daniel
Lenguaje: Python

Referencia: Tarea No. 15

5.  Inicializar un vector con la suma de cada fila de una matriz.

'''

MCF = 20  # Máxima cantidad de filas.
MCC = 20  # Máxima cantidad de columnas.

def pide_ent_pos_msj(msj):
    n = -1	
    while n < 1:
        print(msj, "(>0)", end=" ")
        n = int(input())
    return n

def suma_fila_matriz(matriz, filas, columnas):
    suma_fila = [0 for f in range(filas)]
    for f in range(filas):
        for c in range(columnas):
            suma_fila[f] += matriz[f][c]
    return suma_fila

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

def resultados(matriz, filas, columnas, suma_fila):
    escribe_mat_msj(matriz, filas, columnas, "\nMatriz ingresada:\n")
    print(f"\nLa suma de cada fila es: {suma_fila}\n")

def main():
    matriz = [[0 for c in range(MCC)] for f in range(MCF)]
    print("\nCalculo un vector con la suma de cada fila de una matriz.\n")
    filas = pide_ent_pos_msj("# Filas")
    columnas = pide_ent_pos_msj("# Columnas")
    matriz = leemat_e(matriz, filas, columnas)
    suma_fila = suma_fila_matriz(matriz, filas, columnas)
    resultados(matriz, filas, columnas, suma_fila)
    print("\nFin.\n")

main()
