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
2. Los tipos de sangre son O, A, B y AB. El factor Rhesus (Rh) es una proteína
   heredada que se encuentra en la superficie de los glóbulos rojos. Si la
   sangre contiene esta proteína, la persona es Rh positivo. Si la sangre carece
   de ella, es Rh negativo. Rh positivo es el grupo sanguíneo más frecuente.
   Tomado de https://es.wikipedia.org/wiki/Factor_Rh
   En general, las personas que no somos ilustradas en el tema, decimos que el
   tipo de sangre es A+ u O-, por ejemplo, sin que sea preciso. Haciendo caso
   omiso del concepto real, suponga que se tiene una lista con los siguientes
   datos de varios estudiantes:

   Carné, tipo de sangre y sexo. El tipo de sangre es O+, A+, B+, AB+, O-, A-,
   B- y AB-. El sexo será f (femenino) o m (masculino). Por ejemplo:

   datos_est = [["3567", "A+", 'm'],  ["1122", "A+", 'f'], ["4432", "O+", 'f'], ["8734", "O-", 'm'],  ["1290", "B+", 'f'], ["6512", "A+", 'm'], ["6523", "A-", 'm'], ["9008", "B-", 'm'], ["8745", "A+", 'f'],  ["3131", "A-", 'm'], ["8811", "A+", 'f']]

   Construya una función en Python que inicialice una lista con todos los datos
   de los estudiantes de cierto sexo y cierto tipo de sangre. La misma función
   debe servir para cualquier combinación de esos dos datos que se especifiquen
   como argumentos.

   La lista debe quedar disponible donde se invoque la función.

'''

# Definición de la función.
def filtra_sexo_y_sangre(datos_est, sexo, tipo_sangre):
   filtrados = []
   for dato in datos_est:
     if dato[2] == sexo and dato[1] == tipo_sangre:
       filtrados.append(dato)
   return filtrados

# Ejemplo de datos.
datos_est = [
    ["3567", "A+", 'm'], ["1122", "A+", 'f'], ["4432", "O+", 'f'], ["8734", "O-", 'm'],
    ["1290", "B+", 'f'], ["6512", "A+", 'm'], ["6523", "A-", 'm'], ["9008", "B-", 'm'],
    ["8745", "A+", 'f'], ["3131", "A-", 'm'], ["8811", "A+", 'f']
]

# Invocación del filtro.
sexo = input ("Sexo(f o m): ")
sangre = input ("Tipo de sangre: ")
resultado = filtra_sexo_y_sangre(datos_est, sexo, sangre)

# Verificación del resultado.
print (f"\nEstudiantes filtrados por sexo = {sexo} y tipo sangre = {sangre}:\n")
print(resultado)