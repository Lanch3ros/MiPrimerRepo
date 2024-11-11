'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y Programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Estudiante: Lancheros José, Valero Daniel
Lenguaje: Python

Referencia: Tarea No. 15

4.  Averiguar el mayor valor que hay en la diagonal secundaria de una matriz cuadrada de máximo 30×30 y
    en qué posición está. 

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

def datos_de_entrada (m1):
      fil = pide_entero_pos_max_msj (MCF, "Cantidad de filas, máximo")
      col = pide_entero_pos_max_msj (MCC, "Cantidad de columnas, máximo")
      leemat_e_msj (m1, fil, col, "\nMATRIZ 1")
      return fil, col
def mayor_diagonal_secundaria (m1,fil,col):
      mayor = m1[0][0]
      pos_fi = 0
      pos_co = 0
      for f in range (fil):
            for c in range (col):
                  if f + c == fil-1:
                        if mayor < m1[f][c]:
                              mayor = m1[f][c]
                              pos_fi = f
                              pos_co = c
      return mayor,pos_fi,pos_co
def resultados (m1,fil,col,pos_fi,pos_co,mayor):
      escribe_mat_msj (m1, fil, col, "Matriz 1")
      print ("EL número mayor en la diagonal secundaria es:")
      print (mayor)
      print ("Y esta en la fila:",pos_fi+1,"y en la columna",pos_co+1,"")
    
def main ( ):
      m1 = [[0 for c in range (MCC)] for f in range (MCF)]
      print ("\nHola, bienvenido a este programa")
      fil, col = datos_de_entrada (m1)
      mayor,pos_fi,pos_co = mayor_diagonal_secundaria (m1,fil,col)
      resultados (m1,fil,col,pos_fi,pos_co,mayor)



      print ("\nFINNN\n")

main ( )
