'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y Programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo

Estudiante: Lancheros Ayora José Luis

Lenguaje: Python 
Ref.: Tarea No. 13. Programación modular con vectores. 

2. Programa modular que pide varios números reales y la misma cantidad de números
   enteros que se guardan en dos vectores, respectivamente.

   Hay que inicializar un tercer vector con el resultado de elevar cada número
   del primer vector al valor entero que haya en el segundo vector, en la misma
   posición. Luego, escribe el resultado, incluidos los datos de entrada.

   Ver ejemplo y más detalles en el PDF.

IMPORTANTE:
- El programa modular debe estar formado por mínimo cuatro funciones, incluida la función principal main. 
  Los resultados los dará en una función aparte.
- Haré caso omiso de funciones que hagan lo pedido y no sean de su autoría.
- En la función main se debe ver claramente el plan de desarrollo de la solución del problema.
- Sólo debe utilizar lo que hemos visto en clase.
'''

TMAX = 100

def pide_entero_pos_max_msj(maxi, msj):
    num = 0
    while num <= 0 or num > maxi:
        print(msj, maxi, end=" ")
        num = int(input())
    return num

def leevec_e_msj(v, tv, msj):
    print(msj)
    for pos in range(tv):
        v[pos] = int(input("# "))

def leevec_r_msj(v, tv, msj):
    print(msj)
    for pos in range(tv):
        v[pos] = float(input("# "))

def inic_vector_potencias(reales, enteros, potencias, cn):
    # Eleva cada número real a la potencia del número entero correspondiente
    for i in range(cn):
        potencias[i] = reales[i] ** enteros[i]

def escvec_msj(v, tv, msj):
    print(msj)
    for pos in range(tv):
        print(v[pos], end=" ")
    print()  # Para salto de línea después de mostrar el vector

def resultados(reales, enteros, potencias, cn):
    print("\nRESULTADOS")
    escvec_msj(reales, cn, "\nBASES:")
    escvec_msj(enteros, cn, "\nEXPONENTES:")
    escvec_msj(potencias, cn, "\nRESULTADO DE LAS POTENCIAS:")

def main():
    reales = [0 for p in range(TMAX)]  # Vector para los números reales
    enteros = [0 for p in range(TMAX)]  # Vector para los números enteros
    potencias = [0 for p in range(TMAX)]  # Vector para almacenar los resultados de las potencias

    print("\nIngrese varios números reales y la misma cantidad de números enteros.")
    print("Elevaré cada número real a cada número entero.")
    
    cn = pide_entero_pos_max_msj(TMAX, "\nCantidad de números, maximo")
    
    leevec_r_msj(reales, cn, "\nNúmeros reales (bases):")
    leevec_e_msj(enteros, cn, "\nNúmeros enteros (potencias):")
    
    # Calcular las potencias
    inic_vector_potencias(reales, enteros, potencias, cn)

    resultados(reales, enteros, potencias, cn)
    
    print("\n\nFin.\n\n")

main()
