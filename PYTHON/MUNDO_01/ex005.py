#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Diga um número: '))
a = n-1
s = n+1
print('Analisando o valor {}, o seu antecessor é {} e o seu sucessor é {}'.format(n,a,s))

#OU

n = int(input('Diga um número: '))
print('Analisando o valor {}, o seu antecessor é {} e o seu sucessor é {}'.format(n,(n-1),(n+1)))