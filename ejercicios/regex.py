#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PoC: RegEx

# recomendado: https://www.programiz.com/python-programming/regex
"""

import re

# BUSCAR UN STRING EN OTRO STRING
string = 'Nuestro gobierno quiere prohibir los vídeos con ositos rosas'
pattern = 'ositos'
result = re.findall(pattern, string)
print(result)  # si no lo encuentra, saltará error

cadena = "The rain in Spain"
x = re.search("^The.*Spain$", cadena)
y = re.search("^The.*", cadena)

#^a...b$    # empieza por 'a' y termina por 'b'
pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)
if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")
#.*         # el punto escapa el asterisco. El asterisco es wildcard
"""
-----------------------------------------------------------------------------
Function    Description
========    =================================================================
findall	    Returns a list containing all matches
search	    Returns a Match object if there is a match anywhere in the string
split	    Returns a list where the string has been split at each match
sub	        Replaces one or many matches with a string
-----------------------------------------------------------------------------
"""

# EJEMPLO: Buscar números en una cadena
# ========
# Program to extract numbers from a string
import re
string = 'hola 12 wassup 89. Howdy 34 hihi9'
pattern = '\d+'
result = re.findall(pattern, string)
print(result)
# ['12', '89', '34', '9']