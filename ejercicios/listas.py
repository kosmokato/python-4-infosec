#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PoC: Listas

Las listas son arrays de elementos muy útiles y fáciles de recorrer en un loop
"""

regalos = list()    # definimos la lista
regalos = []        # definición alternativa
regalos2 = ['tren', 'caballito', 'moñeca']  # inizialización con valores

# añadimos elementos
regalos.append('superSoaker')
regalos.append('cebolla')
regalos.append('Germán')
regalos2.append('un palo')

# imprimir lista a pelo
print(regalos)
print(regalos2)

# imprimir elemento a elemento
for x in regalos:
    print(x)

print()  #----------------------------------------

for x in regalos2:
    print(x)

print()  #----------------------------------------
# Acceder a un elemento concreto
print('El cuarto regalo es:')  # [0,N-1]
print(regalos2[3])

# buscar un elemento en una lista:
if 'moñeca' in regalos2:
    print('[+] hohoho, encontrado \'moñeca\'')

# longitud de una lista
longitud = len(regalos)  # int
print(longitud)

# lista -> string
str(regalos2)  # DON'T, esto es forzar y no es elegante

"\t".join(regalos2)  # unir items por el separador "\t"
" ".join(regalos2)  # unir items por el separador " "

# string -> lista
cadena = "asldkjfhaklsjdhfopiqwefhlñkasjdf"
cadena.split("a")  # nos devuelve una cadena, separada por el caracter 'a'. Las 'a' se eliminan.