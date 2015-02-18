#!/usr/bin/ python
# -*- coding: utf-8 -*-

"""def suma_de_digitos(numero):

	numero=str(numero)
	total=0

	for d in numero:

		d=int(d)
		total+=d
	
	print total

suma_de_digitos(84)"""

def suma_de_digitos(n):
	#Calcula el numero de cifras	
	n=str(n)
	longitud=len(n)
	n=int(n)
	total=0

	if longitud==1:

		return n
	else:

		for c in range(longitud-1):
		
			numero=n/10
			modulo=n%10
			n=numero
			
			#Otra forma
			
			"""modulo=n%10
			   n=n/10"""
		
			if c==longitud-2:

				total=total+modulo+n

			else:

				total+=modulo

		return total

print suma_de_digitos(5)
