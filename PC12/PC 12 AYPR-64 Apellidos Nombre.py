'''
Universidad Escuela Colombiana de Ingeniería
Asignatura: Algoritmos y Programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Lenguaje: Python

Estudiante: Nombre (s) Apellidos

Ref.: Prueba corta 12

A la Asociación de Universidades de Bogotá (AUB) le llega cada semestre el dato
de cantidad de estudiantes nuevos en los programas de ingeniería de cada
institución socia.

Actualmente cuenta con los datos de tres años, almacenados en una tabla en la
que las filas son las universidades y las columnas, los semestres lectivos.

Como parte del análisis de los datos mencionados se requiere una función en
Python que inicialice dos vectores, uno con la menor cantidad de estudiantes
nuevos por universidad en un semestre y otro con la mayor cantidad. Los
vectores deben quedar disponibles donde se invoque la función. Con los datos
del ejemplo, serían:

20-1	320
20-2	600
20-1	700
20-1	714
20-2	650

Escriba un ejemplo de invocación de la función:
- Suponga que las variables son las del ejemplo y, por tanto, son las que debe
  usar.
- Tenga en cuenta que los datos podrían ser más, menos o diferentes.
- Recuerde que debe darles nombres significativos a las variables y a las
  funciones. Bajaré la calificación en 0.5 en caso de que no lo sean. 

Notas:
- La función es para los datos del ejemplo o para otros, organizados de
  manera similar.
- Recuerde que debe darles nombres significativos a las variables y a las
  funciones.
- No se pide el programa modular completo, pero sí se debe probar la función
  tantas veces como sea necesario para asegurarse de que hace lo que se pide.

'''

# Ejemplo de datos:
# Matriz con la cantidad de estudiantes por universidad y por semestre.
est_uxs = [[320, 750, 901, 950, 700, 783],
           [913, 600, 1200, 865, 902, 670],
           [700, 702, 780, 815, 830, 901],
           [714, 770, 1105, 940, 903, 960],
           [720, 650, 728, 802, 778, 782]]

# Vector con los nombres de las universidades.
nom_u = ["Los Cerezos", "Los Olivos", "Los Pinos", "Los Eucaliptos", "Los Abedules"]

# Vector con los nombres de los semestres.
nom_s = ["20-1","20-2","21-1","21-2","22-1","22-2"]

cu = 5 # Cantidad de universidades.
cs = 6 # Cantidad de semestres.
