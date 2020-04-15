#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PoC: Estructuras de Control: if/elif/else... switch-case
"""


variable = 9  # es de tipo 'int'
print('[i] variable es de tipo ' + str(type(variable)))

if variable is not 21:
    print('[i] variable no es 21')
elif variable is 9:  # ¿A qué es IGUAL?
    print('[+] variable es 9')
elif variable < 12:  # Compara con otro int
    print('[i] variable es menor que 12')
else:
    pass  # No hacemos nada

# ¿Forma parte de una secuencia?
if variable not in [1, 2, 3, 4]:
    print('[i] variable no está en ' + str([1, 2, 3, 4]))
else:
    print(variable)

# ¿A qué NO ES IGUAL?
if variable != '9':  # deberían ser lo mismo, pero 9 no es '9'
    print('[i] 9 no es \'\9\'')
if str(variable) == '9':  # forzamos variable a ser evaluada como string
    print('[i] str(9) sí es \'\9\'')


# YAPA! 'switch-case's en python
# en C o Java sustituye a varios if/elif/else enlazados
# en python se usa un diccionario

# Declaramos un método que contiene el diccionario
def switch_mes(numero_mes):
    switcher = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }
    # Una vez que lo encontremos realizamos una acción
    # si no encuentra el argumento en el diccionario, imprime error
    print(switcher.get(numero_mes, "[-] No se ha hallado " + str(numero_mes)))

# Invocamos al método consultando un valor:
switch_mes(3)