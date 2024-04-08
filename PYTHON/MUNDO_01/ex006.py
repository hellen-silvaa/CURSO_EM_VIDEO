#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Diga um número: '))
print('O seu dobro é {} e o seu triplo é {}'.format((n*2),(n*3)))
print('E a sua raíz quadrada é {:.2f}'.format(n**(1/2)))
#ou
'''(pow(( n, (1/2)) também obtem a raíz'''



#OU

n = int(input('Diga um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}'.format(n,d))
print('O triplo de {} vale {}. \n A raíz quadrada de {} é igual a {:.2f}.'.format(n,t,n,r))
