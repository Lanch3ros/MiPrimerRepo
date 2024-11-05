'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y Programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Estudiante: Nombre(s) Apellidos, Nombre(s) Apellidos
Lenguaje: Python

Referencia: Tarea No. 15

7.  Sumar las potencias de 2 que haya en una matriz de números enteros positivos.
    Debe invocar a la función es_potencia_de_2 sin modificarla.

'''

MCF = 20 # Máxima cantidad de filas.
MCC = 20 # Máxima cantidad de columnas.

# La función es_potencia_de_2 retorna 1 si el parámetro num es potencia de 2
# o 0 si no lo es.
def es_potencia_de_2 (num):
    pot = 1
    while pot < num:
        pot = pot * 2
    if pot == num:
        return 1 
    else:
        return 0 

def resultados ( ):
      print ("\nEN CONSTRUCCIÓN")
    
def main ( ):
      matriz = [[0 for c in range (MCC)] for f in range (MCF)]
      print ("\nMENSAJE PRINCIPAL")



      print ("\nMENSAJE DE FINALIZACIÓN.\n")

main ( )
