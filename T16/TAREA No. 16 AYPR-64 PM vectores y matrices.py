'''
Universidad Escuela Colombiana de Ingeniería

Asignatura: 	 Algoritmos y Programación, Grupo 64 (AYPR-64)
Profesora: 	 Ingeniera Patricia Salazar Perdomo
Estudiante:      Lancheros Ayora José Luis
Ref.: 		 Tarea No. 16

A la Asociación de Universidades de Bogotá (AUB) le llega cada semestre el dato de
cantidad de estudiantes nuevos en los programas de ingeniería de cada institución socia.
Actualmente cuenta con los datos de los últimos tres años, almacenados en una tabla
en la que las filas son las universidades y las columnas, los semestres lectivos.
Para analizar los datos mencionados se requiere averiguar lo siguiente:

2. Cuántos estudiantes nuevos entraron a programas de ingeniería en los últimos tres años.
3. Cantidad total de estudiantes nuevos por universidad.
4. En los últimos tres años, qué universidad ha recibido más estudiantes en un semestre y cuándo ocurrió.
5. En cuál semestre ingresaron más estudiantes en total y cuántos fueron.
6. En cuáles universidades la admisión ha ido siempre en ascenso.

Importante:
- El programa debe funcionar con otros datos y en mayor o menor cantidad.
- Todo lo que utilice debemos haberlo trabajado formalmente en el curso.
  Favor consultarme en caso de duda.
- No se acepta el uso de funciones que hagan lo que se pide en una o más opciones.
    
'''

MU = 15      # Máxima cantidad de universidades.
MS = 20      # Máxima cantidad de semestres.

def muestra_datos (est_uxs, cu, cs, nom_u, nom_s):
    print (f"\nESTUDIANTES NUEVOS EN INGENIERIA DESDE {nom_s [0]} hasta {nom_s [cs - 1]}")
    print("\n", format ("UNIVERSIDAD", "20s"), end = "")
    for s in range (cs):
        print (format (nom_s [s], "6s"), end = "") 
    for u in range (cu):
        print("\n", format (nom_u [u], "18s"), end = "")
        for s in range (cs):
            print (format (est_uxs [u][s], "6d"), end = "")
    input ("\n\n\t\tPresione cualquier tecla para continuar ")

# 2. Cuántos estudiantes nuevos entraron a programas de ingeniería en los últimos tres años.
def total_nuevos (est_uxs, cu, cs):
    total = 0
    for u in range(cu):
        for s in range(cs):
            total += est_uxs[u][s]
    print(f"\nTOTAL NUEVOS TODAS LAS UNIVERSIDADES: {total}")
    input("\n\t\tPresione cualquier tecla para continuar ")

# 3. Cantidad total de estudiantes nuevos por universidad.
def total_nuevosxu (est_uxs, cu, cs, nom_u):
    print("\nTOTAL NUEVOS POR UNIVERSIDAD")
    for u in range(cu):
        total_u = 0
        for s in range(cs):
            total_u += est_uxs[u][s]
        print(f"{nom_u[u]}: {total_u}")
    input("\n\t\tPresione cualquier tecla para continuar ")

# 4. En los últimos tres años, qué universidad ha recibido
#    más estudiantes en un semestre y cuándo ocurrió.
def u_masnuevos (est_uxs, cu, cs, nom_u, nom_s):
    max_nuevos = 0
    uni_max = ""
    sem_max = ""
    for u in range(cu):
        for s in range(cs):
            if est_uxs[u][s] > max_nuevos:
                max_nuevos = est_uxs[u][s]
                uni_max = nom_u[u]
                sem_max = nom_s[s]
    print(f"\nUNIVERSIDAD CON MÁS NUEVOS: {uni_max} en el semestre {sem_max} con {max_nuevos} estudiantes.")
    input("\n\t\tPresione cualquier tecla para continuar ")

# 5. En cuál semestre ingresaron más estudiantes en total y cuántos fueron.
def sem_masnuevos (est_uxs, cu, cs, nom_s):
    max_total = 0
    sem_max = ""
    for s in range(cs):
        total_s = 0
        for u in range(cu):
            total_s += est_uxs[u][s]
        if total_s > max_total:
            max_total = total_s
            sem_max = nom_s[s]
    print(f"\nSEMESTRE CON MÁS NUEVOS: {sem_max} con {max_total} estudiantes.")
    input("\n\t\tPresione cualquier tecla para continuar ")

# 6. En cuáles universidades la admisión ha ido siempre en ascenso.
def nuevos_ascenso (est_uxs, cu, cs, nom_u):
    print("\nUNIVERSIDADES CON NUEVOS SIEMPRE EN ASCENSO")
    for u in range(cu):
        ascenso = True
        for s in range(1, cs):
            if est_uxs[u][s] <= est_uxs[u][s-1]:
                ascenso = False
                break
        if ascenso:
            print(nom_u[u])
    input("\n\t\tPresione cualquier tecla para continuar ")
    
def main( ):
    # est_uxs es una matriz de MU filas por MS columnas.
    est_uxs = [[320,750,901,950,700,783],
                 [913,600,1200,865,902,670],
                 [700,702,780,815,830,901],
                 [714,770,1105,940,903,960],
                 [720,650,728,802,778,782]]
    # nom_u es un vector de máximo MU posiciones.
    nom_u = ["Los Cerezos","Los Olivos","Los Pinos","Los Eucaliptos","Los Abedules"]
    # nom_s es un vector de máximo MS posiciones.
    nom_s = ["20-1","20-2","21-1","21-2","22-1","22-2"]

    cu = 5   # Cantidad de universidades.
    cs = 6   # Cantidad de semestres.
    opc = 0

    while opc != 7:
        print ("\n\tESTUDIANTES NUEVOS EN PROGRAMAS DE INGENIERÍA\n")
        print ("\t1. Ver datos de nuevos estudiantes\n")
        print ("\t2. Total nuevos\n")
        print ("\t3. Total nuevos por universidad\n")
        print ("\t4. Universidad con más nuevos y en qué semestre\n")
        print ("\t5. Semestre con más nuevos\n")
        print ("\t6. Universidades con nuevos siempre en ascenso\n")
        print ("\t7. Salir\n")
        opc = int (input ("\n\tIngrese opción >> "))
        if opc == 1:
            muestra_datos (est_uxs, cu, cs, nom_u, nom_s)
        elif opc == 2:
            total_nuevos(est_uxs, cu, cs)
        elif opc == 3:
            total_nuevosxu(est_uxs, cu, cs, nom_u)
        elif opc == 4:
            u_masnuevos(est_uxs, cu, cs, nom_u, nom_s)
        elif opc == 5:
            sem_masnuevos(est_uxs, cu, cs, nom_s)
        elif opc == 6:
            nuevos_ascenso(est_uxs, cu, cs, nom_u)
        elif opc == 7:
            print ("\n\nFin.\n\n")

main ( )

