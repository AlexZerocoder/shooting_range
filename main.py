import pygame
import random

#инициализируем Pygame
pygame.init()

#Создадим игровое окно
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#Создадим экран
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Зададим название игры
pygame.display.set_caption('Game Shooting range')

#Создадим иконку для игры
icon = pygame.image.load("img/Shooting_range.jpg")
pygame.display.set_icon(icon)

#Создадим объект для игры
target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

#Зададим рандомные координаты для объекта
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

#Зададим рандомное значение заливки фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

#Дополнительный функционал
# Скорость движения цели
target_speed_x = random.choice([-5, 5])
target_speed_y = random.choice([-5, 5])

# Переменные для подсчета очков и времени игры
score = 0
start_time = time.time()
game_duration = 30  # Игра длится 30 секунд

# Шрифт для отображения очков и таймера
font = pygame.font.Font(None, 36)


#Цикл
running = True

while running:
    #Зададим заливку экрана
    screen.fill(color)

    #Создадим события игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()
#Завершение игры
pygame.quit()