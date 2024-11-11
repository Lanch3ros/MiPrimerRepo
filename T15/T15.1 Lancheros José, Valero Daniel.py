'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y Programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Estudiante: Nombre(s) Apellidos, Nombre(s) Apellidos
Lenguaje: Python

Referencia: Tarea No. 15

1.  Inicializar cada posición de una matriz con el resultado de a^b, donde la base (a) está en la primera
    matriz, y el exponente (b) está en la segunda.

'''

MCF = 20 # Máxima cantidad de filas.
MCC = 20 # Máxima cantidad de columnas.


def pide_ent_pos_msj (msj):
    n = -1	
    while n < 1:
        print (msj, "(>0)", end = " ")
        n = int (input ( ))
    return n

def leemat_e_msj (matrizzz, fil, col, msj):
    print (msj)
    for f in range (fil):
        for c in range (col):
            matrizzz [f][c] = int (input ("\tNúmero entero: "))

def a_pot_b (fil, col, mat_a, mat_b):
      mat_c = [[0 for columna in range (col)] for fila in range (fil)]
      for f in range (fil):
            for c in range (col):
                  mat_c[f][c] = mat_a [f][c] ** mat_b [f][c]
      return mat_c

def escribe_mat_msj (matrizz, fil, col, msj):
    print (msj)
    for f in range (fil):
        for c in range (col):
            print (matrizz [f][c], end = " ")
        print ("\n")    

def resultados (matriz1, matriz2, matriz3, fila, columna):
     escribe_mat_msj (matriz1, fila, columna, "\nLa primera matriz\n" )
     escribe_mat_msj (matriz2, fila, columna, "\nelevada a la segunda matriz\n")
     escribe_mat_msj (matriz3, fila, columna, "\nNos da como resultado la siguiente matriz:\n")

def main ( ):
      m1 = [[0 for c in range (MCC)] for f in range (MCF)]
      m2 = [[0 for c in range (MCC)] for f in range (MCF)]
      print ("\nPido 2 matrices (1 y 2), creo la matriz resultante 3 que es la matriz 1 elevada a la matriz  2.")
      filas = pide_ent_pos_msj ("# Filas")
      columnas = pide_ent_pos_msj ("# Columnas")
      leemat_e_msj (m1, filas, columnas, "Matriz 1")
      leemat_e_msj (m2, filas, columnas, "Matriz 2")
      mat3 = a_pot_b (filas, columnas, m1, m2)
      resultados (m1, m2, mat3, filas, columnas)

      print ("\nFin del programa.\n")

main ( )
