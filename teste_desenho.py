#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tkretangulo.py
#  
#  Autor: ifes <ifes@ifes-vbox>
#  Criado em: 16/11/15 14:02:28
#  Usuário: IFES Serra Lógica Prog\Téc Prog\Prog I\Prog II
#  
#  Função do programa: <resumo da tarefa que o programa realiza.>
#  Versão inicial: 1.0
#  ----------------------------------------------------------------

# http://www.kosbie.net/cmu/fall-10/15-110/handouts/notes-getting-started-with-graphics.html
# http://www.python-course.eu/tkinter_canvas.php
# http://compu2learn.org.uk/python/tkinter-drawing/
# http://www.tutorialspoint.com/python/tk_canvas.htm
#
# Identificadores padrões para cores usuais: 'white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta'

import tkinter
import time
def main():
	janela = tkinter.Tk()
	canvas_altura = 720
	canvas_largura = 1280
	tela = tkinter.Canvas(janela, bg='white', width=canvas_largura, height=canvas_altura)	

	quad = tela.create_rectangle(20,20,150,160,width=2,fill="red")
	tela.pack()
	#~ for i in range(100):
		#~ tela.move(quad,3,3)
		#~ tela.update()
		#~ time.sleep(.1)
	janela.mainloop()
	
	return 0

if __name__ == '__main__':
	main()

