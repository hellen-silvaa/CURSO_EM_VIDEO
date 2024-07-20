'''Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hi = (co ** 2 + ca ** 2 ) ** (1/2)
print(f'O cateto oposto mede {co} o cateto adjacente mede {ca} e a hipotenusa vai medir {hi:.2f}')


from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hi = hypot(co, ca)
print(f'O cateto oposto mede {co} o cateto adjacente mede {ca} e a hipotenusa vai medir {hi:.2f}')'''
