#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PoC: Bytes

Los bytes son delicados, a menudo son variables estáticas y dan muchos problemas. Pero son interesantes para modificar
binarios a bajo nivel.
"""

# string a bytes
cadena = bytes('muchos bytes', 'utf-8')
print(cadena)
print(type(cadena))
cadena2 = bytearray('muchos bytes', 'utf-8')  # alternativa
print(cadena2)
print(type(cadena2))


print()  #-------------------------------------------------
# bytes a hexstring
# hex no es una clase como tal, pero un string de caracteres hex se puede interpretar como números hex
print(cadena.hex())
print(type(cadena.hex()))

print()  #-------------------------------------------------
# hex a bytes
print(bytes.fromhex('546869732070726f6772616d2063616e6e6f742062652072756e20696e20444f53206d6f6465'))

print()  #-------------------------------------------------
# int a bytes
print(bytes([20, 19]))  # int[0, 255]

print()  #-------------------------------------------------
# concatenar bytes
cadena = bytes([20, 19]) + bytes([0, 0])
print(cadena)