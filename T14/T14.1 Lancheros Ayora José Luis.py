"""
Universidad Escuela Colombiana de Ingeniería
Profesora: Ingeniera Patricia Salazar Perdomo

Estudiante: Lancheros Ayora José Luis

Lenguaje: Python
Referencia: Tarea No. 14. Programación modular con vectores.

1. El índice de masa corporal (IMC) permite estimar la cantidad de grasa
   corporal que tiene una persona y determinar, por tanto, si el peso está
   dentro del rango normal o no. 

   Construir una función en Python que calcule el índice de masa corporal (IMC)
   de cada integrante de cierta cantidad familias y, con base en éste, guarde
   en un vector la cantidad de integrantes de cada familia con peso normal o
   adecuado y en otro vector la cantidad total de integrantes bajos de peso,
   con sobrepeso u obesos, sin discriminar por ninguno de esos estados.
   
   El IMC de una persona se calcula como el cociente entre el peso en kilogramos
   y el cuadrado de la estatura en metros:
   
   IMC = peso / (estatura ^ 2)
   
   IMC                  Estado
   Menos de 18.5        Bajo de peso
   [18.5, 24.9]         Peso normal o adecuado
   [25.0, 29.9]         Sobrepeso
   Mayor o igual a 30.0 Obesidad
"""

def por_imc ():
    print ("\nFunción por_imc: La construye el estudiante.")


def resultados (familias, integrantes, cant_f, peso_nor, otro_peso):
    print ("\nResultados del cálculo del IMC por familia\n")
    n = 1
    for f in range (cant_f):
        print ("Familia:", familias [f])
        print ("\t Integrantes", integrantes [f])
        print ("\t Peso normal:", peso_nor [f])
        print ("\t Otro peso:", otro_peso [f])
        input ("\t\t\tPresione Enter para continuar ")



# DATOS DE PRUEBA.
familias = ["López", "Pérez", "Carmona", "Lugo", "Morales", "Durán", "Zapata", "Arnedo", "Ramos"]
integrantes = [3, 2, 4, 3, 5, 3, 6, 3, 4]
cant_f = 9

# Ejemplo de invocación.
por_imc ( )

# Verificación del resultado.
# La función resultados le podría servir. Siéntase en libertad de construir otra similar o mejor.
#resultados (familias, integrantes, cant_f, peso_nor, otro_peso)
