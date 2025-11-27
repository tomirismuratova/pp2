import psycopg2
import pygame
import random
import sys
import time

# Database connection
conn = psycopg2.connect(dbname="suppliers", user="tomiris", host="localhost", port=5432)
cur = conn.cursor()

# user login
def get_user():
    username = input("Enter your username: ")

    # Проверяем, есть ли пользователь в users
    cur.execute("SELECT id, level, highest_score FROM users WHERE name=%s", (username,))
    result = cur.fetchone()

    if result:
        user_id, level, best = result
        print(f"Welcome back, {username}! Level: {level}, Best score: {best}")
        return user_id, level, best
    else:
        # Проверяем есть ли предыдущие попытки с таким именем в user_score
        cur.execute("""
            SELECT MAX(score) FROM user_score
            WHERE user_id IN (SELECT id FROM users WHERE name=%s)
        """, (username,))
        prev_score = cur.fetchone()[0]
        prev_score = prev_score if prev_score is not None else 0

        # Создаём нового пользователя с предыдущим лучшим результатом
        cur.execute("INSERT INTO users (name, highest_score) VALUES (%s, %s) RETURNING id, level, highest_score",
                    (username, prev_score))
        user_id, level, best = cur.fetchone()
        conn.commit()
        print(f"New user created: {username}, starting at level {level}, best previous score: {best}")
        return user_id, level, best


# save score function
def save_score(user_id, score):
    cur.execute("INSERT INTO user_score (user_id, score) VALUES (%s,%s)", (user_id, score))
    cur.execute("UPDATE users SET highest_score = GREATEST(highest_score, %s) WHERE id=%s", (score, user_id))
    conn.commit()
    print("Game saved!")

# start of snake code(from Lab9)
pygame.init()

# константы
SCREEN_WIDTH = 600  # ширина экрана
SCREEN_HEIGHT = 400  # высота экрана
CELL_SIZE = 20  # размер клетки
SPEED = 7  # начальная скорость игры

WHITE = (255, 255, 255)  
GREEN = (0, 255, 0)  
RED = (255, 0, 0)  
BLACK = (0, 0, 0)  

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  #экран
pygame.display.set_caption("Snake Game")  # заголовок окна
font = pygame.font.SysFont("Verdana", 20)  # шрифт для отображения счета

# класс змеи
class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]  # начальное положение змеи
        self.direction = (CELL_SIZE, 0)  # начальное направление вправо
        self.grow = False  # флаг для роста змеи

    def move(self):
        head_x, head_y = self.body[0]  # координаты головы
        dir_x, dir_y = self.direction  # направление движения
        new_head = (head_x + dir_x, head_y + dir_y)  # новая позиция головы

        if not self.grow:
            self.body.pop()  # если не растем, убираем хвост
        self.body.insert(0, new_head)  # добавляем новую голову
        self.grow = False  # сбрасываем флаг увеличения змеи

    def change_direction(self, direction):
        # запрещаем поворот в обратную сторону
        if (direction[0] != -self.direction[0] and direction[1] != -self.direction[1]):
            self.direction = direction  # меняем направление

    def check_collision(self):
        head = self.body[0]  # получаем координаты головы
        # проверка на столкновение с телом или выход за границу экрана
        if head in self.body[1:] or head[0] < 0 or head[1] < 0 or head[0] >= SCREEN_WIDTH or head[1] >= SCREEN_HEIGHT:
            return True
        return False

    def grow_snake(self):
        self.grow = True  # увеличиваем змею

# класс еды
class Food:
    def __init__(self, snake_body):
        self.position = self.generate_position(snake_body)  # создаем начальную позицию еды

    def generate_position(self, snake_body):
        # генерируем случайную позицию для еды, чтобы она не пересекалась с телом змеи
        while True:
            x = random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            if (x, y) not in snake_body:
                return (x, y)

    def respawn(self, snake_body):
        self.position = self.generate_position(snake_body)  # новая еда

# add db login before game
user_id, user_level, highest_score = get_user()


snake = Snake()
food = Food(snake.body)

score = 0  # начальный счет
level = 1  # начальный уровень

# игровой цикл
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE) 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

        elif event.type == pygame.KEYDOWN:
            # управление змеей с помощью стрелок
            if event.key == pygame.K_UP:
                snake.change_direction((0, -CELL_SIZE))  
            elif event.key == pygame.K_DOWN:
                snake.change_direction((0, CELL_SIZE))  
            elif event.key == pygame.K_LEFT:
                snake.change_direction((-CELL_SIZE, 0))  
            elif event.key == pygame.K_RIGHT:
                snake.change_direction((CELL_SIZE, 0))  

    # движение змеи
    snake.move()

    # проверка на столкновение
    if snake.check_collision():
        running = False  # конец игры, если произошло столкновение

    # проверка, съела ли змея еду
    if snake.body[0] == food.position:
        score += 1  # увеличиваем счет
        snake.grow_snake()  # увеличиваем змею
        food.respawn(snake.body)  # создаем новую еду

        # повышение уровня и скорости
        if score % 3 == 0:
            level += 1
            SPEED += 2  

    # отрисовка змеи
    for segment in snake.body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    # отрисовка еды
    pygame.draw.rect(screen, RED, pygame.Rect(food.position[0], food.position[1], CELL_SIZE, CELL_SIZE))

    # отображение счета и уровня
    score_text = font.render(f"Score: {score}", True, BLACK)
    level_text = font.render(f"Level: {level}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (500, 10))

    pygame.display.flip()  # обновление экрана
    clock.tick(SPEED)  # контроль частоты кадров

pygame.quit()
# save score on exit
save_score(user_id, score)

cur.close()
conn.close()
sys.exit()
