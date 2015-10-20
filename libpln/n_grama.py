#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Icaro gavazza
#prog 2
def n_grama(par_str,par_n): 
	listares=[]
	straux=""
	intaux=0
	for ind in range (len(par_str)):
		intaux=ind+par_n
		if intaux <= len(par_str):
			for indn in range(ind,intaux):
				straux+=par_str[indn]
			listares.append(straux)
			straux=""
			#for
		else:
			return listares
		#if
	#for
#def
def main():
	stra="pera"
	int_n=3
	lisngrama = n_grama(stra,int_n)
	print(lisngrama)
	return 0

if __name__ == '__main__':
	main()
