#!/usr/bin/ python
# -*- coding: utf-8 -*-

#Script acepta valores de pesos de diferentes ejercicios, formatea datos y sale en un archivo preparado para enviar email

semana=0
psentadilla=[]
ppress_banca=[]
pdominadas=[]
premo_menton=[]
psentadilla_hack=[]
premo_punta=[]
pcurl_biceps=[]
pjalon_pecho=[]
pextension_cuadri=[]
pcurl_femoral=[]
ptriceps_polea_cabeza=[]
pencogimientos_mancu=[]

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
	
	for p in range(3):
		
		print "Introduzca el ", p+1,"º peso: "
		peso=raw_input()
		#Colocar en un futuro un posible control de errores para la introducción de pesos
		global psentadilla
		psentadilla.append(peso)
	

def press_banca():

	print "Por favor, introduzca los valores de las tres series de press banca de la semana "+semana+": "
	
	for p in range(3):
	
		print "Introduzca el ", p+1,"º peso: "
		peso=raw_input()
		#Colocar en un futuro un posible control de errores para la introducción de pesos
		global ppress_banca
		ppress_banca.append(peso)

def dominadas():
	
	#Introducir en un futuro la opcion de meter el peso de lastre
	
	print "Por favor, introduzca los valores de las tres series de dominadas de la semana "+semana+": "
	
	for p in range(3):
	
		print "Introduzca el ", p+1,"º peso: "
		peso=raw_input()
		#Colocar en un futuro un posible control de errores para la introducción de pesos
		global pdominadas
		pdominadas.append(peso)
		
def remo_menton():

	print "Por favor, introduzca los valores de las tres series de remo menton de la semana "+semana+": "
	
	for p in range(3):
	
		print "Introduzca el ", p+1,"º peso: "
		peso=raw_input()
		#Colocar en un futuro un posible control de errores para la introducción de pesos
		global premo_menton
		premo_menton.append(peso)
		
def sentadilla_hack():

	print "Por favor, introduzca los valores de las tres series de sentadilla hack de la semana "+semana+": "
	
	for p in range(3):
	
		print "Introduzca el ", p+1,"º peso: "
		peso=raw_input()
		#Colocar en un futuro un posible control de errores para la introducción de pesos
		global psentadilla_hack
		psentadilla_hack.append(peso)
		
def remo_punta():

	print "Por favor, introduzca los valores de las tres series de remo en punta de la semana "+semana+": "
	
	for p in range(3):
	
		print "Introduzca el ", p+1,"º peso: "
		peso=raw_input()
		#Colocar en un futuro un posible control de errores para la introducción de pesos
		global premo_punta
		premo_punta.append(peso)

def curl_biceps():

	#Introducir en un futuro la opcion de los claster, que al meter las repes calcule los cluster, etc..
	
	print "Por favor, introduzca los valores de las tres series de curl de biceps de la semana "+semana+": "
	
	for p in range(3):
	
		print "Introduzca el ", p+1,"º peso: "
		peso=raw_input()
		#Colocar en un futuro un posible control de errores para la introducción de pesos
		global pcurl_biceps
		pcurl_biceps.append(peso)

def jalon_pecho():

	print "Por favor, introduzca los valores de las tres series de jalon de pecho de la semana "+semana+": "
	
	for p in range(3):
	
		print "Introduzca el ", p+1,"º peso: "
		peso=raw_input()
		#Colocar en un futuro un posible control de errores para la introducción de pesos
		global pjalon_pecho
		pjalon_pecho.append(peso)
		
def extension_cuadri():

	print "Por favor, introduzca los valores de las tres series de extension de cuadriceps de la semana "+semana+": "
	
	for p in range(3):
	
		print "Introduzca el ", p+1,"º peso: "
		peso=raw_input()
		#Colocar en un futuro un posible control de errores para la introducción de pesos
		global pextension_cuadri
		pextension_cuadri.append(peso)

def curl_femoral():

	print "Por favor, introduzca los valores de las tres series de curl femoral de la semana "+semana+": "
	
	for p in range(3):
	
		print "Introduzca el ", p+1,"º peso: "
		peso=raw_input()
		#Colocar en un futuro un posible control de errores para la introducción de pesos
		global pcurl_femoral
		pcurl_femoral.append(peso)
		
def triceps_polea_cabeza():

	print "Por favor, introduzca los valores de las tres series de triceps en polea por encima de la cabeza de la semana "+semana+": "
	
	for p in range(3):
	
		print "Introduzca el ", p+1,"º peso: "
		peso=raw_input()
		#Colocar en un futuro un posible control de errores para la introducción de pesos
		global ptriceps_polea_cabeza
		ptriceps_polea_cabeza.append(peso)
		
def encogimientos_mancu():

	print "Por favor, introduzca los valores de las tres series de encogimientos con mancuernas de la semana "+semana+": "
	
	for p in range(3):
	
		print "Introduzca el ", p+1,"º peso: "
		peso=raw_input()
		#Colocar en un futuro un posible control de errores para la introducción de pesos
		global pencogimientos_mancu
		pencogimientos_mancu.append(peso)