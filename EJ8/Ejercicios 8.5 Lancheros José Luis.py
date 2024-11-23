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
5. Suponga que se tienen dos listas (es decir, ya existen). Una con código del
   producto, nombre del producto, proveedor y descuento, y otra con código del
   producto y precio por kilo. Por ejemplo:

   datos_prod = [["1234", "lenteja", ["Agricultores Unidos", 30]],
                 ["9831", "queso", ["Agricultores Unidos", 10]],
                 ["3358", "carne", ["Campesinos del Norte", 20]],
                 ["9166", "naranja", ["Campesinos del Norte", 20]],
                 ["1132", "arroz", ["Del Campo a su Mesa", 20]],
                 ["1772", "guanábana", ["Del Campo a su Mesa", 30]],
                 ["9166", "naranja", ["Del Campo a su Mesa", 10]],
                 ["4819", "tomate", ["Campesinos del Norte", 10]],
                 ["1234", "lenteja", ["Campesinos del Norte", 10]],
                 ["3358", "carne", ["Del Campo a su Mesa", 0]],
                 ["3388", "curuba", ["Del Campo a su Mesa", 10]],
                 ["9922", "habichuela", ["Campesinos del Norte", 20]],
                 ["3443", "cebolla cabezona", ["Campesinos del Norte", 0]],
                 ["1114", "cilantro", ["Agricultores Unidos", 10]],
                 ["1772", "guanábana", ["Agricultores Unidos", 0]]]

   cod_prod_precio = [["9831", 12000],
                      ["1132", 2000],
                      ["9166", 800],
                      ["4819", 6500],
                      ["3358", 32000],
                      ["9922", 1500],
                      ["1234", 4000],
                      ["3443", 2300],
                      ["1114", 1200],
                      ["1772", 5500],
                      ["3388", 3000]]

   Construya una función en Python que agregue a la primera lista el precio de
   cada producto, el cual está en la segunda lista.

   La lista modificada debe quedar disponible en la función que invoque a ésta. Con los datos del ejemplo, la primera lista quedaría así:

   datos_prod = [["1234", "lenteja", ["Agricultores Unidos", 30, 4000]],
                 ["9831", "queso", ["Agricultores Unidos", 10, 12000]],
                 ["3358", "carne", ["Campesinos del Norte", 20, 32000]],
                 ["9166", "naranja", ["Campesinos del Norte", 20, 800]],
                 ["1132", "arroz", ["Del Campo a su Mesa", 20, 2000]],
                 ["1772", "guanábana", ["Del Campo a su Mesa", 30, 5500]],
                 ["9166", "naranja", ["Del Campo a su Mesa", 10, 800]],
                 ["4819", "tomate", ["Campesinos del Norte", 10, 6500]],
                 ["1234", "lenteja", ["Campesinos del Norte", 10, 4000]],
                 ["3358", "carne", ["Del Campo a su Mesa", 0, 32000]],
                 ["3388", "curuba", ["Del Campo a su Mesa", 10, 3000]],
                 ["9922", "habichuela", ["Campesinos del Norte", 20, 1500]],
                 ["3443", "cebolla cabezona", ["Campesinos del Norte", 0, 2300]],
                 ["1114", "cilantro", ["Agricultores Unidos", 10, 1200]],
                 ["1772", "guanábana", ["Agricultores Unidos", 0, 5500]]]

'''

# Definición de la función.
def añade_precio (datos_prod, cod_prod_precio):
    for prod in datos_prod:
        for precio in cod_prod_precio:
            if prod[0] == precio[0]:
               prod[2].append(precio[1])
    return datos_prod
        
# Ejemplo de datos de prueba.
datos_prod = [["1234", "lenteja", ["Agricultores Unidos", 30]],
              ["9831", "queso", ["Agricultores Unidos", 10]],
              ["3358", "carne", ["Campesinos del Norte", 20]],
              ["9166", "naranja", ["Campesinos del Norte", 20]],
              ["1132", "arroz", ["Del Campo a su Mesa", 20]],
              ["1772", "guanábana", ["Del Campo a su Mesa", 30]],
              ["9166", "naranja", ["Del Campo a su Mesa", 10]],
              ["4819", "tomate", ["Campesinos del Norte", 10]],
              ["1234", "lenteja", ["Campesinos del Norte", 10]],
              ["3358", "carne", ["Del Campo a su Mesa", 0]],
              ["3388", "curuba", ["Del Campo a su Mesa", 10]],
              ["9922", "habichuela", ["Campesinos del Norte", 20]],
              ["3443", "cebolla cabezona", ["Campesinos del Norte", 0]],
              ["1114", "cilantro", ["Agricultores Unidos", 10]],
              ["1772", "guanábana", ["Agricultores Unidos", 0]]]

cod_prod_precio = [["9831", 12000],
                   ["1132", 2000],
                   ["9166", 800],
                   ["4819", 6500],
                   ["3358", 32000],
                   ["9922", 1500],
                   ["1234", 4000],
                   ["3443", 2300],
                   ["1114", 1200],
                   ["1772", 5500],
                   ["3388", 3000]]

# Invocación.
resultado = añade_precio (datos_prod, cod_prod_precio)

# Verificación del resultado.
print ("Lista con el precio de cada prodcuto\n")
print (resultado)