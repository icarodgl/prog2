#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  TAD_bola.py
#  
#  Copyright 2015 Icaro <icaro@icaro-X550CA>
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
#~ barra vetical dirreita
#~ [598, 320, 600, 340]
#~ (579, 319, 601, 341) 

#~ barra horizontal baixo
#~ [56, 598, 76, 600] 
#~ (55, 579, 77, 601)

#~ barra vertical esquerda
#~ [0, 524, 2, 544]
#~ (-1, 523, 21, 545) 


def cria_bola(diametro,x,y):
	return [x,y,x+diametro,y+diametro]
# cria_bola
def dir_bola(vet,barra,bola):
	
	AX= (barra[0] - bola[0]) #ax
	AY= (barra[1] - bola[1]) #ay
	BX= (barra[2] - bola[2]) #bx
	BY= (barra[3] - bola[3]) #by
	
	### posições possiveis da blinha bater
	VSE = (BX+BY ==0 and AX > 1 and AY > 1) ##vertice superior esquerda
	ME = (BX+BY+AY ==0 and AX > 1) # meio esquerda
	VIE = (AY+BX == 0 and AX >0 and BY < 0) #vertice inferior esquerda
	MB = (AX+BX+AY == 0 and BY < 0) #meio baixo
	VID =(AX+AY ==0 and BX < 0 and BY < 0) # vertice inferior direita
	VSD = (AX+BY == 0 and AY > 0 and BX < 0)# vertice superior direita
	MD = (AX+AY+BY == 0 and BX < 0)# meio direita
	MS = (AX+BX+BY ==0 and AY > 0)# meio superior
	######################################

	if vet =="NE": 
		
		if  VSE or ME or MS:
			return "NO"
			
		if VIE or MB or VID:
			return "SE"
		else:
			return "SO"
		
	if vet =="SE": 
		
		if MS or VSE or VSD:
			return"NE"
		if ME or VIE :
			return "SO"
		else:
			return "SO"
	if vet =="NO": 
		if MD or VSD:
			return"NE"
		if MB or VIE or VID:
			return "SO"
		else:
			return "NE"
	if vet =="SO":
		if MD or VID:
			return "SE"
		if VSD or MS or VSE:
			return "NO"
		else:
			return "SE"
			
			
	return "ops"
### dir_bola
def vet_bola(vet,lado):
	if lado == None:
		return vet
	else:
		if vet =="NE":
			if lado == "H":
				return "SE"
			if lado == "V":
				return "NO"

		if vet =="SE":
			if lado == "H":
				return"NE"
			if lado == "V":
				return "SO"
				
		if vet =="SO":
			if lado == "H":
				return"NO"
			if lado == "V":
				return "SE"
				
		if vet =="NO":
			if lado == "H":
				return"SO"
			if lado == "V":
				return "NE"
		
#fim move_bola
def move_bola(bola, vet):

	if vet =="SE":
		bola[0]+=2
		bola[1]+=2
		bola[2]+=2
		bola[3]+=2
		return bola
			
	if vet =="SO":
		bola[0]+=-2
		bola[1]+=2
		bola[2]+=-2
		bola[3]+=2
		return bola
			
	if vet =="NO":
		bola[0]+=-2
		bola[1]+=-2
		bola[2]+=-2
		bola[3]+=-2
		return bola
	if vet =="NE":
		bola[0]+=2
		bola[1]+=-2
		bola[2]+=2
		bola[3]+=-2
		return bola	
#move_bola
def main():

	
	return 0

if __name__ == '__main__':
	main()

