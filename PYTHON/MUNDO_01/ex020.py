"""Desafio 020: O mesmo professor do desafio 019 
quer sortear a ordem de apresentação de trabalhos
 dos alunos. Faça um programa que leia o nome dos quatro 
 alunos e mostre a ordem sorteada."""

#random é uma biblioteca de funções aleatórias
#shuffle embaralha uma lista
from random import shuffle
n1 = str(input('Digite o nome do primeiro aluno:'))
n2 = str(input('Digite o nome do segundo aluno:'))
n3 = str(input('Digite o nome do terceiro aluno:'))
n4 = str(input('Digite o nome do quarto aluno:'))
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'A ordem de apresentação será: ')
print(lista)