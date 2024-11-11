'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y Programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Estudiante: Lancheros José, Valero Daniel
Lenguaje: Python

Referencia: Tarea No. 15

2.  Restar el contenido de dos matrices.

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

def datos_de_entrada (m1,m2):
      fil = pide_entero_pos_max_msj (MCF, "Cantidad de filas, máximo")
      col = pide_entero_pos_max_msj (MCC, "Cantidad de columnas, máximo")
      leemat_e_msj (m1, fil, col, "\nMATRIZ 1")
      leemat_e_msj (m2, fil, col, "\nMATRIZ 2")   
      return fil, col
def resta (m1,m2,fil,col):
      m3 =[[0 for c in range (col)] for f in range (fil)]
      for f in range (fil):
            for c in range (col):
                  m3[f][c]= m1[f][c] - m2[f][c]
      return m3
      
def resultados (m1,m2,m3,fil,col ):
      escribe_mat_msj (m1, fil, col, "Matriz 1")
      escribe_mat_msj (m2, fil, col, "Matriz 2")
      escribe_mat_msj (m3, fil, col, "Matriz resultante")
    
def main ( ):
      m1 = [[0 for c in range (MCC)] for f in range (MCF)]
      m2 = [[0 for c in range (MCC)] for f in range (MCF)]
      print ("\nHola, bienvenido a este programa")
      fil, col = datos_de_entrada (m1,m2)
      m3 = resta (m1,m2,fil,col)
      resultados (m1,m2,m3,fil,col )
      print ("\nFINN\n")

main ( )
