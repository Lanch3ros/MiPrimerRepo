'''
Universidad Escuela Colombiana de Ingeniería
Asignatura: Algoritmos y Programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Estudiante: Apellidos Nombre(s)
Ref.: Tarea No. 17. Listas.

B. Suponga que se tiene una lista en la que cada registro tiene la siguiente
   estructura:

   [NIT de la empresa colombiana exportadora, monto en millones de pesos de las exportaciones hechas en un año, año, [países a los que se ha exportado]]

   Construya una función que inicialice una lista con el NIT de la empresa que
   exportó a más países, el año en que ocurrió, el monto de las exportaciones y
   la cantidad de países. No se conoce ni se necesita la cantidad de registros
   de la lista datos_export. El recorrido debe hacerlo por contenido, no por
   posición.

   Con los datos del ejemplo, la lista que quedaría disponible en donde se
   invoque la función sería: ["8001647676", 2017, 81447, 8].

   Escriba un ejemplo de invocación de la función. Recuerde que debe darles
   nombres significativos a las variables y a las funciones.

Todo lo que utilice debemos haberlo trabajado en el curso.
Favor consultarme en caso de duda.

'''
   
datos_export = 	[["9001274376", 1435, 2019, ["Chile", "México", "Ecuador", "Argentina", "Brasil"]],
                 ["8001647676", 74350, 2018, ["Portugal", "Francia", "China", "Suecia", "Argentina", "Guatemala", "Egipto"]],
                 ["8000656089", 11302, 2017, ["Brasil", "Costa Rica", "Alemania", "Chile", "Venezuela"]],
                 ["9000113956", 1057, 2019, ["Costa Rica", "Alemania", "Brasil", "Canadá", "Chile"]],
                 ["8999990024", 776, 2018, ["Estados Unidos", "Canadá", "México"]],
                 ["8301286105", 1020, 2018, ["Estados Unidos", "Brasil", "Canadá"]],
                 ["8300012421", 4202, 2019, ["España", "Noruega", "Japón", "Australia", "Perú", "México", "Canadá"]],
                 ["8000656089", 15090, 2019, ["Brasil", "Costa Rica", "Alemania", "Chile", "Venezuela"]],
                 ["8001647676", 63552, 2019, ["Portugal", "Francia", "China", "Canadá", "Guatemala", "Egipto"]],
                 ["9070114903", 645, 2019, ["Ecuador", "Brasil", "Bolivia", "Perú", "Chile"]],
                 ["8301286105", 1343, 2019, ["Estados Unidos", "Canadá", "España"]],
                 ["8300012421", 3112, 2018, ["España", "Noruega", "Japón", "Australia", "Perú", "México", "Canadá"]],
                 ["9001274376", 985, 2018, ["Chile", "México", "Ecuador", "Brasil"]],
                 ["8000656089", 10009, 2018, ["Brasil", "Costa Rica", "Alemania", "Chile", "Venezuela"]],
                 ["8001647676", 81447, 2017, ["Portugal", "Francia", "China", "Suecia", "Argentina", "Guatemala", "Egipto", "India"]],
                 ["8999990024", 867, 2019, ["Estados Unidos", "Canadá", "México"]],
                 ["9001274376", 1742, 2017, ["Chile", "México", "Ecuador", "Bolivia", "Brasil", "República Dominicana"]]]
            
                       
                       
    
