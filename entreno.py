#!/usr/bin/ python
# -*- coding: utf-8 -*-
import sys
#Script acepta valores de pesos de diferentes ejercicios, formatea datos y sale en un archivo preparado para enviar email

semana=0
mes=0
#Implementar el numero de variables dinamicas
series_2=2
series_3=3
series_4=4

rdominadas=[]

psentadilla=[]
ppress_banca=[]
pdominadas=0
premo_menton=[]
psentadilla_hack=[]
premo_punta=[]
pcurl_biceps=[]
pjalon_pecho=[]
pextension_cuadri=[]
pcurl_femoral=[]
ptriceps_polea_cabeza=[]
pencogimientos_mancu=[]

print "\n¡Bienvenido a la interfaz de introducción de datos de entrenamiento! \n"

def mes_in():

	#MEJORAR LA INTRODUCCIÓN DEL MES, YA QUE AL INTRODUCIR LETRAS O SIMBOLOS CRASEA.

	m=raw_input("\nPor favor, introduzca el mes correspondiente a los valores a añadir (valor numérico): ")
	m=int(m)
	print m
	while m<=0 or m>99:
		
		print "\nMes incorrecto, introduzcalo como se indica"
		m=raw_input("\nPor favor, introduzca el mes correspondiente a los valores a añadir (valor numérico): ")
		m=int(m)
		
	else:
	
		global mes
		mes=m
		
		print "\nMes correcto"
		
		
def semana_in():	
	#En esta función se define el mes y la semana de la que se están introduciendo valores
		
	s=raw_input("\nPor favor, introduzca la semana correspondiente a los valores a añadir (valor numérico): ")

	if (s=="1" or s=="2" or s=="3" or s=="4"):
		
		#Con global, hago que asigne a la variable global y que no trate semana como una variable local

		global semana
		semana=s

		print "\nSemana correcta" #implementar la funcion que tenga que ir aqui, el print es de control

	else:

		print "\nSemana incorrecta, introduzcala como se indica"
		#Si la semana introducida es incorrecta, se vuelve a llamar a la función semana_in. 
		semana_in()
		
def sentadilla():

	print "\nPor favor, introduzca los valores de las tres series de setandilla de la semana "+semana+": "
	
	for p in range(series_3):
		
		print "\nIntroduzca el ", p+1,"º peso: "
		peso=raw_input()
		#Colocar en un futuro un posible control de errores para la introducción de pesos
		if len(peso)==0 or peso==chr(32):
			
			global psentadilla
			psentadilla.append(0)
		
		else:
		
			psentadilla.append(peso)
	

def press_banca():

	#Definir en un futuro los distintos press banca
	
	print "\nPor favor, introduzca los valores de las tres series de press banca de la semana "+semana+": "
	
	for p in range(series_3):
	
		print "\nIntroduzca el ", p+1,"º peso: "
		peso=raw_input()
		#Colocar en un futuro un posible control de errores para la introducción de pesos
		global ppress_banca
		ppress_banca.append(peso)

def dominadas():
	
	if semana=="1":
	
		print "\nPor favor, introduzca el numero de repeticiones de cada serie de dominadas SIN LASTRE de la semana "+semana+": "
		
		for p in range(series_3):
		
			print "\nIntroduzca las repeticiones de la ", p+1,"º serie: "
			peso=raw_input()
			global rdominadas
			rdominadas.append(peso)
			
	else:
			
		print "\nPor favor, introduzca los valores de las tres series de dominadas de la semana "+semana+": "
		
		print "\nPor favor, introduzca el numero de repeticiones de las ", series_3," series de dominadas de la semana "+semana+": "
	
		peso=raw_input()
		
		for p in range(series_3):
		
			rdominadas.append(peso)
		
		print "\nIntroduzca el peso de las",series_3,"series de dominadas de la semana "+semana+": "
		
		peso=raw_input()
		global pdominadas
		pdominadas=peso
		
def remo_menton():

	print "\nPor favor, introduzca los valores de las tres series de remo menton de la semana "+semana+": "
	
	for p in range(series_3):
	
		print "\nIntroduzca el ", p+1,"º peso: "
		peso=raw_input()
		#Colocar en un futuro un posible control de errores para la introducción de pesos
		global premo_menton
		premo_menton.append(peso)
		
def sentadilla_hack():

	print "\nPor favor, introduzca los valores de las tres series de sentadilla hack de la semana "+semana+": "
	
	for p in range(series_4):
	
		print "\nIntroduzca el ", p+1,"º peso: "
		peso=raw_input()
		#Colocar en un futuro un posible control de errores para la introducción de pesos
		global psentadilla_hack
		psentadilla_hack.append(peso)
		
def remo_punta():

	print "\nPor favor, introduzca los valores de las tres series de remo en punta de la semana "+semana+": "
	
	for p in range(series_3):
	
		print "\nIntroduzca el ", p+1,"º peso: "
		peso=raw_input()
		#Colocar en un futuro un posible control de errores para la introducción de pesos
		global premo_punta
		premo_punta.append(peso)

def curl_biceps():

	#Introducir en un futuro la opcion de los claster, que al meter las repes calcule los cluster, etc..
	
	print "\nPor favor, introduzca los valores de las tres series de curl de biceps de la semana "+semana+": "
	
	for p in range(series_2):
	
		print "\nIntroduzca el ", p+1,"º peso: "
		peso=raw_input()
		#Colocar en un futuro un posible control de errores para la introducción de pesos
		global pcurl_biceps
		pcurl_biceps.append(peso)

def jalon_pecho():

	print "\nPor favor, introduzca los valores de las tres series de jalon de pecho de la semana "+semana+": "
	#Implementar el numero de variables dinamicas, ya que cada semana cambia
	for p in range(series_4):
	
		print "\nIntroduzca el ", p+1,"º peso: "
		peso=raw_input()
		#Colocar en un futuro un posible control de errores para la introducción de pesos
		global pjalon_pecho
		pjalon_pecho.append(peso)
		
def extension_cuadri():

	print "\nPor favor, introduzca los valores de las tres series de extension de cuadriceps de la semana "+semana+": "
	
	for p in range(series_4):
	
		print "\nIntroduzca el ", p+1,"º peso: "
		peso=raw_input()
		#Colocar en un futuro un posible control de errores para la introducción de pesos
		global pextension_cuadri
		pextension_cuadri.append(peso)

def curl_femoral():

	print "\nPor favor, introduzca los valores de las tres series de curl femoral de la semana "+semana+": "
	
	for p in range(series_4):
	
		print "\nIntroduzca el ", p+1,"º peso: "
		peso=raw_input()
		#Colocar en un futuro un posible control de errores para la introducción de pesos
		global pcurl_femoral
		pcurl_femoral.append(peso)
		
def triceps_polea_cabeza():

	print "\nPor favor, introduzca los valores de las tres series de triceps en polea por encima de la cabeza de la semana "+semana+": "
	
	for p in range(series_2):
	
		print "\nIntroduzca el ", p+1,"º peso: "
		peso=raw_input()
		#Colocar en un futuro un posible control de errores para la introducción de pesos
		global ptriceps_polea_cabeza
		ptriceps_polea_cabeza.append(peso)
		
def encogimientos_mancu():

	print "\nPor favor, introduzca los valores de las tres series de encogimientos con mancuernas de la semana "+semana+": "
	
	for p in range(series_2):
	
		print "\nIntroduzca el ", p+1,"º peso: "
		peso=raw_input()
		#Colocar en un futuro un posible control de errores para la introducción de pesos
		global pencogimientos_mancu
		pencogimientos_mancu.append(peso)
		
"""def fsentadilla():
	sys.stdout = open('file.txt', 'w')
    
	print "Sentadilla:", 

	for p in range(len(psentadilla)):
	
		if p==len(psentadilla)-1:
		
			print psentadilla[p],
	
		else:
		
			print psentadilla[p]+",",

def fpress_banca():


	for p in range(len(ppress_banca)):
	
		if p==len(ppress_banca)-1:
		
			print ppress_banca[p]
			
		else:
		
			print ppress_banca[p]+"," 
"""			


#def fdominadas():
#def fremo_menton():
#def fsentadilla_hack():
#def fremo_punta():
#def fcurl_biceps():
#def fjalon_pecho():
#def fextension_cuadri():
#def fcurl_femoral():
#def ftriceps_polea_cabeza():
#def fencogimientos_mancu():

def formatea():

	"""Como no sé cómo no sobreescribir en un fichero, lo tengo que formatear todo junto en vez de separado, cuando sepa como sobreescribir lo podre hacer por
	separado"""
	
	#Paso mes a string para poder utilizarlo en el nombre del fichero
	global mes
	mes=str(mes)
	
	sys.stdout = open("/home/entrenos/entreno_mes"+mes+"_semana"+semana+".doc", "w")

	print "Lunes:\n"
	
	print "Sentadilla:",
		
	for p in range(len(psentadilla)):
		
		if p==len(psentadilla)-1:
			
			print psentadilla[p]
			
		else:
			
			print str(psentadilla[p])+",",

	print "Press banca con parada en pecho:",
		
	for p in range(len(ppress_banca)):
		
		if p==len(ppress_banca)-1:
			
			print ppress_banca[p]
			
		else:
			
			print ppress_banca[p]+",",
				
	print "Dominadas:",
	
	if semana=="1":
	
		for p in range(len(rdominadas)):
		
			if p==len(rdominadas)-1:
			
				print "1x"+rdominadas[p]+" repeticiones"
				
			else:
			
				print "1x"+rdominadas[p]+",",
				
	else:
	
		print series_3,"x",rdominadas[0],"con", pdominadas,"kg de lastre"
				
	print "Remo al menton con barra Z:",
		
	for p in range(len(premo_menton)):
		
		if p==len(premo_menton)-1:
			
			print premo_menton[p]
			
		else:
			
			print premo_menton[p]+",",
	
	print "\nMiercoles:\n"
	
	print "Press banca normal:",
		
	for p in range(len(ppress_banca)):
		
		if p==len(ppress_banca)-1:
			
			print ppress_banca[p]
			
		else:
			
			print ppress_banca[p]+",",
				
	print "Sentadilla hack:",
		
	for p in range(len(psentadilla_hack)):
		
		if p==len(psentadilla_hack)-1:
			
			print psentadilla_hack[p]
			
		else:
			
			print psentadilla_hack[p]+",",
				
	print "Remo en punta:",
		
	for p in range(len(premo_punta)):
		
		if p==len(premo_punta)-1:
			
			print premo_punta[p]
			
		else:
			
			print premo_punta[p]+",",
				
	print "Curl de biceps con barra en clusters:",
		
	for p in range(len(pcurl_biceps)):
		
		if p==len(pcurl_biceps)-1:
			
			print pcurl_biceps[p]
			
		else:
			
			print pcurl_biceps[p]+",",
				
	print "\nViernes:\n"
	
	print "Press banca parcial:",
		
	for p in range(len(ppress_banca)):
	
		if p==len(ppress_banca)-1:
		
			print ppress_banca[p]
			
		else:
			
			print ppress_banca[p]+",",
	
	print "Jalon al pecho:",
		
	for p in range(len(pjalon_pecho)):
		
		if p==len(pjalon_pecho)-1:
			
			print pjalon_pecho[p]
			
		else:
			
			print pjalon_pecho[p]+",",
				
	print "Extension de cuadriceps:",
		
	for p in range(len(pextension_cuadri)):
		
		if p==len(pextension_cuadri)-1:
			
			print pextension_cuadri[p]
			
		else:
			
			print pextension_cuadri[p]+",",
				
	print "Curl de femoral:",
		
	for p in range(len(pcurl_femoral)):
		
		if p==len(pcurl_femoral)-1:
			
			print pcurl_femoral[p]
			
		else:
			
			print pcurl_femoral[p]+",",
			
	print "Extension de triceps en polea por encima de la cabeza:",
		
	for p in range(len(ptriceps_polea_cabeza)):
		
		if p==len(ptriceps_polea_cabeza)-1:
			
			print ptriceps_polea_cabeza[p]
			
		else:
			
			print ptriceps_polea_cabeza[p]+",",
				
	print "Encogimientos de trapecio con mancuernas:",
		
	for p in range(len(pencogimientos_mancu)):
		
		if p==len(pencogimientos_mancu)-1:
			
			print pencogimientos_mancu[p]
			
		else:
			
			print pencogimientos_mancu[p]+",",

			
mes_in()			
semana_in()
sentadilla()
press_banca()
dominadas()
remo_menton()
sentadilla_hack()
remo_punta()
curl_biceps()
jalon_pecho()
extension_cuadri()
curl_femoral()
triceps_polea_cabeza()
encogimientos_mancu()
formatea()