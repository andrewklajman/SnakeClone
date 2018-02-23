import pygame
import random

## !!!!!!!!!!!!!!!! Initial Parameters !!!!!!!!!!!!!!!! 
FPS = 10
BOARD_SIZE = 30
SQUARE_SIZE = 10
WHITE = (255,255,255)
RED = (128,0,0)
GREEN = (0,255,0)

## !!!!!!!!!!!!!!!! Functions !!!!!!!!!!!!!!!! 
def drawSnake():        [pygame.draw.rect(gd, RED, (block[0]*SQUARE_SIZE,block[1]*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE)) for block in SNAKE]
def drawApple():        pygame.draw.rect(gd, GREEN, (APPLE[0]*SQUARE_SIZE,APPLE[1]*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
def boundaryHit():      return not(0<= SNAKE[0][0] <= BOARD_SIZE - 1) or not(0<= SNAKE[0][1] <= BOARD_SIZE - 1) or (SNAKE[0] in SNAKE[1:])
def updateSnakeHead():  ## Update the snake head to its new position (because it moves or eats an apple)
    if      DIRECTION == 'UP':      SNAKE.insert(0,(SNAKE[0][0],SNAKE[0][1] - 1))
    elif    DIRECTION == 'DOWN':    SNAKE.insert(0,(SNAKE[0][0],SNAKE[0][1] + 1))
    elif    DIRECTION == 'LEFT':    SNAKE.insert(0,(SNAKE[0][0] - 1,SNAKE[0][1]))
    elif    DIRECTION == 'RIGHT':   SNAKE.insert(0,(SNAKE[0][0] + 1,SNAKE[0][1]))
def resetGame():        ## Set the Snake, Apple and direction back to its initial values (random singular places)
    global SNAKE, APPLE, DIRECTION
    SNAKE = [(random.randint(0,BOARD_SIZE),random.randint(0,BOARD_SIZE))]
    APPLE = (random.randint(0,BOARD_SIZE),random.randint(0,BOARD_SIZE))
    DIRECTION = 'UP'
def moveSnake():        ## Set the new snakes heads position and get rid of the last part of the tail
    updateSnakeHead()
    SNAKE.pop()

## !!!!!!!!!!!!!!!! Main Program !!!!!!!!!!!!!!!! 
pygame.init()
gd = pygame.display.set_mode((BOARD_SIZE*SQUARE_SIZE,BOARD_SIZE*SQUARE_SIZE))
clock = pygame.time.Clock()

resetGame()
while True:
##  Get user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if      event.key == pygame.K_UP    and DIRECTION != 'DOWN':    DIRECTION = 'UP'
            elif    event.key == pygame.K_DOWN  and DIRECTION != 'UP':      DIRECTION = 'DOWN'
            elif    event.key == pygame.K_RIGHT and DIRECTION != 'LEFT':    DIRECTION = 'RIGHT'
            elif    event.key == pygame.K_LEFT  and DIRECTION != 'RIGHT':   DIRECTION = 'LEFT'
    moveSnake()                     ## Move the snake
    if SNAKE[0]==APPLE:             ## If the snakes head is on the apple then consider it eaten (and thus the snake grows)
        updateSnakeHead()
        APPLE = (random.randint(0,BOARD_SIZE - 1),random.randint(0,BOARD_SIZE - 1))
    if boundaryHit(): resetGame()   ## Reset the game if the snake goes outside the boundary or tries to eat itself
##  Draw elements onto the surface
    gd.fill(WHITE)
    drawApple()
    drawSnake()
##  Set surface to screen and tick
    pygame.display.update()
    clock.tick(FPS)


    
    
