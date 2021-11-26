import math
import random

import pygame
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800,600))

font = pygame.font.Font('Nexa Light.otf', 50)

text = font.render('Welcome to Pong', True, (255,255,255))

textRect = text.get_rect()

ballX = 0
ballY = 0

ballX_change = 300
bally_change = 300

ball_radius = 20

ball_color = (50,135, 255)

def ball_move():
    if 

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
    pygame.draw.circle(screen, ball_color, (ballX,ballY), ball_radius,0)
    pygame.display.update()