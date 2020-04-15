#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PoC: Estructuras de Control: manejo de excepciones

Pensado para cuando el código peta
"""
# Vamos a provocar un error
try:  # intentamos ejecutar algo
  print(x)
except Exception as e:  # capturamos la excepción para que no pete
    print('[-] Se ha producido un error')
    print(e)