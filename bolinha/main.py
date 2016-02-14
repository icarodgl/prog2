from tkinter import *
import time



heightGame = 1080
widthGame = 1920

heightFrame = 20
widthFrame = 20

heightMatrix = heightGame//heightFrame
widthMatrix = widthGame//widthFrame


def getRow(linha):
	return (linha*widthFrame)+20

def getCol(coluna):
	return (coluna*heightFrame)+20



class Janela():
	Player = None
	Matrix = []


	def __init__(self, toplevel):
		self.canvas = Canvas(toplevel, width = widthGame+40, height = heightGame+40, bg = "black")

		self.canvas.create_rectangle(19, 19, heightGame+10, widthGame+10, fill = "white")
		self.canvas.focus_set()
		
		for i in range(widthMatrix):
			self.Matrix.append([])
			self.Matrix[i].append(1)
			for j in range(1, heightMatrix-1):
				if i == 0 or i == widthMatrix:
					self.Matrix[i].append(1)
				else:
					self.Matrix[i].append(0)
			self.Matrix[i].append(1)



		self.canvas.pack()

	def insertIcon(self, obj_icon, kind):
		if kind == "Player":
			self.Player = obj_icon
			self.Matrix[obj_icon.Position[0]][obj_icon.Position[1]] = 50
		

		self.showIcon("Player")

		

	def movToLeft(self, event):
		self.cleanIcon("Player")
		self.Player.toLeft()
		self.showIcon("Player")


	def movToRight(self, event):
		self.cleanIcon("Player")
		self.Player.toRight()
		self.showIcon("Player")

	def movToUp(self, event):
		self.cleanIcon("Player")
		self.Player.toUp()
		self.showIcon("Player")

	def movToDown(self, event):
		self.cleanIcon("Player")
		self.Player.toDown()
		self.showIcon("Player")


	def cleanIcon(self, icon):
		if icon == "Player":
			cIcon = self.Player.getCoordinates()
			self.canvas.create_polygon(cIcon[0], cIcon[1],\
				cIcon[2], cIcon[3], cIcon[4], cIcon[5], cIcon[6],\
				cIcon[7], cIcon[8], cIcon[9], fill = "white")

	def showIcon(self, icon):
		if icon == "Player":
			cIcon = self.Player.getCoordinates()
			self.canvas.create_polygon(cIcon[0], cIcon[1],\
			cIcon[2], cIcon[3], cIcon[4], cIcon[5], cIcon[6],\
			cIcon[7], cIcon[8], cIcon[9], fill = self.Player.Color)


class Persona():
	Life = 7
	Position = [widthMatrix//2, heightMatrix//2]

	def __init__(self, name, color):
		self.Color = color
		self.Name = name

	def getCoordinates(self):
		x0 = getRow(self.Position[0])  # Canto superior esquerdo
		y0 = getCol(self.Position[1])

		x1 = getRow(self.Position[0]) + widthFrame # Canto superior direito
		y1 = getCol(self.Position[1])

		x2 = getRow(self.Position[0]) + widthFrame # Canto inferior direito
		y2 = getCol(self.Position[1]) + heightFrame

		x3 = getRow(self.Position[0]) # Canto inferior esquerdo
		y3 = getCol(self.Position[1]) + heightFrame
		return [x0, y0, x1, y1, x2, y2, x3, y3, x0, y0]

	def toLeft(self):
		if self.Position[0]-1 >= 0:
			self.Position[0] -= 1
		return self.getCoordinates()

	def toRight(self):
		if self.Position[0]+1 < widthMatrix:
			self.Position[0] += 1
		return self.getCoordinates()

	def toUp(self):
		if self.Position[1]-1 >= 0:
			self.Position[1] -= 1
		return self.getCoordinates()

	def toDown(self):
		if self.Position[1]+1 < heightMatrix:
			self.Position[1] += 1
		return self.getCoordinates()










def main():
	root = Tk()
	window = Janela(root)

	p1 = Persona("Danilo", "blue")

	window.insertIcon(p1, "Player")


	window.canvas.bind("<Left>", window.movToLeft)
	window.canvas.bind("<Right>", window.movToRight)
	window.canvas.bind("<Up>", window.movToUp)
	window.canvas.bind("<Down>", window.movToDown)
	

	root.mainloop()

	print("")

	return 0

if __name__ == "__main__":
	main()
