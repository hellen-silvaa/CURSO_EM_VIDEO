#Desafio 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Ex: Ana Maria de Souza
#primeiro = Ana
#último = Souza

nome = str(input('Digite o seu nome completo: ')).strip().split()
print(f'Primeiro nome: {nome[0]}')
print(f'Último nome: {nome[len(nome) - 1]}')
