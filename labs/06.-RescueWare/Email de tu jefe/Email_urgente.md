Hola, @enigmatico,

Han convocado un GIR para resolver un incidente. Un peligroso ransomware conocido como Pyquaza ha penetrado en la infraestructura de un cliente crítico para la Seguridad Nacional.

Como eres novato/a/e/x no se te ha despertado... pero los Nivel3 llevamos con ello desde la madrugada.

Lab52 ha analizado la muestra que les hemos pasado y han detectado que emplea un cifrado RC4 redundante. Pero parece que los PyquazaCrew son algo torpes, ya que están hardcodeadas... Jeje.


Por ello, han implementado el algoritmo de cifrado/descifrado, adjunto a este correo. Se te ha encomendado la tarea de 

PROGRAMAR UN SCRIPT QUE DESCIFRE LOS FICHEROS DADO 'flag_encrypted.py9u4z4' Y LAS CLAVES DE CIFRADO/DESCIFRADO.


Ánimo,
--
Fdo: @Tu_jefe


--
*NOTA1: RC4 es un sencillo cifrado simétrico: emplea la misma clave para cifrar que para descifrar. De hecho, si se cifra dos veces con la misma clave se obtiene el documento original...*

*NOTA2: Ojo a los formatos: cifrar como hexstrings, guardar como bytes, más info en el informe anexo.*


--
Adjuntos al correo:
____________________________________________________
```
"""
Algoritmo para cifrar cadenas de texto con RC4
"""
def crypt(key, data):
    S = list(range(256))
    j = 0
    for i in list(range(256)):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]
    j = 0
    y = 0
    out = []

    for char in data:
        j = (j + 1) % 256
        y = (y + S[j]) % 256
        S[j], S[y] = S[y], S[j]

        out.append(chr(ord(char) ^ S[(S[j] + S[y]) % 256]))

    return ''.join(out)
____________________________________________________
```
**Informe preliminar del análisis de la muestra Pyquaza.exe**

Se trata de una variante de la familia Pykemon. Por algún motivo, está obsesionado con los ficheros llamados ```'flag.png'```, y sólo cifra estos.

A nivel operativo, abre el fichero con permiso de lectura binaria ```'rb'``` y después convierte a hexstring ```f.read().hex()```.

A continuación, llama a un método de cifrado RC4 con una clave única. De manera redundante repite el proceso, pero con una segunda clave.

Después, añade una firma, b'RAMONWARED', al resultado obtenido.

Finalmente, escribe como bytes ```'wb'``` en un fichero nuevo, eliminando el original.

Se sugiere:
	Invertir la conversión de formatos, manteniendo la coherencia.
	Descrifrar RC4 como hexstrings.
	Ignorar la firma del ransomware (primeros 10 bytes).
	Ser metódico.
	Consultar las dudas.
	La solución debería ocupar menos de 50 líneas de código, sin contar comentarios.