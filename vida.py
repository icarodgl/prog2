#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  vida.py
#  
#  Copyright 2016 icaro <icaro@icaro-X550CA>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


import time
def printamundo(mundo):
	for col in mundo:
		print()
		for lin in col:
			print(lin,end=" ")
	print()
def mundo(larg,alt):
	mundo=[]
	
	for ind in range(larg):
		linha=[]
		for jind in range(alt):
			linha.append(".")
		mundo.append(linha)
	return mundo
	
##fim
def vida(mundo):
	tpvida=[]
	tpmorte=[]
	for col in range(len(mundo)):
		for lin in range(len(mundo[col])):
			vidas= vida_perto(mundo,col,lin)
			if mundo[col][lin] == "@":

			## Qualquer célula viva com menos de dois vizinhos vivos morre de solidão.
				if vidas <= 2 :
					tpmorte.append((col,lin))
					#~ mundo[col][lin] ="."
					
			##Qualquer célula viva com mais de três vizinhos vivos morre de superpopulação.
				if vidas > 4 :
					tpmorte.append((col,lin))
					#~ mundo[col][lin]="."
					
			## Qualquer célula viva com dois ou três vizinhos vivos continua no mesmo estado para a próxima geração.
			
			else:
			##Qualquer célula morta com exatamente três vizinhos vivos se torna uma célula viva.
				if vidas == 3  :
					tpvida.append((col,lin))
					#~ mundo[col][lin]="@"
	adiciona_morte(tpmorte,mundo)
	adiciona_vida(tpvida,mundo)
				
	return mundo
##fim
def vida_perto(mundo, col, lin):
	## definindo a coluna
	#~ if col-2 >= 0:
		#~ colIn=col-2
	if col-1 >= 0:
		colIn=col-1
	else:
		colIn=col
		
	if col+2 <= len(mundo):
		colFi=col+2
	elif col+1 <= len(mundo):
		colFi=col+1
	else:
		colFi=col
		
	#### definindo a linha
	#~ if lin-2 > 0:
		#~ linIn=lin-2
	if lin-1 >= 0:
		linIn=lin-1
	else:
		linIn=lin
		
	if lin+2 <= len(mundo[col]):
		linFi=lin+2
	elif lin+1 <= len(mundo[col]):
		linFi=lin+1
	else:
		linFi=lin
	
	###confere a vida proximo:
	vidas=0
	for elem in range(colIn,colFi):
		#~ print()
		for item in range (linIn,linFi):
			#~ print(mundo[elem][item],end="")
			if mundo[elem][item] == "@":
				vidas+=1
	#~ print()
	#~ print(colIn,colFi," ",linIn,linFi)
	#~ time.sleep(.5)
				
	return vidas
		
##fim
	
def adiciona_vida(vidas,mundo):##listas com tuplas [(col,lin),(1,2),(1,3)]	
	for elem in vidas:
		mundo[elem[0]][elem[1]]="@"
	return mundo
#fim
def adiciona_morte(morte,mundo):##listas com tuplas [(col,lin),(1,2),(1,3)]	
	for elem in morte:
		mundo[elem[0]][elem[1]]="."
	return mundo
#fim

def main(args):
	
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
