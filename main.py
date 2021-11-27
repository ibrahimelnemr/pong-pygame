import math
import random

import pygame
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800,600))

font = pygame.font.Font('Nexa Light.otf', 50)

text = font.render('Welcome to Pong', True, (255,255,255))

textRect = text.get_rect()

ballX = 400
ballY = 300

ballX_change = 1
ballY_change = 1

ball_radius = 20

ball_color = (50,135, 255)

def ball_move():
    global ballX, ballY, ballX_change, ballY_change
    ballX = ballX + ballX_change
    ballY = ballY + ballY_change


running = True
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
    screen.blit(text,textRect)
    ball_move()
    pygame.draw.circle(screen, ball_color, (ballX,ballY), ball_radius,0)
    pygame.display.update()