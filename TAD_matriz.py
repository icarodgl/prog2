#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  TAD_matriz.py
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
def cria_matriz(alt,larg):
	return {"dim":(alt,larg)}
#fim cria_matriz
def setxy_matriz(mat,lin, col,val):
	if mat["dim"][0] > lin and mat["dim"][1] > col:
		mat[(lin,col)]= val
		return mat
	else:
		return None
#fim setxy_matriz
def removeZero_matriz(mat):
	lsaux = []
	for elem in mat:
		if mat[elem] == 0:
			lsaux.append(elem)
	for elem in lsaux:
		del mat[elem]
	return mat
	
#remove zeros
def mostra_matriz(mat):
	for i in range(mat["dim"][0]):
		print("")
		for j in range(mat["dim"][1]):
			if (i,j) not in mat:
				print(0 , end=" ")
			else:
				print(mat(i,j))
	print("\n")
#fim mostra
def getxy_matriz(mat,parx,pary):
	if (parx,pary) in mat:
		return mat[(parx,pary)]
	else:
		return 0
#fim getxy
def soma_matriz(matA,matB):
	if matA["dim"] != matB["dim"]:
		return None
	matR={}
	for elem in matA:
		if elem in matA and elem in matB:
			matR[elem]= matA[elem] + matB[elem]
		if elem in matA and elem not in matB:
			matR[elem]= matA[elem]
		if elem in matB and elem not in matA:
			matR[elem]= matB[elem]
	removeZero_matriz(matR)
	return matR
#fim soma

def multiplica_K_matriz(mat,k):
	for elem in mat:
		mat[elem]=mat[elem]*k
	return mat
#fim multiplica por K
def multiplica_matriz(matA,matB):
	#for in
	return None
	
#fim multiplica matrizes

def pega_valor_matriz(mat,val): #ajuda para o tad_planos
	salva_ini=[100000,100000]
	salva_fim=[0,0]
	ok1=False
	ok2=False
	for elem in mat:
		if mat[elem] == val and elem[0]<= salva_ini[0] and elem[1]<= salva_ini[1] :
			salva_ini[0]=elem[0]
			salva_ini[1]=elem[1]
			ok1=True
		if mat[elem] == val and elem[0]>= salva_fim[0] and elem[1]>= salva_fim[1] :
			salva_fim[0]=elem[0]
			salva_fim[1]=elem[1]	
			ok2=True
			
	if ok1 == False and ok2 == False:
		return None
	else:
		return [salva_ini[0],salva_ini[1],salva_fim[0],salva_fim[1]]
#pega_valor_matriz
def main():
	#~ lin=2
	#~ col=2
	#~ val=0
	#~ k=4
	#~ mat1 = cria_matriz(10,10)
	#~ mat2 = cria_matriz(10,10)
	#~ print(setxy_matriz(mat1,lin,col,val))
	#~ print(removeZero_matriz(mat1))
	#~ mostra_matriz(mat1)
	#~ print(getxy_matriz(mat1,lin,col))
	#~ soma_matriz(mat1, mat2)
	#~ multiplica_K_matriz(mat1,k)
	#~ multi_matriz(mat1,mat2)
	#~ transposta_matris(mat1)
	#~ subtrai(mat1,mat2)
	#~ crop_matriz(mat1,linha,coluna,356)
	return 0

if __name__ == '__main__':
	main()

