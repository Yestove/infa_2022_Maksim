import pandas as pd
import pygame
from pygame.draw import *
from random import randint

print("What's your name?")
player_name = input()
records = pd.read_csv('records.csv', sep=";")

pygame.init()

screen = pygame.display.set_mode((1200, 800))


RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

n = 0
x = []
y = []
r = []
vx = []
vy = []
color = []


def new_ball():
    global x, y, r, color, vx, vy
    """
    Создаёт n различных шаров
    x1, y1 -- координаты центра конкретного шара
    r1 -- радиус конкретного шара
    x, y -- массивы содержащие набор координат x1, y1 для наших n шариков
    r -- массив содержащий радиусы каждого шара
    vx1, vx2 -- проекции скорости конкретного шара на соответствующие оси
    vx, vy -- массивы содержащие наборы vx1, vx2 для наших шаров
    color1 -- цвет конкретного шара
    color -- набор цветов шаров
    """
    x1 = randint(100, 1100)
    y1 = randint(100, 700)
    r1 = randint(10, 100)
    vx1 = randint(-10, 10)
    vy1 = randint(-10, 10)
    color1 = COLORS[randint(0, 5)]
    x += [x1]
    y += [y1]
    r += [r1]
    vx += [vx1]
    vy += [vy1]
    color += [color1]


def create_balls():
    global n, x, y, r, color, vx, vy
    """
    Очищает массивы
    Создает n шаров
    """
    x = []
    y = []
    r = []
    vx = []
    vy = []
    color = []
    n = randint(0, 5)
    for u in range(n):
        new_ball()
        circle(screen, color[u], (x[u], y[u]), r[u])


def mote_balls():
    global x, y, vx, vy, r, n, color
    """
    Проверяет врезался ли шар в стенку
    Смещает все шары
    """
    for g in range(n):
        if x[g] + r[g] >= 1200:
            vx[g] = randint(-10, 0)
            vy[g] = randint(-10, 10)
        if x[g] - r[g] <= 0:
            vx[g] = randint(0, 10)
            vy[g] = randint(-10, 10)
        if y[g] + r[g] >= 800:
            vx[g] = randint(-10, 10)
            vy[g] = randint(-10, 0)
        if y[g] - r[g] <= 0:
            vx[g] = randint(-10, 10)
            vy[g] = randint(-0, 10)
        x[g] += vx[g]
        y[g] += vy[g]
        circle(screen, (color[g]), (x[g], y[g]), r[g])


def mote_all():
    """
    Вызываем функции движения для различных фигур (на случай если будут квадраты, треугольники и тд)
    """
    mote_balls()


def if_score(p, q, k):
    """
    Регистрирует наше касание по фигуре
    """
    (a, b) = event.pos
    for m in range(n):
        if (a - p[m]) ** 2 + (b - q[m]) ** 2 <= k[m] ** 2:
            return True


pygame.display.update()
clock = pygame.time.Clock()
finished = False

score_counter = 0

while not finished:
    clock.tick(30)
    create_balls()
    for i in range(20):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                records = records.append({"Player": player_name, "Score": score_counter}, ignore_index=True)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if if_score(x, y, r):
                    score_counter += 1

        clock.tick(30)
        mote_all()
        fild = pygame.font.Font(None, 48)
        text = fild.render("Score: " + str(score_counter), True, (255, 0, 0))
        screen.blit(text, (50, 50))
        pygame.display.update()
        screen.fill(BLACK)

pygame.quit()
records.groupby(["Player"]).agg({"Score": "sum"})
records.groupby(["Player"]).agg({"Score": "max"})
records.to_csv('records.csv', index=False)
