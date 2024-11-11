'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y Programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Estudiante: Lancheros José, Valero Daniel
Lenguaje: Python

Referencia: Tarea No. 15

3.  Averiguar el mayor valor que hay en la diagonal principal de una matriz cuadrada de máximo 30 x 30
    y en qué posición está. 
'''

MCF = 30 # Máxima cantidad de filas.
MCC = 30 # Máxima cantidad de columnas.

def pide_ent_pos_msj (msj):
    n = -1	
    while n < 1:
        print (msj, "(>0)", end = " ")
        n = int (input ( ))
    return n

def valor_mayor (matrizz, filas, columnas):
      mayor_diagonal = matrizz[0][0]
      for f in range (filas):
           for c in range (columnas):
                if f == c:
                     if mayor_diagonal < matrizz [f][c]:
                          mayor_diagonal = matrizz[f][c] 
      return mayor_diagonal

def leemat_e (matriz, fil, col):
      for f in range (fil):
            for c in range (col):
                  matriz [f][c] = int (input ("\tNúmero entero: "))
      return matriz
     
def escribe_mat_msj (matriz, fil, col, msj):
    print (msj) 
    for f in range (fil):
        for c in range (col):
            print (matriz [f][c], end = " ")
        print ("\n") 

def resultados (matriz, filas, columnas, num_mayor):
      escribe_mat_msj (matriz, filas, columnas, "\nel numero mayor de la diagonal principal de la matriz :\n")
      print (f"es: {num_mayor}")

    
def main ( ):
      matriz = [[0 for c in range (MCC)] for f in range (MCF)]
      print ("\nCalculo el numero mayor de la diagonal principal de una matriz\n")
      filas = pide_ent_pos_msj ("# Filas\n")
      columnas =pide_ent_pos_msj ("# Columnas\n")
      matriz = leemat_e (matriz, filas, columnas)
      numero_mayor = valor_mayor (matriz, filas, columnas)
      resultados (matriz, filas, columnas, numero_mayor)
      print ("\nFin.\n")

main ( )