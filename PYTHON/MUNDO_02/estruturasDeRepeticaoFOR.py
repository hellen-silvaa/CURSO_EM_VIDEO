#Estruturas de repetição FOR
#laços de repetição são utilizados para executar um bloco de código várias vezes.
#O FOR é uma estrutura de repetição com variável de controle.
#A variável de controle é uma variável que controla o número de repetições.
#O FOR é utilizado quando se sabe previamente quantas vezes o bloco de código deve ser repetido.
#Exemplo:

#O FOR é composto por três partes:
#1. A variável de controle
#2. A palavra reservada in
#3. O intervalo
#O intervalo é composto por três partes:
#1. O valor inicial
#2. O valor final
#3. O passo
#O valor inicial é o valor que a variável de controle deve assumir na primeira repetição.
#O valor final é o valor que a variável de controle deve assumir na última repetição.
#O passo é a quantidade de valores que a variável de controle deve incrementar a cada repetição.
#O passo é opcional. Se não for informado, o passo será 1.
# i = int(input('Início: '))
# f = int(input('Fim: '))
# p = int(input('Passo: '))
# for c in range(i, f, p):
#     print(c)
# print('FIM')

# for c in range(0, 6):
#     print('Oi')
s = 0
for c in range(0,4):
    n = int(input('Digite um valor: '))
    s += n
print(f'A soma de todos os valores foi {s}.')