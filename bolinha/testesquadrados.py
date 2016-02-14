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
#  
import tkinter
import time
import TAD_planos as TP
import TAD_bola as TB

def main():
	############## tkinter criando janelas
	janela = tkinter.Tk()	#
	canvas_altura = 600	#
	canvas_largura = 600	#
	tela = tkinter.Canvas(janela, bg='white', width=canvas_largura, height=canvas_altura)	#
	###############
	

	
######## paredes
	plano1= TP.cria_plano("200 200 400 400")
	
	
	plano2= TP.cria_plano("150 350 300 450")
	plano3= TP.cria_plano("300 150 450 300")
	plano4= TP.cria_plano("300 250 350 500")

	tela.create_rectangle(plano1,width=0,fill="red")
	
	tela.create_rectangle(plano2,width=1,fill="blue")
	#~ tela.create_rectangle(plano3,width=1,fill="green")
	#~ tela.create_rectangle(plano4,width=1,fill="lightblue")
	
	

	
	dif1=TP.sobreposicao_planos(plano1,plano2)
	print(dif1[0]-plano2[0],dif1[1]-plano2[1],dif1[2]-plano2[2],dif1[3]-plano2[3])
	#~ dif2=TP.sobreposicao_planos(plano1,plano3)
	#~ print(dif2[0]-plano3[0],dif2[1]-plano3[1],dif2[2]-plano3[2],dif2[3]-plano3[3])
	#~ dif3=TP.sobreposicao_planos(plano1,plano4)
	#~ print(dif3[0]-plano4[0],dif3[1]-plano4[1],dif3[2]-plano4[2],dif3[3]-plano4[3])
######## paredes
	tela.pack()		


	janela.mainloop()	#
	####################
	return 0

if __name__ == '__main__':
	main()

