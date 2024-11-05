'''
Universidad Escuela Colombiana de Ingeniería
Profesora: Ingeniera Patricia Salazar Perdomo

Lenguaje: Python

10.Averiguar si cierto valor entero está en una matriz de enteros cuyos datos ya se conocen. En la función que invoque
a ésta, quedará disponible un 1, si el valor está, o 0 de lo contrario (0, en el caso del ejemplo). Y si la matriz es de otro
tipo, ¿sirve la misma función?
Ejemplo. Valor a buscar: 61


'''

MAXF = 20
MAXC = 20

def prod_matriz (matrizz, filas, columnas, num):
  esta_o_no = 0
  for f in range (filas):
    for c in range (columnas):
      if num == matrizz [f][c]:
        esta_o_no = 1

  return esta_o_no

                  
def escribe_mat (matriz, nf, nc):
  for f in range (0, nf):
    for c in range (0, nc):
      print (matriz[f][c], end = " ")
    print ("\n")

matriz = [[7, -11, -3],
          [12, 14, -4],
          [0, 6, 8]]

nf = 3
nc = 3
val_buscar = 61       
# Ejemplo de invocación.
esta_o_no = prod_matriz (matriz, nf, nc, val_buscar)
# La mando a imprimir para verificar el resultado.
escribe_mat (matriz, nf, nc)
print (f"\nsi el valor que se busca esta en la matriz, retorna 1 de lo contrario retorna 0. el #{val_buscar} es {esta_o_no}\n")