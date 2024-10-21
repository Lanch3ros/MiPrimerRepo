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

# Función que determina si un número es primo
def es_primo(num):
    if num < 2: 
        return False
    for posdiv in range(2, num // 2 + 1):
        if num % posdiv == 0:
            return False
    return True

def escvec(v, tv):
    for pv in range(tv):
        print(v[pv], end=" ")
    print()

def cuenta_en_vector(v, tv, que):
    cont = 0
    for pv in range(tv):
        if v[pv] == que:
            cont += 1
    return cont

def en_conj_2_veces_primo(conjunto_1, c_elem_1, conjunto_2, c_elem_2):
    tercer_vector = []
    contador_primos = 0
    for i in range(c_elem_1):
        numero = conjunto_1[i]
        cantidad = cuenta_en_vector(conjunto_2, c_elem_2, numero)
        if es_primo(cantidad):
            tercer_vector.append(numero)
            contador_primos += 1

    return tercer_vector, contador_primos

# DATOS DE PRUEBA
conjunto_1 = [22, 7, 3, 4, 8, 1, 0, 11, 34, 41, 2, 70, 33, 13, 20]
c_elem_1 = 15
conjunto_2 = [66, 7, 11, 11, 13, 3, 5, 7, 0, 11, 13, 7, 13, 13, 4, 13, 5, 0]
c_elem_2 = 18

# Ejemplo de invocación
tercer_vector, contador_primos = en_conj_2_veces_primo(conjunto_1, c_elem_1, conjunto_2, c_elem_2)

# Verificación del resultado
print("Números del primer vector que aparecen en el segundo una cantidad de veces que es un número primo:")
escvec(tercer_vector, len(tercer_vector))
print(f"Cantidad de números que cumplen la condición: {contador_primos}")
