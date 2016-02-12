#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  jogo_da_vida.py
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
import vida
import tkinter
import time
import os

def cria_mundo(matriz,mundo,tela):
	lis=[]
	#####
	for col in range(len(mundo)):
		for lin in range(len(mundo[col])):
			lis.append("x")
		matriz.append(lis)
		lis=[]
		
	#####
	tamanho = 8
	ho=0
	ver=0
	for col in range (len(matriz)):
		ho+=tamanho
		ver=0
		for lin in range (len(matriz[col])):	
			ver+=tamanho
			if mundo[col][lin] == "@":
				matriz[col][lin]= tela.create_rectangle([ho-tamanho,ver-tamanho,ho-1,ver-1],width=1,fill="blue")
			else:
				matriz[col][lin]= tela.create_rectangle([ho-tamanho,ver-tamanho,ho-1,ver-1],width=1,fill="gray")
	return matriz

def atualiza_mundo(matriz,mundo,tela):
	for col in range (len(matriz)):
		for lin in range (len(matriz[col])):	
			cor = tela.itemcget(matriz[col][lin], option="fill")
			if mundo[col][lin] == "@" and cor == "gray" :
				tela.itemconfig(matriz[col][lin], fill="blue")
			
			if mundo[col][lin] == "." and cor == "blue" :
				tela.itemconfig(matriz[col][lin], fill="gray")
				
	return matriz
def rodaEmTk(mundoA,mundoL,dormir):
	#####################
	janela = tkinter.Tk()	#
	canvas_altura = 820	#
	canvas_largura = 820	#
	tela = tkinter.Canvas(janela, bg='white', width=canvas_largura, height=canvas_altura)
	###prepara
	mundo = vida.mundo(mundoA,mundoL)
	######### vidas :
	#vidas imortais:
	#~ vidas = [(1,5),(1,6),(1,7),\
	#~ (6,5),(6,6),(7,5),(8,6),(7,7),\
	#~ (10,11),(10,12),(10,13),(11,10),(11,11),(11,12),\
	#~ (15,15),(15,16),(16,15),(16,16)] ## blink, bote, sapo e cubo; respectivamente
	
	vidas= [(22,25),(22,26),(23,24),(24,23),(25,23),(26,23),(27,24),(28,25),(28,26)] ## Gun
	
	#~ vidas= [(25,20),(25,21),(25,22),(25,23),(25,24),(25,25),(25,26),\
	#~ (25,27),(25,28),(25,29),(25,30),(25,31),(25,32),(25,33),(25,34),\
	#~ (25,35),(25,36),(25,37),(25,38),(25,39),(25,40),(25,41),(25,42),\
	#~ (25,43),(25,44),(25,45),(25,46),(25,47),(25,48),(25,49),(25,50),\
	#~ (25,51),(25,52) ,(25,53),(25,54),(25,55),(25,56),(25,57),(25,58),\
	#~ (25,59),(25,60),(25,61),(25,62),(25,63),(25,64),(25,65),(25,66),]

	mundo = vida.adiciona_vida(vidas,mundo)
	matriz=[]
	matriz = cria_mundo(matriz,mundo,tela)
	tela.pack()
	time.sleep(dormir)
	###inicia
	while 1:
		mundo = vida.vida(mundo)
		matriz = atualiza_mundo(matriz,mundo,tela)
		tela.update()
		time.sleep(dormir)
		#~ print("tic")
	########################
	janela.mainloop()
	########################
def rodaEmConsole(mundoA,mundoL,dormir):
		#~ #### modo console
	mundo = vida.mundo(mundoA,mundoL)  ## mudar aqui o tamanho do mundo
	
	######### vidas :
	#vidas imortais:
	vidas = [(1,5),(1,6),(1,7),\
	(6,5),(6,6),(7,5),(8,6),(7,7),\
	(10,11),(10,12),(10,13),(11,10),(11,11),(11,12),\
	(15,15),(15,16),(16,15),(16,16)] ## blink, bote, sapo e cubo; respectivamente
	#gun atira projeteis (precisa de um espaço grande)
	#~ vidas= [(12,15),(12,16),(13,14),(14,13),(15,13),(16,13),(17,14),(18,15),(18,16)]
	###
	
	## fim vidas
	mundo = vida.adiciona_vida(vidas,mundo)
	conta=0
	while 1:
		vida.printamundo(mundo)
		mundo = vida.vida(mundo)
		print("geração",conta)
		time.sleep(dormir)
		conta+=1
		os.system("clear")
	########
def main(args):
	mundoA=100 ## altura do mundo
	mundoL=100 ## Largura do mundo
	dormir=0.01 ## tempo entre gerações em segundos

	rodaEmTk(mundoA,mundoL,dormir)
	#~ rodaEmConsole(mundoA,mundoL,dormir)
	

	
	return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
