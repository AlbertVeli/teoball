#!/usr/bin/env python3

import pygame_sdl2
pygame_sdl2.import_as_pygame()

# game_common.py in the same directory
from game_common import *

class Teoball(pygame.sprite.Sprite):
    '''Standard ball example'''

    def __init__(self, pos = [0.0, 0.0], speed = [0.2, 0.2]):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = load_image('intro_ball.png', -1)
        self.w = self.rect.width
        self.h = self.rect.height
        # speed/pos = floats, pos = topleft corner
        self.speed = list(speed)
        self.pos = list(pos)

    # ticks = milliseconds since last frame
    def update(self, ticks):
        '''move ball and calculate bounces'''
        self.pos[0] += self.speed[0] * ticks
        self.pos[1] += self.speed[1] * ticks
        self.rect.topleft = self.pos
        # Collission detection
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

# Init
TARGET_FPS = 120
size = width, height = 800, 600
black = (0, 0, 0)
pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(black)
ball = Teoball(pos = (50, 50), speed = (0.395, 0.333))
bounce_sound = load_sound('punch.wav')
if load_music('bgmusic.mp3'):
    pygame.mixer.music.play(-1)
allsprites = pygame.sprite.Group((ball,))

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
    clock.tick(TARGET_FPS)

print('bye, average fps:', int(clock.get_fps()), 'frames per second')
pygame.quit()
