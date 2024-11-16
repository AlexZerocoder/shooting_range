import pygame
import random
import time

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
clock = pygame.time.Clock()

while running:
    #Зададим заливку экрана
    screen.fill(color)
    # Обновляем время
    elapsed_time = time.time() - start_time
    time_left = max(0, game_duration - int(elapsed_time))

    # Проверяем, закончилось ли время
    if time_left == 0:
        running = False
    # Движение цели
    target_x += target_speed_x
    target_y += target_speed_y

    # Проверка выхода за границы экрана и смена направления
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_speed_x *= -1
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_speed_y *= -1

    #Создадим события игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                # Увеличиваем счет
                score += 1
                # Перемещаем цель
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                # Случайно изменяем скорость и направление после попадания
                target_speed_x = random.choice([-5, 5])
                target_speed_y = random.choice([-5, 5])

    #Отображаем цель на экране
    screen.blit(target_img, (target_x, target_y))

    # Отображаем количество очков и оставшееся время
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    timer_text = font.render(f"Time left: {time_left}", True, (255, 255, 255))
    screen.blit(timer_text, (SCREEN_WIDTH - 180, 10))
    # Обновляем экран
    pygame.display.update()
    # Ограничиваем количество кадров в секунду
    FPS = 60
    clock.tick(FPS)

# Завершаем игру, выводим результат
print(f"Game Over! Your score: {score}")
#Завершение игры
pygame.quit()