#Desafio 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
#- Se ele ainda vai se alistar ao serviço militar.
#- Se é a hora de se alistar.
#- Se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano_atual = date.today().year
ano_nascimento = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nascimento 
print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}.')
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento.')
    ano_alistamento = ano_atual + saldo
    print(f'Seu alistamento será em {ano_alistamento}.')
elif idade > 18:
    saldo = idade -18 
    print(f'Você já deveria ter se alistado há {saldo} anos.')
    ano_alistamento = ano_atual - saldo
    print(f'Seu alistamento foi em {ano_alistamento}.')
else:
    print('Opção inválida. Tente novamente.')