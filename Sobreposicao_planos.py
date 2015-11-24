#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sobreposição_planos.py
#  
#  Autor: ifes <ifes@ifes-vbox>
#  Usuário: IFES Serra Lógica Prog\Téc Prog\Prog I\Prog II
#  
#  Função do programa: <resumo da tarefa que o programa realiza.>
#  Versão inicial: 1.0
#  ----------------------------------------------------------------

import tkinter
import time
import TAD_planos as TP
def main():
	plan1="100 100 500 500"
	plan2="0 200 600 300"
	plan3=""
	plan4=""
	plan5=""
	janela = tkinter.Tk()
	canvas_altura = 720
	canvas_largura = 1280
	tela = tkinter.Canvas(janela, bg='white', width=canvas_largura, height=canvas_altura)	
	#~ quad = tela.create_rectangle(20,20,150,160,width=2,fill="red")
	
	pl1=TP.cria_plano(plan1)
	pl2=TP.cria_plano(plan2)
	quad1= tela.create_rectangle(pl1,width=2,fill="red")
	quad2 = tela.create_rectangle(pl2,width=2,fill="red")
	if None != TP.area_sobreposta(pl1,pl2):
		pl_sob = TP.area_sobreposta(pl1,pl2)
		tela.create_rectangle(pl_sob,width=0,fill="blue")
	tela.pack()
	#~ for i in range(100):
		#~ 
		#~ tela.move(quad1,5,5)
		#~ tela.update()
		#~ time.sleep(.1)
	janela.mainloop()
	
	return 0

if __name__ == '__main__':
	main()

