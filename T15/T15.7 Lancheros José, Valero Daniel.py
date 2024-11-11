'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y Programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Estudiante: Lancheros José, Valero Daniel
Lenguaje: Python

Referencia: Tarea No. 15

7.  Sumar las potencias de 2 que haya en una matriz de números enteros positivos.
    Debe invocar a la función es_potencia_de_2 sin modificarla.

'''

MCF = 20  # Máxima cantidad de filas.
MCC = 20  # Máxima cantidad de columnas.

# La función es_potencia_de_2 retorna 1 si el parámetro num es potencia de 2 o 0 si no lo es.
def es_potencia_de_2(num):
    pot = 1
    while pot < num:
        pot = pot * 2
    if pot == num:
        return 1
    else:
        return 0

def pide_ent_pos_msj(msj):
    n = -1	
    while n < 1:
        print(msj, "(>0)", end=" ")
        n = int(input())
    return n

def suma_potencias_de_2(matriz, filas, columnas):
    suma = 0
    for f in range(filas):
        for c in range(columnas):
            if es_potencia_de_2(matriz[f][c]) == 1:
                suma += matriz[f][c]
    return suma

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

def resultados(matriz, filas, columnas, suma):
    escribe_mat_msj(matriz, filas, columnas, "\nMatriz ingresada:")
    print(f"\nLa suma de las potencias de 2 en la matriz es: {suma}")

def main():
    matriz = [[0 for c in range(MCC)] for f in range(MCF)]
    print("\nSuma de las potencias de 2 en una matriz.\n")
    filas = pide_ent_pos_msj("# Filas")
    columnas = pide_ent_pos_msj("# Columnas")
    matriz = leemat_e(matriz, filas, columnas)
    suma = suma_potencias_de_2(matriz, filas, columnas)
    resultados(matriz, filas, columnas, suma)
    print("\nFin del programa.\n")

main()

