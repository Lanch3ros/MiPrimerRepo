'''
Universidad Escuela Colombiana de Ingeniería
Asignatura: Algoritmos y Programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Lenguaje: Python

Estudiante: Lancheros Ayora José Luis

Ref.: Prueba corta 13

- El tema es listas. Por tanto, debe demostrar dominio del tema cubierto hasta
  el momento, entre otros, el recorrido por contenido. De no ser así,
  calificaré sobre 3.0.
- Los datos pueden ser los de los ejemplos u otros con la misma estructura.
- Haré caso omiso del código que no corresponda a lo visto en clase.

Suponga que se tiene una lista en la que cada elemento es una lista con el
nombre del estudiante y las calificaciones en cada tercio en una asignatura. 

Es decir, cada registro tiene la estructura: [nombre_est, [ t1, t2, t3]]

1. Construya una función en Python que averigüe la calificación promedio de
   todos los estudiantes en la asignatura. Las tres calificaciones valen igual
   (promedio aritmético). La calificación promedio debe quedar disponible donde
   se invoque la función.
2. Construya una función en Python que averigüe la calificación mayor en cierto
   tercio y el nombre del estudiante que la obtuvo. Ese cierto tercio será un
   argumento. La misma función debe servir para cualquiera de los tres tercios. 

   La calificación mayor y el nombre del estudiante deben quedar disponibles donde
   se invoque la función.

   Con los datos del ejemplo, si se tratara del primer tercio, los valores que
   quedarían disponibles serían 4.5 y Claudia Pinzón, si fuera el segundo, 
   serían 5.0 y María Pérez, y si fuera el tercero, 4.8 y Claudia Pinzón.

Escriba un ejemplo de invocación para cada parte 1 y 2. Recuerde lo importante
que es darles nombres significativos a las variables y a las funciones.

Notas:
- Las funciones son para los datos del ejemplo o para otros, organizados de
  manera similar.
- No se pide el programa modular completo, pero sí se debe probar cada función
  tantas veces como sea necesario para asegurarse de que hace lo que se pide.
'''
#Parte 1
def calc_cali_prom (est):
    prom_f  = []
    for dato in est:
        prom = (dato[1][0] + dato[1][1] + dato[1][2]) / 3
        prom_f.append(prom)
    return prom_f

# Ejemplo de datos:
estudiantes = [["María Pérez", [4.3, 5.0, 4.5]], ["Simón Durán", [4.0, 3.8, 3.5]], ["María Pérez", [2.8, 3.5, 4.0]], ["Ricardo Lozano", [2.0, 2.3, 2.5]], ["Ángela Matiz", [3.2, 2.9, 3.3]], ["Claudia Pinzón", [4.5, 4.5, 4.8]], ["Silvia Urbina", [1.9, 1.7, 0.0]], ["Gonzalo Quintana", [3.0, 2.9, 3.4]]]

#Ejemplo de invocacion
promedio = calc_cali_prom (estudiantes)

#verificación del resultado
print ("\nLa calificacion promedio de cada estudiante es:")
ct = 1
for dato in promedio:
    print (f"Estudiante #{ct}")
    print (round(dato, 2))
    ct += 1

#Parte 2
def calc_may_cali_est (estudiantes, tercio):
    nombre = " "
    cali_m = 0
    for dato in estudiantes:
        if dato[1][tercio] > cali_m:
            cali_m = dato[1][tercio]
            nombre = dato[0]
    return cali_m, nombre

#Ejemplo de invocación
tercio = int(input("\nIngrese el tercio: ")) - 1
calificación_my, nombre_c_m = calc_may_cali_est (estudiantes, tercio)

#verificación del resultado
print (f"Del tercio {tercio + 1}, la calificación mas alta fue {calificación_my} obtenida por {nombre_c_m}.")