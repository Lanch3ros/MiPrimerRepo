'''
Universidad Escuela Colombiana de Ingeniería
Asignatura: Algoritmos y Programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Lenguaje: Python

Estudiante: Nombre (s) Apellidos

Ref.: Ejercicios No. 8 - Programa modular con listas

6. Construyan un programa modular para crear y escribir una lista de jugadores
   de baloncesto y cuyos registros tengan la siguiente estructura:

   [apellido, nombre, [estatura en metros, peso en kilogramos]]

   6.1 Cree la lista.
   6.2 Pida y valide la cantidad de jugadores.
   6.3 Pida los datos de los jugadores.
   6.4 Calcule el Índice de Masa Corporal (IMC) y agréguelo a la lista. IMC = peso en kg / (estatura en m)2

	[apellido, nombre, [estatura en metros, peso en kilogramos, imc]]
        Ejemplo: ["Segura", "Sonia", [1.70, 75.2, 26.02]]

   6.5 Escriba un reporte enumerado.

   Cada uno de los puntos se debe desarrollar en una función.

   Sugerencia: Reutilice todo lo que sea posible y que hayamos trabajado en el curso.
  
'''

def pide_ent_pos_msj (msj):
    n = -1	
    while n < 1:
        print (msj, "(>0)", end = " ")
        n = int (input ( ))
    return n

def main ( ):
    print ("Mensaje principal")

    print ("Mensaje de finalización")

main ( )
