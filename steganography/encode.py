#! -*- coding: utf8 -*-

#Última Edición: 26-feb-2017
#Autor: Manuel Alejandro Alvarado Cobo
#Email: ma.alvarado@uniandes.edu.co

import sys
import midi

nombre_archivo = sys.argv[1]
archivo = midi.read_midifile(nombre_archivo)
pista = midi.Track()
mensaje = sys.argv[2]
canales = {}
canal = 0

#Buscar un canal libre
for i in archivo:
	for j in i:
		try:
			j.channel
		except:
			pass
		else:
			if canales.has_key(j.channel):
				canales[j.channel] += 1
			else:
				canales[j.channel] = 1

for c in range(0,15):
	if not canales.has_key(c):
		canal = c
		break

#sanitanizar el mensaje
mensaje = mensaje.upper()
mensaje = mensaje.replace('ñ', 'N')
mensaje = mensaje.replace('á', 'A')
mensaje = mensaje.replace('à', 'A')
mensaje = mensaje.replace('ä', 'A')
mensaje = mensaje.replace('é', 'E')
mensaje = mensaje.replace('è', 'E')
mensaje = mensaje.replace('ë', 'E')
mensaje = mensaje.replace('í', 'I')
mensaje = mensaje.replace('ì', 'I')
mensaje = mensaje.replace('ï', 'I')
mensaje = mensaje.replace('ó', 'O')
mensaje = mensaje.replace('ò', 'O')
mensaje = mensaje.replace('ö', 'O')
mensaje = mensaje.replace('ú', 'U')
mensaje = mensaje.replace('ù', 'U')
mensaje = mensaje.replace('ü', 'U')
mensaje = "-msj-"+mensaje

#codificar el mensaje en el canal elegido
for letra in list(mensaje):
	nota = midi.NoteOnEvent(tick=0, channel=canal, data=[(ord(letra)), 0])
	pista.append(nota)

#escribir un archivo nuevo
archivo.append(pista)
nombre_archivo = nombre_archivo.replace('.mid', ' copia.mid')
midi.write_midifile(nombre_archivo, archivo)

print "El mensaje ha sido codificado en el archivo: "+nombre_archivo+" en el canal "+str(canal)