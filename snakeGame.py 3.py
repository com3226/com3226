import pygame

pygame.init()
# colors
BLUE = (0,0,255); RED = (255,0,0)

#screen
SCR_WIDTH, SCR_HEIGHT = 400, 200
screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
pygame.display.set_caption('Snake Game')

#snake
snake_size = 10

running = True
while running:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(screen, BLUE, [int(SCR_WIDTH/2 - snake_size/2),\
                                    int(SCR_HEIGHT/2 - snake_size/2),\
                                    snake_size, snake_size])
    pygame.display.update()

pygame.quit()
