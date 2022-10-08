import pygame
pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("First Game")

x = -10
y = -10
width = 10
height = 10
vel = 5


run = True
while run:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if pygame.mouse.get_pressed()[0]==True:
        (x1, y1) = pygame.mouse.get_pos()

        x = x1 - 5
        y = y1 - 5

    
    '''
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
    
    if keys[pygame.K_RIGHT]:
        x += vel
    
    if keys[pygame.K_UP]:
        y -= vel
    
    if keys[pygame.K_DOWN]:
        y += vel
    '''
        
    pygame.draw.rect(win, (255, 255, 255), (x, y, width, height))
    pygame.display.update()

pygame.quit()

