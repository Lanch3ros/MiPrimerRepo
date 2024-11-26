'''
Universidad Escuela Colombiana de Ingeniería
Asignatura: Algoritmos y Programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Estudiante: Apellidos Nombre(s)
Ref.: Tarea No. 17. Listas.

A. Complete este programa modular que le doy en Python para que haga lo
   siguiente:

1. Pida el nombre, los apellidos y la fecha de nacimiento de n personas y
   guárdelos en una lista.
   
   La fecha la debe solicitar en la forma día, mes año y cada registro debe
   tener la siguiente estructura:

      [[nombre, apellidos, [día, mes, año]].
      Por ejemplo: [Rafael, Pombo, [15, 3, 1999]]

2. Cree una lista en la que el primer elemento contenga los nombres de las
   personas que cumplen en enero, el segundo elemento, los nombres de las que
   cumplen en febrero, y así sucesivamente. 

   Es posible que en un mes no cumpla nadie.

3. Imprimir la lista en la siguiente forma:
   Mes: cantidad de personas que cumplen en ese mes y los nombres de las
   personas.

   Ejemplo. 

   Enero. 3: Sandra Rogelio Javier
   Febrero. 4: Jaime Sara Gyna Édgar
   …

Todo lo que utilice debemos haberlo trabajado en el curso.
Favor consultarme en caso de duda.
'''

CM = 12 # Cantidad de meses de un año.

def pide_ent_pos_msj (que):
    n = -1	
    while n < 1:
        print (que, "(>0) ", end = " ")
        n = int (input ( ))
    return n

# En esta función se guardan los datos de n personas en la lista personas.
def entrada_datos (n, personas):
      print ("\n\tE N T R A D A   DE   D A T O S")
      for persona in range (n):
           print (f"\nPersona #{persona + 1}")
           nombre = input ("Nombre: ")
           apellido = input ("Apellido: ")
           print ("Ingrese la fecha de nacimiento: ")
           dia = int(input("Dia: "))
           mes = int(input("Mes: "))
           año = int(input("Año: "))
           personas.append([nombre, apellido, [dia, mes, año]])
      return personas

# En esta función se crea una lista con los nombres de las personas que cumplen
# años en determinado mes.
def cumple_un_mes ( ):
    print ("\n\tFunción en construcción.")

# En esta función se agregan 12 listas, una por mes, a la lista lista_cumplexmes.
def cumple_12_meses ( ):
    print ("\n\tFunción en construcción.")
    #cumple_un_mes ( )

# En esta función se escribe el reporte. Obsérvese que no se quieren los
# nombres entre comillas.
def resultados (personas):
    ct = 1
    for persona in personas:
         print (f"Persona #{ct}")
         print (persona)
         ct += 1

  
def main ( ):
      personas = [ ]
      lista_cumplexmes = [ ]
      meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
      print ("\n\tC U M P L E A Ñ O S   POR   M E S")
      n = pide_ent_pos_msj ("\n\n\tCantidad de personas")
      personas = entrada_datos (n, personas)
      cumple_12_meses ( )      
      resultados (personas)
      print ("\n\tFin.\n")

main ( )
