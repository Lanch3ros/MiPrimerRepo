'''
Universidad Escuela Colombiana de Ingeniería
Profesora: Ingeniera Patricia Salazar Perdomo

Lenguaje: Python

5. Calcular el producto de los valores que hay en una matriz de reales que no
   necesariamente es cuadrada. Los datos de la matriz ya se conocen.
   El producto debe quedar disponible en la función que la invoque
   (24391.86, en el caso del ejemplo).

   Ejemplo.	

    13.10   2.25
    -1.50  10.00
     8.41   6.56

'''

MAXF = 20
MAXC = 20

def prod_matriz (matrizz, filas, columnas):
  producto_total = 1
  for f in range (filas):
    for c in range (columnas):
      producto_total = producto_total * matrizz[f][c]
  return producto_total

                  
def escribe_mat (matriz, nf, nc):
  for f in range (0, nf):
    for c in range (0, nc):
      print (matriz[f][c], end = " ")
    print ("\n")

mat = [[13.1, 2.25],
       [-1.5, 10],
       [8.41, 6.56]]

nf = 3
nc = 2
       
# Ejemplo de invocación.
producto_total = prod_matriz (mat, nf, nc)
# La mando a imprimir para verificar el resultado.
escribe_mat (mat, nf, nc)
print (f"\nel producto de los valores que hay en la matriz es {producto_total}\n")
#escribe_mat ( )

