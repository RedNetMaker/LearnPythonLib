import random
import pygame

#Инициализация
pygame.init()

#Создание окна
screen = pygame.display.set_mode((1200, 700))
clock = pygame.time.Clock()

matrix = [[random.randint(0, 9) for _ in range(100)] for _ in range(100)]

#Главный цикл
x = 30
y = 30

is_blue = True
run = True
while run:
    # 1-й раздел ---- Обработка событий ----
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            is_blue = not is_blue

    # 2-й раздел ---- Логика игры ----
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3

    # 3-й раздел ---- Отображение графики ----
    screen.fill((255, 255, 255))

    for i in range(100):
        pygame.draw.line(screen, (0, 0, 0), (i * 6 + x, 0 + y), (i * 6 + x, 99 * 6 + y))
        pygame.draw.line(screen, (0, 0, 0), (0 + x, i * 6 + y), (99 * 6 + x, i * 6 + y))

        for l in range(100):
            match matrix[i][l]:
                case 0:
                    color = (252, 118, 221)
                case 1:
                    color = (168, 81, 24)
                case 2:
                    color = (0, 9, 1)
                case 3:
                    color = (6, 187, 86)
                case 4:
                    color = (85, 225, 10)
                case 5:
                    color = (77, 141, 81)
                case 6:
                    color = (203, 114, 80)
                case 7:
                    color = (151, 211, 205)
                case 8:
                    color = (90, 228, 166)
                case 9:
                    color = (160, 66, 90)

            pygame.draw.rect(screen, color, pygame.Rect(i * 6 + x + 1, l * 6 + y + 1, 5, 5))


    # if is_blue:
    #     color = (0, 128, 255)
    # else:
    #     color = (255, 100, 0)
    # pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

    pygame.display.flip()
    clock.tick(60)

#Закрытие всех модулей Pygame
pygame.quit()