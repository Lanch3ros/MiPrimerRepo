'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y Programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Estudiante: Daniel Valero Quiroga
Lenguaje: Python

Referencia: Tarea No. 15

10. Intercambiar el contenido de dos columnas cualesquiera c1 y c2 de una matriz en la misma matriz. 
    - La matriz no es necesariamente cuadrada.
    - La matriz de índices le podría ser útil.
    - La matriz se debe escribir antes y después del intercambio. 

'''

MCF = 20 # Máxima cantidad de filas.
MCC = 20 # Máxima cantidad de columnas.

def pide_entero_pos_max_msj (maxi, msj):
    num = -1
    while num < 0 or num > maxi:
        print (msj, maxi-1, end = " ")
        num = int (input ( ))
    return num
def pide_entero_pos_max_msj_1 (maxi, msj):
    num = -1
    while num < 0 or num > maxi:
        print (msj, maxi, end = " ")
        num = int (input ( ))
    return num


def leemat_e_msj (matriz, fil, col, msj):
    print (msj)
    for f in range (fil):
        for c in range (col):
            matriz [f][c] = int (input ("\tNúmero entero: "))

def escribe_mat_msj (matriz, fil, col, msj):
    print (msj) 
    for f in range (fil):
        for c in range (col):
            print (matriz [f][c], end = " ")
        print ("\n")

def datos_de_entrada (m1):
      fil = pide_entero_pos_max_msj_1 (MCF, "Cantidad de filas, máximo")
      col = pide_entero_pos_max_msj_1 (MCC, "Cantidad de columnas, máximo")
      leemat_e_msj (m1, fil, col, "\nMATRIZ 1")
      return fil, col



def intercambiar_filas_msj(matriz, c1, c2, fil, col):
    print("\nMatriz antes del intercambio:")
    escribe_mat_msj(matriz, fil, col, "MATRIZ ANTES DEL INTERCAMBIO")

    for f in range(fil):
        matriz[f][c1], matriz[f][c2] = matriz[f][c2], matriz[f][c1]

    print("\nMatriz después del intercambio:")
    escribe_mat_msj(matriz, fil, col, "MATRIZ DESPUÉS DEL INTERCAMBIO")




def main ( ):
      matriz = [[0 for c in range (MCC)] for f in range (MCF)]
      fil, col = datos_de_entrada (matriz)
      c1 = pide_entero_pos_max_msj(fil, "Índice de la primera columna. de 0 a")
      c2 = pide_entero_pos_max_msj(fil, "Índice de la segunda fila. de 0 a")
      intercambiar_filas_msj(matriz, c1, c2, fil, col)

main ( )
