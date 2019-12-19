#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PoC: Operaciones con ficheros
"""

# Abrir un fichero
f = open('filename', 'r')  # asignamos un puntero al fichero a la variable f, abierto para LEER (r)
data = f.read()
f.close()  # CIERRA LOS FICHEROS SIEMPRE

g = open('filename2', 'w')  # asignamos fichero2 a 'g', para ESCRIBIR (w)
g.write('escribe un string')  # lo que escribamos debe ser string
g.close()

#----------------
f = open('filename', 'rb')  # abrir para leer como bytes
g = open('filename2', 'wb')  # abrir para escribir bytes
f.close()
g.close()
#----------------
"""
---------------------------------------------------------------------------------------
Parámetros para abrir el fichero
=======================================================================================
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
---------------------------------------------------------------------------------------
"""


import os  # librerías para interactuar con el OS
path = './'  # recomendamos paths enteros. En Windows los paths van con \\
print(os.listdir(path))  # listado de ficheros
os.path.isfile(path)


# CSV
# ===
import csv  # no es necesario usarla: un csv es una 'tabla' con columnas separadas con comas.
# csv es una abstracción de texto a tabla, pero es texto

import csv
with open('writeData.csv','rt')as f:  # otra manera de castear ficheros. LO LO DEMÁS VA TABULADO DEBAJO
    data = csv.reader(f)
    for row in data:
        print(row)

#----------------
with open('cosicas.txt') as fichero:  # otra manera de castear ficheros. LO LO DEMÁS VA TABULADO DEBAJO
    data = csv.reader(fichero, delimiter=',')
    lineas = 0
    for row in data:
        print(row)
#----------------
with open('writeData.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    #way to write to csv file
    writer.writerow(['Programming language', 'Designed by', 'Appeared', 'Extension'])
    writer.writerow(['Python', 'Guido van Rossum', '1991', '.py'])
    writer.writerow(['Java', 'James Gosling', '1995', '.java'])
    writer.writerow(['C++', 'Bjarne Stroustrup', '1985', '.cpp'])