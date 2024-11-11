'''
Universidad Escuela Colombiana de Ingeniería
Profesora: Ingeniera Patricia Salazar Perdomo
Lenguaje: Python

Referencia: Funciones reutilizables de uso frecuente
'''
# PIDE UN ENTERO EN UN INTERVALO.

def pide_entero_interv (linf, lsup):
    print ("Ingrese un entero entre", linf, " y ", lsup, ": ", end = " ")
    num = int (input ( ))  
    while num < linf or num > lsup:
        print ("Ingrese un entero entre", linf, " y ", lsup, ": ", end = " ")
        num = int (input ( ))        
    return num

def pide_entero_interv_msj (linf, lsup, mensaje):
    num = linf - 1
    while num < linf or num > lsup:
        print (mensaje, " (entre", linf, "y", lsup, ")", end = " ")
        num = int (input ( ))
    return num

def pide_ent_pos_msj (msj):
    n = -1	
    while n < 1:
        print (msj, "(>0)", end = " ")
        n = int (input ( ))
    return n

def pide_entero_pos_max_msj (maxi, msj):
    num = 0
    while num <= 0 or num > maxi:
        print (msj, maxi, end = " ")
        num = int (input ( ))
    return num

# INICIALIZA UNA MATRIZ CON LOS DATOS QUE DA EL USUARIO.

def leemat_r (matriz, fil, col):
    for f in range (fil):
        for c in range (col):
            matriz [f][c] = float (input ("\tNúmero real: "))

def leemat_r_msj (matriz, fil, col, msj):
    print (msj)
    for f in range (fil):
        for c in range (col):
            matriz [f][c] = float (input ("\tNúmero real: "))

def leemat_e (matriz, fil, col):
    for f in range (fil):
        for c in range (col):
            matriz [f][c] = int (input ("\tNúmero entero: "))
            
def leemat_e_msj (matriz, fil, col, msj):
    print (msj)
    for f in range (fil):
        for c in range (col):
            matriz [f][c] = int (input ("\tNúmero entero: "))

def leemat_c (matriz, fil, col):
    for f in range (fil):
        for c in range (col):
            matriz [f][c] = input ("\tValor: ")
            
# ESCRIBE UNA MATRIZ.

def escribe_mat (matriz, fil, col):
    for f in range (fil):
        for c in range (col):
            print (matriz [f][c], end = " ")
        print ("\n")    

def escribe_mat_msj (matriz, fil, col, msj):
    print (msj) 
    for f in range (fil):
        for c in range (col):
            print (matriz [f][c], end = " ")
        print ("\n") 

def escribe_mat_e (matriz, fil, col):
    for f in range (fil):
        for c in range (col):
            print (format (matriz [f][c], "4d"), end = " ")
        print ("\n")

def escribe_mat_e_msj (matriz, fil, col, msj):
    print (msj)
    for f in range (fil):
        for c in range (col):
            print (format (matriz [f][c], "4d"), end = " ")
        print ("\n")
        
def escribe_mat_r (matriz, fil, col):
    for f in range (fil):
        for c in range (col):
            print (format (matriz [f][c], "5.1f"), end = " ")
        print ("\n")

def escribe_mat_r_msj (matriz, fil, col, msj):
    print (msj)
    for f in range (fil):
        for c in range (col):
            print (format (matriz [f][c], "5.1f"), end = " ")
        print ("\n")
        
