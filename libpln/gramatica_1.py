#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 
#  
#  Autor: Icaro Duarte Gavazza
#  Criado em: 15/09/15 14:51:52
#  Usuário: IFES Serra Lógica Prog\Téc Prog\Prog I\Prog II
#  
#  Função do programa: <manipular strings.>
#  Versão inicial: 1.0
#  ----------------------------------------------------------------
def separaPals(paramtxt):
	strbuffer = ""
	lst = []
	
	for elem in paramtxt:
		if (elem == "-" or elem == "'") or elem.isalnum():
			strbuffer += elem
		else:
			if strbuffer != "":
				lst.append(strbuffer)
				strbuffer = ""			
			#if
		#else
	#for
	if len(strbuffer) > 0:
		lst.append(strbuffer)
		
	return lst
#fim separaPalavras		

def extrairPlural(lstparam):
	dicsufixo = {"as":"as","es":"es","os":"os","is":"is","ns":"ns"}
	lstaux = []
	
	for pal in lstparam:
		aux = (pal[len(pal)-2])+(pal[len(pal)-1])
		
		if aux in dicsufixo:
			lstaux.append(pal)
			aux = ""
		#if
	#for
		
	return lstaux
#fim extrairPlural

def extrairdimi(lstparam):
	dicsufixo = {"nha": 1,"nho": 1}
	lstaux = []
	for pal in lstparam:
		if len(pal) > 3:
			aux = (pal[len(pal)-3])+(pal[len(pal)-2])+(pal[len(pal)-1])
		#if
		
		if aux in dicsufixo:
			lstaux.append(pal)
			aux = ""
		#if
	#for 
	return lstaux
#fim extrairdimi	

def extraiaument(lstparam):
	dicsufixo = {"ão": 1,"rra": 1,"zão":"zão"}
	lstaux = []
	
	for pal in lstparam:
		if len(pal) > 3:
			aux = (pal[len(pal)-3])+(pal[len(pal)-2])+(pal[len(pal)-1])
		#if
		if aux in dicsufixo:
			lstaux.append(pal)
			aux = ""
		#if
	#for	
	return lstaux
#fim extraiaument	
def main():
	strtxt = input("Digite um texto: ")
	lstpals = [] 
	lstpals = separaPals(strtxt)
	print(extraiaument(lstpals))
	print(extrairPlural(lstpals))
	print(extraiaument(lstpals))
	return 0

if __name__ == '__main__':
	main()

