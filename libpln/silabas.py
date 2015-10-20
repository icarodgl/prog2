#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  silabas.py
#  
#  Copyright 2015 Icaro Duarte gavazza Lima <icarodgl@gmail.com>
#  
def silabas(parstr):
	vog={"a","e","i","o","u","y"}
	con={"b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","x","w","z"}
	cond={"s","r","l","s","c","n"}
	resultado=[]
	straux=""
	for ind in range(len(parstr)): 
		if ind == 0 and parstr[ind] in vog:## insere se a palavra iniciar com vogal
			resultado.append(parstr[ind])
		#if
		straux+=parstr[ind] ## acumula letras
		if straux[0] in con:
			
	#if
	return resultado
	#fim

def main():
	palavrastr="cachorro"
	print(silabas(palavrastr))
	return 0
#fim
if __name__ == '__main__':
	main()

