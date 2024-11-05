'''
Universidad Escuela Colombiana de Ingeniería
Profesora: Ingeniera Patricia Salazar Perdomo

Lenguaje: Python

7. Hallar el mayor de los números positivos y pares que haya en la matriz. Los datos de la matriz ya se conocen. El mayor
debe quedar disponible en la función que la invoque (56, en el caso del ejemplo). Si no hay positivos pares en la matriz, el
valor que quedará disponible será -1.


   Ejemplo.	

    34      -99     -33      93
    61      11      87       111
    0       56      48      -8  

'''


MAXF = 20
MAXC = 20

def prod_matriz (matrizz, filas, columnas):
  mayor = -1
  for f in range (filas):
    for c in range (columnas):
        if matrizz[f][c] % 2 == 0 and matrizz[f][c] > 0:
            if mayor < matrizz[f][c]:
                mayor = matrizz[f][c]
  return mayor

                  
def escribe_mat (matriz, nf, nc):
  for f in range (0, nf):
    for c in range (0, nc):
      print (matriz[f][c], end = " ")
    print ("\n")

mat = [[34, -99, -33, 93],
       [61, 11, 87, 111],
       [0, 56, 48, -8]]

nf = 3
nc = 4
       
# Ejemplo de invocación.
mayor = prod_matriz (mat, nf, nc)
# La mando a imprimir para verificar el resultado.
escribe_mat (mat, nf, nc)
print (f"\nel numero par mayor que hay en la matriz es {mayor}\n")