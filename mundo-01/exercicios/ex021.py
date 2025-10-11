import pygame
pygame.init()
pygame.mixer.music.load('/home/claudio/Estudos/cursopython/mundo-01/exercicios/ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
