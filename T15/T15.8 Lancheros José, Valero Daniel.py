'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y Programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Estudiante: Lancheros José, Valero Daniel
Lenguaje: Python

Referencia: Tarea No. 15

8.  Contar los números primos que haya en una matriz de números enteros positivos. Debe invocar a la función
    es_primo sin modificarla.

'''

MCF = 20 # Máxima cantidad de filas.
MCC = 20 # Máxima cantidad de columnas.

# La función es_primo retorna 1 si el parámetro num es primo
# o 0 si no lo es.
def es_primo (num):
    if num <= 1:
        return 0
    for posdiv in range (2, num // 2 + 1):
        if num % posdiv == 0:
            return 0
    return 1

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

def cont_primos (m1,fil,col):
    cont = 0
    for f in range (fil):
        for c in range (col):
            num = m1[f][c]
            if es_primo (num) == 1:

                cont = cont + 1
    return cont

def datos_de_entrada (m1):
      fil = pide_entero_pos_max_msj (MCF, "Cantidad de filas, máximo")
      col = pide_entero_pos_max_msj (MCC, "Cantidad de columnas, máximo")
      leemat_e_msj (m1, fil, col, "\nMATRIZ 1")
      return fil, col

def resultados (m1,fil,col,cont ):
      escribe_mat_msj (m1, fil, col, "MATRIZ:")
      print("Hay ",cont," números primos")

    
def main ( ):
      m1 = [[0 for c in range (MCC)] for f in range (MCF)]
      fil, col = datos_de_entrada (m1)
      cont = cont_primos  (m1,fil,col)
      resultados (m1,fil,col,cont )
      print ("\nFINN\n")

main ( )
