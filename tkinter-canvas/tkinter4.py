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
	canvas.create_oval(50, 50, 250, 150, fill="yellow")
	canvas.create_polygon(50,30,150,50,250,30,150,10, fill="green")
	canvas.create_line(50, 50, 250, 150, fill="red", width=5)
	canvas.create_text(150, 100, text="Amazing!", fill="purple", font="Helvetica 26 bold underline")
	canvas.create_text(150, 100, text="Carpe Diem!", anchor=SW, fill="orange", font="Times 18 italic")
	root.mainloop()
		
	return 0

if __name__ == '__main__':
	main()

