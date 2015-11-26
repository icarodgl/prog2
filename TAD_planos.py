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
def sobreposicao_planos(pl1,pl2):
	pontos=[]
	
	for i in range(len(pl1)):
		for j in range(len(pl2)):
			if i in [0,2]:
				if j in [1,3]:
					pontos.append((pl1[i],pl2[j]))
					pontos.append((pl1[i],pl1[j]))
					
					pontos.append((pl2[i],pl1[j]))
					pontos.append((pl2[i],pl2[j]))	
	print(pontos)				
	pontos = magica_planos(pl1,pl2,pontos)
	return pontos
# fim sobreposição_planos

def magica_planos(pl1,pl2,pontos):
	lsaux=[]
	menor = ()
	maior = ()
	for elem in pontos:
		
		if elem[0] >= pl1[0] and elem[0] <= pl1[2]:#ponto esta no pl1[x]?
			if elem[1] >= pl1[1] and elem[1] <= pl1[3]:#ponto esta pl1[y]
				
				if elem[0] >= pl2[0] and elem[0] <= pl2[2]:#ponto esta no pl2[x]
					if elem[1] >= pl2[1] and elem[1] <= pl2[3]:#ponto esta pl2[y]
						lsaux.append(elem)#esta entre xy de pl1 e pl2
	for elemA in lsaux:
		for elemB in lsaux:
			if elemA[0] < elemB[0] and elemA[1] < elemB[1]:#menor xy
				menor = elemA #lado menor
			if elemA[0] > elemB[0] and elemA[1] > elemB[1]:# maior xy
				maior = elemA #lado maior
	if maior != () and menor != ():
		return [menor[0],menor[1],maior[0],maior[1]] #retorna bonitinho
	else:
		return None
#acabou a magica =/
def main():
	p1="10 10 50 50"
	p2="60 60 70 70"
	#~ plano1=cria_plano(p1)
	#~ plano2=cria_plano(p2)
	#~ print(plano1,plano2)
	#~ print(area_sobreposta(plano1,plano2))
	p1=cria_plano(p1)
	
	p2=cria_plano(p2)
	
	sobreposto = sobreposicao_planos(p1,p2)
	print(sobreposto)
	return 0

if __name__ == '__main__':
	main()

