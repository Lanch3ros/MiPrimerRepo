'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y Programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Lenguaje: Python

Ejemplo 3.1. Escribir los primeros n números pares. Versión 1.
'''

def primeros_n_pares ( ):
    print ("Escribo los primeros números pares.")
    n = int (input ("¿Cuántos quiere? "))
    print ("\nLos primeros", n, "números pares son:")
    par = 2
    cont = 1
    while cont <= n:       
        print (par, end = " ")
        par = par + 2
        cont = cont + 1
    print ("\n\nFin.")

primeros_n_pares ( )



