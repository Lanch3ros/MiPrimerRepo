'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y Programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Estudiante: Nombre(s) Apellidos, Nombre(s) Apellidos
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

def resultados ( ):
      print ("\nEN CONSTRUCCIÓN")
    
def main ( ):
      matriz = [[0 for c in range (MCC)] for f in range (MCF)]
      print ("\nMENSAJE PRINCIPAL")



      print ("\nMENSAJE DE FINALIZACIÓN.\n")

main ( )
