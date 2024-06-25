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


def jogo():
    Star = {}

    while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    arquivo = open("salvos.txt","w")
                    arquivo.write(str(Star))
                    arquivo.close()
                    quit()
                elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                    arquivo = open("salvos.txt","w")
                    arquivo.write(str(Star))
                    arquivo.close()
                    quit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    nome_star = simpledialog.askstring("...","Insira um nome:")
                    if not nome_star:
                        nome_star = (f"Desconhecido {evento.pos}")
                    Star[nome_star] = evento.pos




                elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_F1:
                    try:
                        arquivo = open("salvos.txt","w")
                        arquivo.write(str(Star))
                        arquivo.close()
                    except:
                        pass

                elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_F2:
                    try:
                        tela.fill(branco)
                        arquivo = open("salvos.txt","r")
                        Star = eval(arquivo.read())
                        arquivo.close()
                    except:
                        pass
                elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_Fs3:
                        Star = {}             
                        arquivo = open("salvos.txt","w")
                        arquivo.write(str(Star))
                        arquivo.close()

            tela.blit(fundo,(0,0))

            salvar_texto = fonte.render("Aperte F1 para salvar os pontos",True,branco)
            tela.blit(salvar_texto,(5,0))
            carregar = fonte.render("Aperte F2 para carregar os pontos",True,branco)
            tela.blit(carregar,(5,15))
            excluir = fonte.render("Aperte F3 para salvar os pontos",True,branco)
            tela.blit(excluir,(5,30))

            for key, value in Star.items():
                texto = fonte.render(key,True,branco)
                tela.blit(texto,value)
                pygame.draw.circle(tela,branco,value,5)
            teste = list(Star.values())
            for pos in range(len(teste)-1):
                pygame.draw.line(tela,branco,teste[pos],teste[pos +1],1)

            pygame.display.update()
            clock.tick(60)
jogo()
