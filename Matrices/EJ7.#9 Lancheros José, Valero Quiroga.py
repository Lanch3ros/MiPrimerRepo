'''
Universidad Escuela Colombiana de Ingeniería
Profesora: Ingeniera Patricia Salazar Perdomo

Lenguaje: Python

9.Calcular el producto de los valores que hay en las filas impares (1, 3…) de una matriz real que no necesariamente
es cuadrada. Los datos de la matriz ya se conocen. El producto debe quedar disponible en la función que la invoque (en el
caso del ejemplo sería -13903.07).

   Ejemplo.	

    13.10   2.25
    -1.50  10.00
     8.41   6.56

'''

MAXF = 20
MAXC = 20

def prod_matriz (matrizz, filas, columnas):
  producto_total = 1
  for f in range (1, filas, 2):
    for c in range (columnas):
      producto_total *= matrizz[f][c]
  return producto_total

                  
def escribe_mat (matriz, nf, nc):
  for f in range (0, nf):
    for c in range (0, nc):
      print (matriz[f][c], end = " ")
    print ("\n")

matriz = [[4.1, 3.9, -1.1],
          [6.4, -5.1, 8.7],
          [3.0, 5.6, 9.2],
          [-2.0, -5.1, 4.8]]

nf = 4
nc = 3
       
# Ejemplo de invocación.
producto_total = prod_matriz (matriz, nf, nc)
# La mando a imprimir para verificar el resultado.
escribe_mat (matriz, nf, nc)
print (f"\nel producto de los valores que hay en la matriz es {producto_total}\n")