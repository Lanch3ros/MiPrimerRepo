"""
Universidad Escuela Colombiana de Ingeniería
Profesora: Ingeniera Patricia Salazar Perdomo

Estudiante: Lancheros Ayora José Luis

Lenguaje: Python
Referencia: Tarea No. 14. Programación modular con vectores.

3. Se tienen dos vectores con números enteros positivos. Los vectores no son
   necesariamente del mismo tamaño. Construir una función en Python que
   inicialice un tercer vector con los números del primer vector que están en
   el segundo vector una cantidad de veces que es un número primo. También se
   quiere saber cuántos números satisficieron la condición.

   Para saber si la cantidad de veces es un número primo, debe invocar la
   función es_primo sin hacerle modificación alguna.  El vector y su tamaño
   deben quedar disponibles donde se invoque la función.

   Los datos de los vectores (contenido y tamaño) ya se conocen.
	
   Ejemplo:
   
   Conjunto de números 1 	22 7 3 4 8 1 0 11 34 41 2 70 33 13 20

   Conjunto de números2 	66 7 11 11 13 3 5 7 0 11 13 7 13 13 4 13 5 0

   Resultado. 4 números del primer conjunto están en el segundo conjunto
              una cantidad de veces que es un número primo:

              Vector de números que cumplen la condición 7 0 11 13

   Escriba un ejemplo de invocación. Recuerde la importancia de dar nombres
   significativos a las variables y a las funciones.
"""

# Averigua si el parámetro num es primo. Si lo es, retorna 1, y si no lo es, retorna 0.
def es_primo (num):
    if num < 2: 
       return 0
    for posdiv in range (2, num // 2 + 1):
        if num % posdiv == 0:
           return 0
        posdiv = posdiv + 1
    return 1

def escvec (v, tv):
    for pv in range (tv):
        print (v[pv], end = " ")
        
def cuenta_en_vector (v, tv, que):
    cont = 0
    for pv in range (tv):
        if v [pv] == que:
            cont = cont + 1
    return cont    


    
def en_conj_2_veces_primo ( ):
    print ("\nFunción en_conj_2_veces_primo: La construye el estudiante.")



# DATOS DE PRUEBA.
conjunto_1 = [22, 7, 3, 4, 8, 1, 0, 11, 34, 41, 2, 70, 33, 13, 20]
c_elem_1 = 15
conjunto_2 = [66, 7, 11, 11, 13, 3, 5, 7, 0, 11, 13, 7, 13, 13, 4, 13, 5, 0]
c_elem_2 = 18

# Ejemplo de invocación.
en_conj_2_veces_primo ( )

# Verificación del resultado.
