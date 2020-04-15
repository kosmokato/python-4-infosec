#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PoC: Variables globales y locales

Los métodos y las variables se han de definir ANTES de usarlos
"""


def sumaTres( num ):
    b = num + a
    return b  # accede a 'a' porque es global


# Variables globales
a = 3
resultado = sumaTres(a)
print(resultado)

resultado = sumaTres(b)  # 'b' está definida en 'sumaTres'
print(resultado)



#--------------------------------------
#   *   *   *
#--------------------------------------

# CONVERSIONES DE VARIABLES (Casting)
# =========================
variable = 'A'  #hexstring, también '0xA'

#hex2int
variable_int = int( variable, base = 16 )
print( variable )
print( variable_int )

#int2hex
hex( variable_int )

#hex2bytes
variable.encode()               #
bytes([0xf])                    # alternativa
bytearray.fromhex('abdcfe65')   #

#bytes2hex


#str2bytes
cadena = 'aaaa'
cadena_byes = cadena.encode('utf-8')
#bytes2str
cadena = cadena_byes.encode('utf-8')


#str2int
int(var)
#int2str
variable = 1
str(variable)