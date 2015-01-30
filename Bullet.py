import math,sys,pygame
from Ball import Ball

class Bullet(Ball):
	def __init__(self, pos, bspeed, heading):
		Ball.__init__(self, "Resources/Object/Bullet/bullet.png", [0,0], pos)
		if heading == "up":
			self.speedy = -bspeed
			self.image = pygame.image.load("Resources/Object/Bullet/bulletup.png")
		if heading == "down":
			self.speedy = bspeed
			self.image = pygame.image.load("Resources/Object/Bullet/bulletdown.png")	
		if heading == "right":
			self.speedx = bspeed
			self.image = pygame.image.load("Resources/Object/Bullet/bulletright.png")
		if heading == "left":
			self.speedx = -bspeed
			self.image = pygame.image.load("Resources/Object/Bullet/bulletleft.png")
		self.rect = self.image.get_rect(center = self.rect.center)

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

