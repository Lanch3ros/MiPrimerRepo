'''
Universidad Escuela Colombiana de Ingeniería Algoritmos y
Programación (AYPR) Profesora: Ingeniera Patricia Salazar Perdomo

Estudiante: Lancheros Ayora José Luis

Lenguaje: Python Ref.: Tarea No. 13. Programación modular con vectores.

1. Programa modular que pide varios números enteros, los guarda en un vector,
   cuenta los impares, calcula el producto de los pares y luego escribe los
   resultados, incluidos los datos de entrada.

   Ver ejemplo y más detalles en el PDF.

IMPORTANTE:
- El programa modular debe estar formado por mínimo cuatro funciones,
  incluida la función principal main. 
  Los resultados los dará en una función aparte.
- Haré caso omiso de funciones que hagan lo pedido y no sean de su autoría.
- En la función main se debe ver claramente el plan de desarrollo de la solución del problema.
- Sólo debe utilizar lo que hemos visto en clase.
'''

TMAX = 100

def pide_entero_pos_max_msj (maxi, msj):
    num = 0
    while num <= 0 or num > maxi:
        print (msj, maxi, end = " ")
        num = int (input ( ))
    return num

def leevec_e (v, tv):
    print ("\nDatos del vector")
    for pos in range (0, tv):
        v [pos] = int (input ("Ingrese número entero "))

def c_imp_prod_pares (numeros, cn):
    c_impares = 0
    p_pares = 1
    for i in range (cn):
        if numeros[i] % 2 == 0:
            p_pares *= numeros[i]
        else:
            c_impares += 1
    if c_impares == cn:
        p_pares = 0
    
    return c_impares, p_pares

def escvec (v, tv):
    for pos in range (0, tv):
        print (v [pos], end = " ")

def resultados (numeros, cn, c_impares, p_pares):
    print ("\nRESULTADOS")
    print ("En los números dados:", end = " ")
    escvec (numeros, cn)
    print (f"hay {c_impares} impares y el producto de los pares es {p_pares}.")
    
def main ( ):
    numeros = [0 for p in range (TMAX)]
    print ("\nIngrese varios números enteros. Averiguaré la cantidad de impares")
    print ("y calcularé el producto de los números pares.")
    cn = pide_entero_pos_max_msj (TMAX, "\nCantidad de números, maximo")
    leevec_e (numeros, cn)
    c_impares, p_pares = c_imp_prod_pares (numeros, cn)
    resultados (numeros, cn, c_impares, p_pares)
    print ("\n\nFin.\n\n")

main ( )