#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tkline.py
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
	# Chama o construtor (pense na janela como um TAD) da janela.
	janela = tkinter.Tk()
	
	# Define as dimensões da área interior da janela, o canvas.
	canvas_altura = 400
	canvas_largura = 600
	
	# Cria o TAD área de desenho e o encaixa no interior da janela. Janela = canvas + bordas + barra de título.
	tela = tkinter.Canvas(janela, bg='white', width=canvas_altura, height=canvas_altura)	
	
	# Cria uma linha indo das coordenadas (x,y) 50,50 até as coordenadas (x,y) 250,150.
	# As coordenadas dizem respeito ao interior do canvas da janela,a variável tela.
	# Para mais propriedades da linha, leia:
	#	http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/create_line.html
	tela.create_line(50, 50, 250, 150, fill="red", width=10)	
	
	tela.create_line(50, 80, 250, 180, fill="blue", width=5, arrow=tkinter.BOTH)	
	
	tela.create_line(50, 110, 250, 210, fill="green", width=5, dash=(3,5))	
	
	# Cria um poligono aberto a partir das coordenadas fornecidas como entrada. As coordenadas podem ser fornecidas
	# em pares 0,y0,x1,y1,x2,y2,...,xn,yn. Ou podem ser armazenadas em uma lista e a lista ser passada como
	# parâmetro da função create_line. As coordenadas dizem respeito ao interior do canvas da janela,a variável tela.
	# O polígono é formado por uma série de segmentos de linhas. 
	lstpontos = [70, 160, 90, 210, 130, 220, 90, 240, 70, 280, 50, 240, 10, 220, 50, 200]
	tela.create_line(lstpontos, fill="green", width=5)	
	
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

