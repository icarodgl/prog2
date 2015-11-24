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

def main():
	# Chama o construtor (pense na janela como um TAD) da janela.
	janela = tkinter.Tk()
	
	# Define as dimensões da área interior da janela, o canvas.
	canvas_altura = 400
	canvas_largura = 600
	
	# Cria o TAD área de desenho e o encaixa no interior da janela. Janela = canvas + bordas + barra de título.
	tela = tkinter.Canvas(janela, bg='white', width=canvas_largura, height=canvas_altura)	
	
	# Cria um retângulo a partir das coordenadas x,y do canto esquerdo superior e das coordenadas x,y do canto 
	# direito inferior.
	#
	# Para mais propriedades de retângulo, leia:
	#   http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/create_rectangle.html
	tela.create_rectangle(20,20,150,160,width=2,fill="red")
	tela.create_rectangle(80,200,140,250,width=2,fill="blue",outline='red')
	tela.create_rectangle(200,20,350,160,width=0,fill="cyan")
	tela.create_rectangle(160,200,360,250,width=2,fill="green", dash=(3,5))	
		
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

