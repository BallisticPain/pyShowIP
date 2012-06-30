#!/usr/bin/env python

import os
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((350,75))
pygame.display.set_caption('pyShowIP')
screen.fill((159, 182, 205))

# Create a font
font = pygame.font.Font(None, 72)

# Render the text
text = font.render(os.getenv('CURRENT_IP'), True, (255, 255, 255), (159, 182, 205))

# Create a rectangle
textRect = text.get_rect()

# Center the rectangle
textRect.centerx = screen.get_rect().centerx
textRect.centery = screen.get_rect().centery

# Blit the text
screen.blit(text, textRect)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
