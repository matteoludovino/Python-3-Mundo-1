import pygame

pygame.init()
pygame.mixer.music.load('C:/Users/Name/Downloads/Lady Gaga - Paparazzi.mp3')
pygame.mixer.music.play(loops=0)
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
pygame.mixer.music.stop()