#!/usr/bin/python3
# -*- coding: utf-8 -*- 

"""
3.- **Redes**
	Lanza un ARP y sácame un listado de los usuarios en mi red identificaditos. Busca MAC y saca datos -> buscar página para eso
"""
import sys
import os
import subprocess

#Lanzar comando





"""
┌───Host───┐
│      /¯/|│
│|¯¯¯||¯| |│
│|___|| | |│
│  |  |_|/ │
│/::::/~() │
└──────────┘
#------------
┌──Server──┐
│          │
│   /¯¯/|  │
│  |¯¯| |  │
│  |..| |  │
│  |__|/   │
└──────────┘
192.168.137.235
#------------
┌──Laptop──┐
│          │
│  |¯¯¯|   │
│  |___|   │
│ /::::/~()│
│ ¯¯¯¯¯    │
└──────────┘
#------------
┌────AP────┐
│          │
│          │
│  |____|  │
│  /____/  │
│  ¯¯¯¯¯   │
└──────────┘
#------------
┌──Router──┐
│          │
│   ◜¯|¯◝  │
│  (-> <-) │
│   ◟_|_◞  │
│          │
└──────────┘
#-----------
┌──Phone──┐
│         │
│   ┌─┐   │
│   │ │   │
│   └·┘   │
│         │
└─────────┘
"""


# píntame 4 equipos
N = 4
lista = list()
lista.append('┌───Host───┐')
lista.append('│      /¯/|│')
lista.append('│|¯¯¯||¯| |│')
lista.append('│|___|| | |│')
lista.append('│  |  |_|/ │')
lista.append('│/::::/~() │')
lista.append('└──────────┘')

router = list()
router.append('┌──Router──┐')
router.append('│          │')
router.append('│   ◜¯|¯◝  │')
router.append('│  (-> <-) │')
router.append('│   ◟_|_◞  │')
router.append('│          │')
router.append('└──────────┘')

ap = list()
ap.append('┌────AP────┐')
ap.append('│          │')
ap.append('│          │')
ap.append('│  |____|  │')
ap.append('│  /____/  │')
ap.append('│  ¯¯¯¯¯   │')
ap.append('└──────────┘')

for i in range(0, len(lista)):
	parque = ""
	for k in range(0,N/2):
		parque += lista[i]	# píntame N/2 equipos
	parque += router[i]	 	# píntame router
	for k in range(0,N/2):
		parque += lista[i]	# píntame N/2 equipos
	parque += ap[i]			# píntame ap
	for k in range(0,N/2):
		parque += lista[i] 	# píntame N/2 equipos
	print(parque)