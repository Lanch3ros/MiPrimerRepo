'''
UNIVERSIDAD ESCUELA COLOMBIANA DE INGENIERÍA

Asignatura: Algoritmos y Programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Estudiante (s): Lancheros José Luis
Ref.: Ejercicios No. 8. Funciones en Python con listas.

• Construir una función en Python que solucione el problema. 
• Escribir un ejemplo de invocación de la función.
• Hay que darles nombres significativos a las variables y a las funciones.
• Hacer pruebas suficientes a la función para asegurarse de que hace lo pedido.
• No se pide la solución modular completa.

Importante: 
El tema es listas. Por tanto, debe demostrar dominio del tema cubierto hasta
el momento, entre otros, el recorrido por contenido.
                                                                                                       	
4. Suponga que se tiene una lista de estudiantes con nombre y calificaciones de
   cada tercio en una asignatura. Por ejemplo:

   estudiantes = [["María Pérez", [4.3, 5.0, 4.5]],
                  ["Simón Durán", [4.0, 3.8, 3.5]],
                  ["María Pérez", [2.8, 3.5, 4.0]],
                  ["Ricardo Lozano", [2.0, 2.3, 2.5]],
                  ["Ángela Matiz", [3.2, 2.9, 3.3]],
                  ["Claudia Pinzón", [4.5, 4.5, 5.0]],
                  ["Silvia Urbina", [1.9, 1.7, 0.0]],
                  ["Gonzalo Quintana", [3.0, 2.9, 3.4]]]

   Construya una función en Python que guarde en otra lista los estudiantes y
   la definitiva, siempre y cuando esta última esté en un rango que también
   será enviado como argumento. Para el cálculo de la definitiva hay que tener
   en cuenta que las dos primeras calificaciones valen 30 %, cada una, y la
   tercera, 40 %.

   La lista debe quedar disponible en la función que invoque a ésta. Los datos
   pueden ser otros, con la misma estructura. Con los datos del ejemplo, si el
   rango fuera [1.0, 2.9], la lista quedaría así:
   
   [["Ricardo Lozano", 2.3], ["Silvia Urbina", 1.1]]

'''

# Definición de la función.
def estudiante_y_definitiva_int (estudiantes, li, ls):
   definitiva_est = []
   for dato in estudiantes:
      nombre = dato[0]
      nota_final = (dato[1][0]*0.3 + dato[1][1]*0.3 + dato[1][2]*0.4)
      if li <= nota_final <= ls:
         definitiva_est.append([nombre, nota_final])
   return definitiva_est

# Ejemplo de datos de prueba.
estudiantes = [["María Pérez", [4.3, 5.0, 4.5]],
               ["Simón Durán", [4.0, 3.8, 3.5]],
               ["María Pérez", [2.8, 3.5, 4.0]],
               ["Ricardo Lozano", [2.0, 2.3, 2.5]],
               ["Ángela Matiz", [3.2, 2.9, 3.3]],
               ["Claudia Pinzón", [4.5, 4.5, 5.0]],
               ["Silvia Urbina", [1.9, 1.7, 0.0]],
               ["Gonzalo Quintana", [3.0, 2.9, 3.4]]]


# Invocación.
print ("\nIngrese el intervalo")
li = float(input("Limite inferior: "))
ls = float(input("Limite superior: "))
resultado = estudiante_y_definitiva_int (estudiantes, li, ls)

# Verificación del resultado.
print (f"\nLista de estudiantes con definitiva entre {li} y {ls}.\n")
print (resultado)
