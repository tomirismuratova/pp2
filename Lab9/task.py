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

player_width = 40
player_height = 40
player_x = WIDTH // 2
player_y = HEIGHT - 100
player_speed = 5

coins = []
coin_radius = 15
coin_spawn_rate = 30  

score = 0
font = pygame.font.SysFont(None, 36)

def draw_triangle(surface, color, x, y):
    p1 = (x, y - player_height // 2)          
    p2 = (x - player_width // 2, y + player_height // 2)  
    p3 = (x + player_width // 2, y + player_height // 2)  
    pygame.draw.polygon(surface, color, [p1, p2, p3])
    return pygame.Rect(x - player_width//2, y - player_height//2, player_width, player_height)

def spawn_coin():
    x = random.randint(coin_radius, WIDTH - coin_radius)
    y = random.randint(coin_radius, HEIGHT - coin_radius)
    coins.append(pygame.Rect(x - coin_radius, y - coin_radius, coin_radius*2, coin_radius*2))

running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x - player_width // 2 > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x + player_width // 2 < WIDTH:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y - player_height // 2 > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y + player_height // 2 < HEIGHT:
        player_y += player_speed

    if random.randint(1, coin_spawn_rate) == 1:
        spawn_coin()

    for coin in coins[:]:
        pygame.draw.circle(screen, RED, (coin.x + coin_radius, coin.y + coin_radius), coin_radius)
   
        player_rect = pygame.Rect(player_x - player_width//2, player_y - player_height//2, player_width, player_height)
        if player_rect.colliderect(coin):
            coins.remove(coin)
            score += 1

    draw_triangle(screen, GREEN, player_x, player_y)

    score_text = font.render(f"Score: {score}", True, (0,0,0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
