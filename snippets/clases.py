#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PoC: Operaciones con ficheros
"""

class Persona:
    #constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprime_cosa(self):
        print('---------')
        print(self.nombre + ' dice: auxilio, me desmayo')

# crear objeto
becario = Persona("Comosellame", 22)

# invocar atributos dentro de la clase
print('nombre:\t' + becario.nombre)
print('edad:\t' + str(becario.edad))
becario.imprime_cosa()