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


def limpia_dato(d):

	#Función que limpia el dato introducido para que pueda ser comprobado en la siguiente función
	
	#Si, en el dato introducido, se encuentra un espacio en blanco y un punto 
	
	if (d.find(" ")!=-1 and d.find(".")!=-1):
	
		#Se reemplaza, el espacio en blanco o el punto, por una cadena vacia, es decir, se elimina
		
		d=d.replace(".","")
		d=d.replace(" ","")
		
		#Se devuelve el dato "limpio"
		
		return d
		
	#Si, en el dato introducido, se encuentra un espacio en blanco 
	
	elif d.find(" ")!=-1:
	
		#Se reemplaza, el espacio en blanco, por una cadena vacia, es decir, se elimina
		
		d=d.replace(" ","")
		
		#Se devuelve el dato limpio
		
		return d
		
	#Si, en el dato introducido, se encuentra un espacio en blanco 
	
	elif d.find(".")!=-1:
	
		#Se reemplaza, el punto, por una cadena vacia
		
		d=d.replace(".","")
		
		#Se devuelve el dato "limpio"
		
		return d
	
	#Si no encuentra ni espacios en blanco ni puntos, se devuelve el dato segun se ha introducido
	
	else:
		
		#Se devuelve el dato segun se ha introducido
		
		return d
		
		
def comprueba_dato(d):

	#Función que comprueba que el número introducido sea realmente un número
	
	#Inicializa c a cero
	
	c=0
	
	#If que comprueba que la cadena no sea una cadena vacia
	
	if len(d)>0:
	
		#While que recorre carácter a carácter comprobando si son digitos
		
		while d[c].isdigit()==True:
		
			#Si es un digito y ademas es el ultimo, decuelve un False(que se utiliza en el while, para salir de este), verificando que la cadena está 
			#compuesta de solo digitos
			
			if c==(len(d)-1):
			
				return False
				
			#Si es un digito pero no es el último, hace c+1, para poder seguir iterando por el numero	
			
			else:
			
				c+=1
				
		#En el momento que el numero contenga un carácter que no sea un digito, devolverá True, para que el ciclo while siga ejecutandose		
		
		else:
		
			return True
			
	#Si la cadena está vacia, devolverá True, para que el ciclo while siga ejecutandose
	
	else:
	
		return True


def mes_in():

	#MEJORAR LA INTRODUCCIÓN DEL MES, YA QUE AL INTRODUCIR LETRAS O SIMBOLOS CRASEA.

	m=raw_input("\nPor favor, introduzca el mes correspondiente a los valores a añadir (valor numérico): ")
	m=int(m)
	print m
	print type(m)
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
	#HACERLA CON UN WHILE, MEJOR!!
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
		
		print "\nIntroduzca el", p+1,"º peso: "
		peso=raw_input()
				
		global psentadilla
		
		while comprueba_dato(limpia_dato(peso)):
		
			print "\nIntroduzca el", p+1,"º peso: "
			peso=raw_input()
			
		else:
			
			psentadilla.append(peso)
	

def press_banca():

	#Definir en un futuro los distintos press banca
	
	print "\nPor favor, introduzca los valores de las tres series de press banca de la semana "+semana+": "
	
	for p in range(series_3):
	
		print "\nIntroduzca el", p+1,"º peso: "
		peso=raw_input()
		
		while comprueba_dato(limpia_dato(peso)):
		
			print "\nIntroduzca el", p+1,"º peso: "
			peso=raw_input()
			
		else:
		
			ppress_banca.append(peso)

def dominadas():
	
	if semana=="1":
	
		print "\nPor favor, introduzca el numero de repeticiones de cada serie de dominadas SIN LASTRE de la semana "+semana+": "
		
		global rdominadas
		
		for p in range(series_3):
		
			print "\nIntroduzca las repeticiones de la", p+1,"º serie: "
			peso=raw_input()
			

			
			
			while comprueba_dato(limpia_dato(peso)):
			
				print "\nIntroduzca las repeticiones de la", p+1,"º serie: "
				peso=raw_input()
				
			else:
			
				rdominadas.append(peso)
			
	else:
			
		print "\nPor favor, introduzca los valores de las tres series de dominadas de la semana "+semana+": "
		
		print "\nPor favor, introduzca el numero de repeticiones de las ", series_3," series de dominadas de la semana "+semana+": "
	
		peso=raw_input()
			
		while comprueba_dato(limpia_dato(peso)):
		
			print "\nPor favor, introduzca el numero de repeticiones de las ", series_3," series de dominadas de la semana "+semana+": "
			peso=raw_input()
			
		else:
		
			for p in range(series_3):
			
				rdominadas.append(peso)
			
		print "\nIntroduzca el peso de las",series_3,"series de dominadas de la semana "+semana+": "
		
		peso=raw_input()
				
		global pdominadas
		
		while comprueba_dato(limpia_dato(peso)):
		
			print "\nIntroduzca el peso de las",series_3,"series de dominadas de la semana "+semana+": "
			peso=raw_input()
			
		else:
		
			pdominadas=peso
		
def remo_menton():

	print "\nPor favor, introduzca los valores de las tres series de remo menton de la semana "+semana+": "
	
	for p in range(series_3):
	
		print "\nIntroduzca el ", p+1,"º peso: "
		peso=raw_input()

		global premo_menton
		
		while comprueba_dato(limpia_dato(peso)):
		
			print "\nIntroduzca el", p+1,"º peso: "
			peso=raw_input()
			
		else:
			
			premo_menton.append(peso)
		
def sentadilla_hack():

	print "\nPor favor, introduzca los valores de las tres series de sentadilla hack de la semana "+semana+": "
	
	for p in range(series_4):
	
		print "\nIntroduzca el", p+1,"º peso: "
		peso=raw_input()
		
		global psentadilla_hack
		
		while comprueba_dato(limpia_dato(peso)):
		
			print "\nIntroduzca el", p+1,"º peso: "
			peso=raw_input()
			
		else:
			
			psentadilla_hack.append(peso)
		
def remo_punta():

	print "\nPor favor, introduzca los valores de las tres series de remo en punta de la semana "+semana+": "
	
	for p in range(series_3):
	
		print "\nIntroduzca el", p+1,"º peso: "
		peso=raw_input()
		
		global premo_punta
		
		while comprueba_dato(limpia_dato(peso)):
		
			print "\nIntroduzca el", p+1,"º peso: "
			peso=raw_input()
			
		else:
			
			premo_punta.append(peso)
			
def curl_biceps():

	#Introducir en un futuro la opcion de los claster, que al meter las repes calcule los cluster, etc..
	
	print "\nPor favor, introduzca los valores de las tres series de curl de biceps de la semana "+semana+": "
	
	for p in range(series_2):
	
		print "\nIntroduzca el", p+1,"º peso: "
		peso=raw_input()

		global pcurl_biceps
		
		while comprueba_dato(limpia_dato(peso)):
		
			print "\nIntroduzca el", p+1,"º peso: "
			peso=raw_input()
			
		else:
			
			pcurl_biceps.append(peso)

def jalon_pecho():

	print "\nPor favor, introduzca los valores de las tres series de jalon de pecho de la semana "+semana+": "
	#Implementar el numero de variables dinamicas, ya que cada semana cambia
	for p in range(series_4):
	
		print "\nIntroduzca el", p+1,"º peso: "
		peso=raw_input()

		global pjalon_pecho
		
		while comprueba_dato(limpia_dato(peso)):
		
			print "\nIntroduzca el", p+1,"º peso: "
			peso=raw_input()
			
		else:
			
			pjalon_pecho.append(peso)
		
def extension_cuadri():

	print "\nPor favor, introduzca los valores de las tres series de extension de cuadriceps de la semana "+semana+": "
	
	for p in range(series_4):
	
		print "\nIntroduzca el", p+1,"º peso: "
		peso=raw_input()

		global pextension_cuadri
		
		while comprueba_dato(limpia_dato(peso)):
		
			print "\nIntroduzca el", p+1,"º peso: "
			peso=raw_input()
			
		else:
			
			pextension_cuadri.append(peso)
			
def curl_femoral():

	print "\nPor favor, introduzca los valores de las tres series de curl femoral de la semana "+semana+": "
	
	for p in range(series_4):
	
		print "\nIntroduzca el", p+1,"º peso: "
		peso=raw_input()
		
		global pcurl_femoral
		
		while comprueba_dato(limpia_dato(peso)):
		
			print "\nIntroduzca el", p+1,"º peso: "
			peso=raw_input()
			
		else:
			
			pcurl_femoral.append(peso)
		
def triceps_polea_cabeza():

	print "\nPor favor, introduzca los valores de las tres series de triceps en polea por encima de la cabeza de la semana "+semana+": "
	
	for p in range(series_2):
	
		print "\nIntroduzca el", p+1,"º peso: "
		peso=raw_input()
		
		global ptriceps_polea_cabeza
		
		while comprueba_dato(limpia_dato(peso)):
		
			print "\nIntroduzca el", p+1,"º peso: "
			peso=raw_input()
			
		else:
			
			ptriceps_polea_cabeza.append(peso)
			
def encogimientos_mancu():

	print "\nPor favor, introduzca los valores de las tres series de encogimientos con mancuernas de la semana "+semana+": "
	
	for p in range(series_2):
	
		print "\nIntroduzca el", p+1,"º peso: "
		peso=raw_input()

		global pencogimientos_mancu
		
		while comprueba_dato(limpia_dato(peso)):
		
			print "\nIntroduzca el", p+1,"º peso: "
			peso=raw_input()
			
		else:
			
			pencogimientos_mancu.append(peso)
		
		
#IDEA PARA EL FUTURO, FORMATEAR POR SEPARADO Y METER TODAS LAS FUNCIONES EN UNA FUNCIÓN PRINCIPAL
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
			
			print str(ppress_banca[p])+",",
				
	print "Dominadas:",
	
	if semana=="1":
	
		for p in range(len(rdominadas)):
		
			if p==len(rdominadas)-1:
			
				print "1x"+str(rdominadas[p])+" repeticiones"
				
			else:
			
				print "1x"+str(rdominadas[p])+",",
				
	else:
	
		print series_3,"x",rdominadas[0],"con", pdominadas,"kg de lastre"
				
	print "Remo al menton con barra Z:",
		
	for p in range(len(premo_menton)):
		
		if p==len(premo_menton)-1:
			
			print premo_menton[p]
			
		else:
			
			print str(premo_menton[p])+",",
	
	print "\nMiercoles:\n"
	
	print "Press banca normal:",
		
	for p in range(len(ppress_banca)):
		
		if p==len(ppress_banca)-1:
			
			print ppress_banca[p]
			
		else:
			
			print str(ppress_banca[p])+",",
				
	print "Sentadilla hack:",
		
	for p in range(len(psentadilla_hack)):
		
		if p==len(psentadilla_hack)-1:
			
			print psentadilla_hack[p]
			
		else:
			
			print str(psentadilla_hack[p])+",",
				
	print "Remo en punta:",
		
	for p in range(len(premo_punta)):
		
		if p==len(premo_punta)-1:
			
			print premo_punta[p]
			
		else:
			
			print str(premo_punta[p])+",",
				
	print "Curl de biceps con barra en clusters:",
		
	for p in range(len(pcurl_biceps)):
		
		if p==len(pcurl_biceps)-1:
			
			print pcurl_biceps[p]
			
		else:
			
			print str(pcurl_biceps[p])+",",
				
	print "\nViernes:\n"
	
	print "Press banca parcial:",
		
	for p in range(len(ppress_banca)):
	
		if p==len(ppress_banca)-1:
		
			print ppress_banca[p]
			
		else:
			
			print str(ppress_banca[p])+",",
	
	print "Jalon al pecho:",
		
	for p in range(len(pjalon_pecho)):
		
		if p==len(pjalon_pecho)-1:
			
			print pjalon_pecho[p]
			
		else:
			
			print str(pjalon_pecho[p])+",",
				
	print "Extension de cuadriceps:",
		
	for p in range(len(pextension_cuadri)):
		
		if p==len(pextension_cuadri)-1:
			
			print pextension_cuadri[p]
			
		else:
			
			print str(pextension_cuadri[p])+",",
				
	print "Curl de femoral:",
		
	for p in range(len(pcurl_femoral)):
		
		if p==len(pcurl_femoral)-1:
			
			print pcurl_femoral[p]
			
		else:
			
			print str(pcurl_femoral[p])+",",
			
	print "Extension de triceps en polea por encima de la cabeza:",
		
	for p in range(len(ptriceps_polea_cabeza)):
		
		if p==len(ptriceps_polea_cabeza)-1:
			
			print ptriceps_polea_cabeza[p]
			
		else:
			
			print str(ptriceps_polea_cabeza[p])+",",
				
	print "Encogimientos de trapecio con mancuernas:",
		
	for p in range(len(pencogimientos_mancu)):
		
		if p==len(pencogimientos_mancu)-1:
			
			print pencogimientos_mancu[p]
			
		else:
			
			print str(pencogimientos_mancu[p])+",",

			
print "\n¡Bienvenido a la interfaz de introducción de datos de entrenamiento! \n"

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
