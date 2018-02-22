import pygame

FPS = 5
BOARD_SIZE = 71
SQUARE_SIZE = 10
DIRECTION = 'UP'

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

pygame.quit()
pygame.init()
gd = pygame.display.set_mode((BOARD_SIZE*SQUARE_SIZE,BOARD_SIZE*SQUARE_SIZE))
clock = pygame.time.Clock()

def drawBlock(pos):
    pygame.draw.rect(gd, RED, (pos[0]*SQUARE_SIZE,pos[1]*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))

head = (int(BOARD_SIZE/2),int(BOARD_SIZE/2))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: DIRECTION = 'UP'
            elif event.key == pygame.K_DOWN: DIRECTION = 'DOWN'
            elif event.key == pygame.K_RIGHT: DIRECTION = 'RIGHT'
            elif event.key == pygame.K_LEFT: DIRECTION = 'LEFT'

    if DIRECTION == 'UP': head = (head[0],head[1] - 1)
    elif DIRECTION == 'DOWN': head = (head[0],head[1] + 1)
    elif DIRECTION == 'LEFT': head = (head[0] - 1,head[1])
    elif DIRECTION == 'RIGHT': head = (head[0] + 1,head[1])

    print(head)

    gd.fill(WHITE)
    drawBlock(head)
    pygame.display.update()
    clock.tick(FPS)
