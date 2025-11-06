import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600  # размеры экрана
WHITE = (255, 255, 255)  
BLACK = (0, 0, 0)  
RED = (255, 0, 0)  
GREEN = (0, 255, 0)  
BLUE = (0, 0, 255)  
COLORS = [BLACK, RED, GREEN, BLUE, WHITE]  
COLOR_NAMES = ["Black", "Red", "Green", "Blue", "Eraser"]  
BUTTON_SIZE = 50  


screen = pygame.display.set_mode((WIDTH, HEIGHT))  # создаем экран
pygame.display.set_caption("Drawing Tool")  # заголовок окна
screen.fill(WHITE)  # заполняем экран белым цветом

current_color = BLACK  # начальный цвет
drawing = False  
mode = "pen"  # начальный режим 
start_pos = None  # начальная позиция
points = []  

buttons = []
for i, color in enumerate(COLORS):
    buttons.append(pygame.Rect(10 + i * (BUTTON_SIZE + 10), HEIGHT - 60, BUTTON_SIZE, BUTTON_SIZE))  #кнопки для цветов

def draw():
    for i, button in enumerate(buttons):
        pygame.draw.rect(screen, COLORS[i], button)  # рисуем кнопки
        if COLORS[i] == WHITE:  
            pygame.draw.rect(screen, BLACK, button, 2)
        if COLORS[i] == current_color:  # если это выбранный цвет, рисуем рамку
            pygame.draw.rect(screen, WHITE, button, 3)

def get_color(pos):
    for i, button in enumerate(buttons):
        if button.collidepoint(pos):  #была ли нажата кнопка
            return COLORS[i]  # возвращаем выбранный цвет
    return None


def smoothline(screen, points, width, color):
    if len(points) < 2:  
        return
    for i in range(len(points) - 1):
        start = points[i]
        end = points[i + 1]
        dx = start[0] - end[0]
        dy = start[1] - end[1]
        iterations = max(abs(dx), abs(dy))
        for j in range(iterations):
            progress = j / iterations
            aprogress = 1 - progress
            x = int(aprogress * start[0] + progress * end[0])  # вычисляем координаты X
            y = int(aprogress * start[1] + progress * end[1])  # вычисляем координаты Y
            pygame.draw.circle(screen, color, (x, y), width)  # рисуем точку

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # закрытие окна
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # если нажата левая кнопка мыши
                new_color = get_color(event.pos)  # получаем выбранный цвет
                if new_color is not None:
                    current_color = new_color  # меняем текущий цвет
                    mode = "eraser" if new_color == WHITE else "pen"  # если выбрали ластик, меняем режим
                else:
                    drawing = True 
                    start_pos = event.pos  # сохраняем начальную точку
                    points = [start_pos]  # добавляем первую точку
        elif event.type == pygame.MOUSEBUTTONUP:
            if mode in ["rectangle", "circle"] and start_pos:
                end_pos = event.pos
                if mode == "rectangle":
                    x = min(start_pos[0], end_pos[0])
                    y = min(start_pos[1], end_pos[1])
                    width = abs(start_pos[0] - end_pos[0])
                    height = abs(start_pos[1] - end_pos[1])
                    pygame.draw.rect(screen, current_color, (x, y, width, height), 2)
                elif mode == "circle":
                    radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                    pygame.draw.circle(screen, current_color, start_pos, radius, 2)
            drawing = False 

            points = []  
        elif event.type == pygame.MOUSEMOTION:
            if drawing and mode == "pen":
                points.append(event.pos)  
                smoothline(screen, points, 5, current_color)  # рисуем плавную линию
                points = points[-2:]
            elif drawing and mode == "eraser":
                pygame.draw.circle(screen, WHITE, event.pos, 10)  # рисуем ластик
        elif event.type == pygame.KEYDOWN:
            # смена режима рисования
            if event.key == pygame.K_p:
                mode = "pen"  # режим ручки
            elif event.key == pygame.K_e:
                mode = "eraser"  # режим ластика
            elif event.key == pygame.K_r:
                mode = "rectangle"  # рисуем квадрат
            elif event.key == pygame.K_c:
                mode = "circle"  # рисуем круг

    draw()  # отрисовка кнопок на экране
    pygame.display.flip()  # обновление экрана
    clock.tick(60) 

pygame.quit()
sys.exit()