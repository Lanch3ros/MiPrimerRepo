'''
UNIVERSIDAD ESCUELA COLOMBIANA DE INGENIERÍA

Asignatura: 	Algoritmos y Programación, grupo 64 (AYPR-64)
Profesora: 	Ingeniera Patricia Salazar Perdomo				 		    
Ref.: 		Ejercicios No. 7. Funciones en Python con matrices.
                                                                                                                      	
11. Se tiene una matriz con los caracteres de un texto. Construya la función
    descifra_texto que escriba el texto recorriendo la matriz de abajo hacia
    arriba y de derecha a izquierda.

Ejemplo.
.	o	r	t
s	e	a	m
	l	a	
e	c	a	h
	a	c	i
t	c	á	r
p		a	L

En el caso del ejemplo, el texto sería: La práctica hace al maestro.

La matriz y su tamaño ya se conocen. Escriba un ejemplo de invocación de la
función. Use los datos de prueba. Cuando se asegure de que hace lo que se
pide, cree otros con una matriz de tamaño diferente y otro mensaje.

Recuerde que debe darles nombres significativos a las variables y a las funciones.
'''

def descifra_texto (matrizz, filas, columnas):
    for f in range(filas - 1, -1, -1):
        for c in range(columnas - 1, -1, -1):
            print(matrizz[f][c], end="")
    print("\n")

                  
def escribe_mat (matriz, nf, nc):
  for f in range (0, nf):
    for c in range (0, nc):
      print (matriz[f][c], end = " ")
    print ("\n")


texto_cifrado = [['.', 'o', 'r', 't'],
                 ['s', 'e', 'a', 'm'],
                 [' ', 'l', 'a', ' '],
                 ['e', 'c', 'a', 'h'],
                 [' ', 'a', 'c', 'i'],
                 ['t', 'c', 'á', 'r'],
                 ['p', ' ', 'a', 'L']]

nf = 7
nc = 4

print ("El mensaje de la matriz:\n")
escribe_mat (texto_cifrado, nf, nc)
print ("es\n")
descifra_texto (texto_cifrado, nf, nc)



