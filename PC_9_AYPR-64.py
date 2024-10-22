'''
Universidad Escuela Colombiana de Ingeniería
Profesora: Ingeniera Patricia Salazar Perdomo

Estudiante: Lancheros Ayora José Luis

Lenguaje: Python
Referencia: Prueba corta No. 9. Programación modular con vectores.

Se tienen dos vectores. uno con los nombres de las asignaturas (nom_as) de
cierto plan de estudios y otro con la calificación promedio obtenida
(calif_prom). Los vectores y su tamaño (cant_as) ya se conocen. 

a. Construya una función en Python que averigüe el nombre de la asignatura con
   la menor calificación promedio y cuál fue. Los resultados deben quedar
   disponibles donde se invoque la función. Es decir, no debe escribirlos en
   ella.
   Escriba un ejemplo de invocación (tenga en cuenta los nombres de las
   variables que se dan).  

b. Construya una función en Python que averigüe la cantidad de asignaturas con
   calificación promedio que pertenezca al intervalo [3.0, mayor calificación
   promedio (uno de los resultados de la parte a que no debe averiguar de nuevo)].
   El resultado debe quedar disponible donde se invoque la función. Es decir,
   no debe escribirlo en ella.
   Escriba un ejemplo de invocación (tenga en cuenta los nombres de las
   variables que se dan).  
'''

print ("\nPARTE a.")

# Definición de la función.
def calc_mayor_calif_y_nom (nombre, calif_p, materias):
   calif_mayor = 0
   materia_mayor = " "
   for i in range (materias):
      if calif_p[i] > calif_mayor:
         calif_mayor = calif_p[i]
         materia_mayor = nombre[i]

   return calif_mayor, materia_mayor

# Datos de prueba.
nom_as = ["CALD", "CIPP", "AYPR", "FIEM", "HGCL"]
calif_prom = [3.1, 4.2, 4.1, 4.0, 2.8]
cant_as = 5

# Ejemplo de invocación.
calif_mayor, materia_mayor = calc_mayor_calif_y_nom (nom_as, calif_prom, cant_as)

# Verificación del resultado.
print (f"La materia con la califficacion promedio mas alta es {materia_mayor} y es {calif_mayor}.")

print ("\nPARTE b.")

# Definición de la función.
def materias_en_intervalo (calif, materias, calif_mayor):
   ct_as = 0
   for i in range (materias):
      if calif[i] >= 3 and calif[i] <= calif_mayor:
         ct_as += 1
   return ct_as

# Ejemplo de invocación.

ct_as = materias_en_intervalo (calif_prom, cant_as, calif_mayor)

# Verificación del resultado.
print (f"Hay {ct_as} de materias que se encuentran en el intervalo [3, {calif_mayor}].\n")