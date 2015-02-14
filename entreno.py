#!/usr/bin/ python
# -*- coding: utf-8 -*-

#Script acepta valores de pesos de diferentes ejercicios, formatea datos y sale en un archivo preparado para enviar email

print "¡Bienvenido a la interfaz de introducción de datos de entrenamiento! \n"


def semana_in():

	semana=raw_input("Por favor, introduzca la semana correspondiente a los valores a añadir(valor numérico): ")

	if (semana=="1" or semana=="2" or semana=="3" or semana=="4"):

		print "Semana correcta" #implementar la funcion que tenga que ir aqui, el print es de control

	else:

		print "Semana incorrecta, introduzcala como se indica"

