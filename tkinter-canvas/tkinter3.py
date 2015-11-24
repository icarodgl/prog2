#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sem título.py
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

from tkinter import *

def main():
	root = Tk()
	canvas = Canvas(root, width=300, height=200)
	canvas.pack()
	canvas.create_rectangle(  0,   0, 150, 150, fill="yellow")
	canvas.create_rectangle(100,  50, 250, 100, fill="orange", width=5)
	canvas.create_rectangle( 50, 100, 150, 200, fill="green", outline="red", width=3)
	canvas.create_rectangle(125,  25, 175, 190, fill="purple", width=0)
	root.mainloop()
	
	return 0

if __name__ == '__main__':
	main()

