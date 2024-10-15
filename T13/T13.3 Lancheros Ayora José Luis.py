'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y Programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo

Estudiante: Lancheros Ayora José Luis

Lenguaje: Python 
Ref.: Tarea No. 13. Programación modular con vectores. 

3. Programa modular que pide varios números enteros y dos intervalos [x, y] y
   (p, q); calcula la cantidad y la suma de los números impares que pertenezcan
   a la intersección de los intervalos. Luego, escribe el resultado, incluidos
   los datos de entrada.
   
   Ver ejemplo y más detalles en el PDF.

IMPORTANTE:
- El programa modular debe estar formado por mínimo cuatro funciones, incluida la función principal main. 
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

def pide_interv_e (intervalo, extremo_inf, extremo_sup):
    print ("\nIntervalo", intervalo)
    li = 1
    ls = 0
    while li >= ls:
        li = int (input (extremo_inf))
        ls = int (input (extremo_sup))
    return [li, ls]

def pide_intervalos ( ):
    [x, y] = pide_interv_e ("[x, y]", "\t\tx = ", "\t\ty = ")
    [p, q] = pide_interv_e ("(p, q)", "\t\tp = ", "\t\tq = ")
    return [x, y, p, q]
    
def cantidad_suma_impares (numeros, x, y, p, q, cn):
    ct_impares = 0
    suma_impares = 0
    for i in range (cn):
        if numeros[i] % 2 != 0:
            if x <= numeros[i] <= y and p < numeros[i] < q:
                ct_impares += 1
                suma_impares += numeros[i]
    return ct_impares, suma_impares
    
def escvec (v, tv):
    for pos in range (0, tv):
        print (v [pos], end = " ")

def resultados (numeros, cn, x, y, p, q, ct_impares, suma_impares):
    print ("\nRESULTADOS")
    print ("En los números dados:", end = " ")
    escvec (numeros, cn)
    print (f"hay {ct_impares} impares que pertenecen a la")
    print (f"intersección de los intervalos [{x}, {y}] y [{p}, {q}] y suman {suma_impares}.")
    
def main ( ):
    numeros = [0 for p in range (TMAX)]
    print ("\nIngrese varios números enteros, así como los límites de dos")
    print ("intervalos [x, y] y (p, q). Calcularé la cantidad y la suma de los")
    print ("números impares que pertenecen a la intersección de los intervalos.")
    cn = pide_entero_pos_max_msj (TMAX, "\nCantidad de números, maximo")
    leevec_e (numeros, cn)
    [x, y, p, q] = pide_intervalos ( )
    ct_impares, suma_impares = cantidad_suma_impares (numeros, x, y, p, q, cn)

    resultados (numeros, cn, x, y, p, q, ct_impares, suma_impares)

    print ("\n\nFin.\n\n")

    
main ( )