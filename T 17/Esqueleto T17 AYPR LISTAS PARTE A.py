'''
Universidad Escuela Colombiana de Ingeniería
Asignatura: Algoritmos y Programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Estudiante: Lancheros Jose, Valero Daniel
Ref.: Tarea No. 17. Listas.

A. Complete este programa modular que le doy en Python para que haga lo
   siguiente:

1. Pida el nombre, los apellidos y la fecha de nacimiento de n personas y
   guárdelos en una lista.
   
   La fecha la debe solicitar en la forma día, mes año y cada registro debe
   tener la siguiente estructura:

      [[nombre, apellidos, [día, mes, año]].
      Por ejemplo: [Rafael, Pombo, [15, 3, 1999]]

2 . Con base en el resultado de la función del punto 1, función que cree una 
    lista con los nombres de las personas que cumplen en un mes que le llega
    como parámetro (1 – 12). La lista sólo contendrá los nombres, ningún otro dato.

3. Cree una lista en la que el primer elemento contenga los nombres de las
   personas que cumplen en enero, el segundo elemento, los nombres de las que
   cumplen en febrero, y así sucesivamente. 

   Es posible que en un mes no cumpla nadie.

4. Imprimir la lista en la siguiente forma:
   Mes: cantidad de personas que cumplen en ese mes y los nombres de las
   personas.

   Ejemplo. 

   Enero. 3: Sandra Rogelio Javier
   Febrero. 4: Jaime Sara Gyna Édgar
   …

Todo lo que utilice debemos haberlo trabajado en el curso.
Favor consultarme en caso de duda.
'''

CM = 12  # Cantidad de meses de un año.

def pide_ent_pos_msj(que):
    n = -1
    while n < 1:
        print(que, "(>0) ", end=" ")
        n = int(input())
    return n

# En esta función se guardan los datos de n personas en la lista personas.
def entrada_datos(n, personas):
    print("\n\tE N T R A D A   D E   D A T O S")
    for persona in range(n):
        print(f"\nPersona #{persona + 1}")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        print("Ingrese la fecha de nacimiento: ")
        dia = int(input("Día: "))
        mes = int(input("Mes: "))
        año = int(input("Año: "))
        personas.append([nombre, apellido, [dia, mes, año]])

# En esta función se crea una lista con los nombres de las personas que cumplen años en determinado mes.
def cumple_un_mes(personas, mes):
    filtrados = []
    for persona in personas:
        if persona[2][1] == mes:
            filtrados.append(persona[0])
    return filtrados

# En esta función se agregan 12 listas, una por mes, a la lista lista_cumplexmes.
def cumple_12_meses(personas, lista_cumplexmes):
    for mes in range(1, CM + 1):
        lista_cumplexmes.append(cumple_un_mes(personas, mes))

# En esta función se escribe el reporte.
def resultados(lista_cumplexmes, meses):
    print("\n\tR E P O R T E   D E   C U M P L E A Ñ O S\n")
    for i in range(CM):
        cantidad = len(lista_cumplexmes[i])
        nombres = " ".join(lista_cumplexmes[i])
        print(f"{meses[i]}. {cantidad}: {nombres}")

def main():
    personas = []
    lista_cumplexmes = []
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    print("\n\tC U M P L E A Ñ O S   P O R   M E S")
    n = pide_ent_pos_msj("\n\n\tCantidad de personas")
    entrada_datos(n, personas)
    cumple_12_meses(personas, lista_cumplexmes)
    resultados(lista_cumplexmes, meses)
    print("\n\tFin.\n")

main()
