'''Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
Ex: Digite um número: 6.127
O número 6.127 tem a parte Inteira 6.

n1 = float(input('Digite um número: '))
n2 = n1 // 1
print(f'O valor digitado foi {n1} e a sua porção inteira é {n2: .0f} ')'''
#math é uma biblioteca matemática
#import faz a importação de uma biblioteca
#trunc corta a parte decimal
from math import trunc
num = float(input('Digite um valor: '))
print(f'O valor digitado foi {num} e a sua porção inteira é {trunc(num)} ')

