#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  abre_arq_frequencia.py
#  
#  Copyright 2015 Icaro Duarte gavazza Lima <icarodgl@gmail.com>


from separapals import *
from frequencia_pals import *
def imprime (pdic):
	arq = open("save.txt","w")
	for elem in pdic:
		print (elem," ",pdic[elem])
		arq.write(elem + ":" + str(pdic[elem]) + "\n")
	arq.close()
	

def main():
	arq = open("./bases-de-textos/bibliacatnt.txt","rt")
	listapals=[]
	dicfreq={}
	while arq.readline() != "":
		linha = arq.readline()
		listapals= separaPals(linha)
		dicfreq = frequenciador(listapals,dicfreq)
	#while
	imprime(dicfreq)
	arq.close()
	return 0

if __name__ == '__main__':
	main()

