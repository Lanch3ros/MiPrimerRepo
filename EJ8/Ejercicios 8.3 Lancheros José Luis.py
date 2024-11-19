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
3. Suponga que se tienen dos listas (es decir, ya existen). Una con código del
   producto, nombre del producto, proveedor, descuento y precio por kilo, y otra
   con código y nombre del proveedor. Por ejemplo:

   datos_prod = [["1234", "lenteja", ["1516", 30, 4000]],
                 ["9831", "queso", ["1516", 10, 12000]],
                 ["3358", "carne", ["9128", 20, 32000]],
                 ["9166", "naranja", ["9128", 20, 800]],
                 ["1132", "arroz", ["6427", 20, 2000]],
                 ["1772", "guanábana", ["6427", 30, 5500]],
                 ["9166", "naranja", ["6427", 10, 800]],
                 ["4819", "tomate", ["9128", 10, 6500]],
                 ["1234", "lenteja", ["9128", 10, 4000]],
                 ["3358", "carne", ["6427", 0, 32000]],
                 ["3388", "curuba", ["6427", 10, 3000]],
                 ["9922", "habichuela", ["9128", 20, 1500]],
                 ["3443", "cebolla cabezona", ["9128", 0, 2300]],
                 ["1114", "cilantro", ["1516", 10, 1200]],
                 ["1772", "guanábana", ["1516", 0, 5500]]]

   datos_provee = [["1516", "Agricultores Unidos"],
                   ["9128", "Campesinos del Norte"],
                   ["6427", "Del Campo a su Mesa"]]

   Construya una función en Python que agregue una lista a la segunda lista con
   los productos de cada proveedor, los cuales están en la primera lista.

   La lista modificada debe quedar disponible donde se invoque la función.
   Con los datos del ejemplo, la segunda lista quedaría así:

   datos_provee = [["1516", "Agricultores Unidos", ["lenteja", "queso", "cilantro", "guanábana"]],
                  ["9128", "Campesinos del Norte", ["carne", "naranja", "tomate", "lenteja", "habichuela", "cebolla cabezona"]],
                  ["6427", "Del Campo a su Mesa", ["arroz", "guanábana", "naranja", "carne", "curuba"]]]

'''

# Definición de la función
def agrega_productos_a_proveedores(datos_prod, datos_provee):
    for proveedor in datos_provee:
        codigo_proveedor = proveedor[0]
        productos = []
        for producto in datos_prod:
            codigo_producto = producto[2][0]
            nombre_producto = producto[1]
            if codigo_producto == codigo_proveedor:
                productos.append(nombre_producto)
        proveedor.append(productos)

# Ejemplo de datos
datos_prod = [
    ["1234", "lenteja", ["1516", 30, 4000]],
    ["9831", "queso", ["1516", 10, 12000]],
    ["3358", "carne", ["9128", 20, 32000]],
    ["9166", "naranja", ["9128", 20, 800]],
    ["1132", "arroz", ["6427", 20, 2000]],
    ["1772", "guanábana", ["6427", 30, 5500]],
    ["9166", "naranja", ["6427", 10, 800]],
    ["4819", "tomate", ["9128", 10, 6500]],
    ["1234", "lenteja", ["9128", 10, 4000]],
    ["3358", "carne", ["6427", 0, 32000]],
    ["3388", "curuba", ["6427", 10, 3000]],
    ["9922", "habichuela", ["9128", 20, 1500]],
    ["3443", "cebolla cabezona", ["9128", 0, 2300]],
    ["1114", "cilantro", ["1516", 10, 1200]],
    ["1772", "guanábana", ["1516", 0, 5500]],
]

datos_provee = [
    ["1516", "Agricultores Unidos"],
    ["9128", "Campesinos del Norte"],
    ["6427", "Del Campo a su Mesa"],
]

# Invocación de la función
agrega_productos_a_proveedores(datos_prod, datos_provee)

# Verificación del resultado
print("\nLista de proveedores con productos:\n")
for proveedor in datos_provee:
    print(proveedor)