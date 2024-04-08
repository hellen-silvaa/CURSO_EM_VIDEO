#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Qual seu salário?'))
novo = salario + (salario * 15 / 100)
print(f'O seu sálario anterior era {salario}, e com um aumento de 15%, o seu sálario será {aumento:.2f}')

