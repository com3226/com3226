import pygame

pygame.init()
clock = pygame.time.time.Clock()

# colors
BLUE = (0,0,255); RED = (255,0,0); WHITE = (255,255,255)
BLACK = (0,0,0)

#screen
SCR_WIDTH, SCR_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
pygame.display.set_caption('Snake Game')

#snake
snake_size = 10
snake_pos_x = int(SCR_WIDTH/2 - snake_size/2)
snake_pos_y = int(SCR_HEIGHT/2 - snake_size/2)
snake_posx_change = 0
snake_posy_change = 0

running = True
while running:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pgame.KEYDOWN:
            if event.kay == pygame.K_UP:
                snake_posy_change = 0
                snake_posy_change = -10
            if event.kay == pygame.K_DOWN:
                snake_posy_change = 0
                snake_posy_change = 10
            if event.kay == pygame.K_LEFT:
                snake_posy_change = -10
                snake_posy_change = 0
            if event.kay == pygame.K_RIGHT:
                snake_posy_change = 10
                snake_posy_change = 0
    snake_pos_x += snake_posx_change
    snake_pos_y += snake_posy_change
    screen.fill(WHITE)
                
    pygame.draw.rect(screen, BLUE, [snake_pos_x, snake_pos_y, snake_size, snake_size])
    pygame.display.update()
    clock.tick(30)
pygame.quit()
