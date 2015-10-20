#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  abre aquivo.py
#  
#  Copyright 2015 Icaro Duarte gavazza Lima <icarodgl@gmail.com>
#  
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
	buff= ""
	dicresp={"dia":"","mes":"","ano":""}
	dicmeses={"janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro","jan","fev","mar","abr","mai","jun","jul","ago","set","out","nov","dez"}
	for ind in range (len(lispals)):
	
		if lispals[ind].lower() in dicmeses :
			
			dicresp["mes"]=lispals[ind].lower()
			if buff.isdecimal():
				 dicresp["dia"]=buff
			#
			if buff in ["de","do"]:
				dicresp["dia"] = lispals[ind-2]
			if len(lispals)>= 2 and (lispals[ind-2]).isdecimal():
				dicresp["dia"]=lispals[ind-2]
			#
		#
		if lispals[ind].isdecimal():
			if int(lispals[ind]) <= 12 and buff in ["do","de"]:
				if buff.isdecimal():
					 dicresp["dia"]=int(buff)
				dicresp["mes"]=int(lispals[ind])
		#
		if lispals[ind].isdecimal():
			if int(lispals[ind]) >= 1800:
				dicresp["ano"]=int(lispals[ind])
			#if
		#if
		buff= lispals[ind]
	#for
	return dicresp
def imprimedata(dicdatas,parint):

		if dicdatas["dia"] != "" :
			print(parint, "- dia: ", dicdatas["dia"])
		if dicdatas["mes"] != "" :
			print(parint, "- mes: ", dicdatas["mes"])
		if dicdatas["ano"] != "" :
			print(parint, "- ano: ", dicdatas["ano"])

def main():
	cont=0
	arq = open("./bases-de-textos/coddefesaconsumidor.txt","rt")
	while arq.readline() != "":
		linha = arq.readline()
		dicdatas = extraidata(linha)
		cont+=1
		imprimedata(dicdatas,cont)
	arq.close()
	return 0

if __name__ == '__main__':
	main()

