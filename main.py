import pygame
import os
import tkinter as tk
from tkinter import simpledialog

pygame.init()

tamanho  = ( 1000, 563)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("SPACE MARKER")
fundo= pygame.image.load("assets/bg.jpg")
pygame.mixer.music.load("assets/Space_Machine_Power.mp3")
pygame.mixer.music.play(-1)
fonte = pygame.font.SysFont("comicsans",15)

branco  = (255,255,255)

while True:                                  
    for evento in pygame.event.get():        
        if evento.type == pygame.QUIT:       
            quit()
    tela.fill(branco) 
    tela.blit(fundo,(0,0))



    pygame.display.update()
    clock.tick(60)
pygame.quit()