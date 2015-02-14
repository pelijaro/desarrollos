#!/usr/bin/ python
# -*- coding: utf-8 -*-
from random import randint

tablero=[]

for n in range(5):

	tablero.append(["O"]*5)

def print_tablero(tablero):

	for fila in tablero:

		print " ".join(fila)

print "Juguemos a la batalla naval! \n"

print_tablero(tablero)

def fila_aleatoria(tablero):

	return randint (0, len(tablero)-1)

def columna_aleatoria(tablero):

	return randint(0, len(tablero)-1)

barco_fila=fila_aleatoria(tablero)
barco_columna=columna_aleatoria(tablero)

for turn in range(4):

	adivina_fila=int(raw_input("\nAdivina fila: "))
	adivina_columna=int(raw_input("Adivina columna: ")) 


	if barco_fila==adivina_fila and barco_columna==adivina_columna:

		print "\nFelicitaciones, hundiste mi barco!\n"
		break

	elif  adivina_fila not in range(len(tablero)) or adivina_columna\
        not in range(len(tablero)):

		print "\nHuy, eso ni siquiera esta en el oceano\n"

	elif tablero[adivina_fila][adivina_columna]=="X":

		print "\nYa dijiste eso\n"

	else:
		print "\nAgua, no tocaste mi barco \n"
		tablero[adivina_fila][adivina_columna]="X"
	
	print "Ha sido tu turno: %i " % (turn+1)+ "\n"

	print_tablero(tablero)

	if turn==3:

		print "\nFin del juego"
		



