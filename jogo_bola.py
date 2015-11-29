#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  jogo_bola.py
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

import tkinter
import time
import TAD_planos as TP
import TAD_bola as TB
def main():
	############## tkinter criando janelas
	janela = tkinter.Tk()	#
	canvas_altura = 600		#
	canvas_largura = 600	#
	tela = tkinter.Canvas(janela, bg='white', width=canvas_largura, height=canvas_altura)	#
	###############
	

	
######## paredes
	plano1= TP.cria_plano("0 0 600 2")
	plano2= TP.cria_plano("0 0 2 600")
	plano3= TP.cria_plano("598 0 600 600")
	plano4= TP.cria_plano("0 598 600 600")
	plano_A= TP.cria_plano("200 200 202 600")
	plano_B= TP.cria_plano("300 300 600 302")
	
	tela.create_rectangle(plano_B,width=0,fill="red")
	tela.create_rectangle(plano_A,width=0,fill="red")
	tela.create_rectangle(plano1,width=0,fill="red")
	tela.create_rectangle(plano2,width=0,fill="red")
	tela.create_rectangle(plano3,width=0,fill="red")
	tela.create_rectangle(plano4,width=0,fill="red")
######## paredes
	
	# bola
	bola = TB.cria_bola(50,10,100)
	boll = tela.create_oval(bola,width=0,fill="red")
	# bola
	tela.pack()		
	
## fisica da bola
	barra= None
	vet = "SE"
	barras=[plano1,plano2,plano3,plano4,plano_A,plano_B]
	while 1:
		for elem in barras:
			if TP.sobreposicao_planos(bola,elem) != None:
				barra = TP.direcao_parede(elem)
				vet = TB.vet_bola(vet,barra)
				print(vet,barra)
			
		TB.move_bola(bola,vet)
		boll = tela.create_oval(bola,width=2,fill="red")
		tela.update()
		time.sleep(.01)
		#~ if TB.vet_bola(vet,barra) == "NO":
			
			#~ tela.move(boll,-1,-1)
			#~ tela.update()
			#~ time.sleep(.01)	
			
		#~ if TB.vet_bola(vet,barra) == "SE":
			
			#~ tela.move(boll,1,1)
			#~ tela.update()
			#~ time.sleep(.01)	
			
		#~ if TB.vet_bola(vet,barra) == "SO":
			
			#~ tela.move(boll,-1,1)
			#~ tela.update()
			#~ time.sleep(.01)	
			
	
## fisica da bola

	################### escrevendo janela com tkinter
		#
	janela.mainloop()	#
	####################
	return 0

if __name__ == '__main__':
	main()

