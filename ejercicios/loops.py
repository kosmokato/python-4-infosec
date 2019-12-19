#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PoC: Estructuras de Control: loops for y loops while
"""

# FOR
# ===
# Estos bucles con fáciles de controlar y muy sencillos

# Recorrer un rango de números (I)
# --------------------------------
for x in range(6):  # range = [0,N-1]
  print(x)


print('#-------------------------------------')
# Recorrer un rango de números (II)
# ---------------------------------
for x in range(2, 6):  # range = [M,N-1]
  print(x)


print('#-------------------------------------')
# Recorrer un rango de números (III)
# ----------------------------------
for x in range(1, 17, 3):  # range = [M,N-1], paso=3
    print(x)


print('#-------------------------------------')
# Recorrer los elementos de una lista
# -----------------------------------
fruits = ["money", "women", "power"]
for x in fruits:
  if x == "women":
    continue  # omite el match
  print(x)


print('#-------------------------------------')
# Abortar al primer match
# -----------------------------------
fruits = ["money", "women", "power"]
for x in fruits:
  if x == "women":
    break
  print(x)


# ///////////////////////////////////////////////
# WHILE
# =====
# Estos bucles pueden ser infinitos y colgar la máquina, ojo

i = 1
while i < 6:    # mientas se cumpla esta condición, iterará
  print(i)      # acción
  i += 1        # debemos modificar los elementos en cada iteración o no saldremos nunca