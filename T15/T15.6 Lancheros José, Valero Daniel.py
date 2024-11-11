'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y Programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Estudiante: Lancheros José, Valero Daniel
Lenguaje: Python

Referencia: Tarea No. 15

6.  Inicializar un vector con la suma de cada columna de una matriz.

'''

MCF = 20 # Máxima cantidad de filas.
MCC = 20 # Máxima cantidad de columnas.

def pide_entero_pos_max_msj (maxi, msj):
    num = 0
    while num <= 0 or num > maxi:
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
        
def escribe_vect_msj (vector, p, msj):
    print (msj) 
    for pos in range (p):
      print (vector [pos], end = " ")

def datos_de_entrada (m1):
      fil = pide_entero_pos_max_msj (MCF, "Cantidad de filas, máximo")
      col = pide_entero_pos_max_msj (MCC, "Cantidad de columnas, máximo")
      leemat_e_msj (m1, fil, col, "\nMATRIZ 1")
      return fil, col
def vector_suma (m1, fil,col):
      vector = [0 for p in range (fil)]
      for c in range (col):
            suma = 0
            for f in range (fil):
                  suma = suma + m1[f][c]
            vector[c] = suma
      return vector

            
def resultados (m1, fil, col,vector):
      escribe_mat_msj (m1, fil, col, "Matriz 1")
      escribe_vect_msj (vector, col, "EL vector de la suma de las columnas es:")

    
def main ( ):
      m1 = [[0 for c in range (MCC)] for f in range (MCF)]
      print ("\nHola")
      fil, col = datos_de_entrada (m1)
      vector = vector_suma (m1, fil,col)
      resultados (m1, fil, col,vector)
      print ("\nFINN.\n")

main ( )
