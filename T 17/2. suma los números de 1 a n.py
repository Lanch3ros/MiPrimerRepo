'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y Programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Lenguaje: Python

Ejemplo 2. Sumar los números de 1 a n.

Observaciones:
- La variable num es un contador que a la vez contiene el número
  que se quiere sumar.
- La variable suma es un acumulador. En ella se lleva la suma.
'''

def suma_num_1_n ( ):
    print ("Sumo los números de 1 hasta donde me diga.")
    n = int (input ("¿Hasta dónde? "))
    suma = 0
    num = 1
    while num <= n:
        suma = suma + num
        num = num + 1
    print ("La suma de los números de 1 a", n, "es:", suma, end = ".")
    print ("\nFin.")

suma_num_1_n ( )



