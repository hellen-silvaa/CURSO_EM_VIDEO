"""Desafio 019: Um professor quer sortear um dos seus quatro
 alunos para apagar o quadro. Faça um programa que 
 ajude ele, lendo o nome deles e escrevendo o nome do
  escolhido."""
  #choice escolhe um valor aleatório de uma lista
from random import choice
n1 = str(input('Digite o nome do primeiro aluno:'))
n2 = str(input('Digite o nome do segundo aluno:'))
n3 = str(input('Digite o nome do terceiro aluno:'))
n4 = str(input('Digite o nome do quarto aluno:'))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print(f'O aluno escolhido foi {escolhido}')
