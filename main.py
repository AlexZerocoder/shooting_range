import pygame
#инициализируем Pygame
pygame.init

#Создадим игровое окно
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#Создадим экран
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Зададим название игры
pygame.display.set_caption(«Game Shooting range»)

#Создадим иконку для игры
icon = pygame.image.load("img/shooting_range.jpg")
pygame.display.set_icon(icon)

#Зададим рандомные координаты для объекта
target_image = pygame.image.load("img/target.png")
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

#Зададим рандомное значение заливки фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
import random

#Создадим объект для игры



#Цикл
running = True
while running:
    pass

#Завершение игры
pygame.quit