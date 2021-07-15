import pygame.mixer

__bgm = pygame.mixer.Sound("data/bgm/bgm.ogg")


def play(loop):
    __bgm.play(loops=loop)


def stop():
    __bgm.stop()