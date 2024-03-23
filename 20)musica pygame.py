import pygame

pygame.init()
pygame.mixer.music.load('exx.mp3')
pygame.mixer.music.play()

# espera o som terminar
while pygame.mixer.music.get_busy():
    pass