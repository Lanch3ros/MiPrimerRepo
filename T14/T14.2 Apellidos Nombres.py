"""
Universidad Escuela Colombiana de Ingeniería
Profesora: Ingeniera Patricia Salazar Perdomo

Estudiante: Apellidos Nombre

Lenguaje: Python
Referencia: Tarea No. 14. Programación modular con vectores.

2. Se tiene un vector llamado palabra con los caracteres de una palabra, un
   carácter en cada posición. Construya una función en Python que averigüe si
   la palabra guardada en el vector contiene todas las vocales y una sola vez
   cada una.

   El resultado debe quedar disponible donde se invoque la función, es decir,
   no se debe escribir en ella. Los datos del vector (contenido y tamaño) ya
   se conocen.

   Ejemplo 1:	arquitecto
   Resultado: 	La palabra arquitecto contiene todas las vocales una sola vez.

   Ejemplo 2: 	consiguiera
   Resultado: 	La palabra consiguiera no contiene todas las vocales una sola
                vez.

   Ejemplo 3: 	abuelita
   Resultado: 	La palabra abuelita no contiene todas las vocales una sola vez.

Escriba un ejemplo de invocación de la función. Recuerde lo importante que es
darles nombres significativos a las variables y a las funciones.

"""

def escvec (v, tv):
    for pv in range (tv):
        print (v[pv], end = " ")

def vocales_una_vez ( ):
    print ("\nFunción vocales_una_vez: La construye el estudiante.")



vocales = ['a', 'e', 'i', 'o', 'u']
cv = 5

# DATOS DE PRUEBA.
palabra1 = ['i', 'm', 'a', 'g', 'i', 'n', 'a', 'b', 'l', 'e']
cc1 = 10
palabra2 = ['a', 'b', 'u', 'e', 'l', 'i', 't', 'o']
cc2 = 8

# Ejemplo de invocación.
vocales_una_vez ( )

# Verificación del resultado.



