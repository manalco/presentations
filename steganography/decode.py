#! -*- coding: utf8 -*-

#Última Edición: 26-feb-2017
#Autor: Manuel Alejandro Alvarado Cobo
#Email: ma.alvarado@uniandes.edu.co

import sys
import midi

archivo = midi.read_midifile(sys.argv[1])
mensaje = ""
canales = {}
canal = -1

#Buscar canales usados
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

for c in canales:
	inicializador = ""
	for pista in archivo:
		for evento in pista:
			if isinstance(evento, midi.NoteOnEvent) and evento.channel == c and len(inicializador) < 5:
				inicializador += chr(evento.data[0])
			else:
				if inicializador == "-msj-":
					canal = c
					break
		if canal >= 0:
			break
	if canal >= 0:
		break

for pista in archivo:
	for evento in pista:
		if isinstance(evento, midi.NoteOnEvent) and evento.channel == canal:
			mensaje += chr(evento.data[0])

mensaje = mensaje.replace('-msj-', '')

print "el mensaje es: '"+mensaje+"'"