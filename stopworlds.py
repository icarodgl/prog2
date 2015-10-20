#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  stopworlds.py
#  
#  Copyright 2015 Icaro Duarte gavazza Lima <icarodgl@gmail.com>
#  
import sys
import libpln
def removesw(parstr, parsw, parresp):
	listStr=libpln.separaPals(parstr)
	for elem in listStr:
		if elem.lower() not in parsw and elem.lower() not in parresp:
			parresp.append(elem.lower())
		#
	#
	return parresp
#
def listador():
	lsresp=[]
	arq = open("/home/icaro/escola/prog 2/bases-de-textos/stopworlds-ptbr.txt","r")
	linha= arq.readline()
	straux=""
	while linha != "":
		linha= arq.readline()
		if linha[-1 : len(linha)] == "\n" :
			straux = linha[0 : (len(linha)-1)]
			lsresp.append(straux)
		else:
			lsresp.append(linha)
	#
	return lsresp
#
def salvaresp(parls):
	arq= open(input("nome do arquivo a ser salvo"),"w")
	for elem in parls:
		arq.write(elem+"\n")
	#
	print("salvo")
#
def main():
	sw=listador()
	lsresp=[]
	nomearq="/home/icaro/escola/prog 2/bases-de-textos/bibliacatnt.txt" #input("nome do arquivo")
	arq = open(nomearq,"r")
	linha= arq.readline()
	while linha != "":
		removesw(linha, sw, lsresp)
		linha= arq.readline()
	#
	salvaresp(lsresp)
	return 0
#
if __name__ == '__main__':
	main()

