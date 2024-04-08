# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Quanto dinheiro você tem na carteira? '))
dolar = real / 5.03
euro = real / 5.46
print(f'Com R${real} você pode comprar US${dolar:.2f} e €{euro:.2f} ')
