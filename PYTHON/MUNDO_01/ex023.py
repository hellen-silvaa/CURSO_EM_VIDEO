#Desafio 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Ex: Digite um número: 1834
#Unidade: 4
#Dezena: 3
#Centena: 8
#Milhar: 1

num = int(input('Digite um número de 0 a 9999: '))
#pega o número e divide por 1, 10, 100 e 1000, depois pega o resto da divisão por 10
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
