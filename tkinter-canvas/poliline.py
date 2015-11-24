#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tkpoline.py
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

import tkinter

def main():
	# Chama o construtor (pense na janela como um TAD) da janela.
	janela = tkinter.Tk()
	
	# Define as dimensões da área interior da janela, o canvas.
	canvas_altura = 400
	canvas_largura = 600
	
	# Cria o TAD área de desenho e o encaixa no interior da janela. Janela = canvas + bordas + barra de título.
	tela = tkinter.Canvas(janela, bg='white', width=canvas_largura, height=canvas_altura)	
	
	# Cria um poligono a partir das coordenadas fornecidas como entrada. As coordenadas podem ser fornecidas
	# em pares 0,y0,x1,y1,x2,y2,...,xn,yn. Ou podem ser armazenadas em uma lista e a lista ser passada como
	# parâmetro da função create_polygon. As coordenadas dizem respeito ao interior do canvas da janela,a variável tela.
	#
	# Para mais propriedades de poligono, leia:
	#	http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/create_line.html
	lstpontos = [70, 110, 90, 150, 130, 170, 90, 190, 70, 230, 50, 190, 10, 170, 50, 150]
	tela.create_polygon(lstpontos, width=2, fill='green', outline='blue')
		
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

