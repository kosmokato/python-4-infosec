#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PoC: Strings

Las strings/cadenas de caracteres se utilizan mucho, son recurrentes y se puede aplicar gran cantidad de operaciones sobre ellas
"""

# OPERACIONES CON STRINGS
# =======================

cadena = ''  # también: "". <"> está jerárquicamente sobre <'>

# longitud de la cadena
longitud = len(cadena)

# concatenar cadenas
cadena = 'Me gustan l' + 'os macarrones'

# caracteres raros
# '\n' -> salto de línea
print(':a\nb;')
# '\r' -> retorno de carro
print(':a\rb;')
# '\t' -> tabulador
print(':a\tb;')

print()  #-------------------------------------------------
# buscar un elemento
posicion = cadena.find('l')
print(posicion)

print()  #-------------------------------------------------
# buscar una cadena en otra cadena
# La teoría dice que:  str.find(str, beg=0, end=len(string))
palabra = 'macarrones'
print(cadena.find(palabra))
print(cadena.find('e',5))  # comienza en 5
# si devuelve -1 es que no se ha hallado

print()  #-------------------------------------------------
# reemplazar caracteres de una cadena
print('cadena')
cadena = cadena.replace('a', 'i')
cadena = cadena.replace('e', 'i')
cadena = cadena.replace('o', 'i')
cadena = cadena.replace('u', 'i')
print(cadena)

print()  #-------------------------------------------------
# string a lista (segmentar una cadena)
cadena = 'creo que cada año estás más gordo'
print(cadena)
print(type(cadena))
print()
cadena = cadena.split(' ')
print(cadena)
print(type(cadena))  # se ha convertido en lista


print()  #-------------------------------------------------
print()  #-------------------------------------------------
# CONVERSIONES
# ============
# ascii a unicode
# unicode a ascii

print()  #-------------------------------------------------
# string a int
cadena = '69'  # no debe contener letras
print(type(cadena))
cadena2 = int(cadena)
print(type(cadena2))
print(cadena2)

print()  #-------------------------------------------------
# string a bytes
# necesitamos especificar la codificación de la cadena para que python sepa cómo codificar el hex.
cadena = 'abuelito'
cadehex = cadena.encode("utf-8").hex()
print(cadena)
print(cadehex)

print()  #-------------------------------------------------
# string a bytes
cadena = 'abuelito'
cadebytes = cadena.encode()
print(cadena)
print(cadebytes)
# alternativa
print(bytes(cadena, "utf-8"))

#-----------------------
# YAPA: .join()
secuencia = ("Casi", "mese", "olbida")
x = "#".join(secuencia)  # empalma los elementos con '#' en medio
print(x)
