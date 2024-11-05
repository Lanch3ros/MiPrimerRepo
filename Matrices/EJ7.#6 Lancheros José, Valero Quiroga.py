'''
Universidad Escuela Colombiana de Ingeniería
Profesora: Ingeniera Patricia Salazar Perdomo

Lenguaje: Python

. Calcular y escribir el producto de los números que hay en las posiciones de la matriz con fila impar (1, 3,…) y
columna par (0, 2, …). La matriz es de números enteros y su máximo tamaño es 50×50. Los datos de la matriz ya se
conocen. El producto debe quedar disponible en la función que la invoque (-48, en el caso del ejemplo).

   Ejemplo.	

    7   -11    -3
    12  14     -4
    0    6     8  

'''


MAXF = 20
MAXC = 20

def prod_matriz (matrizz, filas, columnas):
  producto_total = 1
  for f in range (filas):
    for c in range (columnas):
      if f % 2 != 0 and c % 2 == 0:
         producto_total *= matrizz[f][c]
  return producto_total

                  
def escribe_mat (matriz, nf, nc):
  for f in range (0, nf):
    for c in range (0, nc):
      print (matriz[f][c], end = " ")
    print ("\n")

mat = [[7, -11, -3],
       [12, 14, -4],
       [0, 6, 8]]

nf = 3
nc = 3
       
# Ejemplo de invocación.
producto_total = prod_matriz (mat, nf, nc)
# La mando a imprimir para verificar el resultado.
escribe_mat (mat, nf, nc)
print (f"\nel producto de los valores que hay en la matriz es {producto_total}\n")