import pygame
from Ball import Ball

class Bullet(Ball):
	def __init__(self, pos, bspeed, heading, heading2 = None):
		Ball.__init__(self, "Resources/Object/Bullet/bullet.png", [0,0], pos)
		if heading == "up" or heading2 == "up":
			self.speedy = -bspeed
		if heading == "down" or heading2 == "down":
			self.speedy = bspeed
		if heading == "right" or heading2 == "right":
			self.speedx = bspeed
		if heading == "left" or heading2 == "left":
			self.speedx = -bspeed

	def collideZombie(self, other):
		if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
			if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
				if (self.radius + other.radius) > self.distance(other.rect.center):
					self.living = False
	
	def collideWall(self, width, height):
		if not self.didBounceX:
			#print "trying to hit Wall"
			if self.rect.left < 0 or self.rect.right > width:
				self.living = False
		if not self.didBounceY:
			if self.rect.top < 0 or self.rect.bottom > height:
				self.living = False
        
    
