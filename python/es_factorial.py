#!/usr/bin/ python
# -*- coding: utf-8 -*-

"""def factorial(numero):

	factorial=1	

	while numero>0:
		
		factorial*=numero
		numero-=1
	return factorial"""

def factorial(numero):

	factorial=1

	for f in range(numero,0,-1):

		factorial*=f

	return factorial

print factorial(12)
		

