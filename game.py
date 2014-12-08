import pygame, sys, random
#from Ball import Ball
#from PlayerBall import PlayerBall

pygame.init()

clock = pygame.time.Clock()

width = 800 
height = 600
size = width, height

bgColor = r,g,b = 0, 0, 0
#bgI = pygame.image.load("dayzeyroimages/dayz zeyro/Resources/Object/Background/New Road.jpg")
#bgR = bgI.get_rect()

screen = pygame.display.set_mode(size)

player = PlayerBall([width/2, height/2])

balls = []
balls += [Ball("images/Ball/ball.png", [4,5], [100, 125])]

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w or event.key == pygame.K_UP:
				player.go("up")
			if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
				player.go("right")
			if event.key == pygame.K_s or event.key == pygame.K_DOWN:
				player.go("down")
			if event.key == pygame.K_a or event.key == pygame.K_LEFT:
				player.go("left")
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_w or event.key == pygame.K_UP:
				player.go("stop up")
			if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
				player.go("stop right")
			if event.key == pygame.K_s or event.key == pygame.K_DOWN:
				player.go("stop down")
			if event.key == pygame.K_a or event.key == pygame.K_LEFT:
				player.go("stop left")
