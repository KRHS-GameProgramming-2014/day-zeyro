import pygame, sys, random
from Ball import Ball
from Player import Player
from Bullet import Bullet
#from HUD import Text
#from HUD import Score


pygame.init()

clock = pygame.time.Clock()

width = 800 
height = 600
size = width, height
bg = pygame.image.load("Resources/Object/Background/Sure.png")

bgColor = r,g,b = 200, 0, 200
screen = pygame.display.set_mode(size)
fullscreen = False 
bgImage = pygame.image.load("Resources/Object/Background/Sure.png").convert()
bgImage = pygame.transform.scale (bgImage, (800, 600))
bgRect = bgImage.get_rect()
player = Player([width/20, height/20])

balls = []
balls += [Ball("Resources/Object/Zombie/zombie.png", [4,5], [250, 275])]

bullets = []

#timer = Score([80, height - 25], "Time: ", 36)
#timerWait = 0
#timerWaitMax = 6

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
            if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                bullets += player.shoot()
            if event.key == pygame.K_KP1 or event.key == pygame.K_KP1:
                player.gun = player.pistol
                player.shoot("stop")
            if event.key == pygame.K_RETURN :
                print event.mod, pygame.KMOD_RALT
                if event.mod & pygame.KMOD_RALT: #Binary and with KMOD_RIGHT to filter out other mod keys
                    if fullscreen:
                        pygame.display.set_mode(size)
                        fullscreen = True
                    else:
                        pygame.display.set_mode(size, pygame.FULLSCREEN)
                        fullscreen = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                player.go("stop up")
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.go("stop right")
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.go("stop down")
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.go("stop left")
        
    if len(balls) < 3:
        if random.randint(0, 1*60) == 0:
            balls += [Ball("Resources/Object/Zombie/zombie.png",
                      [random.randint(0,10), random.randint(0,10)],
                      [random.randint(100, width-100), random.randint(100, height-100)])
                      ]
                      
    #if timerWait < timerWaitMax:
       #timerWait += 1
    #else:
       #timerWait = 0
       #timer.increaseScore(.1)
    player.update(width, height)
    #timer.update()
    
    for ball in balls:
        ball.update(width, height)
    for bullet in bullets:
        bullet.update(width, height)   
        
    #for bully in balls:
        #for victem in balls:
           #bully.collideBall(victem)
           #bully.collidePlayer(player)
    for bullet in bullets:
        for ball in balls:
            bullet.collideZombie(ball)
            #enemy.collideBullet(bullet)
    
    for ball in balls:
        for bullet in bullets:
            ball.collideBullet(bullet)
    
    for bullet in bullets:
         if not bullet.living:
            bullets.remove(bullet)
            
    for ball in balls:
       if not ball.living:
           balls.remove(ball)
    
    bgColor = r,g,b
    screen.fill(bgColor)
    screen.blit(bg,bgRect)
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    for bullet in bullets:
        screen.blit(bullet.image, bullet.rect)
    screen.blit(player.image, player.rect)
    #screen.blit(timer.image, timer.rect)
    pygame.display.flip()
    clock.tick(45)
