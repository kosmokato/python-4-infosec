#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PoC: Diccionarios

Tipo de struct que almacena datos de la forma clave-valor.
Es como una lista, pero en vez de acceder por índice numérico se accede por el nombre de la clave.
Clave conocida, se consulta el valor.
Básicamente un JSON.
"""

# construir diccionario
myComputer = dict(marca="MSI", modelo="MegaMolón", año=2019, precio=950)
# alternativa
myComputer = {
    "marca": "MSI",
    "modelo": "MegaMolón",
    "año": 2019,
    "precio": 950
}
print(myComputer)
print(myComputer["modelo"])
# una manera más elegante de acceder
print(myComputer.get("marca"))

# modificar un valor:
myComputer["precio"] = 850
print(myComputer)

# recorrer diccionario
for x in myComputer:
    print(x)                # claves
    print(myComputer[x])    # valores
    print('\n')

# recorrer valores de diccionario
for x in myComputer.values():
    print(x)

# recorrer elementos completos
for x in myComputer.items():
    print(x)

# buscar una clave
if "marca" in myComputer: print('\"marca\" in myComputer')

# añadir una clave-valor nueva
myComputer["Usuario"] = 'sudo'
print(myComputer)

# Eliminar una clave
myComputer.pop("Usuario")
print(myComputer)
myComputer.popitem()  # borra el último item añadido
print(myComputer)
# alternativa
del myComputer["modelo"]  # NOTA: si no especificamos, borra todo el modelo
print(myComputer)

# limpiar diccionario
myComputer.clear()

# copiar diccionario
myComputer2 = myComputer.copy()
#alternativa
myComputer2 = dict(myComputer)  # forzamos diccionario

# diccionarios anidados
hijo1 = {
  "nombre" : "Nome",
  "año" : 2004
}
hijo2 = {
  "nombre" : "toqueslo",
  "año" : 2004
}
hijo3 = {
  "nombre" : "shuevos",
  "año" : 2004
}

myFamilia = {
  "hijo1" : hijo1,
  "hijo2" : hijo2,
  "hijo3" : hijo3
}


"""
===========================================================================
            MÉTODOS DE LOS DICCIONARIOS
===========================================================================
Method	        Description
--------------- -----------------------------------------------------------
clear()         Removes all the elements from the dictionary
copy()          Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and values
get()	        Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()    Returns the value of the specified key. If the key does not
                exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary
===========================================================================
"""