import pygame
import random
import sys
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
clock = pygame.time.Clock()

ball_radius = 20
player_x = WIDTH // 2
player_y = HEIGHT - 100
player_speed = 5
enemies = []
enemy_width = 50
enemy_height = 50
enemy_speed = 5
enemy_spawn_rate = 20

def draw_triangle(surface, color, rect):
    p1 = (rect.x, rect.y + rect.height)
    p2 = (rect.x + rect.width, rect.y + rect.height)
    p3 = (rect.x + rect.width // 2, rect.y)
    pygame.draw.polygon(surface, color, [p1, p2, p3])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x - ball_radius > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x + ball_radius < WIDTH:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y - ball_radius > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y + ball_radius < HEIGHT:
        player_y += player_speed

    if random.randint(1, enemy_spawn_rate) == 1:
        enemy_y = random.randint(0, WIDTH - enemy_width)
        rect = pygame.Rect(-enemy_width, enemy_y, enemy_width, enemy_height)
        enemies.append(rect)
    for rect in enemies[:]: 
        rect.x += enemy_speed
        if rect.x > HEIGHT:
            enemies.remove(rect)

    player_rect = pygame.Rect(player_x - ball_radius, player_y - ball_radius, 
                              ball_radius * 2, ball_radius * 2)
    
    for rect in enemies:
        if player_rect.colliderect(rect):
            print("lose")
            running = False

    screen.fill(WHITE)
    pygame.draw.circle(screen, GREEN, (player_x, player_y), ball_radius)
    
    for rect in enemies:
        draw_triangle(screen, RED, rect)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()