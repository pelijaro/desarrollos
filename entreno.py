#!/usr/bin/ python
# -*- coding: utf-8 -*-

#Script acepta valores de pesos de diferentes ejercicios, formatea datos y sale en un archivo preparado para enviar email

semana=0
sentadilla=[]
press_banca=[]
dominadas=[]
remo_menton=[]
sentadilla_hack=[]
remo_punta=[]
curl_biceps=[]
jalon_pecho=[]
extension_cuadri=[]
curl_femoral=[]
triceps_polea_cabeza=[]
encogimientos_mancu=[]

print "¡Bienvenido a la interfaz de introducción de datos de entrenamiento! \n"

def semana_in():	
	#En esta función se define la semana de la que se están introduciendo valores
	s=raw_input("Por favor, introduzca la semana correspondiente a los valores a añadir (valor numérico): ")

	if (s=="1" or s=="2" or s=="3" or s=="4"):
		
		#Con global, hago que asigne a la variable global y que no trate semana como una variable local

		global semana
		semana=s

		print "\nSemana correcta\n" #implementar la funcion que tenga que ir aqui, el print es de control

	else:

		print "\nSemana incorrecta, introduzcala como se indica\n"
		#Si la semana introducida es incorrecta, se vuelve a llamar a la función semana_in. 
		semana_in()

def sentadilla():

	print "Por favor, introduzca los valores de las tres series de setandilla de la semana "+semana+": "

semana_in()
sentadilla()


#def press_banca():

#def dominadas():

#def remo_menton():

#def sentadilla_hack():

#def remo_punta():

#def curl_biceps():

#def jalon_pecho():

#def extension_cuadri():

#def curl_femoral():

#def triceps_polea_cabeza():

#def encogimientos_mancu():
