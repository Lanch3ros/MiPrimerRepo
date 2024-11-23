'''
Universidad Escuela Colombiana de Ingeniería
Asignatura: Algoritmos y Programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Lenguaje: Python

Estudiante: Lancheros José Luis

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

def datos_jug (jugadores):
    lista = []
    for jugador in range(jugadores):
        print (f"\nJugador #{jugador + 1}")
        nombre = str(input("Nombre: "))
        apellido = str(input("Apellido: "))
        estatura = float(input("Estatura(m): "))
        peso = float(input("Peso(kg): "))
        lista.append([apellido, nombre,[estatura, peso]])
    return lista

def calculo_imc (lista):
    for jugador in lista:
        imc = jugador[2][1] / jugador[2][0]**2
        jugador[2].append(imc)

def resultado (lista):
    for jugador in lista:
        ct = 1
        print (f"\nJugador #{ct}")
        print (f"{jugador[1]} {jugador[0]} mide {jugador[2][0]}m y pesa {jugador[2][1]}kg.")
        print (f"IMC = {round(jugador[2][2], 2)}")
        ct += 1

def pide_ent_pos_msj (msj):
    n = -1	
    while n < 1:
        print (msj, "(>0)", end = " ")
        n = int (input ( ))
    return n

def main ( ):
    print ("Bienvenido al programa de Jugadores de futbol, pedire la cantidad de jugadores, apellido, nombre, estatura y peso.")
    jugadores = pide_ent_pos_msj ("\nCantidad de jugadores")
    lista = datos_jug (jugadores)
    calculo_imc (lista)
    resultado (lista)
    print ("\nFin del programa")

main ( )
