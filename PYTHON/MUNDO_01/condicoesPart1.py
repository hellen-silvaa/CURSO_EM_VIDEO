#Estruturas sequenciais e condicionais
# Estrutura sequencial é uma sequência de comandos que são executados um após o outro.
# Estrutura condicional é uma sequência de comandos que são executados de acordo com uma condição.



#identação é a forma como o python identifica o bloco de código
#tab = 4 espaços
# : = indica que o bloco de código vai começar

#if = se
# else = senão
# elif = senão se

#Exemplo 1
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')

#Exemplo 2
#condição simplificada
# tempo = int(input('Quantos anos tem seu carro? '))
# print('Carro novo' if tempo <=3 else 'Carro velho')
# print('--FIM--')

# #Exemplo 3
# nome = str(input('Qual é o seu nome? '))
# if nome == 'Hellen':
#     print('Que nome bonito!')
# else:
#     print('Seu nome é tão normal!')
#     print(f'Bom dia, {nome}!')

#Exemplo 4
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua média foi {m:.1f}')
if m >= 6.0:
    print('Sua média foi boa! Parabéns!')
else:
    print('Sua média foi ruim! Estude mais!')

#Exemplo 5
#Condição simplificada
# n1 = float(input('Digite a primeira nota: '))
# n2 = float(input('Digite a segunda nota: '))
# m = (n1 + n2) / 2
# print(f'A sua média foi {m:.1f}')
# print('Sua média foi boa! Parabéns!' if m >= 6.0 else 'Sua média foi ruim! Estude mais!')
