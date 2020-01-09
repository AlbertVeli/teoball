#!/usr/bin/env python3

import pygame
# game_common.py in the same directory
from game_common import *

class Teoball(pygame.sprite.Sprite):
    '''Standard ball example'''

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = load_image('intro_ball.png', -1)
        self.w = self.rect.width
        self.h = self.rect.height
        # Keep speed and pos as floats, upper left corner
        self.speed = [0.395, 0.333]
        self.pos = [0.0, 0.0]

    # ticks = milliseconds since last frame
    def update(self, ticks):
        '''move ball and calculate bounces'''
        self.pos[0] += self.speed[0] * ticks
        self.pos[1] += self.speed[1] * ticks
        self.rect.left = int(self.pos[0])
        self.rect.top = int(self.pos[1])
        self.rect.move_ip(self.speed[0], self.speed[1])
        bounce = False
        if self.pos[0] < 0:
            bounce = True
            self.speed[0] = abs(self.speed[0])
        elif self.pos[0] + self.w > width:
            bounce = True
            self.speed[0] = -abs(self.speed[0])
        if self.pos[1] < 0:
            bounce = True
            self.speed[1] = abs(self.speed[1])
        elif self.pos[1] + self.h > height:
            bounce = True
            self.speed[1] = -abs(self.speed[1])
        if bounce:
            bounce_sound.play()

size = width, height = 640, 480
black = (0, 0, 0)
pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(black)
ball = Teoball()
bounce_sound = load_sound('punch.wav')
allsprites = pygame.sprite.RenderPlain((ball,))

# Main loop
running = True
while running:

    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False

    # Update positions
    allsprites.update(clock.get_time())

    # Draw
    screen.blit(background, (0, 0))
    allsprites.draw(screen)
    pygame.display.flip()
    clock.tick()

print('bye, average fps:', int(clock.get_fps()), 'frames per second')
pygame.quit()
