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

def nuevo_mes():
	#HACER LOS CONTROLES DE DATOS INTRODUCIDOS!

	nombre_fich=raw_input("¿Qué nombre le quiere dar al nuevo mes de entrenamiento?: ")

	dias=raw_input("¿Qué dias de la semana se entrenará? Introduzcalos separados por comas: ").lower()

	ejercicios=raw_input("¿Que ejercicios componen el mes? Introduzcalos por orden de ejecución, diario y posicional en el día: ").lower()

	fich=open("/home/ejimenez/Documentos/desarrollos/pruebas/"+nombre_fich+".doc", "w")
	fich.write(dias+"\n"+ejercicios)
	fich.close()
	
	
def main(o):

	if o == "1":

		nuevo_mes()
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

print main(menu())
