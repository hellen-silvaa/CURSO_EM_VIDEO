#Desafio 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

#pygame é uma biblioteca de funções para jogos
import pygame
#init inicializa o pygame
pygame.init()
#mixer é uma função para música
pygame.mixer.music.load('ex021.mp3')
#play inicia a música
pygame.mixer.music.play()
pygame
