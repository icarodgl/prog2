#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pega_datas.py
#  
#  Autor: Icaro Duarte Gavazza Lima ifes <ifes@ifes-vbox>
#  Criado em: 22/09/15 13:21:10
#  Usuário: IFES Serra Lógica Prog\Téc Prog\Prog I\Prog II
#  
#  Função do programa:  retirar datas de um texto alocando em um dicionario com chaves {dia, mes e ano}
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

def extraidata(parstr):
	lispals=separaPals(parstr)
	dicresp={}
	dicmeses={"janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro","jan","fev","mar","abr","mai","jun","jul","ago","set","out","nov","dez"}
	for ind in range (len(lispals)):
		if lispals[ind] in dicmeses:
			dicresp["mes"]=lispals[ind]
		#if
		if lispals[ind].isdecimal():
			if int(lispals[ind]) >= 32:
				dicresp["ano"]=lispals[ind]
			#if
		#if
		if lispals[ind].isdecimal():
			if int(lispals[ind]) < 32:
				dicresp["dia"]=lispals[ind]
			#if
		#if
	#for
	return dicresp
def main():
	strtext="hoje 11 de set 2015"
	print(extraidata(strtext))
	return 0

if __name__ == '__main__':
	main()

