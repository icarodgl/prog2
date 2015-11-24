#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lib_planos.py
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
import TAD_matriz as trix

def cria_plano(parstr):
	lsplano = parstr.split()
	for ind in range(len(lsplano)):
		num= lsplano[ind]
		lsplano[ind]=int(num)
	return lsplano
# fim cria_plano

def area_sobreposta(plano1,plano2):## o primeiro plano está na camada a cima.
	matrix = trix.cria_matriz(100000,100000)
	matrix2 = trix.cria_matriz(100000,100000)
	
	for i in range (plano1[0] , plano1[2]):
		for j in range (plano1[1], plano1[3]):
			trix.setxy_matriz(matrix,i,j,1)
			
	for i in range (plano2[0],plano2[2]):
		for j in range (plano2[1],plano2[3]):
			trix.setxy_matriz(matrix2,i,j,1)
			
	revolution = trix.soma_matriz(matrix,matrix2)
	
	inter = trix.pega_valor_matriz(revolution,2)
			
	if inter == None:
		return None
	else:
		return inter
	
#fim area_sobreposta

def main():
	p1="100 100 200 200" ## xy inicial , xy final
	p2=" 150 150 250 250" ## xy inicial , xy final
	plano1=cria_plano(p1)
	plano2=cria_plano(p2)
	print(plano1,plano2)
	print(area_sobreposta(plano1,plano2))
	return 0

if __name__ == '__main__':
	main()

