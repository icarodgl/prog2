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

def cria_bola(diametro,x,y):
	return [x,y,x+diametro,y+diametro]
# cria_bola

def vet_bola(vet,lado):
	if lado == None:
		return vet
	else:
		if vet =="NE":
			if lado == "H":
				return "SE"
			if lado == "L":
				return "NO"

		if vet =="SE":
			if lado == "H":
				return"NE"
			if lado == "L":
				return "SO"
				
		if vet =="SO":
			if lado == "H":
				return"NO"
			if lado == "L":
				return "SE"
				
		if vet =="NO":
			if lado == "H":
				return"SO"
			if lado == "L":
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

