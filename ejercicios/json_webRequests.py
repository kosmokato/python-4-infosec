#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PoC: Parseo de Json. Peticiones web. Parseo de respuestas web.

Los Json funcionan como 'diccionarios', recomendado mirar 'diccionarios.py'
"""

import requests
import json

codigo = requests.get('http://google.com')  # nos devuelve un resultado 200 si éxito. Esta respuesta tiene más chicha
texto = codigo.text  # extraemos como texto la respuesta completa

"""
**Json example:**
{"menu": {
  "id": "file",
  "value": "File",
  "popup": {
    "menuitem": [
      {"value": "New", "onclick": "CreateNewDoc()"},
      {"value": "Open", "onclick": "OpenDoc()"},
      {"value": "Close", "onclick": "CloseDoc()"}
    ]
  }
}}
**The same text expressed as XML:**

<menu id="file" value="File">
  <popup>
    <menuitem value="New" onclick="CreateNewDoc()" />
    <menuitem value="Open" onclick="OpenDoc()" />
    <menuitem value="Close" onclick="CloseDoc()" />
  </popup>
</menu>
"""


myIP = json.loads( requests.get('https://api.ipify.org/?format=json' ).text )
print( 'IP: ' + myIP["ip"] )