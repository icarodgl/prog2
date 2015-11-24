#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# TAD_complexos.py
#  
#  Autor: ifes <ifes@ifes-vbox>
#  Criado em: 06/11/15 10:20:08
#  Usuário: IFES Serra Lógica Prog\Téc Prog\Prog I\Prog II
#  
#  Função do programa: <resumo da tarefa que o programa realiza.>
#  Versão inicial: 1.0
#  ----------------------------------------------------------------



def cria_imaginarioSTR(parstr):
	dicima={"real":"","imag":"","opera":""}
	aux=""
	for elem in parstr:
		aux+=elem
		if dicima["real"] =="" and elem in ["+","-"]:
			dicima["real"]=float(aux[:-1])
			aux=""
		#
		if elem == "i":
			dicima["imag"]=float(aux[:-1])
		
		#
		if elem in ["+","-"]:
			dicima["opera"]=elem
		#	
	return dicima
#cria STR

def cria_imaginario(parR, parI):
	return {"real":parR,"imag":parI,"opera":""}
#Fim Cria

def conjugado(parimag):
	dicomp={}
	dicomp["imag"]=(parimag["imag"])*(-1)
	dicomp["real"]=(parimag["real"])
	return dicomp
	
##conjugado
def oposto (parcomp):
	parcomp["imag"]=(parcomp["imag"])*(-1)
	parcomp["real"]=(parcomp["real"])*(-1)
	return parcomp
def soma_imaginario(parimag, parimag2):
	resposta={"opera":0,"real":0,"imag":0}
	resposta["real"]= parimag["real"]+parimag2["real"]
	resposta["imag"]= parimag["imag"]+parimag2["imag"]

	return resposta
##	Soma
def multiplica_imaginario(parimag,parimag2):
	resposta={}
	r1=(parimag["real"])*parimag2["real"]
	i1=(parimag["real"])*(parimag2["imag"])
	i2=parimag["imag"]*parimag2["real"]
	r2=(parimag["imag"]*parimag2["imag"])*(-1)
	resposta = soma_imaginario(parimag,parimag2)
	
	return resposta
## Multiplica

def divide_imagnario(parcomp,parcomp2):
	conjSec= conjugado(parcomp2)
	dividendo= multiplica_imaginario(parcomp, conjSec) 
	divisor=multiplica_imaginario(parcomp2, conjSec)
	print(str(dividendo["real"])+str(dividendo["imag"])+"i / "+str( divisor["real"]))
## divide
def subtrai_imaginario(parimag,parimag2):
	resposta={"opera":0,"real":0,"imag":0}
	resposta["real"]= parimag["real"]-parimag2["real"]
	resposta["imag"]= parimag["imag"]-parimag2["imag"]
	resposta["opera"]= parimag["opera"]
	return resposta
## Subtrai
def imprime_imaginario(img):
	print("%.1f %s %.1fi" %(img["real"],img["opera"],img["imag"]))
#fim Imprime
def main():


	#~ imagin = cria_imaginario(2,-3)
	#~ imagin2 = cria_imaginario(-1,2)
	#~ divide_imagnario(imagin,imagin2)
	#~ imprime_imaginario(imagin)
	#~ imprime_imaginario(imagin2)
	#~ imprime_imaginario(soma_imaginario(imagin,imagin2))
	#~ #imprime_imaginario(multiplica_imaginario(imagin,imagin2))
	#~ imprime_imaginario(subtrai_imaginario(imagin,imagin2))
	
	return 0

if __name__ == '__main__':
	main()

