#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sem título.py
#  
#  Autor: Icaro Duarte Gavazza Lima <ifes@ifes-vbox>
#  Criado em: 25/09/15 10:36:09
#  Usuário: IFES Serra Lógica Prog\Téc Prog\Prog I\Prog II
#  
#  Função do programa: Justifica uma string.
#  Versão inicial: 1.0
#  ----------------------------------------------------------------
def corrente(parstr,parint):
	strpal=""
	ind= parint
	if not parstr[parint].isalnum() or parint > len(parstr):
		 return None
	#if
	
	while parstr[ind].isalnum() and len(parstr) > 0: #rebobina
		ind-=1
	#while
	while parstr[ind+1].isalnum():
		ind+=1
		strpal+=parstr[ind]
	#while

	return strpal
#fim
def justificador(parstr,parint):
	indic=0
	intcont=0
	lisresp=[]
	checa=True
	while checa == True:
		checa=False
		if len(parstr)> intcont:
			
#			if parstr[intcont].isalnum:
#				indic = intcont+parint
#				while indic > 0 and parstr[indic].isalnum() : #rebobina
#					indic-=1
#				intcont=indic
			lisresp.append(parstr[intcont:indic])
			intcont+=parint
			checa=True
		#if
	#while
	return lisresp
			
def imprime(parlista):
	
	for elem in parlista:
		print(elem)

#fim
def main():
	textstr="Neste sentido, a mobilidade dos capitais internacionais é uma das consequências do processo de comunicação como um todo."
	tamanho=20
	listares=[]
	listares=justificador(textstr,tamanho)
	imprime(listares)
	return 0

if __name__ == '__main__':
	main()

