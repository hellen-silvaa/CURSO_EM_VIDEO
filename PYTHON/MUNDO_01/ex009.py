#Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
num = int(input('Digite umm número para ver sua tabuada: '))
print('-'*12)
print(f'{num} x {1} = {num*1}' )
print(f'{num} x {2} = {num*2}' )
print(f'{num} x {3} = {num*3}' )
print(f'{num} x {4} = {num*4}' )
print(f'{num} x {5} = {num*5}' )
print(f'{num} x {6} = {num*6}' )
print(f'{num} x {7} = {num*7}' )
print(f'{num} x {8} = {num*8}' )
print(f'{num} x {9} = {num*9}' )
print(f'{num} x {10} = {num*10}' )
print(''*12)

#OU

n = int(input('Digite um numero para ver a tabuada: '))
i = 1
while i < 10:
    print(f'{n} x  {i} = {n*i}')
    i+=1
print(f'{n} x {i+0} = {n*(i+0)}')
