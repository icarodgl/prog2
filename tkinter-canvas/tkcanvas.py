#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tkcanvas.py
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

def main():
	# Chama o construtor (pense na janela como um TAD) d ajanela.
	janela = tkinter.Tk()
	
	# Define as dimensões da área interior da janela, o canvas.
	canvas_altura = 720
	canvas_largura = 1080
	
	# Cria o TAD área de desenho e o encaixa no interior da janela. Janela = canvas + bordas + barra de título.
	#
	# Para outras propriedades do canvas: 
	#   http://www.tutorialspoint.com/python/tk_canvas.htm
	#   http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/canvas.html
	tela = tkinter.Canvas(janela, bg='purple', width=canvas_altura, height=canvas_altura)	
	
	# Conclui o arranjo dos elementos no canvas/área de desenho. Nesse caso, não existe
	# nenhum elemento no interior do canvas. Mesmo assim a chamada deve ser feita.
	tela.pack()
	
	# Ativa a janela processando (desenhando) todos os objetos no interior do seu canvas.
	# No caso corrente, o único elemento no interior do canvas é o próprio canvas, ou a 
	# própria superfície de desenho.
	janela.mainloop()
	
	return 0

if __name__ == '__main__':
	main()

