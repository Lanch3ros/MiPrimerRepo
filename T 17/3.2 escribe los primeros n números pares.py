'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y Programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Lenguaje: Python

Ejemplo 3.2. Escribir los primeros n números pares. Versión 2.
Observaciones:
- No se usa un contador.
'''

def primeros_n_pares_v2 ( ):
    print ("Escribo los primeros números pares.")
    n = int (input ("¿Cuántos quiere? "))
    print ("\nLos primeros", n, "números pares son:")
    par = 2
    while par <= 2 * n:       
        print (par, end = " ")
        par = par + 2
    print ("\n\nFin.")

primeros_n_pares_v2 ( )




