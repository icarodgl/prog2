#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  achapalavras.py
#  
#  Autor: Icaro Duarte Gavazza Lima
#  Criado em: 18/09/15 10:40:00
#  Usuário: IFES Serra Lógica Prog\Téc Prog\Prog I\Prog II
#  
#  Função do programa: identificar palavra de uma string em uma posição dada.
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
	ind+=1
	while parstr[ind].isalnum() and len(parstr) > ind+1 : # pega a palavra
		strpal+=parstr[ind]
		ind+=1
	#while
	return strpal
#fim

def anterior(parstr,parint):
	strpal=""
	ind= parint
	
	if not parstr[parint].isalnum() or parint < 0:
		 return None
	#if
	while parstr[ind].isalnum() and len(parstr) > 0 and ind >= 0: #rebobina até o primeiro espaço
		ind-=1
		if ind <=0 :
			return None
		#if
	#while
	while not parstr[ind].isalnum() and len(parstr) > 0 and ind >= 0: #rebobina até a primeira letra
		ind-=1
		if ind <=0 :
			return None
		#if
	#while
	while parstr[ind].isalnum() and len(parstr) > 0 and ind >= 0: #rebobina a palavra
		ind-=1
	#while
	ind+=1
	while parstr[ind].isalnum():# escreve a palavra
		strpal+=parstr[ind]
		ind+=1
	#while
	return strpal
#fim


def posterior(parstr,parint):
	strpal=""
	ind= parint
	
	if not parstr[parint].isalnum() or parint > len(parstr):
		 return None
	#if
	
	while parstr[ind].isalnum() and len(parstr) > 0: #avança até o primeiro espaço
		if ind+1 >= len(parstr):
			return None
		#if
		ind+=1
	#while
	while not parstr[ind].isalnum() and len(parstr) > 0: #avança enquanto for separador
		if ind+1 >= len(parstr):
			return None
		#if
		ind+=1
	#while
	while parstr[ind].isalnum():# escreve a palavra
		if ind+1 >= len(parstr):
			return None
		#if
		strpal+=parstr[ind]
		ind+=1
	#while
	return strpal
#fim

def main():
	textstr="Goiaba deixa a salada melhor."
	intpos=9
	print(corrente(textstr, intpos))
	print(anterior(textstr,intpos))
	print(posterior(textstr,intpos))
	return 0
#fim
if __name__ == '__main__':
	main()

