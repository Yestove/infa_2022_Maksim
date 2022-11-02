import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

circle(screen, (255, 255, 0), (200, 175), 100)
circle(screen, (255, 0, 0), (150, 145), 15)
circle(screen, (255, 0, 0), (250, 145), 15)
circle(screen, (0, 0, 0), (150, 145), 10)
circle(screen, (0, 0, 0), (250, 145), 10)
polygon(screen, (0, 0, 255), [(155, 200), (155, 210), (245, 210), (245, 200)])
polygon(screen, (0, 0, 255), [(125, 110), (125, 120), (170, 130), (170, 120)])
polygon(screen, (0, 0, 255), [(225, 120), (225, 130), (270, 120), (270, 110)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
