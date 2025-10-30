import pygame
pygame.init()

window_size = (800, 600) 
screen = pygame.display.set_mode(window_size) 
pygame.display.set_caption("Draw circle")
ball_color = pygame.Color('red')  
bg_color = pygame.Color('white')  

ball_pos = [400, 300]  # начальная позиция шара

ball_radius = 25 

speed = 20  

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_UP]: 
        ball_pos[1] = max(ball_pos[1] - speed, ball_radius)  
    if keys[pygame.K_DOWN]:
        ball_pos[1] = min(ball_pos[1] + speed, window_size[1] - ball_radius)  
    if keys[pygame.K_LEFT]:
        ball_pos[0] = max(ball_pos[0] - speed, ball_radius)  
    if keys[pygame.K_RIGHT]:
        ball_pos[0] = min(ball_pos[0] + speed, window_size[0] - ball_radius) 
    #ball_pos[1] это вертикальная координата шара(Y). чем меньше Y тем выше на экране 
    #ball_pos[0]это горизонтальная координата шараX). чтобы идти влево уменьшаем X.
    
    screen.fill(bg_color)  # очистка экрана, чтобы не оставались следы
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)  # рисовка шара
    pygame.display.flip()  
    pygame.time.Clock().tick(24)  