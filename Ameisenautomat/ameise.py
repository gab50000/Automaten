#!/usr/bin/python

import pygame

class ameise:
	def __init__(self, lattice, pos, direction):
		self.lattice=lattice
		self.pos=pos
		self.direction=direction

		
	def move(self):
		if self.direction=="N":
			self.pos[0]-=1
			if self.pos[0]<0:
				self.pos[0]+=len(lattice)
			if lattice[self.pos[0]][self.pos[1]]:
				lattice[self.pos[0]][self.pos[1]]=False
				self.direction="W"
			else:
				lattice[self.pos[0]][self.pos[1]]=True
				self.direction="O"
		elif self.direction=="O":
			self.pos[1]+=1
			if self.pos[1]>=len(lattice[0]):
				self.pos[1]-=len(lattice[0])
			if lattice[self.pos[0]][self.pos[1]]:
				lattice[self.pos[0]][self.pos[1]]=False
				self.direction="N"
			else:
				lattice[self.pos[0]][self.pos[1]]=True
				self.direction="S"
		elif self.direction=="S":
			self.pos[0]+=1
			if self.pos[0]>=len(lattice):
				self.pos[0]-=len(lattice)
			if lattice[self.pos[0]][self.pos[1]]:
				lattice[self.pos[0]][self.pos[1]]=False
				self.direction="O"
			else:
				lattice[self.pos[0]][self.pos[1]]=True
				self.direction="W"
		elif self.direction=="W":
			self.pos[1]-=1
			if self.pos[1]<0:
				self.pos[1]+=len(lattice[0])
			if lattice[self.pos[0]][self.pos[1]]:
				lattice[self.pos[0]][self.pos[1]]=False
				self.direction="S"
			else:
				lattice[self.pos[0]][self.pos[1]]=True
				self.direction="N"
				
class gitter:
	def __init__(self, lattice, window, size):
		self.lattice=lattice
		self.window=window
		self.size=size
		self.boxheight=size[1]/len(lattice)
		self.boxwidth=size[0]/len(lattice[0])
		
	def draw(self):
		for i in range(len(self.lattice[0])):
			for j in range(len(self.lattice)):
				if lattice[i][j]:
					self.window.fill((0,0,255), pygame.Rect((i*self.boxwidth, (j+1)*self.boxheight, self.boxwidth, self.boxheight)))
		for i in range(1,len(self.lattice)):
			pygame.draw.line(self.window, (200,200,200), (0, i*self.boxheight), (self.size[0], i*self.boxheight))
		for i in range(1,len(self.lattice[0])):
			pygame.draw.line(self.window, (200,200,200), (i*self.boxwidth, 0), (i*self.boxwidth, self.size[1]))
			

size=(800,800)
field=[100, 100]
pygame.init()
fps=pygame.time.Clock()
window=pygame.display.set_mode(size)

lattice=[[False for i in range(field[0])] for j in range(field[1])]
ant= ameise(lattice, [field[0]/2, field[1]/2], "N")
lattice[field[0]/2][field[1]/2]=True
git=gitter(lattice, window, size)

while 1:
		window.fill(pygame.Color(255,255,255))
		ant.move()
		git.draw()
		pygame.display.update()
		fps.tick(120)

pygame.quit()
