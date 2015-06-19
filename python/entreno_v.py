#!/usr/bin/ python
# -*- coding: utf-8 -*-

import sys

print "\n\nBienvenido al programa de seguimiento de tus entrenamientos!\n\n"


def menu():

	print "1- Nuevo mes de entrenamiento"
	print "2- Añadir nueva semana al mes"
	print "3- Enviar mes de entrenamiento por correo"
	print "4- Mostrar mes en documento(doc, pdf, documento de texto plano)"
	print "5- Para finalizar el programa\n\n"
	opcion=raw_input("Por favor, introduzca el numero de una de las siguientes opciones: ")
	return opcion

#def nuevo_mes():

def main(o):

	if o == "1":

		return "\nHas introducido la opcion 1"

	elif o == "2":

		return "\nHas introducido la opcion 2"

	elif o == "3":

		return "\nHas introducido la opcion 3"

	elif o == "4":

		return "\nHas introducido la opcion 4"

	elif o == "5":
		
		return "\nHasta la próxima!"
		sys.exit()
	else:
		print "\nHas introducido una opcion incorrecta, por favor introduzcala bien\n"
		return main(menu())		

#print main(menu())
