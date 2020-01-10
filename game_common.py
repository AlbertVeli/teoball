# Some helper functions, mainly
# from the chimp.py example

import pygame_sdl2 as pygame
from pygame_sdl2.locals import *
from pygame_sdl2.compat import geterror
import os

# Local globals
main_dir = os.path.split(os.path.abspath(__file__))[0]
resources_dir = os.path.join(main_dir, "resources")

# Functions

# Colorkey -1 -> use pixel in upper left corner
def load_image(name, colorkey=None):
    fullname = os.path.join(resources_dir, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print("Cannot load image:", fullname)
        raise SystemExit(str(geterror()))
    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return (image, image.get_rect())

def load_sound(name):
    class NoneSound:
        def play(self):
            pass

    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join(resources_dir, name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error:
        print("Cannot load sound: %s" % fullname)
        #raise SystemExit(str(geterror()))
    return sound

def load_music(name):
    fullname = os.path.join(resources_dir, name)
    if not os.path.isfile(fullname):
        print('Drop an mp3 to %s for background music' % fullname)
        return False
    try:
        pygame.mixer.music.load(fullname)
    except:
        print('Cannot load music: %s' % fullname)
        print(geterror())
        #raise SystemExit(str(geterror()))
        return False
    return True
