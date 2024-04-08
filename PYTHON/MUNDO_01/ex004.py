#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

algo = input('Digite algo: ')
print('O tipo primitivo deste valor é', type(algo))
print('Só tem espaços', algo.isspace())
print('É um número? ', algo.isnumeric())
print('É alfabético', algo.isalpha())
print(('É alfanúmerico?', algo.isalnum()))
print(('Está em maiúsculas?', algo.isupper()))
print(('Está em mainúsculas?', algo.islower()))
print(('Está capitalizada??', algo.istitle()))