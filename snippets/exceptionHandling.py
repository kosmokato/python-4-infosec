#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

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

# Show error line without stopping the program
try:
	print(x)
except Exception as e:
	exc_type, exc_obj, exc_tb = sys.exc_info()
	fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
	print("[-] Error: " + str(e))
	print(exc_type, fname, exc_tb.tb_lineno)
