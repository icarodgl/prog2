#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  jogo_bola.py
#  
#  Copyright 2015 Icaro <icaro@icaro-X550CA>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, orCaptura de tela de 2016-01-30 11:10:10
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
#  00:55:04: Arquivo C:\Users\icaro\Desktop\bolinha\jogo_bola.py aberto (1).
import tkinter
import time
import TAD_planos as TP
import TAD_bola as TB

def cria_obstaculos(matriz,tela):
	ho=0
	ver=0
	for col in range (len(matriz)):
		ho+=50
		ver=0
		for lin in range (len(matriz[col])):	
			ver+=20
			if matriz[col][lin] == 1:
				matriz[col][lin]= tela.create_rectangle([ho-50,ver-20,ho-1,ver-1],width=1,fill="lightblue")

	return matriz
##fim
def quebratijolos(matriz,bola,tela,vet):
	tijolo = []
	for col in range (len(matriz)):
		for lin in range (len(matriz[col])):
			posbola = tela.bbox(bola)
			tijolo = tela.bbox(matriz[col][lin])
			if posbola != None and  tijolo != None:
				sobreposto = TP.sobreposicao_planos(posbola,tijolo)
				if tijolo != None and sobreposto != None:
					vet = TB.dir_bola(vet,sobreposto,posbola)	
					tela.delete(matriz[col][lin])
					matriz[col][lin]=[0,0,0,0]
	return vet		
#fim
def barras_laterais(barras,boll,vet,tela):
	for elem in range(len(barras)):
		posbola = tela.bbox(boll)
		sobreposto = TP.sobreposicao_planos(posbola,barras[elem])
		if sobreposto != None:
			vet = TB.dir_bola(vet,sobreposto,posbola)
	return vet
####
#~ def movecomando(janela,comando):
	#~ ws = janela.winfo_screenwidth()
	#~ hs = janela.winfo_screenheight()
	
	#~ x = janela.winfo_pointerxy()[0]
	#~ print(x, ws,hs)
	#~ input()
	janela.move(comando,x)
#~ ##
def main():
	############## tkinter criando janelas
	janela = tkinter.Tk()	#
	canvas_altura = 600	#
	canvas_largura = 620	#
	tela = tkinter.Canvas(janela, bg='white', width=canvas_largura, height=canvas_altura)	#
	###############
	

	
######## paredes
	plano1= TP.cria_plano("0 0 620 10")
	plano2= TP.cria_plano("0 0 10 600")
	plano3= TP.cria_plano("610 0 620 600")
	plano4= TP.cria_plano("0 590 620 600")
################### mapa
	#~ matriz=[[0]]
	matriz = [	[0,0,1,1,1,0,0,0,0,0,0],\
				[1,1,1,1,1,1,0,0,0,0,0],\
				[1,1,1,1,1,1,1,0,0,0,0],\
				[1,1,1,1,1,1,1,1,0,0,0],\
				[0,1,1,1,1,1,1,1,1,0,0],\
				[0,0,1,1,1,1,1,1,1,1,1],\
				[0,1,1,1,1,1,1,1,1,1,0],\
				[0,1,1,1,1,1,1,1,1,0,0],\
				[1,1,1,1,1,1,1,1,0,0,0],\
				[1,1,1,1,1,1,1,0,0,0,0],\
				[1,1,1,1,1,1,0,0,0,0,0],\
				[0,0,1,1,1,0,0,0,0,0,0]]
	mat = cria_obstaculos(matriz,tela)
################## mapa
	tela.create_rectangle(plano1,width=0,fill="black")
	tela.create_rectangle(plano2,width=0,fill="black")
	tela.create_rectangle(plano3,width=0,fill="black")
	tela.create_rectangle(plano4,width=0,fill="black")
	###barra do jogador:
	comando = tela.create_rectangle([300,580,400,600],width=0,fill="purple")
######## paredes
	
	# bola
	bola = TB.cria_bola(20,400,500)
	boll = tela.create_oval(bola,width=1,fill="green")

	#img = tela.create_image(10,10,image="pkb.png")
	# bola
	tela.pack(padx=10, pady=10)		
	
## fisica da bola
	barra= None
	vet = "SO"
	barras=[plano1,plano2,plano3,plano4]
	tela.delete(boll)
	while 1:
		boll = tela.create_oval(bola,width=2,fill="black")
		### moldura
		vet = barras_laterais(barras,boll,vet,tela)
		### tijolinhos
		vet = quebratijolos(mat,boll,tela,vet)
		###		
		TB.move_bola(bola,vet)
		##comando
		#~ movecomando(tela,comando)
		##
		tela.update()
		time.sleep(.005)
		tela.delete(boll)


		
		
## fisica da bola

	################### escrevendo janela com tkinter
		#
	janela.mainloop()	#
	####################
	return 0

if __name__ == '__main__':
	main()

