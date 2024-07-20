#Desafio 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas
#- O nome com todas as letras minúsculas
#- Quantas letras ao todo (sem considerar espaços)
#- Quantas letras tem o primeiro nome

nome_completo = str(input('Digite seu nome completo: '))
print(f'Seu nome em maiúsculas é {nome_completo.upper()}' 
        f'Seu nome em minúsculas é {nome_completo.lower()}'
        f'Seu nome tem ao todo {len(nome_completo) - nome_completo.count(" ")} letras'
        f'Seu primeiro nome tem {nome_completo.find(" ")} letras'
     )

separa = nome_completo.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')