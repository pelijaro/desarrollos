#!/usr/bin/ python
# -*- coding: utf-8 -*-

print "\n\nBienvenido al programa de seguimiento de tus entrenamientos!\n\n"


def menu():

	print "1- Nuevo mes de entrenamiento"
	print "2- Añadir nueva semana al mes"
	print "3- Enviar mes de entrenamiento por correo"
	print "4- Mostrar mes en documento(doc, pdf, documento de texto plano)\n\n"
	opcion=raw_input("Por favor, introduzca el numero de una de las siguientes opciones: ")
	return opcion


def main(o):

	if o == "1":

		return "Has introducido la opcion 1"

	elif o == "2":

		return "Has introducido la opcion 2"

	elif o == "3":

		return "Has introducido la opcion 3"

	elif o == "4":

		return "Has introducido la opcion 4"

	else:

		return "Has introducido una opcion incorrecta, por favor introduzcala bien"


print main(menu())
