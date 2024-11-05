'''
Universidad Escuela Colombiana de Ingeniería
Profesora: Ingeniera Patricia Salazar Perdomo

Lenguaje: Python

8.Hallar el rango al que pertenecen los números que hay en una matriz. Los datos de la matriz ya se conocen. El resultado
debe quedar disponible en la función que la invoque ([-99, 111], en el caso del ejemplo).


   Ejemplo.	

    34      -99     -33  
    61      111     87
    0       56      48    
    3       6       31


'''

MAXF = 20
MAXC = 20

def prod_matriz (matrizz, filas, columnas):
  mayor = matrizz[0][0]
  menor = matrizz [0][0]
  for f in range (filas):
    for c in range (columnas):
        if matrizz[f][c] > mayor:
          mayor = matrizz [f][c]
        if matrizz [f][c] < menor:
          menor = matrizz [f][c]
  return mayor, menor

                  
def escribe_mat (matriz, nf, nc):
  for f in range (0, nf):
    for c in range (0, nc):
      print (matriz[f][c], end = " ")
    print ("\n")

mat = [[34, -99, -33],
        [61, 111, 87],
        [0, 56, 48],
        [3, 6, 31]]

nf = 4
nc = 3
       
# Ejemplo de invocación.
mayor, menor = prod_matriz (mat, nf, nc)
# La mando a imprimir para verificar el resultado.
escribe_mat (mat, nf, nc)
print (f"\nel rangoque hay en la matriz es desde {menor} hasta {mayor}\n")