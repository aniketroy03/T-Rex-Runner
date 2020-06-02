import pygame
import math
import random
pygame.init()
screen = pygame.display.set_mode((500,300))
pygame.display.set_caption("Dino")

background = pygame.image.load('ground.png')

#dino
dinoimg = pygame.image.load('dino.png')
dinoX = 88
dinoY = 191
dinoX_move = 0
dinoY_move = 0

#cactus
cactusimg = pygame.image.load('cactus.png')
cactusX = 470
cactusY = 191
cactusX_move = -2
cactusY_move = 0

#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',16)
textX = 1
textY = 1
#game over
over = pygame.font.Font('freesansbold.ttf',32)

def dino(x,y):
    screen.blit(dinoimg,(x,y))
def cactus(x,y):
    screen.blit(cactusimg,(x,y))
def isCollision(dinoX,dinoY,cactusX,cactusY):
    distance = math.sqrt(math.pow(dinoX-cactusX,2) + (math.pow(dinoY-cactusY,2)))
    if distance < 40:
        return True
    else:
        return False
def game_over():
    end = over.render("GAME OVER",True,(0,0,0))
    screen.blit(end,(150,150))
def show_score(x,y):
    score = font.render("Score: " + str(score_value),True,(0,0,0))
    screen.blit(score,(x,y))



run = True
while run:
    screen.fill((193, 224, 224))
    screen.blit(background,(0,180))
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            if dinoY == 191:
                dinoY_move = -1
            
                
            
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_SPACE:
            if dinoY != 191:
                dinoY_move = 1
            
                                
    #dino stop
    dinoY += dinoY_move
    if dinoY >= 191:
        dinoY = 191

    if dinoY == 100:
        dinoY_move = 1

    collide = isCollision(dinoX,dinoY,cactusX,cactusY)
    if collide:
        cactusX = 20000
        dinoX = 20000
        game_over()


    
    #cactus
    cactusX += cactusX_move
    if cactusX <=0:
        score_value +=1 
        cactusX = 470


    
    dino(dinoX,dinoY)
    cactus(cactusX,cactusY)
    show_score(textX,textY)
    pygame.display.update()
