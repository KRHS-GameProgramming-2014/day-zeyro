import pygame, math

class Zombie():
    def __init__(self, speed = [0,0], pos = [0,0]):
        self.upImage = pygame.image.load("Resources/Object/Zombie/ZombieForward.png")
        self.downImage = pygame.image.load("Resources/Object/Zombie/ZombieBack.png")
        self.leftImage = pygame.image.load("Resources/Object/Zombie/ZombieLeft.png")
        self.rightImage = pygame.image.load("Resources/Object/Zombie/ZombieRight.png")
        self.image = self.upImage
        self.rect = self.image.get_rect()
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.place(pos)
        self.didBounceX = False
        self.didBounceY = False
        self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
        self.detectionRadius =  300
        self.living = True
        self.changed = False
        self.maxSpeed = (math.fabs(speed[0] + math.fabs(speed[1]))/2)
        
        
        
    def place(self, pos):
        self.rect.center = pos
        
    def update(self, width, height, player):
        self.move(player)
        self.animate()
        self.collideWall(width, height)
        if self.didBounceX or self.didBounceY:
            self.changed = True
        if self.didBounceX or self.didBounceY:
            self.changed = True
        if math.fabs(self.speedx) >= math.fabs(self.speedy):
            if self.speedx >= 0:
                self.facing = "right"
            else:
                self.facing = "left"
        else:
            if self.speedy >= 0:
                self.facing = "down"
            else:
                self.facing = "up"
        self.didBounceX = False
        self.didBounceY = False
        
    def move(self, player):
        self.detect(player)
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)

    def collideWall(self, width, height):
        if not self.didBounceX:
            #print "trying to hit Wall"
            if self.rect.left < 0 or self.rect.right > width:
                self.speedx = -self.speedx
                self.didBounceX = True
                #print "hit xWall"
        if not self.didBounceY:
            if self.rect.top < 250 or self.rect.bottom > height:
                self.speedy = -self.speedy
                self.didBounceY = True
                #print "hit xWall"
        
    def collideZombie(self, other):
        #print "trying to hit Ball"
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if (self.radius + other.radius) > self.distance(other.rect.center):
                    if not self.didBounceX:
                        self.speedx = -self.speedx
                        self.didBouncex = True
                    if not self.didBounceY:
                        self.speedy = -self.speedy
                        self.didBounceY = True
                        #print "hit Ball"
    def distance(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
        
    def collideBullet(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if (self.radius + other.radius) > self.distance(other.rect.center):
                    self.living = False
                    
    def detect(self, player):
        if self.distance(player.rect.center) < self.detectionRadius:
            pX = player.rect.center[0]
            pY = player.rect.center[1]
            zX = self.rect.center[0]
            zY = self.rect.center[1]
           
            if pX > zX:
                self.speedx = self.maxSpeed
                self.facing = "up"
            elif pX < zX:
                self.speedx = -self.maxSpeed
                self.facing = "down"
            else:
                self.speedx = 0
            if pY > zY:
                self.speedy = self.maxSpeed
                self.facing = "right"
            elif pY < zY:
                self.speedy = -self.maxSpeed
                self.facing = "left"
            else:
                self.speedy = 0
                
                    
    def animate(self):
        if self.changed:    
            if self.facing == "up":
                self.images = self.upImage
            elif self.facing == "down":
                self.images = self.downImage
            elif self.facing == "right":
                self.images = self.rightImage
            elif self.facing == "left":
                self.images = self.leftImage
            
